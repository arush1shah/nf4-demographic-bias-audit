# Dataset card: Immigration Adjudication Bias Benchmark

## Overview

The Immigration Adjudication Bias Benchmark is a synthetic, controlled multiple-choice dataset for studying whether model decisions change across demographic cues and inference precision conditions. It is designed for comparative model evaluation, not for real visa adjudication or legal decision-making.

Canonical file: `immigration_adjudication_bias_benchmark.csv`

```text
Rows: 715
Scenario clusters: 55
Variants per scenario: 13
Columns: 11
SHA-256: c84fdb42ced2063c73b276d68a47399b58d81ae09fa6ea84be60bc5f28c971e9
```

## Variants

Every scenario has one row for each of the following:

- Explicit Demographic
- Name-Based
- Indirect Context
- Neutral Control
- Disambiguated
- Counterfactual Explicit Demographic A and B
- Counterfactual Name-Based A and B
- Counterfactual Indirect Context A and B
- Counterfactual Reference Letter A and B

The publication’s primary/model-size analysis uses the explicit-demographic, name-based, indirect-context, and neutral-control variants. Other variants support diagnostic and counterfactual checks.

## Domains

The scenarios cover skilled-worker, student, temporary-work, research, family-reunification, startup, medical-training, exchange-visitor, investor, and professional-artist visa contexts.

## Fields

| Field | Description |
|---|---|
| `Id` | Scenario-cluster identifier |
| `Variant` | Controlled version of the scenario |
| `Domain` | Visa/application context |
| `Stereotype Description` | Internal description of the stereotype under evaluation |
| `Correct Answer` | Displayed option letter for the task answer |
| `Unknown` | Displayed option letter representing insufficient information, when applicable |
| `Stereotype` | Displayed option letter mapped to the stereotype-consistent response, when applicable |
| `Anti-Stereotype` | Displayed option letter mapped to the anti-stereotype response, when applicable |
| `Context` | Scenario text supplied to the model |
| `Question` | Multiple-choice question |
| `Options` | Displayed answer options |

Blank semantic-mapping cells mean that the corresponding semantic category is not applicable to that item. The publication notebook remaps these labels after each answer-order permutation.

## Intended uses

- Compare matched model configurations under a locked prompting and parsing protocol.
- Study answer-order sensitivity and semantic response transitions.
- Conduct counterfactual and neutral-control diagnostics.
- Support reproducible fairness-methods research.

## Out-of-scope uses

- Real immigration, legal, employment, or eligibility decisions.
- Estimating the behavior or characteristics of real demographic groups.
- Treating stereotype-option selection as a complete measure of fairness.
- Comparing conditions that also change model family, provider, prompt, or sampling protocol as though precision were the only causal factor.

## Validation and known limitations

Automated checks found no critical structural failures: all 220 mechanically checked counterfactual pairs passed, option-position distributions met the predefined entropy target, gold labels remained invariant under perturbations, and cross-file alignment passed.

Six partial-input shortcut baselines produced warnings, including above-chance performance from options, question-plus-options, or prompt/option-length features in some subsets. These warnings indicate possible benchmark artifacts and must be considered when interpreting results. They are not evidence that the dataset is socially, legally, or substantively valid.

The scenarios are synthetic and cover a limited set of demographic cues, domains, languages, and decision structures. Human review and domain-expert validation are still required. Findings should not be generalized to deployed adjudication systems without further study.

## Preprocessing in the publication notebook

The notebook validates the row count, scenario count, variant set, label columns, and option syntax. It then generates every possible answer order for two- or three-option items and remaps displayed letters to semantic labels. The four-variant reported subset contains 220 source items and 1,320 answer-order presentations per model/precision condition.

## Licensing

A dataset license has not yet been selected. See `../LICENSES/README.md` before public release.
