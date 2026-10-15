"""Exercise repository mutations that must block validation."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_workspace", ROOT / "scripts/validate_workspace.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class WorkspaceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ai-workspace-validation-", dir=ROOT.parent)
        assert Path(self.temp.name).resolve().parent == ROOT.parent.resolve()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "design-runs", ".venv", "outputs"))
        self.registry_path = self.root / "registry/skills.yaml"
        self.registry = json.loads(self.registry_path.read_text(encoding="utf-8"))

    def save(self):
        self.registry_path.write_text(json.dumps(self.registry), encoding="utf-8")

    def test_current_workspace_is_valid(self):
        self.assertEqual([], validator.validate(self.root))

    def test_missing_skill_blocks_validation(self):
        (self.root / self.registry["skills"]["image-analysis"]["path"]).unlink()
        self.assertTrue(validator.validate(self.root))

    def test_missing_workflow_dependency_blocks_validation(self):
        self.registry["workflows"]["sublimation"]["steps"].append("imaginary-agent")
        self.save()
        self.assertTrue(validator.validate(self.root))

    def test_dependency_cycle_blocks_validation(self):
        self.registry["skills"]["image-analysis"]["requires_before"] = ["sublimation-layout"]
        self.save()
        self.assertTrue(validator.validate(self.root))

    def test_promotion_without_executed_cases_is_rejected(self):
        self.registry["skills"]["image-analysis"]["status"] = "stable"
        self.save()
        self.assertTrue(validator.validate(self.root))

    def test_pass_without_evidence_is_rejected(self):
        manifest = self.root / "evals/cases.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["cases"][0]["status"] = "PASS"
        manifest.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(validator.validate(self.root))

    def test_logical_intake_alone_cannot_promote_a_skill(self):
        self.registry["skills"]["product-specs"]["status"] = "beta"
        self.save()
        self.assertTrue(validator.validate(self.root))

    def test_reference_outside_repo_is_rejected(self):
        self.registry["skills"]["image-analysis"]["path"] = "../outside/SKILL.md"
        self.save()
        self.assertTrue(validator.validate(self.root))

if __name__ == "__main__":
    unittest.main()
