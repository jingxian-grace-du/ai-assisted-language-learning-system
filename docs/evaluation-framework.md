# Evaluation framework

## Why evaluation is separate from generation

A fluent notebook can still omit important targets, add unsupported meaning, assign the wrong retrieval task, or create excessive review burden. Generation quality must therefore be decomposed into independently measurable dimensions.

## Evaluation layers

### Source segmentation

- session-boundary accuracy;
- topic-boundary precision and recall;
- speaker and source-span attribution;
- unresolved-boundary rate.

### Learning-target selection

- target recall against an approved standard;
- target precision;
- missed explicit learning signals;
- unsupported targets;
- redundant-target rate;
- estimated review burden.

### Semantic fidelity

Check preservation of:

- actor and perspective;
- event and object;
- causal relationship;
- chronology;
- polarity;
- certainty and qualification;
- reported speech versus learner conclusion;
- stance and material factual detail.

### Notebook construction

- Note Type assignment accuracy;
- Context Cloze deletion quality;
- paired Topic Retell identity;
- Topic Retell Front logical-stage coverage without task-label redundancy or
  answer leakage;
- Vocabulary answerability;
- Guidance completeness;
- prompt–answer–highlight count, order, meaning, and boundary agreement.

### Operational correctness

- schema validity;
- deterministic gate results;
- rendered-display correctness;
- canonical export correctness;
- Anki reconciliation counts and field identity;
- learner confirmation of the rendered cards after import;
- privacy-gate result.

### Automation quality

- percentage advancing without review;
- percentage routed to appropriate review;
- false automatic-pass rate;
- unnecessary-review rate;
- correction effort per session;
- recurrence rate for previously classified error classes.

## Interpreting a 95% target

A statement such as “95% coverage” is incomplete unless it identifies:

- the evaluated unit;
- the authority or approved reference;
- whether the metric is precision, recall, or another measure;
- the dataset and evaluation period;
- treatment of ambiguous items;
- confidence intervals or sample limitations where relevant.

No pipeline metric should be presented as a percentage improvement in a learner's English ability.

## Gold standards and calibration

Historical human-reviewed notebooks can support private calibration, but they are not automatically perfect labels. An evaluation record should distinguish:

- explicit learner choices;
- protocol-required decisions;
- annotator judgement;
- later corrections;
- unresolved ambiguity.

Gold data must remain outside the public repository. Only aggregate, non-reconstructive metrics may be published.

## Release principle

An increase in automatic throughput is not an improvement if semantic drift, missed targets, privacy risk, or unnecessary review burden increases. Release decisions should use a balanced quality profile rather than one headline score.
