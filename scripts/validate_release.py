#!/usr/bin/env python3
"""Validate the static publication release and, optionally, final artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "immigration_adjudication_bias_benchmark.csv"
NOTEBOOK = ROOT / "notebooks" / "fairness_bias_audit_publication.ipynb"
EXPECTED_SHA256 = "c84fdb42ced2063c73b276d68a47399b58d81ae09fa6ea84be60bc5f28c971e9"
EXPECTED_VARIANTS = {
    "Explicit Demographic",
    "Name-Based",
    "Indirect Context",
    "Neutral Control",
    "Disambiguated",
    "Counterfactual Explicit Demographic A",
    "Counterfactual Explicit Demographic B",
    "Counterfactual Name-Based A",
    "Counterfactual Name-Based B",
    "Counterfactual Indirect Context A",
    "Counterfactual Indirect Context B",
    "Counterfactual Reference Letter A",
    "Counterfactual Reference Letter B",
}
REQUIRED_COLUMNS = {
    "Id",
    "Variant",
    "Domain",
    "Stereotype Description",
    "Correct Answer",
    "Unknown",
    "Stereotype",
    "Anti-Stereotype",
    "Context",
    "Question",
    "Options",
}
STATIC_FILES = [
    ROOT / "README.md",
    ROOT / "RELEASE_CHECKLIST.md",
    ROOT / "CITATION.cff",
    ROOT / "data" / "DATASET_CARD.md",
    ROOT / "data" / "THIRD_PARTY_DATA.md",
    ROOT / "environment" / "requirements.txt",
    ROOT / "results" / "README.md",
]
STRICT_RESULTS = [
    "results/environment/environment.json",
    "results/immigration_benchmark/data_preparation_manifest.json",
    "results/immigration_benchmark/structure_aware_position_balanced_tests.csv",
    "results/immigration_benchmark/core_ambiguous_transition_counts.csv",
    "results/model_size/qwen_size_answer_order_results.csv",
    "results/model_size/qwen_size_generation_manifest.json",
    "results/model_size/qwen_size_model_effects.csv",
    "results/bbq/bbq_selected_items.csv",
    "results/bbq/bbq_generation_parser_results.csv",
    "results/bbq/protocol_comparison_summary.csv",
    "results/crows_pairs/crows_pairs_item_results.csv",
    "results/compas/compas_fixed_500_pair_sample.csv",
    "results/compas/compas_three_configuration_pair_results.csv",
    "results/compas/compas_three_configuration_summary.csv",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="require final outputs, URL, and licenses")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    for path in [*STATIC_FILES, DATASET, NOTEBOOK]:
        if not path.is_file():
            errors.append(f"Missing required static file: {path.relative_to(ROOT)}")

    if DATASET.is_file():
        if sha256(DATASET) != EXPECTED_SHA256:
            errors.append("Benchmark SHA-256 does not match the reviewed release candidate.")
        with DATASET.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 715:
            errors.append(f"Benchmark has {len(rows)} rows; expected 715.")
        if len({row["Id"] for row in rows}) != 55:
            errors.append("Benchmark must contain 55 scenario IDs.")
        if {row["Variant"] for row in rows} != EXPECTED_VARIANTS:
            errors.append("Benchmark variant set differs from the locked 13-variant design.")
        if set(rows[0]) != REQUIRED_COLUMNS:
            errors.append("Benchmark columns differ from the documented schema.")

    if NOTEBOOK.is_file():
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        notebook_text = "\n".join(
            "".join(cell.get("source", [])) for cell in notebook.get("cells", [])
        )
        for obsolete in [
            "custom_bias_dataset_nuanced_multiple_choice_corrected",
            "corrected_mc_answer_order_diagnostic",
        ]:
            if obsolete in notebook_text:
                errors.append(f"Notebook still contains obsolete reference: {obsolete}")
        if "immigration_adjudication_bias_benchmark.csv" not in notebook_text:
            errors.append("Notebook does not reference the canonical benchmark filename.")

    release_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in [ROOT / "README.md", NOTEBOOK]
        if path.is_file()
    )
    if "sk-or-v1-" in release_text:
        errors.append("Possible OpenRouter secret found in the release surface.")

    placeholder = "[PERMANENT REPOSITORY URL OR DOI]"
    if placeholder in release_text:
        warnings.append("Permanent repository URL/DOI has not been inserted.")
    if not any(path.name.lower().startswith("license") and path.name != "README.md" for path in (ROOT / "LICENSES").glob("*")):
        warnings.append("Code and dataset licenses have not been selected.")

    if args.strict:
        for relative in STRICT_RESULTS:
            if not (ROOT / relative).is_file():
                errors.append(f"Missing final result: {relative}")
        if placeholder in release_text:
            errors.append("Strict release still contains the repository URL/DOI placeholder.")
        if any("licenses have not been selected" in warning for warning in warnings):
            errors.append("Strict release requires explicit code and data licenses.")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\nRelease validation failed with {len(errors)} error(s).")
        return 1
    print("\nRelease validation passed." + (" Strict checks enabled." if args.strict else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
