import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { spawn, spawnSync } from 'node:child_process';
import { createInterface } from 'node:readline';
import { after, before, test } from 'node:test';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const launcher = join(root, 'scripts/codegraph.mjs');
const env = { ...process.env, CODEGRAPH_TELEMETRY: '0', DO_NOT_TRACK: '1', CODEGRAPH_NO_DOWNLOAD: '1', CODEGRAPH_NO_DAEMON: '1', CODEGRAPH_MCP_TOOLS: 'explore' };
mkdirSync(join(root, '.tools'), { recursive: true });
const fixtures = mkdtempSync(join(root, '.tools/codegraph-tests-'));
const a = join(fixtures, 'alpha');
const b = join(fixtures, 'beta');
// Missing-index case must not live below AI-Workspace's own indexed root:
// CodeGraph can legitimately resolve an indexed ancestor for a subdirectory.
const absent = mkdtempSync(join(dirname(root), 'codegraph-no-index-'));

function run(...args) {
  const result = spawnSync(process.execPath, [launcher, ...args], { cwd: root, env, encoding: 'utf8', timeout: 60000 });
  assert.ifError(result.error);
  assert.equal(result.status, 0, result.stdout + result.stderr);
  return result.stdout;
}

class MCPPeer {
  constructor(project) {
    this.sequence = 0;
    this.pending = new Map();
    this.stderr = '';
    this.process = spawn(process.execPath, [launcher, 'serve', '--mcp', '--no-watch', '--path', project], {
      cwd: project, env, windowsHide: true, stdio: ['pipe', 'pipe', 'pipe'],
    });
    this.process.stderr.on('data', chunk => { this.stderr = (this.stderr + chunk).slice(-6000); });
    this.lines = createInterface({ input: this.process.stdout });
    this.lines.on('line', line => {
      if (!line.trim()) return;
      let message;
      try { message = JSON.parse(line); } catch { return; }
      if (message.method && message.id !== undefined) {
        if (message.method === 'roots/list') {
          this.send({ jsonrpc: '2.0', id: message.id, result: { roots: [{ uri: pathToFileURL(project).href, name: 'fixture' }] } });
        } else {
          this.send({ jsonrpc: '2.0', id: message.id, error: { code: -32601, message: 'Method not supported by test client' } });
        }
        return;
      }
      const waiter = this.pending.get(message.id);
      if (!waiter) return;
      this.pending.delete(message.id);
      clearTimeout(waiter.timer);
      if (message.error) waiter.reject(new Error(JSON.stringify(message.error)));
      else waiter.resolve(message.result);
    });
    this.process.on('error', error => this.rejectPending(error));
    this.process.on('exit', code => this.rejectPending(new Error(`MCP exited ${code}: ${this.stderr}`)));
  }
  rejectPending(error) {
    for (const waiter of this.pending.values()) { clearTimeout(waiter.timer); waiter.reject(error); }
    this.pending.clear();
  }
  send(message) { this.process.stdin.write(JSON.stringify(message) + '\n'); }
  request(method, params = {}) {
    const id = ++this.sequence;
    return new Promise((resolveRequest, reject) => {
      const timer = setTimeout(() => { this.pending.delete(id); reject(new Error(`${method} timed out: ${this.stderr}`)); }, 30000);
      this.pending.set(id, { resolve: resolveRequest, reject, timer });
      this.send({ jsonrpc: '2.0', id, method, params });
    });
  }
  async initialize() {
    const result = await this.request('initialize', { protocolVersion: '2024-11-05', capabilities: { roots: { listChanged: false } }, clientInfo: { name: 'ai-workspace-codegraph-check', version: '1.0.0' } });
    this.send({ jsonrpc: '2.0', method: 'notifications/initialized' });
    return result;
  }
  async close() {
    if (this.process.exitCode !== null) return;
    await new Promise(resolveClose => {
      const timer = setTimeout(() => { this.process.kill(); resolveClose(); }, 5000);
      this.process.once('exit', () => { clearTimeout(timer); resolveClose(); });
      this.process.stdin.end();
    });
    this.lines.close();
  }
}

