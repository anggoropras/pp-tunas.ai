---
name: hybrid-text-analysis
description: Design and execute a hybrid method combining computational text mining with qualitative interpretation for social media, policy, public administration, and other unstructured text. Use when moving from large text corpora to explainable themes, frames, narratives, or evidence-based findings.
---

# Hybrid Text Mining and Qualitative Analysis

## Core principle
Text mining identifies patterns and reduces large corpora; qualitative analysis interprets meaning in context. Neither substitutes for the other. Treat computational outputs as leads for interpretation, not self-validating facts.

## Staged method
1. **Question and construct:** define the concept (topic, frame, stance, sentiment, claim, narrative) and how it differs from adjacent concepts.
2. **Corpus audit:** establish source, unit, dates, language, sampling, duplicates, missingness, and inclusion/exclusion rules.
3. **Preprocessing protocol:** preserve source text; create reproducible normalized fields; document tokenization, stopword lists, stemming/lemmatization, language-specific handling, and treatment of negation, sarcasm, slang, emojis, and code-switching.
4. **Exploration:** frequency, n-grams, collocations, keyness, temporal patterns, and co-occurrence. Use these to develop or refine a coding frame.
5. **Computational modelling:** choose a method suited to the question and corpus (e.g., topic model, supervised classifier, embeddings/clustering). Explain parameters, random seeds, software versions, and model selection. Avoid claiming topics are objectively discovered.
6. **Qualitative sampling:** select posts across topics, time periods, actors, engagement levels, and outliers. State the sampling logic and retain contradictory/negative cases.
7. **Close reading and coding:** code context, speaker position, target, claim, evidence, frame, affect, rhetorical device, stance, and interactional context as needed. Develop a codebook with definitions and inclusion/exclusion examples.
8. **Validation:** use multiple coders or review cycles where feasible; report agreement (e.g., Cohen's kappa or Krippendorff's alpha) only where assumptions and sample support it. Compare machine classifications to human-coded data and report errors.
9. **Integration:** create a joint display linking computational patterns to qualitative examples, explanations, counterexamples, and confidence.
10. **Conclusions:** distinguish descriptive pattern, interpretation, and causal explanation. State scope conditions and limitations.

## Model selection guidance
- Topic modelling: compare coherence and interpretability; inspect representative documents and topic stability. Do not label a topic from top words alone.
- Sentiment: use only where sentiment is a meaningful construct; distinguish sentiment toward target, emotion, stance, and policy support. Validate local language, sarcasm, and mixed sentiment.
- Classification: report training labels, class balance, split strategy, leakage controls, precision, recall, F1, confusion matrix, and threshold.
- Embeddings/clustering: report embedding model, distance metric, clustering method, parameters, and stability checks.
- Keyword/lexicon methods: document lexicon provenance and domain adaptation; do not treat generic sentiment dictionaries as ground truth for Indonesian discourse.

## Indonesian-language considerations
Preserve original spelling and code-switching alongside normalized text. Handle Bahasa Indonesia, Javanese, regional varieties, abbreviations, slang, affixes, reduplication, irony, and culturally specific references. Avoid destructive stemming before assessing its effect. Use domain- and period-specific stopwords; retain politically meaningful terms and negation.

## Required integration table
| Computational pattern | Qualitative interpretation | Supporting evidence | Counterexample | Confidence |
|---|---|---|---|---|
| Topic/theme cluster | Meaning in context | IDs or anonymized excerpts | Contradictory case | High/medium/low |

## Output
Include corpus audit; preprocessing decisions; model and parameters; validation results; codebook; integrated findings; examples and counterexamples; limitations; reproducibility instructions.
