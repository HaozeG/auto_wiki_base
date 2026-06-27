---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.1
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 1.0
  self_containedness: 1.0
sources:
- https://kili-technology.com/blog/fineweb2-dataset-guide
tags:
- nlp
- dataset
- multilingual
- common-crawl
- llm-training
- fineweb
type: entity
updated: '2026-06-26'
---

# FineWeb2 Dataset

FineWeb2 is a large-scale multilingual pre-training dataset comprising 20 terabytes of text data covering over 1,000 languages, constructed from 96 snapshots of Common Crawl. It was published in January 2026 as part of the FineWeb family of datasets. The dataset employs a language-adaptive filtering pipeline that applies per-language quality thresholds, integrates deduplication as a sampling signal rather than a hard removal step, and validates filter effectiveness against reference datasets including Wikipedia and OSCAR. FineWeb2 is designed for training large language models (LLMs) with broad linguistic coverage, and it provides guidelines for mixing its multilingual content with English-heavy corpora using temperature sampling. Its scale and multilingual breadth make it a significant resource for improving LLM performance on low-resource languages.

## Key Claims

- FineWeb2 contains 20 TB of text data across over 1,000 languages.
- It was built from 96 snapshots of Common Crawl.
- The dataset uses a language-adaptive filtering pipeline with separate quality thresholds per language.
- Deduplication is treated as a sampling signal, not a strict removal criterion, to preserve data diversity.
- Reference datasets such as Wikipedia and OSCAR are used to validate the quality filters.
- Mixing FineWeb2 with English-dominant training data is recommended using temperature sampling for balanced coverage.
- The dataset was released in January 2026.

## Relationships

FineWeb2 has no documented relationships with other entities currently covered in this wiki. Potential future connections include pages on Common Crawl, multilingual LLM training, and dataset curation pipelines.

## Sources

- Kili Technology: "A Guide to the FineWeb2 Dataset: How It's Built, Filtered, and Used for Training LLMs" (2026): https://kili-technology.com/blog/fineweb2-dataset-guide

