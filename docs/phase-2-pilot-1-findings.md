# Phase 2 Pilot 1 aggregate findings

This report contains only non-reconstructive aggregate results from the first
private full Shadow Mode cycle. No diary wording, screenshots, source IDs,
notebook text, Anki content, or personal facts are included.

## Scope

The cycle completed:

- frozen experimental prediction and Pilot Bundle handoff;
- complete private source-archive validation;
- independent manual notebook and source-fidelity review;
- Manual-Gold Ledger materialisation;
- RM-8 target-level comparison and RM-9 calibration;
- learner-approved stable notebook finalisation;
- Anki import reconciliation;
- learner review of the rendered cards.

The experimental candidate remained prohibited from direct Anki import. The
Anki notes came from the separately reviewed stable Protocol v3.5 path.

## RM-8 aggregate comparison

The frozen prediction contained 17 candidates and the manual-gold ledger
contained 33 target decisions. The structural comparator reported:

| Outcome | Count |
| --- | ---: |
| Exact true positive | 4 |
| False positive | 7 |
| False negative | 23 |
| Partial target | 4 |
| Wrong learning function | 2 |
| Wrong Note Type | 0 |
| Semantic drift | 0 |

Under the current comparator's exact-match definition, precision was 36.4% and
recall was 14.8%. Partial-target and wrong-function matches are reported as
separate error classes rather than credited as exact matches. These metrics are
therefore a calibration baseline, not a claim about English ability or a final
card-level quality score.

The 33 manual-gold targets were later consolidated into 13 final Anki notes:
five Context Cloze, five Topic Retell, no standalone Vocabulary, and three
Guidance notes. Target counts and note counts are intentionally not treated as
equivalent units.

## Post-RM-8 card findings

Two card-design correction classes were recorded separately from RM-8:

1. One Guidance unit needed an already-authorised synonym alternative and its
   bilingual tested positions to remain aligned. Existing rules covered this;
   it was classified as an execution failure and did not create a new rule.
2. All five Topic Retell Fronts initially used a redundant task label and
   broad-topic cues that did not preserve the complete logical skeleton. The
   learner-approved correction removed the label, used arrows for progression
   or causality, and used semicolons for parallel information. This was
   classified as insufficient enforcement of the existing concise-cue rule.

The Topic Retell clarification has been added consistently to the experimental
specification, Shadow Mode profile, and replacement ChatGPT Project
Instructions. A repository test prevents those three surfaces from silently
drifting apart.

## Decision

The cycle is complete as a private learning cycle, but the system is not
production-ready. Automatic target selection, automatic Anki import, and any
reduction in human review remain blocked. At least one further independent
Shadow Mode cycle is required, and review thresholds must be based on repeated
error-class and false-pass evidence rather than pilot count alone.
