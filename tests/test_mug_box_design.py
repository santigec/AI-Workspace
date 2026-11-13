"""Structural regression checks, not visual print approval."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MugBoxDesignTests(unittest.TestCase):
    def test_version_is_registered(self):
        registry = json.loads((ROOT / 'registry/skills.yaml').read_text(encoding='utf-8'))
        self.assertEqual('0.2.3', registry['skills']['mug-box-design']['version'])

    def test_geometry_contract_is_consistent(self):
        for name in ('tribe/skills/mug-box-design/SKILL.md',
                     'tribe/standards/mug-box-design-rules.md',
                     'tribe/templates/mug-box-qa.md',
                     'workflows/tribe/mug-box-design.md'):
            with self.subTest(path=name):
                content = (ROOT / name).read_text(encoding='utf-8')
                for value in ('50–80 mm', '40–80 mm', '45–105 mm', '120 mm'):
                    self.assertIn(value, content)
                self.assertNotIn('es un anclaje de composición', content)
                self.assertNotIn('anclaje de referencia a 120 mm', content)
        self.assertEqual(200, 50 + 30 + 120)
        self.assertEqual(200, 40 + 40 + 120)

    def test_full_motif_bounds_and_lateral_exception_are_explicit(self):
        rules = (ROOT / 'tribe/standards/mug-box-design-rules.md').read_text(encoding='utf-8')
        for text in ('caja delimitadora COMPLETA', 'cabello', 'efectos protagonistas',
                     'motivos laterales permanecen permitidos', 'variante explícita',
                     'su ancho requiere confirmación de plantilla física'):
            self.assertIn(text, rules)

    def test_many_lateral_motifs_keep_upright_compact_stacks(self):
        for name in ('tribe/skills/mug-box-design/SKILL.md',
                     'tribe/standards/mug-box-design-rules.md',
                     'tribe/templates/mug-box-qa.md',
                     'workflows/tribe/mug-box-design.md'):
            with self.subTest(path=name):
                content = (ROOT / name).read_text(encoding='utf-8')
                for text in ('rostros derechos', '90°', 'envolvente inferior',
                             'proporcionalmente', 'único logo central',
                             'umbral numérico'):
                    self.assertIn(text, content.lower())

    def test_art_has_no_decorative_perimeter_frame(self):
        for name in ('tribe/skills/mug-box-design/SKILL.md',
                     'tribe/standards/mug-box-design-rules.md',
                     'tribe/templates/mug-box-qa.md',
                     'workflows/tribe/mug-box-design.md'):
            with self.subTest(path=name):
                content = (ROOT / name).read_text(encoding='utf-8').lower()
                self.assertIn('sin borde', content)
                self.assertIn('marco', content)
                self.assertIn('fondo', content)

    def test_all_visible_elements_keep_verified_theme_identity(self):
        for name in ('tribe/skills/mug-box-design/SKILL.md',
                     'tribe/standards/mug-box-design-rules.md',
                     'tribe/templates/mug-box-qa.md',
                     'workflows/tribe/mug-box-design.md'):
            with self.subTest(path=name):
                content = (ROOT / name).read_text(encoding='utf-8').lower()
                self.assertIn('bandera', content)
                self.assertIn('uniforme', content)
                self.assertIn('tem', content)
                self.assertIn('genéric', content)



if __name__ == '__main__':
    unittest.main()

