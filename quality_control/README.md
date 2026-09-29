# Quality-control artifacts

The internal automated audit workbook is not included as-is because it contains local filesystem paths and sheets for open-ended datasets that are not part of the reported experiment.

If the workbook is published, first create a sanitized, multiple-choice-only copy that:

- replaces absolute local paths with repository-relative paths;
- removes unused open-ended-dataset sheets;
- retains the methodology, executive summary, multiple-choice checks, issues, pair details, position entropy, coverage, context lengths, and relevant correction log;
- clearly describes the six non-critical partial-input shortcut warnings; and
- states that automated validation is not a substitute for human, legal, or domain-expert review.