let peer;
let handshake;
before(async () => {
  for (const directory of [a, b, absent]) {
    mkdirSync(directory, { recursive: true });
    writeFileSync(join(directory, '.gitignore'), '.codegraph/\n.codegraph-*/\nnode_modules/\n');
  }
  writeFileSync(join(a, 'pricing.py'), 'def price_total(value):\n    return "PROJECT_ALPHA_ONLY", value * 2\n');
  writeFileSync(join(b, 'pricing.py'), 'def price_total(value):\n    return "PROJECT_BETA_ONLY", value * 3\n');
  writeFileSync(join(a, 'OrderService.java'), 'public class OrderService {\n    public int calculateInvoice(int value) { return value * 2; }\n}\n');
  writeFileSync(join(a, 'checkout.ts'), 'export function submitOrder(value: number): number {\n  return value + 1;\n}\n');
  run('init', a, '--yes');
  run('init', b, '--yes');
  peer = new MCPPeer(a);
  handshake = await peer.initialize();
});
after(async () => { if (peer) await peer.close(); });

test('pinned CodeGraph version and platform bundle are runnable', () => {
  const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
  const lock = JSON.parse(readFileSync(join(root, 'package-lock.json'), 'utf8'));
  const pinned = pkg.devDependencies['@colbymchenry/codegraph'];
  assert.equal(run('--version').trim(), pinned);
  assert.equal(lock.packages['node_modules/@colbymchenry/codegraph'].version, pinned);
});

test('real MCP handshake exposes only the intended navigation tool', async () => {
  assert.ok(handshake.serverInfo?.name);
  const result = await peer.request('tools/list');
  assert.deepEqual(result.tools.map(tool => tool.name), ['codegraph_explore']);
});

test('Python, Java and TypeScript fixture symbols are actually indexed', () => {
  for (const [name, language] of [['price_total', 'python'], ['calculateInvoice', 'java'], ['submitOrder', 'typescript']]) {
    const nodes = JSON.parse(run('query', name, '--path', a, '--limit', '5', '--json'));
    assert.ok(nodes.some(item => item.node.name === name && item.node.language === language), JSON.stringify(nodes));
  }
});

test('projectPath isolates same-named symbols in two projects', async () => {
  for (const [projectPath, expected, unexpected] of [[a, 'PROJECT_ALPHA_ONLY', 'PROJECT_BETA_ONLY'], [b, 'PROJECT_BETA_ONLY', 'PROJECT_ALPHA_ONLY']]) {
    const result = await peer.request('tools/call', { name: 'codegraph_explore', arguments: { query: 'pricing.py price_total', projectPath, maxFiles: 1 } });
    assert.ok(!result.isError, JSON.stringify(result));
    const body = result.content.filter(item => item.type === 'text').map(item => item.text).join('\n');
    assert.ok(body.includes(expected), body);
    assert.ok(!body.includes(unexpected), body);
  }
});

test('a missing index returns guidance rather than fabricated source', async () => {
  const result = await peer.request('tools/call', { name: 'codegraph_explore', arguments: { query: 'price_total', projectPath: absent, maxFiles: 1 } });
  const body = result.content.filter(item => item.type === 'text').map(item => item.text).join('\n');
  assert.match(body, /init|not.{0,30}index/i);
  assert.ok(!body.includes('PROJECT_ALPHA_ONLY') && !body.includes('PROJECT_BETA_ONLY'), body);
});

test('explicit sync makes newly added behavior discoverable', () => {
  writeFileSync(join(b, 'pricing.py'), 'def price_total(value):\n    return "PROJECT_BETA_ONLY", value * 3\n\ndef revised_discount(value):\n    return value - 4\n');
  run('sync', b);
  const nodes = JSON.parse(run('query', 'revised_discount', '--path', b, '--json'));
  assert.ok(nodes.some(item => item.node.name === 'revised_discount'), JSON.stringify(nodes));
});
