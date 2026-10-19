"""Register the pinned local CodeGraph for Codex without replacing other settings."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '# BEGIN AI-WORKSPACE CODEGRAPH'
END = '# END AI-WORKSPACE CODEGRAPH'
GUIDE_BEGIN = '<!-- BEGIN AI-WORKSPACE CODEGRAPH -->'
GUIDE_END = '<!-- END AI-WORKSPACE CODEGRAPH -->'


def merge_block(text, start, end, block):
    if text.count(start) != text.count(end) or text.count(start) > 1:
        raise ValueError('Invalid or duplicate AI-Workspace CodeGraph markers')
    if start not in text:
        return text + ('\n' if text and not text.endswith('\n') else '') + ('\n' if text else '') + block + '\n'
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + block + after


def configure(codex_home, node):
    codex_home = Path(codex_home).resolve()
    node = str(Path(node).resolve())
    launcher = ROOT / 'scripts/codegraph.mjs'
    pinned = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))['devDependencies']['@colbymchenry/codegraph']
    cli = subprocess.run([node, str(launcher), '--version'], capture_output=True, text=True, timeout=30, check=True)
    if cli.stdout.strip() != pinned:
        raise ValueError('Installed CodeGraph does not match package.json; run npm ci')
    config = codex_home / 'config.toml'
    guidance = codex_home / 'AGENTS.md'
    old_config = config.read_text(encoding='utf-8') if config.exists() else ''
    old_guide = guidance.read_text(encoding='utf-8') if guidance.exists() else ''
    existing = tomllib.loads(old_config)
    if 'codegraph' in existing.get('mcp_servers', {}) and BEGIN not in old_config:
        raise ValueError('A CodeGraph entry already exists outside our managed block; review and merge it manually')
    block = '\n'.join([
        BEGIN, '[mcp_servers.codegraph]',
        'command = ' + json.dumps(node, ensure_ascii=False),
        'args = ' + json.dumps([str(launcher), 'serve', '--mcp'], ensure_ascii=False),
        'startup_timeout_sec = 30', 'tool_timeout_sec = 120',
        'enabled_tools = ["codegraph_explore"]',
        'env = { CODEGRAPH_MCP_TOOLS = "explore", CODEGRAPH_TELEMETRY = "0", DO_NOT_TRACK = "1", CODEGRAPH_NO_DOWNLOAD = "1" }', END,
    ])
    updated = merge_block(old_config, BEGIN, END, block)
    parsed = tomllib.loads(updated)
    # Check all existing settings, not only other MCP entries, survive unchanged.
    before = {k: v for k, v in existing.items() if k != 'mcp_servers'}
    after = {k: v for k, v in parsed.items() if k != 'mcp_servers'}
    if before != after:
        raise ValueError('Unrelated Codex settings would change')
    other_before = {k: v for k, v in existing.get('mcp_servers', {}).items() if k != 'codegraph'}
    other_after = {k: v for k, v in parsed.get('mcp_servers', {}).items() if k != 'codegraph'}
    if other_before != other_after:
        raise ValueError('Unrelated MCP entries would change')
    guide = '\n'.join([
        GUIDE_BEGIN, '## CodeGraph para las oficinas de AI-Workspace',
        f'En desarrollo de software gobernado por AI-Workspace, consultar `{ROOT / "software-office/standards/codegraph.md"}`.',
        'Para explorar simbolos o flujos, usar CodeGraph si esta disponible y el proyecto esta indexado, con projectPath explicito y maxFiles acotado (por ejemplo 3-5).',
        'Reutilizar el contexto suficiente ya devuelto; leer solo lo faltante o necesario para editar/verificar. Para busquedas textuales exactas o formatos no cubiertos, usar herramientas de archivos.',
        'No confundir relaciones estaticas con comportamiento probado; atender avisos de indice obsoleto y ejecutar pruebas. Sin indice usar lectura dirigida y no indexar directorios amplios por defecto.',
        'Los indices .codegraph son locales, no van a Git. No afirmar ahorro de tokens sin medirlo ni conexion MCP en un chat que no dispone de la herramienta.', GUIDE_END,
    ])
    updated_guide = merge_block(old_guide, GUIDE_BEGIN, GUIDE_END, guide)
    changes = [(config, updated, old_config), (guidance, updated_guide, old_guide)]
    changes = [(p, content) for p, content, old in changes if content != old]
    if not changes:
        return {'status': 'unchanged', 'version': pinned, 'files': []}
    backup = codex_home / 'backups' / ('ai-workspace-codegraph-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    backup.mkdir(parents=True, exist_ok=False)
    for path, _ in changes:
        if path.exists():
            shutil.copy2(path, backup / path.name)
    for path, content in changes:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + '.codegraph-tmp')
        with temporary.open('x', encoding='utf-8', newline='\n') as stream:
            stream.write(content)
        os.replace(temporary, path)
    return {'status': 'configured', 'version': pinned, 'files': [str(p) for p, _ in changes], 'backup': str(backup)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex-home', type=Path, default=Path.home() / '.codex')
    parser.add_argument('--node', default=shutil.which('node'))
    args = parser.parse_args()
    if not args.node:
        parser.error('Node launcher not found; pass --node with its absolute path')
    try:
        print(json.dumps(configure(args.codex_home, args.node), ensure_ascii=False, indent=2))
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(1, f'CodeGraph setup failed: {exc}\n')


if __name__ == '__main__':
    main()
