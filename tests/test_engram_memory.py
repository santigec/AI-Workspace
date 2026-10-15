import sys
import os
import subprocess
from pathlib import Path
from unittest.mock import patch
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import engram_memory as memory
import sync_workspace as sync

class EngramIntegrationTest(unittest.TestCase):
    def test_explicit_project_and_no_cloud(self):
        with patch.object(memory, 'executable', return_value='engram'), patch.object(memory.subprocess, 'run') as run:
            with patch.dict(os.environ, {'ENGRAM_CLOUD_SYNC':'true'}):
                memory.action('export')
        self.assertEqual(run.call_args.args[0], ['engram','sync','--project','ai-workspace'])
        self.assertEqual(run.call_args.kwargs['env']['ENGRAM_CLOUD_SYNC'], 'false')

    def test_import_is_import_not_export(self):
        with patch.object(memory, 'run') as run:
            memory.action('import')
        run.assert_called_once_with('sync','--import')

    def test_memory_only_stages_only_engram(self):
        commands=[]
        def git(*args, **kwargs):
            commands.append(args)
            if args[:2]==('branch','--show-current'):return 'develop'
            if args[0]=='rev-list':return '0'
            return ''
        with patch.object(sync,'git',side_effect=git),patch.object(sync,'memory_action') as action:
            sync.synchronize('push','memory update',memory_only=True)
        action.assert_called_once_with('export')
        self.assertIn(('add','--all','--','.engram'),commands)
        self.assertNotIn(('add','--all'),commands)

    def test_failed_export_does_not_stage_or_publish(self):
        commands=[]
        def git(*args, **kwargs):
            commands.append(args)
            if args[:2]==('branch','--show-current'):return 'develop'
            if args[0]=='rev-list':return '0'
            return ''
        with patch.object(sync,'git',side_effect=git),patch.object(sync,'memory_action',side_effect=RuntimeError('memory unavailable')):
            with self.assertRaises(RuntimeError):sync.synchronize('push','update')
        self.assertFalse(any(c[0] in ('add','commit','push') for c in commands))

if __name__=='__main__':unittest.main()
