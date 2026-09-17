# Protocol gap analysis

## Purpose

The current protocol has evolved primarily through notebook correction, audit failures, rendering checks, Anki export, import reconciliation, and post-cycle review. It contains important enforcement mechanisms, but it does not yet specify the front of the pipeline with comparable precision.

This document separates mature areas from missing generation requirements before the protocol is revised again.

## Relatively mature areas

The existing system has substantial rules for:

- source-authority ordering and fallback;
- manual-mark-first processing during calibrated workflows;
- stable item-level coverage ledgers;
- technical definitions of tested coverage;
- semantic fidelity and prevention of unsupported rewriting;
- Context Cloze and paired Topic Retell consistency;
- Guidance completeness and prompt–answer–highlight alignment;
- bidirectional target-boundary audits;
- linked invalidation when one Guidance component changes;
- notebook content, card-design, and render gates;
- canonical Anki exports and bounded import copies;
- collection reconciliation;
- global same-error-class scans;
- post-cycle learning and protocol-delta classification.

These rules remain valuable. They should become executable specifications where possible rather than being discarded during front-end redesign.

## Primary missing layer: raw material to first notebook

The protocol does not yet define, with sufficient precision and testability:

### 1. Session and source boundaries

- What constitutes one diary session?
- How are interruptions, corrections, side conversations, and later additions represented?
- Which source content is immutable?
- How are user speech and AI speech distinguished?

### 2. Topic reconstruction

- What evidence starts, continues, merges, splits, or closes a topic?
- How are narrative, reflection, vocabulary search, and guidance related?
- How should uncertain topic boundaries be represented?

### 3. Learning-signal detection

Candidate signals include description of an unknown word, explicit language questions, repeated reformulation, accepted corrections, recurring misuse, unnatural but understandable phrasing, and explicit requests to retain an expression. The protocol must define evidence, precedence, and false-positive controls.

### 4. Learning-value selection

The system needs a governed method for balancing:

- personal communicative relevance;
- future reusability;
- evidence of imperfect mastery;
- naturalness and accuracy;
- independence from one-off details;
- memory burden;
- novelty relative to existing notes.

Card quotas must not replace learning-value judgement.

### 5. Canonical content construction

The protocol must say when grammar correction, naturalisation, consolidation, and removal of oral redundancy are permitted, and how each transformation remains linked to the source meaning.

### 6. Note-type assignment

The criteria for Context Cloze, Topic Retell, Vocabulary, Guidance, duplication across roles, consolidation, and rejection need machine-testable decision records.

### 7. Confidence and exception routing

The system needs calibrated thresholds and reasons for automatic passage, sampling, focused human review, unresolved conflict, and rejection.

### 8. Personalisation without uncontrolled inference

The system should learn a user's demonstrated target preferences and proficiency over time without inferring sensitive traits, allowing old generated output to validate new output, or silently changing the authority hierarchy.

## Research questions

- What is the smallest source span that preserves enough context for reliable selection?
- How should precision and recall be weighted when excessive cards impose a review cost?
- Can target selection be evaluated independently from wording quality?
- Which errors can deterministic validators catch, and which require semantic evaluation?
- How should evaluator disagreement be represented?
- When is a manual notebook a gold standard, and when is it merely one annotator's preference?
- How can the system estimate readiness for automatic export without masking uncertainty?

## Recommended protocol development method

1. freeze the current protocol as a documented baseline;
2. extract normative rules into uniquely identified requirements;
3. map each requirement to a pipeline stage, validator, and failure state;
4. define front-end schemas before adding prose rules;
5. develop a synthetic conformance suite;
6. evaluate generation privately against separately stored approved standards;
7. classify every failure before revising the protocol;
8. promote only generalisable, sufficiently evidenced rules.

The next protocol version should be a controlled architectural revision, not an accumulation of isolated patches.
