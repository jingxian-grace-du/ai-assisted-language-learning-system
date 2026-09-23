# Phase 2 calibration workflow

Phase 2 learns from future use without requiring the learner to design a complete
generation protocol in advance.

## Private cycle

```text
Complete source archive
→ topic evidence packets
→ experimental notebook prediction
→ independent manual notebook
→ Codex private source archive and source-fidelity review
→ Codex Manual-Gold Ledger and source-linked comparison
→ error classification and same-class scan
→ specification delta decision
→ learner-approved stable notebook and card-design audit
→ Anki import reconciliation and rendered-card confirmation
→ post-cycle completion record
```

The manual notebook and all comparison content remain outside the repository.
The ChatGPT Project stage ends after the Pilot Bundle is frozen. RM-8, RM-9 and
protocol calibration run in Codex against a complete private source archive.

## What the learner reviews

The learner does not review protocol paragraphs. The learner edits or confirms
the notebook in the normal way. The system converts those edits into structured
differences and asks a question only when source evidence and existing authority
cannot resolve a material ambiguity.

The manual notebook defines mandatory coverage, not an exclusive whitelist.
Every valid manual mark must be represented unless the learner explicitly
approves exclusion. Prediction-only targets remain in a separate AI
Supplementary review queue until the learner accepts or rejects them against
source fidelity, usefulness, de-duplication, retrieval boundary, and evidence.
Their provenance remains in the private audit trail but need not appear on the
final Anki card.

## What the system learns

The comparison distinguishes:

- topic-boundary preferences;
- selected and rejected learning targets;
- unfamiliar vocabulary versus complete-expression targets;
- Guidance selection;
- target boundaries;
- Note Type choices;
- citation-form normalisation;
- synonym and usage-boundary routing;
- expected versus generated Cloze card counts;
- complete visible Chinese Context Cloze prompts;
- Topic Retell chronology, causality, and event identity;
- semantic-fidelity failures;
- unnecessary review burden.

Only generalisable differences become specification changes. One-off content
choices remain calibration data rather than global rules.

## Two calibration stages

RM-8 compares the frozen experimental prediction with independent manual gold.
It measures topic segmentation, target selection, target boundaries, learning
function, and proposed Note Type without using later card corrections to improve
the historical prediction.

After manual content approval, the workflow re-enters Protocol v3.5. Card
design, rendering, export, import, reconciliation, and live review form a
separate post-RM-8 stage. Corrections in that stage are retained in the
post-cycle learning record and classified independently. This prevents a good
final Anki card from hiding an earlier prediction or card-design error.

The private cycle is complete only when both tracks are evidenced: RM-8/RM-9
are materialised, and the stable master, export, import reconciliation, and
learner review have passed. The frozen experimental manifest remains
`anki_ready: false` throughout; only the separately approved stable output may
enter Anki.

## Automation progression

```text
full notebook review
→ difference-only review
→ low-confidence and exclusion review
→ high-confidence sampling
→ exception-only review
```

The transition between levels depends on measured false automatic passes and
correction effort, not the number of completed sessions alone.
