# Munyarwanda-Ai
Kinyarwanda-focused AI platform for building accessible, useful, and culturally relevant AI experiences.

🇷🇼 **Munyarwanda AI**

Created and developed by **Mukamyi Izere Arcange**.

## LLM Development Pipeline

The repository now includes the reproducible **Munyarwanda AI LLM v0.1** training pipeline under [`llm/`](llm/).

The pipeline covers:

- approved Kinyarwanda dataset acquisition and provenance
- dataset validation and quality gates
- PII/safety review workflow
- deduplication before splitting
- tokenizer analysis
- Kinyarwanda benchmark evaluation
- candidate base-model comparison
- QLoRA/LoRA fine-tuning
- held-out evaluation and error analysis
- OpenAI-compatible inference API for integration with the web application

### Current model status

The LLM pipeline is ready for execution, but a final trained model is **not claimed yet**. Actual training requires approved data, GPU benchmark measurements, a selected base model, a real QLoRA run, and evaluation.

### Recommended execution order

```text
DATA → VALIDATE → DEDUP → BENCHMARK → SELECT MODEL → QLoRA PILOT → EVALUATE → TRAIN v0.1 → SERVE → INTEGRATE
```

See [`llm/README.md`](llm/README.md) for the complete workflow.

## Project areas

- 🇷🇼 Kinyarwanda Language AI
- 🤖 Large Language Models
- 🧠 Natural Language Processing
- 🔎 Retrieval-Augmented Generation (RAG)
- 💬 AI Assistants
- 📚 Language Technology
- ⚙️ AI Engineering

## Important

Do not commit passwords, API keys, restricted datasets, private credentials, or copyrighted source text that you are not permitted to redistribute. Use provenance and license records for every training source.

© 2026 Mukamyi Izere Arcange. All rights reserved for the proprietary application code unless a file or dependency states otherwise. Third-party model and dataset terms remain applicable to their respective materials.
