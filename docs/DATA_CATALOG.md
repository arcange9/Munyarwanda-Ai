# Munyarwanda AI — Kinyarwanda Data Catalog

The repository stores dataset metadata and download/validation code, not large third-party raw datasets. Datasets should be downloaded at training time and checked for license, access, provenance, PII, quality, duplication and language before use.

## Priority groups

### Core Kinyarwanda text
- `mbazaNLP/kinyarwanda_monolingual_v01.1` — large Kinyarwanda monolingual collection; gated; review current terms before use.
- `Andrews2017/KINNEWS-and-KIRNEWS-Corpus` — Kinyarwanda news corpus for language and domain coverage.
- `Kinyarwanda-NLP/kinyarwandaTexts` — Kinyarwanda text collection and processing resources.

### Instruction, QA and retrieval
- `C4IR-RW/kinya-ag-retrieval` — Kinyarwanda agriculture retrieval/QA resource.
- Build a first-party instruction dataset from reviewed Kinyarwanda prompts and answers instead of relying only on translated English instructions.

### Language intelligence
- `anzeyimana/kinyabert-acl2022` — KinyaBERT resources and evaluation tasks.
- `masakhane-io/masakhane-ner` — NER evaluation including Kinyarwanda.
- `afrisenti-semeval-2023` — sentiment evaluation including Kinyarwanda.

### Translation
- `DigitalUmuganda/kinyarwanda-english-machine-translation-dataset` — Kinyarwanda↔English parallel data; verify the current dataset card before training use.

### Speech (separate track)
- Common Voice Kinyarwanda — ASR resource; do not put raw audio in this repository.
- `DigitalUmuganda/Afrivoice_Kinyarwanda` — multimodal/speech resource with controlled access.
- `mbazaNLP/kinyarwanda-tts-dataset` — TTS resource; gated.

### Rwanda grounding / RAG
- Official Rwanda public information and open-data sources can feed the knowledge layer.
- Store source URL, publisher, publication/update date, license and retrieval timestamp for each ingested document.

## Required metadata

Each source entry should record: source ID, URL/Hugging Face ID, license, access status, language, domain, approximate size, intended task, redistribution permission, PII risk, validation status and SHA-256 for downloaded artifacts.

## Training policy

Never train on a dataset merely because it is downloadable. The pipeline should fail closed when license/access metadata is missing or contradictory.
