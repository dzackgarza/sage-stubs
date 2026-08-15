#!/usr/bin/env python3
"""Assert that the full-tree quality gates cannot silently degrade.

This check is intentionally independent of the workflow engine. It catches
edits that remove an analyzer, scope type checking back to generated/changed
files, enable a baseline, or weaken the strict configurations.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def require_text(path: Path, needles: list[str], errors: list[str]) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"{path.relative_to(ROOT)} is missing", errors)
        return ""
    for needle in needles:
        if needle not in text:
            fail(f"{path.relative_to(ROOT)} must contain `{needle}`", errors)
    return text


def check_pyproject(errors: list[str]) -> None:
    path = ROOT / "pyproject.toml"
    data = tomllib.loads(path.read_text(encoding="utf-8"))

    mypy = data.get("tool", {}).get("mypy", {})
    required_true = {
        "strict",
        "disallow_any_expr",
        "disallow_any_decorated",
        "disallow_any_unimported",
        "disallow_any_generics",
        "disallow_subclassing_any",
    }
    for key in sorted(required_true):
        if mypy.get(key) is not True:
            fail(f"pyproject.toml [tool.mypy].{key} must be true", errors)
    if mypy.get("incremental") is not False:
        fail("pyproject.toml [tool.mypy].incremental must be false", errors)
    if mypy.get("follow_imports") != "normal":
        fail("pyproject.toml [tool.mypy].follow_imports must be normal", errors)

    selectors = set(data.get("tool", {}).get("ruff", {}).get("lint", {}).get("select", []))
    required_selectors = {"E4", "E7", "E9", "F", "I", "ANN", "UP", "PYI", "RUF"}
    missing = required_selectors - selectors
    if missing:
        fail(f"pyproject.toml Ruff selectors missing {sorted(missing)}", errors)


def check_basedpyright(errors: list[str]) -> None:
    path = ROOT / "pyrightconfig.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("pyrightconfig.json is missing", errors)
        return

    expected = {
        "typeCheckingMode": "strict",
        "reportAny": "error",
        "reportExplicitAny": "error",
        "reportMissingImports": "error",
        "reportUnknownParameterType": "error",
        "reportUnknownArgumentType": "error",
        "reportUnknownVariableType": "error",
        "reportUnknownMemberType": "error",
        "reportMissingParameterType": "error",
        "reportMissingTypeArgument": "error",
        "reportUntypedBaseClass": "error",
        "reportUnannotatedClassAttribute": "error",
        "reportUnusedImport": "error",
        "reportInvalidCast": "error",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            fail(f"pyrightconfig.json {key} must be {value!r}", errors)
    if data.get("enableTypeIgnoreComments") is not False:
        fail("pyrightconfig.json enableTypeIgnoreComments must be false", errors)
    if any("baseline" in key.lower() for key in data):
        fail("pyrightconfig.json must not enable a diagnostic baseline", errors)


def check_workflows(errors: list[str]) -> None:
    quality = require_text(
        ROOT / ".github" / "workflows" / "stub-quality.yml",
        [
            "schedule:",
            "ruff format --check sage-stubs/",
            "Run strict mypy over every committed stub",
            "--no-incremental",
            "--follow-imports=normal",
            "sage-stubs/",
            "basedpyright --project pyrightconfig.json --outputjson",
            "semgrep scan",
            "scripts/audit_stub_quality.py",
            "--fail-on warning",
            "scripts/check_guardrails.py --all",
            "scripts/check_quality_config.py",
            "actions/upload-artifact@v7",
        ],
        errors,
    )
    populate = require_text(
        ROOT / ".github" / "workflows" / "populate-stubs.yml",
        [
            "Ruff formatting, complete stub surface",
            "Mypy strict, complete tree",
            "--no-incremental",
            "--follow-imports=normal",
            "sage-stubs/",
            "Basedpyright strict, complete tree",
            "basedpyright --project pyrightconfig.json --outputjson",
            "Semgrep generated and erased-type audit",
            "scripts/audit_stub_quality.py",
            "--fail-on warning",
            "Require every validator",
            "scripts/check_quality_config.py",
        ],
        errors,
    )

    for path, text in (
        (".github/workflows/stub-quality.yml", quality),
        (".github/workflows/populate-stubs.yml", populate),
    ):
        if re.search(r"mypy[^\n]*changed-stubs|changed-stubs[^\n]*mypy", text):
            fail(f"{path} scopes mypy to changed/generated files", errors)
        if re.search(r"basedpyright[^\n]*(?:changed|generated)-stubs", text):
            fail(f"{path} scopes basedpyright to changed/generated files", errors)


def check_hook(errors: list[str]) -> None:
    require_text(
        ROOT / ".githooks" / "pre-commit",
        ["scripts/check_quality_config.py"],
        errors,
    )


def check_semgrep(errors: list[str]) -> None:
    required_rules = [
        "sage-stubs.generated-scaffold",
        "sage-stubs.fabricated-sage-object",
        "sage-stubs.explicit-any",
        "sage-stubs.builtins-object-erasure",
        "sage-stubs.opaque-object-signature",
        "sage-stubs.object-return-type",
        "sage-stubs.erased-generic-argument",
        "sage-stubs.domain-parameter-as-scalar",
        "sage-stubs.generated-class-without-bases",
        "sage-stubs.blanket-arithmetic-self",
        "sage-stubs.local-diagnostic-suppression",
        "sage-stubs.generator-object-fallback",
        "sage-stubs.generator-placeholder-fallback",
        "sage-stubs.generator-name-based-integer-guess",
    ]
    require_text(
        ROOT / ".semgrep" / "stub-quality.yml",
        [f"id: {rule}" for rule in required_rules],
        errors,
    )


def main() -> int:
    errors: list[str] = []
    check_pyproject(errors)
    check_basedpyright(errors)
    check_workflows(errors)
    check_hook(errors)
    check_semgrep(errors)

    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        print(f"\n{len(errors)} quality-configuration violation(s).", file=sys.stderr)
        return 1

    print("quality configuration: full-tree gates present and strict.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
