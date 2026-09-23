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
- A later reciprocal omission scan proposed six additional source-supported
  targets. All six were accepted after focused learner review, without changing
  the frozen historical prediction.
- The final stable output contained 32 notes: 10 Context Cloze, 5 Topic Retell,
  17 Vocabulary, and 0 Guidance. One existing Topic Retell note was also updated
  in place to integrate an approved expression naturally.
- Initial structural reconciliation found 26 notes and 26 generated cards, with
  no field, tag, deck, duplicate, template, or per-note card-count mismatch.
  Later learner visual review identified semantic card-design errors that those
  structural checks could not detect. Eleven existing notes were corrected in
  place; the note and card counts remained unchanged.

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
5. In bilingual Context Cloze, only the English target positions are removed.
   The Chinese Prompt remains a complete visible meaning cue; mirroring the
   English blanks in Chinese changes the retrieval task and is a design error.
6. Topic Retell validation must compare chronology, causality, and event
   identity against the approved notebook. Template validity and broad topic
   coverage cannot detect a misplaced event or an omitted material transition.
7. Manual Gold needs a reciprocal omission scan after source verification.
   Human review is a mandatory coverage floor but may itself omit or misclassify
   a useful source-supported target. Discoveries remain separately
   approval-gated, and possible human errors create a review alert rather than
   an automatic gold rewrite.
8. Topic Retell is itself a strong Feynman-style retrieval task. An exact phrase
   in its Back does not automatically require a paired card. Additional
   Vocabulary or Context Cloze is justified only by a distinct function such as
   synonym distinction, usage boundary, focused local retrieval, or later
   demonstrated failure. This routing policy remains provisional.

## Decision

The learner visually confirmed the last six added notes and the one updated
Topic Retell note after structural reconciliation. The second private cycle is
therefore complete. Production automation remains blocked. Two cycles show that
the governed private workflow can reach a verified final import, while target
selection, target boundaries, function assignment, supplementary review, and
card-design checks still require human judgement. Further independent cycles
are required before any review threshold can be relaxed.
