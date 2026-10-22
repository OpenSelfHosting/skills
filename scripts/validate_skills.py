#!/usr/bin/env python3
"""Dependency-free structural validator for OpenSelfHosting Skills."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "SKILL.md must begin with YAML frontmatter opened by ---"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, "YAML frontmatter closing --- was not found"
    values: dict[str, str] = {}
    # This repository's required scalar fields are intentionally simple. Nested metadata is ignored.
    for line in lines[1:end]:
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        match = KEY_RE.match(line)
        if not match:
            return values, f"Unsupported or malformed frontmatter line: {line!r}"
        key, value = match.groups()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            value = value[1:-1].replace('\\"', '"').replace('\\\\', '\\')
        elif value.startswith("'") and value.endswith("'") and len(value) >= 2:
            value = value[1:-1].replace("''", "'")
        values[key] = value
    return values, None


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return ["Missing skills/ directory"], []

    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skill_dirs:
        errors.append("No skill directories found under skills/")

    discovered: set[str] = set()
    for directory in skill_dirs:
        name = directory.name
        discovered.add(name)
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"skills/{name}: directory name must be lowercase kebab-case and <= 64 characters")
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"skills/{name}: missing SKILL.md")
            continue
        props, parse_error = parse_frontmatter(skill_file)
        if parse_error:
            errors.append(f"skills/{name}/SKILL.md: {parse_error}")
            continue
        for key in ("name", "description"):
            if not props.get(key, "").strip():
                errors.append(f"skills/{name}/SKILL.md: missing required frontmatter field {key!r}")
        if props.get("name") != name:
            errors.append(f"skills/{name}/SKILL.md: frontmatter name {props.get('name')!r} must match directory")
        description = props.get("description", "")
        if len(description) > 1024:
            errors.append(f"skills/{name}/SKILL.md: description exceeds 1024 characters")
        if len(description) < 30:
            warnings.append(f"skills/{name}/SKILL.md: description may be too vague (< 30 characters)")
        body_lines = skill_file.read_text(encoding="utf-8").splitlines()
        if len(body_lines) > 500:
            errors.append(f"skills/{name}/SKILL.md: exceeds 500 lines ({len(body_lines)})")
        if len(body_lines) > 350:
            warnings.append(f"skills/{name}/SKILL.md: approaching 500-line guidance ({len(body_lines)} lines)")

        # Check simple relative Markdown links to files/directories within the skill.
        for lineno, line in enumerate(body_lines, start=1):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith(("#", "mailto:")):
                    continue
                rel_target = target.split("#", 1)[0].split("?", 1)[0]
                if not rel_target:
                    continue
                resolved = (directory / rel_target).resolve()
                if not resolved.is_relative_to(directory.resolve()):
                    errors.append(f"skills/{name}/SKILL.md:{lineno}: link escapes skill directory: {target}")
                elif not resolved.exists():
                    errors.append(f"skills/{name}/SKILL.md:{lineno}: broken relative link: {target}")

        eval_file = root / "evals" / name / "cases.json"
        if not eval_file.is_file():
            errors.append(f"skills/{name}: missing evals/{name}/cases.json")
        else:
            try:
                data = json.loads(eval_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                errors.append(f"evals/{name}/cases.json: invalid JSON ({exc})")
                continue
            if data.get("skill") != name:
                errors.append(f"evals/{name}/cases.json: skill field must equal {name!r}")
            cases = data.get("cases")
            if not isinstance(cases, list) or len(cases) < 3:
                errors.append(f"evals/{name}/cases.json: expected at least 3 cases")
                continue
            seen_ids: set[str] = set()
            for idx, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    errors.append(f"evals/{name}/cases.json: case {idx} must be an object")
                    continue
                case_id = case.get("id")
                if not isinstance(case_id, str) or not case_id.strip():
                    errors.append(f"evals/{name}/cases.json: case {idx} needs a non-empty id")
                elif case_id in seen_ids:
                    errors.append(f"evals/{name}/cases.json: duplicate case id {case_id!r}")
                else:
                    seen_ids.add(case_id)
                if not isinstance(case.get("prompt"), str) or len(case["prompt"].strip()) < 10:
                    errors.append(f"evals/{name}/cases.json: case {case_id or idx} needs a realistic prompt")
                for key in ("expected_behaviors", "unacceptable_behaviors"):
                    value = case.get(key)
                    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                        errors.append(f"evals/{name}/cases.json: case {case_id or idx} needs non-empty string list {key}")

    # Detect eval directories with no matching skill.
    eval_root = root / "evals"
    if eval_root.is_dir():
        for eval_dir in sorted(p for p in eval_root.iterdir() if p.is_dir()):
            if eval_dir.name not in discovered:
                errors.append(f"evals/{eval_dir.name}: no matching skill directory")

    # Check README has a catalog reference for every skill; human review still required for meaning.
    readme = root / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8")
        for name in sorted(discovered):
            if f"skills/{name}/SKILL.md" not in content:
                errors.append(f"README.md: missing catalog link for {name}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root (default: parent of scripts/)")
    args = parser.parse_args()
    root = args.root.resolve()
    errors, warnings = validate(root)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1
    print(f"Validation passed: {len([p for p in (root / 'skills').iterdir() if p.is_dir()])} skills; {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
