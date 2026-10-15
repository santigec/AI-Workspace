"""Explicit start/end synchronization; never force, stash or discard local work."""
import argparse
import subprocess
import sys
from pathlib import Path
from engram_memory import action as memory_action

ROOT = Path(__file__).resolve().parents[1]

def git(*args, capture=False):
    result = subprocess.run(['git', *args], cwd=ROOT, text=True,
                            stdout=subprocess.PIPE if capture else None,
                            check=True)
    return result.stdout.strip() if capture else ''

def require_branch():
    if git('branch', '--show-current', capture=True) != 'develop':
        raise RuntimeError('Use branch develop; no automatic branch switching is performed.')

def synchronize(action, message=None, memory_only=False):
    require_branch()
    if action == 'status':
        git('status', '--short', '--branch')
        git('log', '-1', '--oneline')
        return
    if action == 'pull':
        if git('status', '--porcelain', capture=True):
            raise RuntimeError('Local changes exist. Publish or resolve them before pulling.')
        git('pull', '--ff-only', 'origin', 'develop')
        memory_action('import')
        memory_action('context')
    else:
        git('fetch', 'origin', 'develop')
        behind = int(git('rev-list', '--count', 'HEAD..origin/develop', capture=True))
        if behind:
            raise RuntimeError('GitHub has newer changes. Preserve local work and reconcile before publishing.')
        memory_action('export')
        if memory_only:
            if git('diff', '--cached', '--name-only', capture=True):
                raise RuntimeError('Staged changes exist. Review before a memory-only commit.')
            git('add', '--all', '--', '.engram')
        else:
            git('add', '--all')
        if git('diff', '--cached', '--name-only', capture=True):
            git('commit', '-m', message)
        git('push', 'origin', 'develop')
    print('Synchronization completed. Update the other computer before editing.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['pull', 'push', 'status'])
    parser.add_argument('--message', help='Required commit description for push')
    parser.add_argument('--memory-only', action='store_true', help='Stage only .engram on push')
    args = parser.parse_args()
    if args.action == 'push' and not args.message:
        parser.error('push requires --message')
    try:
        synchronize(args.action, args.message, args.memory_only)
    except (RuntimeError, subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
