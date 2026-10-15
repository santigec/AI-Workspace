from pathlib import Path
import importlib.util
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parents[1]/'scripts'))
import sync_workspace as sync

class SynchronizationSafetyTest(unittest.TestCase):
    def test_pull_refuses_dirty_checkout(self):
        commands = []
        def git(*args, **kwargs):
            commands.append(args)
            if args[:2] == ('branch', '--show-current'):return 'develop'
            if args[:2] == ('status', '--porcelain'):return ' M design-runs/example.png'
            return ''
        with patch.object(sync, 'git', side_effect=git):
            with self.assertRaisesRegex(RuntimeError, 'Local changes'):
                sync.synchronize('pull')
        self.assertFalse(any(c[0] == 'pull' for c in commands))

    def test_publish_refuses_outdated_base_before_staging(self):
        commands = []
        def git(*args, **kwargs):
            commands.append(args)
            if args[:2] == ('branch', '--show-current'):return 'develop'
            if args[0] == 'rev-list':return '1'
            return ''
        with patch.object(sync, 'git', side_effect=git):
            with self.assertRaisesRegex(RuntimeError, 'newer changes'):
                sync.synchronize('push', 'my work')
        self.assertFalse(any(c[0] in ('add','commit','push') for c in commands))

    def test_other_branch_is_not_switched_implicitly(self):
        with patch.object(sync, 'git', return_value='main') as git:
            with self.assertRaisesRegex(RuntimeError, 'develop'):
                sync.synchronize('pull')
        self.assertEqual(git.call_count, 1)

if __name__ == '__main__':
    unittest.main()
