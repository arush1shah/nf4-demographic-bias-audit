# NF4 Quantization and Demographic Bias

This repository accompanies **“Does NF4 Quantization Amplify Demographic Bias?”** It contains the publication reproduction notebook, the Immigration Adjudication Bias Benchmark, and the structure needed to archive item-level model outputs, run manifests, and statistical summaries.

## Release status

This is a **release candidate**. The notebook and benchmark are present and validated. Before making the repository public, the final model-output folders must be copied from Colab and checked against the final paper.

## Repository contents

| Path | Purpose |
|---|---|
| `notebooks/fairness_bias_audit_publication.ipynb` | End-to-end publication notebook for the reported immigration benchmark, model-size, BBQ, CrowS-Pairs, and exploratory COMPAS analyses |
| `data/immigration_adjudication_bias_benchmark.csv` | Authored 715-row benchmark used by the notebook |
| `data/DATASET_CARD.md` | Dataset construction, fields, intended use, and limitations |
| `data/THIRD_PARTY_DATA.md` | Upstream datasets retrieved by the notebook and therefore not vendored here |
| `results/` | Destination for item-level predictions, manifests, selected row IDs, and statistical summaries |
| `environment/requirements.txt` | Python dependencies pinned or bounded by the notebook |
| `figures/` | Optional rendered figures; all figures are regenerated from released results |
| `quality_control/` | Optional location for a sanitized automated quality-audit artifact |
| `scripts/validate_release.py` | Static release validator; use `--strict` immediately before publication |

## Reproduce the analyses

1. Open the [publication Colab](https://colab.research.google.com/drive/1oguS6yAjgPbft-Gg438hqTYzuhYW5IcI).
2. Select a GPU runtime.
3. Run the environment cell.
4. Upload `data/immigration_adjudication_bias_benchmark.csv` when requested.
5. Run the numbered sections in order. The COMPAS cell is gated because it includes paid OpenRouter calls.
6. Run the final release-file audit. Files marked `Required = True` belong in `results/`; rendered figures are optional.
7. Copy all required output files out of `/content` before the Colab runtime ends.

The notebook records environment information, model identifiers, source checksums, and item-level predictions. Reruns should report newly observed results rather than replace them with the archived headline values printed in the notebook.

## Benchmark integrity

The released CSV contains 715 rows: 55 scenario clusters, each represented by 13 controlled variants. Its SHA-256 checksum is:

```text
c84fdb42ced2063c73b276d68a47399b58d81ae09fa6ea84be60bc5f28c971e9
```

Automated validation found no critical structural failures. Six partial-input shortcut baselines produced non-critical warnings; these are documented in the dataset card and should not be interpreted as proof of demographic or legal validity.

## Third-party assets

BBQ, CrowS-Pairs, and the COMPAS-derived source table are retrieved from their upstream projects by the notebook. They are not relicensed by this repository. Qwen checkpoints are accessed through Hugging Face. The OpenRouter analysis requires the user’s own API key; credentials must never be committed.
