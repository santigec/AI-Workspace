"""Local UML rendering and freshness checks; no semantic approval is inferred."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import struct
import subprocess
import sys
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOOLCHAIN = ROOT / 'software-office/tools/uml-toolchain.json'


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def choose_java(explicit=None, download=False):
    if explicit:
        return explicit
    config = json.loads(TOOLCHAIN.read_text(encoding='utf-8'))
    if sys.platform == 'win32':
        if __import__('platform').machine().lower() not in {'amd64', 'x86_64'}:
            raise ValueError('This local Java bundle is Windows x64; pass --java with a compatible runtime')
        pin = config['java_windows_x64']
        folder = ROOT / '.tools/uml' / ('java-' + pin['version'])
        candidates = list(folder.glob('*/bin/java.exe'))
        if candidates:
            return str(candidates[0])
        if download:
            folder.mkdir(parents=True, exist_ok=True)
            archive = folder / 'runtime.zip'
            request = urllib.request.Request(pin['url'], headers={'User-Agent': 'AI-Workspace-UML-setup'})
            with urllib.request.urlopen(request, timeout=90) as response, archive.open('wb') as output:
                shutil.copyfileobj(response, output)
            if digest(archive) != pin['sha256']:
                raise ValueError('Java download checksum mismatch')
            with zipfile.ZipFile(archive) as bundle:
                for entry in bundle.infolist():
                    name = entry.filename.replace('\\', '/')
                    target = (folder / name).resolve()
                    if ':' in name or not target.is_relative_to(folder.resolve()) or stat.S_ISLNK(entry.external_attr >> 16):
                        raise ValueError('Invalid path in Java archive')
                bundle.extractall(folder)
            candidates = list(folder.glob('*/bin/java.exe'))
            if not candidates:
                raise ValueError('Java executable absent from verified bundle')
            return str(candidates[0])
        raise ValueError('Local UML Java is missing; run uml.py setup or pass --java with Java 11+')
    return shutil.which('java') or 'java'


def local_file(project, name):
    if not isinstance(name, str) or not name or '\\' in name or ':' in name:
        raise ValueError(f'Expected portable project-relative file: {name!r}')
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Path outside project')
    target = (project / relative).resolve()
    if not target.is_relative_to(project) or not target.is_file():
        raise ValueError(f'Missing file or path outside project: {name}')
    return target


def load_inventory(project, manifest):
    project = Path(project).resolve()
    path = local_file(project, manifest)
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('diagrams'), list) or not data['diagrams']:
        raise ValueError('Expected schema_version 1 and a nonempty diagrams list')
    ids = set()
    for item in data['diagrams']:
        if not isinstance(item, dict) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(item.get('id', ''))):
            raise ValueError('Invalid diagram id')
        if item['id'] in ids:
            raise ValueError('Duplicate diagram id')
        ids.add(item['id'])
        if item.get('engine') not in {'plantuml', 'mermaid'} or item.get('scope') not in {'example', 'observed', 'proposed'}:
            raise ValueError('Invalid engine or model scope')
        source = local_file(project, item.get('source'))
        if source.suffix != ('.puml' if item['engine'] == 'plantuml' else '.mmd'):
            raise ValueError('Engine and source extension disagree')
        if not isinstance(item.get('code_refs'), list) or any(not isinstance(p, str) for p in item['code_refs']):
            raise ValueError('code_refs must be a list of relative paths')
        if item['scope'] == 'observed' and not item['code_refs']:
            raise ValueError('Observed models need inspected code references')
        for name in item['code_refs']:
            local_file(project, name)
    return project, path, data['diagrams']


def tool_fingerprint():
    config = json.loads(TOOLCHAIN.read_text(encoding='utf-8'))
    config['renderer_script_sha256'] = digest(Path(__file__))
    return hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()


def state_path(manifest):
    return manifest.with_name(manifest.stem + '.render-state.json')


def load_state(manifest):
    path = state_path(manifest)
    if path.is_symlink():
        raise ValueError('Render state must not be a symbolic link')
    if not path.exists():
        return {'schema_version': 1, 'diagrams': {}}
    state = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(state, dict) or state.get('schema_version') != 1 or not isinstance(state.get('diagrams'), dict):
        raise ValueError('Invalid render state; inspect it before replacing')
    return state


def inputs(project, item):
    return {'source': item['source'], 'engine': item['engine'], 'scope': item['scope'],
            'source_sha256': digest(local_file(project, item['source'])),
            'code_refs': {name: digest(local_file(project, name)) for name in item['code_refs']},
            'toolchain_sha256': tool_fingerprint()}


def check(project, manifest):
    project, path, items = load_inventory(project, manifest)
    state = load_state(path)
    errors = []
    for item in items:
        record = state['diagrams'].get(item['id'])
        if not record:
            errors.append(f'{item["id"]}: NOT_RENDERED')
            continue
        if record.get('inputs') != inputs(project, item):
            errors.append(f'{item["id"]}: STALE_SOURCE_CODE_OR_TOOLCHAIN')
        artifacts = record.get('artifacts')
        if not isinstance(artifacts, dict) or set(artifacts) != {'svg', 'png'}:
            errors.append(f'{item["id"]}: MISSING_ARTIFACT_RECORD')
            continue
        for extension, entry in artifacts.items():
            # Output names are controlled by diagram id, never arbitrary state paths.
            expected = f'outputs/uml/{item["id"]}.{extension}'
            if not isinstance(entry, dict) or entry.get('path') != expected:
                errors.append(f'{item["id"]}: INVALID_ARTIFACT_PATH')
                continue
            try:
                artifact = local_file(project, expected)
                if digest(artifact) != entry.get('sha256'):
                    errors.append(f'{item["id"]}: MODIFIED_{extension.upper()}')
            except ValueError:
                errors.append(f'{item["id"]}: MISSING_{extension.upper()}')
    return errors


def setup(java):
    config = json.loads(TOOLCHAIN.read_text(encoding='utf-8'))
    target = ROOT / '.tools/uml' / f'plantuml-{config["plantuml"]["version"]}.jar'
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        request = urllib.request.Request(config['plantuml']['url'], headers={'User-Agent': 'AI-Workspace-UML-setup'})
        temporary = target.with_suffix('.jar.part')
        with urllib.request.urlopen(request, timeout=45) as response, temporary.open('wb') as output:
            shutil.copyfileobj(response, output)
        if digest(temporary) != config['plantuml']['sha256']:
            raise ValueError('PlantUML download checksum mismatch; not installed')
        temporary.replace(target)
    if digest(target) != config['plantuml']['sha256']:
        raise ValueError('PlantUML checksum mismatch; inspect local installation')
    result = subprocess.run([java, '-jar', str(target), '-version'], capture_output=True, timeout=30, check=True)
    if config['plantuml']['version'] not in result.stdout.decode('utf-8', errors='replace'):
        raise ValueError('Unexpected PlantUML version')
    cli = ROOT / 'node_modules/@mermaid-js/mermaid-cli/src/cli.js'
    metadata = ROOT / 'node_modules/@mermaid-js/mermaid-cli/package.json'
    if not cli.is_file() or json.loads(metadata.read_text(encoding='utf-8'))['version'] != config['mermaid_cli']:
        raise ValueError('Mermaid CLI is missing or not pinned; run npm ci')
    return target


def find_browser(explicit=None):
    candidates = [explicit, shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chromium-browser'),
                  'C:/Program Files/Google/Chrome/Application/chrome.exe',
                  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe']
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(Path(candidate).resolve())
    raise ValueError('No local Chrome/Chromium found; pass --browser with its path')


def render(project, manifest, java, node, browser=None, review_note=None, selected=None):
    project, path, items = load_inventory(project, manifest)
    old = load_state(path)
    chosen = [item for item in items if not selected or item['id'] == selected]
    if not chosen:
        raise ValueError('Unknown diagram id')
    # Check all review conditions before rendering any diagram.
    for item in chosen:
        previous = old['diagrams'].get(item['id'], {}).get('inputs')
        current = inputs(project, item)
        if previous and previous.get('code_refs') != current['code_refs'] and previous.get('source_sha256') == current['source_sha256'] and not (review_note or '').strip():
            raise ValueError(f'{item["id"]}: code changed with unchanged model; review and pass --review-note or update the model')
    jar = setup(java)
    output = project / 'outputs/uml'
    if not output.resolve().is_relative_to(project):
        raise ValueError('Output directory escapes project')
    output.mkdir(parents=True, exist_ok=True)
    records = {item['id']: old['diagrams'][item['id']] for item in items if item['id'] in old['diagrams']}
    for item in chosen:
        source = local_file(project, item['source'])
        artifacts = {}
        for extension in ('svg', 'png'):
            target = output / f'{item["id"]}.{extension}'
            if target.is_symlink():
                raise ValueError('Artifact target must not be a symbolic link')
            if item['engine'] == 'plantuml':
                text = source.read_text(encoding='utf-8')
                if len(re.findall(r'^\s*@startuml\b', text, re.M)) != 1 or len(re.findall(r'^\s*@enduml\b', text, re.M)) != 1:
                    raise ValueError('One @startuml/@enduml diagram per source is required')
                result = subprocess.run([java, '-Djava.awt.headless=true', '-DPLANTUML_SECURITY_PROFILE=SANDBOX', '-jar', str(jar), f'-t{extension}', '-pipe', '-failfast2', '-charset', 'UTF-8'],
                                        input=text.encode('utf-8'), capture_output=True, timeout=90)
                if result.returncode:
                    raise ValueError('PlantUML failed: ' + result.stderr.decode('utf-8', errors='replace')[:2000])
                content = result.stdout
            else:
                config_dir = ROOT / '.tools/uml'
                puppet = config_dir / 'puppeteer.json'
                mermaid = config_dir / 'mermaid.json'
                puppet.write_text(json.dumps({'executablePath': find_browser(browser), 'headless': True}), encoding='utf-8')
                mermaid.write_text(json.dumps({'securityLevel': 'strict', 'theme': 'neutral'}), encoding='utf-8')
                result = subprocess.run([node, str(ROOT / 'node_modules/@mermaid-js/mermaid-cli/src/cli.js'), '-i', str(source), '-o', str(target), '-p', str(puppet), '-c', str(mermaid), '-b', 'white'],
                                        capture_output=True, timeout=90)
                if result.returncode:
                    raise ValueError('Mermaid failed: ' + result.stderr.decode('utf-8', errors='replace')[:2000])
                content = target.read_bytes()
            if extension == 'png':
                if content[:8] != b'\x89PNG\r\n\x1a\n' or not all(struct.unpack('>II', content[16:24])):
                    raise ValueError('Renderer did not produce a valid nonempty PNG')
            elif b'<svg' not in content or b'</svg>' not in content:
                raise ValueError('Renderer did not produce SVG')
            target.write_bytes(content)
            artifacts[extension] = {'path': target.relative_to(project).as_posix(), 'sha256': digest(target)}
        records[item['id']] = {'inputs': inputs(project, item), 'artifacts': artifacts, 'review_note': review_note or '',
                               'semantic_review': 'REQUIRED', 'visual_review': 'REQUIRED'}
    state_path(path).write_text(json.dumps({'schema_version': 1, 'diagrams': records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return [item['id'] for item in chosen]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['setup', 'render', 'check'])
    parser.add_argument('--project', type=Path, default=ROOT)
    parser.add_argument('--manifest', default='docs/uml/diagrams.json')
    parser.add_argument('--java')
    parser.add_argument('--node', default=shutil.which('node') or 'node')
    parser.add_argument('--browser')
    parser.add_argument('--review-note')
    parser.add_argument('--diagram')
    args = parser.parse_args()
    try:
        if args.action == 'setup':
            java = choose_java(args.java, download=True)
            print(json.dumps({'status': 'INSTALLED', 'plantuml': str(setup(java)), 'java': java}))
        elif args.action == 'render':
            java = choose_java(args.java)
            print(json.dumps({'status': 'RENDERED', 'diagrams': render(args.project, args.manifest, java, args.node, args.browser, args.review_note, args.diagram), 'semantic_and_visual_review': 'REQUIRED'}))
        else:
            errors = check(args.project, args.manifest)
            print(json.dumps({'status': 'STALE' if errors else 'CURRENT_HASHES', 'errors': errors, 'semantic_correctness': 'NOT_VERIFIED'}))
            return 1 if errors else 0
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(f'UML operation failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
