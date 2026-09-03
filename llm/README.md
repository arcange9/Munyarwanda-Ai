# Munyarwanda AI LLM — Final v0.1 Pipeline

**Created by Mukamyi Izere Arcange**

This directory contains the production-oriented pipeline for building a Kinyarwanda-focused language model adapter and serving it behind the Munyarwanda AI web application.

## Status

This is an engineering-complete, reproducible pipeline. It does **not** falsely claim that a final model has already been trained. A real training run requires approved datasets, GPU benchmark measurements, base-model selection, QLoRA training, and evaluation.

## Pipeline

1. Acquire only datasets whose licenses/terms have been reviewed.
2. Clean and normalize text.
3. Run PII and safety filters.
4. Deduplicate before train/validation splitting.
5. Generate measurable corpus statistics.
6. Validate JSONL instruction data.
7. Compare tokenizers and candidate base models.
8. Run the Kinyarwanda benchmark.
9. Select the base model using measured results and hardware fit.
10. Run a QLoRA/LoRA pilot.
11. Evaluate on held-out data and benchmark items.
12. Perform error analysis.
13. Train the release adapter.
14. Serve the model through an OpenAI-compatible API.
15. Connect the Munyarwanda AI provider abstraction to the self-hosted endpoint.

## Candidate models

The included configuration evaluates Qwen3-1.7B-Base, Qwen3-4B-Base and Qwen3-8B-Base. They are candidates, not a predetermined winner. Verify current model-card terms before redistribution.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_environment.py
python scripts/acquire_hf.py --source manifests/source_manifest.json
python modeling/validate_dataset.py --input data/processed/instructions.jsonl
python modeling/tokenizer_analysis.py --model Qwen/Qwen3-1.7B-Base --text data/processed/text.jsonl
python evaluation/run_benchmark.py --model Qwen/Qwen3-1.7B-Base --benchmark data/benchmark/benchmark_v1.jsonl
python modeling/train_qlora.py --config configs/phase32.yaml --smoke-test
```

Real training starts only after the dataset and benchmark gates pass.
