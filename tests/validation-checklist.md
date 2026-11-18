# Skill Validation Checklist

Validate every skill after editing.

## Structure
- [ ] Each skill lives in `.claude/skills/<kebab-case-name>/SKILL.md`.
- [ ] Each SKILL.md begins with valid YAML frontmatter delimited by `---`.
- [ ] `name` is lowercase kebab-case and matches the directory name.
- [ ] `description` explains both capability and explicit trigger conditions.
- [ ] The body contains actionable steps, not only generic role descriptions.
- [ ] Referenced relative files exist.

## Methodological quality
- [ ] Research question and unit of analysis are explicit.
- [ ] Data provenance, collection window, and sampling limitations are required.
- [ ] Operational definitions and denominators are stated for metrics.
- [ ] Computational outputs require validation and qualitative review.
- [ ] Findings distinguish observation, inference, and causal claims.
- [ ] Limitations and ethical safeguards are included.
- [ ] No claim of population representativeness from platform data alone.

## Operational test prompts
1. "Analyze this CSV of tweets about #JogjaOraDidol from January to March."
2. "Map citizen mentions and government replies for this official account."
3. "Combine topic modelling with qualitative coding for this corpus."
4. "Track whether this online issue appears in official policy documents."
5. "Write a methods section and identify the limits of this dataset."

## Expected behavior
- Select one or more matching skills based on their descriptions.
- Ask only for missing information that changes the analysis materially.
- Inspect supplied files and schema before proposing transformations.
- Never fabricate datasets, quotes, metrics, API access, or policy chronology.
- Produce a reproducible analysis plan even when the supplied data is insufficient.
