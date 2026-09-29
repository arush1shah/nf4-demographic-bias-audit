# Publication release checklist

## Already complete

- [x] Canonical benchmark filename selected.
- [x] Publication notebook updated to use the canonical filename and output paths.
- [x] Benchmark validated as 715 rows, 55 scenario IDs, and 13 variants.
- [x] Repository excludes research drafts, temporary audit folders, caches, and credentials.
- [x] Dataset card, third-party-data notice, environment specification, and validation script added.

## Required before the repository becomes public

- [ ] Run every analysis reported in the final paper.
- [ ] Run the Colab release-file audit and resolve every missing row marked `Required = True`.
- [ ] Copy the generated item-level predictions, run manifests, selected row IDs, and statistical summaries into `results/` using the mapping in `results/README.md`.
- [ ] Confirm that the archived outputs reproduce the numbers in the final paper.
- [ ] Run `python scripts/validate_release.py --strict`.
- [ ] Create the permanent archive/DOI after the public repository contents are final.

## Optional

- [ ] Copy rendered figures into `figures/` if required by the venue or desired for convenience.
- [ ] Add a sanitized multiple-choice-only quality-audit workbook to `quality_control/`.
