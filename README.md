# Munyarwanda AI

🇷🇼 **Kinyarwanda-focused AI platform and LLM research project.**

Created and developed by **Mukamyi Izere Arcange**.

## What is included

This repository contains the web application and the reproducible LLM development pipeline in one project.

- ChatGPT-style streaming chat UI
- Kinyarwanda / English / mixed-language support
- Conversation history
- Authentication and ownership-protected conversations
- Markdown/code rendering without raw HTML injection
- Rate limiting
- Provider abstraction (OpenRouter, Groq, OpenAI-compatible, self-hosted Munyarwanda LLM)
- Optional Google web research with source cards
- Translation and exploration pages
- Dataset provenance and governance workflow
- Dataset validation, deduplication, quality/safety gates
- Kinyarwanda benchmark and tokenizer analysis
- QLoRA/LoRA training pipeline
- OpenAI-compatible inference server

## Google web research

The chat can search the web through **Google Programmable Search / Custom Search JSON API** when the user enables `Search web`, and it can also automatically search for queries that clearly require current information (for example latest news or current releases). Search credentials stay server-side in environment variables.

Set:

```env
GOOGLE_CSE_API_KEY=...
GOOGLE_CSE_ID=...
```

If Google search is not configured, normal chat continues to work.

## LLM status

The repository includes the complete engineering pipeline, but **does not claim that Munyarwanda AI LLM v0.1 has already been trained**. Training becomes a release only after approved datasets, real GPU runs, benchmark results, held-out evaluation, and human review are completed.

## Execution order

```text
DATA → VALIDATE → DEDUP → QUALITY/SAFETY → BENCHMARK → SELECT BASE MODEL
→ QLoRA PILOT → EVALUATE → ERROR ANALYSIS → TRAIN v0.1 → SERVE → INTEGRATE
```

See [`llm/README.md`](llm/README.md) and [`llm/docs/`](llm/docs/) for the model pipeline.

## Data and model policy

Do not commit secrets, API keys, private credentials, restricted datasets, or source text that you do not have permission to redistribute. Dataset and model licenses remain applicable to their original materials. Large binaries and model checkpoints should use appropriate external storage or Git LFS; GitHub blocks regular repository files over 100 MiB and recommends Git LFS for large files.

## License

The application and original project materials are proprietary unless a file or dependency explicitly states otherwise. Third-party datasets, models, and libraries retain their own licenses.

© 2026 Mukamyi Izere Arcange.
