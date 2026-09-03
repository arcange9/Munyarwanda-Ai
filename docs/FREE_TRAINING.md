# Free / No-Budget Training Path

## Recommended engine: Unsloth

Unsloth is an open-source training stack with local training support and free notebook workflows. It supports LoRA/QLoRA and can be used without starting a paid cloud training job.

Official project: https://github.com/unslothai/unsloth

## Practical route

1. Download datasets through the project acquisition scripts.
2. Validate license, provenance, PII, language and quality.
3. Prepare train/validation/test splits.
4. Start with a small 1B–4B class model pilot.
5. Use QLoRA/SFT first.
6. Evaluate on MunyarwandaBench before scaling.
7. Export the adapter/model and serve it through the existing provider abstraction.

## Compute options

- Local GPU: no cloud training bill, limited by your hardware.
- Free notebook environments such as Colab: GPU availability and limits vary and are not guaranteed.
- Hugging Face AutoTrain: local usage is free; hosted hardware can incur charges.

## Important

A free training tool does not make unlimited GPU compute free. The no-budget strategy is to use efficient QLoRA, small pilot models and free/available notebook compute, then scale only when evaluation shows the improvement is worth the compute.
