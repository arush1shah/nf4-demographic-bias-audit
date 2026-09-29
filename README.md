# NF4 Quantization and Demographic Bias

This repository contains the publication notebook and custom dataset for **“Does NF4 Quantization Amplify Demographic Bias?”**

## Files

- `Fairness_Bias_Audit_Publication.ipynb` — the complete Colab notebook.
- `data/immigration_adjudication_bias_benchmark.csv` — the 715-row Immigration Adjudication Bias Benchmark.
- `data/DATASET_CARD.md` — information about the dataset, its fields, intended uses, and limitations.

## Run the notebook

Open the [publication notebook in Google Colab](https://colab.research.google.com/drive/1oguS6yAjgPbft-Gg438hqTYzuhYW5IcI?usp=sharing), select a GPU runtime, and run the numbered cells in order. When prompted, upload `immigration_adjudication_bias_benchmark.csv` from the `data` folder.

The notebook downloads the third-party benchmark sources used by the reported analyses. The COMPAS/OpenRouter section is gated because it can make paid API calls.
