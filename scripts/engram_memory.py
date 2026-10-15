"""Project-scoped Engram memory. No cloud mode, prompts or design files exported."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECT = 'ai-workspace'

def executable():
    override = os.environ.get('ENGRAM_BINARY')
    candidates = [override, shutil.which('engram'), str(Path.home()/'.local/bin/engram.exe'),
                  str(ROOT/'.tools/engram/engram.exe')]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError('Engram is not installed. Run python scripts/install_engram.py, then retry.')

def run(*args):
    env = os.environ.copy()
    env['ENGRAM_PROJECT'] = PROJECT
    env['ENGRAM_CLOUD_SYNC'] = 'false'
    subprocess.run([executable(), *args], cwd=ROOT, env=env, check=True)

def seed():
    run('init', PROJECT) if not (ROOT/'.engram/config.json').exists() else None
    topics = json.loads((ROOT/'continuity/memory-topics.json').read_text(encoding='utf-8'))['topics']
    for topic in topics:
        run('save', topic['title'], topic['content'], '--project', PROJECT,
            '--type', topic['type'], '--scope', 'project', '--topic', topic['key'])
    registry = json.loads((ROOT/'registry/skills.yaml').read_text(encoding='utf-8'))
    for name,entry in registry['skills'].items():
        content = (f"Skill {name}, dominio {entry['domain']}, versión {entry['version']}, estado {entry['status']}. "
                   f"Instrucciones canónicas en {entry['path']}. Leer ese archivo y referencias antes de ejecutar. "
                   'Las instrucciones completas viajan en Git; esta memoria es un índice, no sustituye el skill.')
        run('save', 'Skill '+name, content, '--project', PROJECT, '--type', 'config',
            '--scope', 'project', '--topic', 'skills/'+name)

def action(name):
    if name == 'seed':seed()
    elif name == 'export':run('sync', '--project', PROJECT)
    elif name == 'import':run('sync', '--import')
    elif name == 'context':run('context', '--project', PROJECT)
    elif name == 'status':run('sync', '--status')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['seed','export','import','context','status'])
    args = parser.parse_args()
    action(args.action)
