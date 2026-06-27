---
cold_start: false
created: '2025-04-08'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1
tags:
- dataset
- nlp
- hugging_face
- web_scraping
type: entity
updated: '2025-04-08'
---

# FineWeb

FineWeb is a 15-trillion-token web-scale text dataset publicly released by Hugging Face's FineData team, designed for pretraining large language models. It was created by systematically decanting the Common Crawl web archive through a multi-stage filtering pipeline that removes low-quality and noisy content while retaining high-quality linguistic data. The dataset emphasizes rigorous deduplication, quality filtering based on text statistics, language detection, and removal of boilerplate content. FineWeb-Edu is a curated subset of FineWeb focusing on educational content, selected by classifier scores. The dataset is intended to provide researchers with a high-quality alternative to earlier web corpora, supporting reproducible language model research at scale.

## Key Claims

- FineWeb contains approximately 15 trillion tokens extracted from the Common Crawl web archive.
- The dataset undergoes multi-stage filtering including deduplication, quality filtering using text statistics, language identification, and boilerplate removal.
- FineWeb-Edu is a subset of FineWeb that selects educational content via a classifier, providing a higher-quality subset for domain-specific pretraining.
- The dataset is released by Hugging Face's FineData team and is publicly available for download.
- The creation process aims to produce a high-quality web text corpus suitable for large language model pretraining, addressing issues of noise and low-quality content in earlier web datasets.

## Relationships

No existing wiki pages are directly related to FineWeb as of this writing. Future pages might include connections to Common Crawl, other web-scale datasets, or Hugging Face's data ecosystem.

## Sources

- https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1
