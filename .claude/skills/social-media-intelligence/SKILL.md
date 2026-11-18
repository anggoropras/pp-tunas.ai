---
name: social-media-intelligence
description: Build a rigorous social media intelligence workflow from supplied or lawfully collected platform data. Use when the user asks to collect, clean, profile, classify, analyze, visualize, or report social media posts, conversations, hashtags, engagement, sentiment, topics, or networks for research or policy analysis.
---

# Social Media Intelligence

## Purpose
Conduct reproducible, ethical, evidence-aware analysis of social media data. Treat platform data as a partial, algorithmically mediated trace of online activity, not a representative sample of the population.

## Workflow
1. **Clarify the research object.** Identify platform, account/keyword/hashtag, geography, period, unit of analysis (post, account, interaction, thread), research question, and intended inference.
2. **Check data provenance and permissions.** Record collection method, API/export source, access date, query, pagination, missing fields, sampling limits, platform terms, and applicable privacy constraints. Do not bypass access controls, scrape private content, or infer sensitive personal traits.
3. **Profile the corpus.** Report raw rows, unique IDs, duplicates, missingness, date coverage, languages, repost/quote/reply proportions, and exclusions. Preserve an immutable raw copy; create a documented analytical copy.
4. **Clean transparently.** Normalize Unicode and whitespace; preserve original text; standardize timestamps to UTC while retaining source timezone; handle URLs, mentions, hashtags, emojis, and reposts according to the research question. Never silently delete dialect, slang, spelling variation, or minority-language content.
5. **Analyze in layers.** Start with descriptive time series and engagement distributions. Add topic modelling, text classification/sentiment, and network analysis only when they answer explicit questions and data quality supports them.
6. **Validate.** Inspect samples of preprocessing and model outputs; manually code a stratified sample; report precision/recall/F1 where labels exist; test alternative topic counts, thresholds, and time windows; document uncertainty.
7. **Interpret.** Distinguish platform affordances, visible engagement, coordinated activity, organic participation, and public opinion. Avoid causal claims without a design that supports causality.
8. **Report reproducibly.** Deliver research question, corpus/provenance, operational definitions, methods, findings, limitations, ethical handling, source citations, and reusable code/configuration.

## Analytical modules
- Descriptive analytics: volume over time, unique authors, interaction types, engagement distributions, temporal spikes.
- Text analytics: language identification, keyness, n-grams, topic models, stance/sentiment only with validated labels or transparent model limitations.
- Network analytics: mention/reply/retweet/follow networks where available; define nodes, edges, direction, weights, isolates, time window, and centrality measures.
- Event analysis: compare issue events and official actions against time series; do not label a spike as a policy effect without additional evidence.

## Required safeguards
- Do not equate likes, reposts, or hashtag volume with agreement or representativeness.
- Do not identify private individuals or publish handle-level rankings unless ethically justified and necessary.
- Suppress or aggregate small groups when disclosure risk exists.
- Do not classify bots or coordinated actors from a single metric. Use multiple transparent indicators and label findings as probabilistic.
- Keep raw personal data out of public reports and Git repositories.
- Cite platform documentation and collection sources; record the date accessed.

## Output format
1. Executive summary
2. Research questions and scope
3. Data provenance and corpus profile
4. Operational definitions
5. Methods and validation
6. Results (tables/figures)
7. Interpretation for research or policy
8. Limitations and ethical considerations
9. Reproducibility appendix

## Completion criteria
The task is incomplete if provenance, time coverage, unit of analysis, exclusions, validation, or limitations are missing.
