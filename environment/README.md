# Environment provenance

`requirements.txt` mirrors the dependency constraints installed by the publication notebook. PyTorch is intentionally not reinstalled because the Colab GPU image provides a CUDA-compatible build.

The notebook writes the exact active Python, GPU, and package information to `/content/shtem_publication_outputs/environment.json`. Copy that generated file to `results/environment/environment.json` after the final run; it is stronger provenance than the mutable Colab image name alone.
