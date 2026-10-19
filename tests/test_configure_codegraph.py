"""Protect existing Codex settings during the shared CodeGraph registration."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('configure_codegraph', ROOT / 'scripts/configure_codegraph.py')
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)
VERSION = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))['devDependencies']['@colbymchenry/codegraph']


class ConfigureCodeGraphTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='codegraph-config-', dir=ROOT.parent)
        self.addCleanup(self.directory.cleanup)
        self.home = Path(self.directory.name)
        self.config = self.home / 'config.toml'
        self.guide = self.home / 'AGENTS.md'
        self.mock = patch.object(setup.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, VERSION + '\n', ''))
        self.mock.start()
        self.addCleanup(self.mock.stop)

    def configure(self):
        return setup.configure(self.home, ROOT / 'synthetic-node-launcher')

    def test_preserves_other_settings_and_backs_up_original_files(self):
        original = 'model = "existing-model"\n[mcp_servers.existing]\ncommand = "existing-server"\nargs = ["--example"]\n'
        self.config.write_text(original, encoding='utf-8')
        self.guide.write_text('Existing project-independent instructions.\n', encoding='utf-8')
        result = self.configure()
        data = tomllib.loads(self.config.read_text(encoding='utf-8'))
        self.assertEqual(data['model'], 'existing-model')
        self.assertEqual(data['mcp_servers']['existing']['args'], ['--example'])
        self.assertEqual(data['mcp_servers']['codegraph']['enabled_tools'], ['codegraph_explore'])
        self.assertEqual((Path(result['backup']) / 'config.toml').read_text(encoding='utf-8'), original)
        self.assertTrue(self.guide.read_text(encoding='utf-8').startswith('Existing project-independent instructions.'))

    def test_repeated_setup_is_idempotent(self):
        self.configure()
        original = self.config.read_bytes(), self.guide.read_bytes()
        self.assertEqual(self.configure()['status'], 'unchanged')
        self.assertEqual(original, (self.config.read_bytes(), self.guide.read_bytes()))

    def test_unmanaged_codegraph_is_not_overwritten(self):
        original = '[mcp_servers.codegraph]\ncommand = "another-installation"\n'
        self.config.write_text(original, encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.configure()
        self.assertEqual(self.config.read_text(encoding='utf-8'), original)
        self.assertFalse(self.guide.exists())

    def test_bad_guidance_markers_do_not_partially_write_config(self):
        self.config.write_text('model = "existing-model"\n', encoding='utf-8')
        self.guide.write_text(setup.GUIDE_BEGIN, encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'markers'):
            self.configure()
        self.assertEqual(self.config.read_text(encoding='utf-8'), 'model = "existing-model"\n')

    def test_mismatched_installation_does_not_write_config(self):
        with patch.object(setup.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '0.0.0\n', '')):
            with self.assertRaisesRegex(ValueError, 'does not match'):
                self.configure()
        self.assertFalse(self.config.exists())


if __name__ == '__main__':
    unittest.main()
