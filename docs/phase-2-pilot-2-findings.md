# Phase 2 Pilot 2 aggregate findings

This report contains only non-reconstructive aggregate results from the second
privately completed Shadow Mode cycle. No diary wording, source-chat content,
screenshots, notebook text, Anki card content, source IDs, or personal facts are
included.

## Scope

The cycle completed the frozen Pilot Bundle handoff, private source validation,
independent manual notebook review, RM-8/RM-9 comparison, supplementary-target
review, learner-approved stable notebook finalisation, Anki import
reconciliation, and rendered-card confirmation.

The historical experimental candidate remained frozen. Later policy
clarification and card-design corrections were recorded separately rather than
used to improve the historical prediction.

## Aggregate outcomes

- Manual Gold contained 37 marked learning targets; final coverage was 37/37.
- Five prediction-only targets were routed to focused AI Supplementary review.
- All five supplements were accepted after evidence, usefulness,
  de-duplication, retrieval-boundary, and source-fidelity review.
- The final stable output contained 26 notes: 10 Context Cloze, 5 Topic Retell,
  11 Vocabulary, and 0 Guidance.
- Import reconciliation found 26 notes and 26 generated cards, with no field,
  tag, deck, duplicate, rendering, or per-note card-count mismatch.

The original structural comparator treated manual silence as rejection. That
made all five prediction-only targets appear to be false positives. The
historical result is preserved, but the reviewed outcomes are now classified as
Accepted AI Supplements. Manual-Gold coverage and supplementary acceptance are
therefore reported separately.

## Reusable findings

1. The manual notebook is a mandatory coverage floor, not an exclusive
   whitelist. Every valid manual mark must be covered, while source-supported
   prediction-only targets require a separate focused review.
2. Standalone Vocabulary verbs and phrasal verbs use context-independent
   citation forms. Incidental source tense belongs in examples or evidence
   unless the inflection itself is the target.
3. Near-synonyms with meaningful register, setting, institutional, relational,
   or pragmatic differences require an independently answerable usage-boundary
   unit and the `Type::SynonymContrast` tag.
4. All blanks in a Context Cloze unit intended as one card use `c1`. Later
   cloze indices require an intentional, learner-approved split, and generated
   card counts must be reconciled before import.

## Decision

The second private cycle is complete, but production automation remains
blocked. Two cycles show that the governed private workflow can reach a
verified final import, while target selection, target boundaries, function
assignment, supplementary review, and card-design checks still require human
judgement. Further independent cycles are required before any review threshold
can be relaxed.
