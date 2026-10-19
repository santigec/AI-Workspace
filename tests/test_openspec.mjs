import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { test } from 'node:test';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const cli = join(root, 'node_modules/@fission-ai/openspec/bin/openspec.js');
const tools = join(root, '.tools');
mkdirSync(tools, { recursive: true });

function run(cwd, ...args) {
  const result = spawnSync(process.execPath, [cli, ...args], {
    cwd, encoding: 'utf8', timeout: 30000,
    env: { ...process.env, OPENSPEC_TELEMETRY: '0', DO_NOT_TRACK: '1', CI: '1' },
  });
  assert.ifError(result.error);
  return { code: result.status, out: result.stdout, err: result.stderr };
}

function fixture(config = 'schema: spec-driven\n') {
  // Fixtures remain local and ignored so failed CLI runs can be inspected.
  const cwd = mkdtempSync(join(tools, 'openspec-test-'));
  mkdirSync(join(cwd, 'openspec/changes'), { recursive: true });
  mkdirSync(join(cwd, 'openspec/specs'), { recursive: true });
  writeFileSync(join(cwd, 'openspec/config.yaml'), config);
  return cwd;
}

function change(cwd, spec) {
  const dir = join(cwd, 'openspec/changes/fix-permission');
  mkdirSync(join(dir, 'specs/access'), { recursive: true });
  writeFileSync(join(dir, '.openspec.yaml'), 'schema: spec-driven\ncreated: 2026-10-19\n');
  writeFileSync(join(dir, 'proposal.md'), '## Why\nPrevent unauthorized updates.\n\n## What Changes\n- Reject unauthorized requests.\n\n## Capabilities\n### New Capabilities\n- `access`: Restrict updates.\n\n## Impact\nAPI permissions and tests.\n');
  writeFileSync(join(dir, 'specs/access/spec.md'), spec);
  return dir;
}

const valid = '## ADDED Requirements\n\n### Requirement: ACCESS-001 Restrict updates\nThe API SHALL reject unauthorized updates.\n\n#### Scenario: Unauthorized request\n- **WHEN** an unauthorized user submits an update\n- **THEN** the API returns forbidden without changing data\n';

test('CLI version agrees with the reproducible dependency and lockfile', () => {
  const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
  const lock = JSON.parse(readFileSync(join(root, 'package-lock.json'), 'utf8'));
  const expected = pkg.devDependencies['@fission-ai/openspec'];
  assert.equal(lock.packages['node_modules/@fission-ai/openspec'].version, expected);
  const result = run(root, '--version');
  assert.equal(result.code, 0, result.err);
  assert.equal(result.out.trim(), expected);
});

test('structural validation accepts a requirement with a verifiable scenario', () => {
  const cwd = fixture();
  change(cwd, valid);
  const result = run(cwd, 'validate', 'fix-permission', '--strict', '--no-interactive');
  assert.equal(result.code, 0, result.out + result.err);
});

test('a requirement without scenarios is rejected rather than marked verified', () => {
  const cwd = fixture();
  change(cwd, '## ADDED Requirements\n\n### Requirement: ACCESS-001 Restrict updates\nThe API SHALL reject unauthorized updates.\n');
  const result = run(cwd, 'validate', 'fix-permission', '--strict', '--no-interactive');
  assert.notEqual(result.code, 0, result.out + result.err);
});

test('apply remains blocked while specs, design and tasks are missing', () => {
  const cwd = fixture();
  const dir = join(cwd, 'openspec/changes/incomplete');
  mkdirSync(dir);
  writeFileSync(join(dir, '.openspec.yaml'), 'schema: spec-driven\n');
  const result = run(cwd, 'instructions', 'apply', '--change', 'incomplete', '--json');
  assert.equal(result.code, 0, result.err);
  const data = JSON.parse(result.out);
  assert.equal(data.state, 'blocked', result.out);
});

for (const profile of ['sitop-v2', 'tribe-sport']) {
  test(`${profile} injects its documentation profile through real CLI instructions`, () => {
    const config = readFileSync(join(root, `software-office/templates/openspec/${profile}.config.yaml`), 'utf8');
    const cwd = fixture(config);
    change(cwd, valid);
    const result = run(cwd, 'instructions', 'specs', '--change', 'fix-permission', '--json');
    assert.equal(result.code, 0, result.err);
    const data = JSON.parse(result.out);
    assert.ok(Array.isArray(data.rules) && data.rules.length > 0, result.out);
    if (profile === 'sitop-v2') {
      assert.match(data.context, /Java Spring Boot.*Angular/);
      assert.ok(data.rules.some(rule => rule.includes('F1') && rule.includes('F3')));
    } else {
      assert.match(data.context, /Python Django.*Railway/);
      assert.match(data.context, /no exigir los formularios F0-F5/);
      assert.ok(data.rules.every(rule => !/F[0-5]/.test(rule)));
    }
  });
}
