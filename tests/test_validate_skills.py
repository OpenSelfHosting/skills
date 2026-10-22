from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import parse_frontmatter, validate  # noqa: E402


class FrontmatterTests(unittest.TestCase):
    def test_parses_required_fields(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SKILL.md"
            path.write_text('---\nname: example-skill\ndescription: "A useful skill description longer than thirty chars."\nlicense: MIT\n---\n# Test\n', encoding="utf-8")
            props, error = parse_frontmatter(path)
            self.assertIsNone(error)
            self.assertEqual(props["name"], "example-skill")
            self.assertTrue(props["description"].startswith("A useful"))

    def test_rejects_missing_opening_frontmatter(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SKILL.md"
            path.write_text("# No frontmatter\n", encoding="utf-8")
            _, error = parse_frontmatter(path)
            self.assertIsNotNone(error)


class RepositoryValidationTests(unittest.TestCase):
    def test_project_repository_passes_structural_validation(self):
        errors, _warnings = validate(ROOT)
        self.assertEqual(errors, [])

    def test_detects_directory_name_mismatch_and_bad_eval(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "skills" / "wrong-name").mkdir(parents=True)
            (root / "skills" / "wrong-name" / "SKILL.md").write_text(
                '---\nname: other-name\ndescription: "This description is long enough for validation checks."\n---\n# Example\n', encoding="utf-8"
            )
            (root / "evals" / "wrong-name").mkdir(parents=True)
            (root / "evals" / "wrong-name" / "cases.json").write_text(json.dumps({"skill": "wrong-name", "cases": []}), encoding="utf-8")
            (root / "README.md").write_text("", encoding="utf-8")
            errors, _warnings = validate(root)
            self.assertTrue(any("must match directory" in item for item in errors))
            self.assertTrue(any("at least 3 cases" in item for item in errors))
            self.assertTrue(any("missing catalog link" in item for item in errors))

    def test_detects_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill_dir = root / "skills" / "link-check"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                '---\nname: link-check\ndescription: "A focused description that satisfies validation limits."\n---\nRead [missing](references/not-here.md).\n', encoding="utf-8"
            )
            (root / "evals" / "link-check").mkdir(parents=True)
            cases = {"skill": "link-check", "cases": [{"id": f"case-{i}", "prompt": "Please do this realistic task", "expected_behaviors": ["Check the evidence"], "unacceptable_behaviors": ["Invent a result"]} for i in range(3)]}
            (root / "evals" / "link-check" / "cases.json").write_text(json.dumps(cases), encoding="utf-8")
            (root / "README.md").write_text("skills/link-check/SKILL.md", encoding="utf-8")
            errors, _warnings = validate(root)
            self.assertTrue(any("broken relative link" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
