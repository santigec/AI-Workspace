#!/usr/bin/env node
// Shared local launcher: keep the caller's cwd and resolve tools from this repo.
import { existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const shim = join(root, 'node_modules/@colbymchenry/codegraph/npm-shim.js');
if (!existsSync(shim)) {
  process.stderr.write('CodeGraph is not installed in AI-Workspace. Run npm ci in that repository first.\n');
  process.exit(1);
}
const child = spawn(process.execPath, [shim, ...process.argv.slice(2)], {
  cwd: process.cwd(), stdio: 'inherit', windowsHide: true,
  env: { ...process.env, CODEGRAPH_TELEMETRY: '0', DO_NOT_TRACK: '1', CODEGRAPH_NO_DOWNLOAD: '1' },
});
child.on('error', error => { process.stderr.write(`${error.message}\n`); process.exitCode = 1; });
child.on('exit', code => { process.exitCode = code ?? 1; });
