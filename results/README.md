# Results archive

This directory is intentionally empty except for this guide until the final Colab run is complete. Do not substitute printed headline values for item-level outputs.

Copy the generated files into the following structure:

```text
results/
  environment/
    environment.json
  immigration_benchmark/
    data_preparation_manifest.json
    structure_aware_position_balanced_tests.csv
    core_ambiguous_transition_counts.csv
  model_size/
    qwen_size_answer_order_results.csv
    qwen_size_generation_manifest.json
    qwen_size_model_effects.csv
  bbq/
    bbq_selected_items.csv
    bbq_generation_parser_results.csv
    protocol_comparison_summary.csv
  crows_pairs/
    crows_pairs_item_results.csv
  compas/
    compas_fixed_500_pair_sample.csv
    compas_three_configuration_pair_results.csv
    compas_three_configuration_summary.csv
```

The final Colab cell displays the precise runtime path for each artifact and marks rendered figures as optional. Before committing outputs, inspect them for credentials, local absolute paths, or unrelated data.
