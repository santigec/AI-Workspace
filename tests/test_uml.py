"""Freshness and path boundaries; these unit fixtures do not certify UML semantics."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('uml_tools', ROOT / 'scripts/uml.py')
uml = importlib.util.module_from_spec(spec)
spec.loader.exec_module(uml)


class UMLFreshnessTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='uml-check-', dir=ROOT.parent)
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name).resolve()
        (self.project / 'docs/uml').mkdir(parents=True)
        (self.project / 'src').mkdir()
        (self.project / 'outputs/uml').mkdir(parents=True)
        (self.project / 'src/service.py').write_text('def total():\n    return 1\n', encoding='utf-8')
        self.source = self.project / 'docs/uml/service.puml'
        self.source.write_text('@startuml\nclass Servicio\n@enduml\n', encoding='utf-8')
        self.item = {'id': 'service', 'engine': 'plantuml', 'scope': 'observed', 'source': 'docs/uml/service.puml', 'code_refs': ['src/service.py']}
        self.manifest = self.project / 'docs/uml/diagrams.json'
        self.save_manifest()
        artifacts = {}
        for extension in ('svg', 'png'):
            path = self.project / f'outputs/uml/service.{extension}'
            path.write_bytes(b'synthetic-unit-artifact-' + extension.encode())
            artifacts[extension] = {'path': path.relative_to(self.project).as_posix(), 'sha256': uml.digest(path)}
        self.record = {'inputs': uml.inputs(self.project, self.item), 'artifacts': artifacts, 'semantic_review': 'REQUIRED', 'visual_review': 'REQUIRED'}
        self.save_state()

    def save_manifest(self):
        self.manifest.write_text(json.dumps({'schema_version': 1, 'diagrams': [self.item]}), encoding='utf-8')

    def save_state(self):
        uml.state_path(self.manifest).write_text(json.dumps({'schema_version': 1, 'diagrams': {'service': self.record}}), encoding='utf-8')

    def check(self):
        return uml.check(self.project, 'docs/uml/diagrams.json')

    def test_unchanged_hashes_are_current_without_semantic_approval(self):
        self.assertEqual(self.check(), [])
        self.assertEqual(self.record['semantic_review'], 'REQUIRED')

    def test_diagram_edit_is_stale(self):
        self.source.write_text('@startuml\nclass OtroServicio\n@enduml\n', encoding='utf-8')
        self.assertIn('service: STALE_SOURCE_CODE_OR_TOOLCHAIN', self.check())

    def test_code_edit_is_stale(self):
        (self.project / 'src/service.py').write_text('def total():\n    return 2\n', encoding='utf-8')
        self.assertIn('service: STALE_SOURCE_CODE_OR_TOOLCHAIN', self.check())

    def test_toolchain_change_is_stale(self):
        with patch.object(uml, 'tool_fingerprint', return_value='different'):
            self.assertIn('service: STALE_SOURCE_CODE_OR_TOOLCHAIN', self.check())

    def test_artifact_tampering_is_detected(self):
        (self.project / 'outputs/uml/service.svg').write_bytes(b'changed')
        self.assertIn('service: MODIFIED_SVG', self.check())

    def test_missing_image_requires_render_on_new_machine(self):
        (self.project / 'outputs/uml/service.png').unlink()
        self.assertIn('service: MISSING_PNG', self.check())

    def test_source_path_change_with_same_content_is_stale(self):
        (self.project / 'docs/uml/copy.puml').write_bytes(self.source.read_bytes())
        self.item['source'] = 'docs/uml/copy.puml'
        self.save_manifest()
        self.assertIn('service: STALE_SOURCE_CODE_OR_TOOLCHAIN', self.check())

    def test_reference_cannot_escape_project(self):
        self.item['code_refs'] = ['../outside.py']
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'outside'):
            self.check()

    def test_duplicate_diagram_ids_rejected(self):
        self.manifest.write_text(json.dumps({'schema_version': 1, 'diagrams': [self.item, self.item]}), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.check()

    def test_observed_model_requires_code_references(self):
        self.item['code_refs'] = []
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'references'):
            self.check()

    def test_unchanged_model_cannot_silently_accept_changed_code(self):
        (self.project / 'src/service.py').write_text('def total():\n    return 3\n', encoding='utf-8')
        with patch.object(uml, 'setup') as setup:
            with self.assertRaisesRegex(ValueError, 'review-note'):
                uml.render(self.project, 'docs/uml/diagrams.json', 'java', 'node')
            setup.assert_not_called()

    def test_explicit_review_note_allows_progress_to_renderer(self):
        (self.project / 'src/service.py').write_text('# Comment only\ndef total():\n    return 1\n', encoding='utf-8')
        with patch.object(uml, 'setup', side_effect=ValueError('renderer reached')):
            with self.assertRaisesRegex(ValueError, 'renderer reached'):
                uml.render(self.project, 'docs/uml/diagrams.json', 'java', 'node', review_note='Only a comment changed; domain and operations stay identical.')


if __name__ == '__main__':
    unittest.main()
