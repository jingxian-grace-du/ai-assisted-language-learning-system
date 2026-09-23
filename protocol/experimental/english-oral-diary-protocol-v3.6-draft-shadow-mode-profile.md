# English Oral Diary Protocol v3.6-draft

## Phase 2 Shadow Mode Profile

- Status: Experimental execution profile
- Stable baseline: English Oral Diary Protocol v3.5
- Experimental extension: Raw Material Processing Specification v0.1
- Technical export contract: Phase 2 Interchange Contract v0.1
- Intended environment: Private ChatGPT Project with project-only memory
- Automatic Anki export or import: Prohibited
- Promotion status: Not a stable Protocol release
- Pilot clarification: 0.1.3 (coverage floor, lexical citation forms, contrast
  routing, and single-card Cloze enforcement)

## 1. Purpose

This profile makes the experimental Raw Material Processing Specification v0.1
executable during the next English Oral Diary cycle without weakening or
silently replacing the validated Protocol v3.5 workflow.

Protocol v3.5 remains authoritative for established night-session behaviour,
morning retrieval, manual-notebook authority, content and card audits,
finalisation, canonical export, Anki import, reconciliation, and post-cycle
learning.

Specification v0.1 governs only the experimental path from complete raw source
material to the first structured notebook candidate and its comparison with the
manual notebook.

Phase 2 Interchange Contract v0.1 governs only machine-readable Pilot Bundle
and Manual-Gold Ledger export structure. It does not change semantic authority
or the learning workflow.

If the two documents conflict outside that experimental scope, Protocol v3.5
controls. Within the experimental scope, a material unresolved conflict blocks
progress and must be recorded rather than inferred away.

## 2. Activation and mode state

### 2.1 Activation trigger

Enable this profile only when the learner says exactly:

```text
English Oral Diary — Phase 2 Shadow Mode
```

The ordinary trigger `English oral diary` continues to start stable Protocol
v3.5 unless the learner explicitly requests Phase 2 Shadow Mode.

### 2.2 Required activation acknowledgement

Before free speaking begins, report:

```text
Stable baseline: Protocol v3.5
Experimental extension: Raw Material Processing Specification v0.1
Execution profile: Protocol v3.6-draft — Phase 2 Shadow Mode
Interchange contract: Phase 2 Interchange Contract v0.1
Automatic Anki export/import: disabled
Session ID: <stable ID>
Open topic: none
Source capture status: ready
```

If any required project source cannot be read, do not claim that Shadow Mode is
active. Identify the missing source and remain in stable mode or wait for the
learner's direction.

### 2.3 Session identity

Assign one stable session ID:

```text
EOD-YYYY-MM-DD-S01
```

Every topic, source span, evidence packet, checkpoint, candidate, and audit
result created during the cycle must link to this session ID.

## 3. Source capture

### 3.1 Source of truth

The complete current project chat is the private Conversation Source Archive for
the first Shadow Mode pilot. Do not reconstruct the archive from memory,
summaries, Topic Reference Checkpoints, or the Night Reference Record.

Assign stable sequential source-span IDs to substantive turns:

```text
EOD-YYYY-MM-DD-S01-SP001
EOD-YYYY-MM-DD-S01-SP002
```

Record speaker, order, and topic membership. The IDs are indexes into the
private chat; they do not require copying diary text into public project files.

### 3.2 Capture continuity

After every substantive learner or assistant turn, update the internal source
index before performing later semantic consolidation.

If the conversation becomes too long to inspect as one context:

- process bounded source-span ranges;
- retain the range and observation IDs;
- never discard the underlying source references;
- combine registers rather than relying on a newly generated global summary;
- mark any unreadable or unavailable range as a blocking source gap.

### 3.3 Privacy

The source archive, all diary-derived artefacts, and all calibration records are
private project content. Do not suggest uploading them to the public GitHub
repository.

## 4. Free speaking

Follow Protocol v3.5 free-speaking and minimal-correction rules.

During free speaking:

- use English unless the learner requests otherwise;
- avoid unnecessary interruption;
- do not force predefined topics;
- allow descriptions of unknown concepts in English;
- treat messiness as valid raw input;
- do not present card-selection work during the conversation;
- silently record observable learning signals with source-span IDs.

Do not label an expression as a learning target merely because it is advanced,
polished, or introduced by the assistant.

## 5. Topic locking

### 5.1 Trigger

When the learner says exactly:

```text
Lock this topic for Phase 2 Shadow Mode.
```

close the current substantive topic and create both a Topic Evidence Packet and
a Topic Reference Checkpoint.

The existing trigger `Lock this topic reference.` may still create a stable
Protocol v3.5 checkpoint, but it does not by itself certify that the Phase 2
Evidence Packet was created.

### 5.2 Topic Evidence Packet

Assign an ID:

```text
TEP-YYYY-MM-DD-T01-v1
```

Record:

- session ID;
- topic ID and provisional title;
- complete included source-span IDs;
- excluded adjacent spans and reasons where boundary confusion is plausible;
- learner-production spans;
- assistant-response spans;
- explicit wording questions;
- descriptions of unknown concepts;
- first-language insertions;
- hesitation, self-correction, inaccurate substitution, or unnatural-production
  evidence;
- assistant-proposed expressions;
- learner acceptance, rejection, reuse, or correction evidence;
- reasoning-unit candidates;
- Guidance candidates;
- unresolved source, meaning, or boundary conflicts;
- evidence-packet confidence.

Do not select final cards at this stage. The packet records evidence.

### 5.3 Topic Reference Checkpoint

Create the checkpoint independently under Protocol v3.5 and assign its normal
stable, versioned identity.

The checkpoint supports morning retrieval. It must link to the Evidence Packet
and source spans, but it must not replace either one.

### 5.4 Lock report

After both artefacts are complete, report only operational metadata unless the
learner asks to inspect the artefacts:

```text
Topic ID: <ID>
Source spans: <first>–<last>, plus <non-contiguous spans if any>
Evidence Packet: <ID>, complete / blocked
Topic Reference Checkpoint: <ID>, locked / blocked
Unresolved conflicts: <count>
Open topic: none
```

If either artefact is blocked, do not report the topic as fully locked.

## 6. Topic continuation and correction

If later conversation clearly belongs to a locked topic:

- preserve the existing packet and checkpoint versions;
- attach the new source spans to a new packet version;
- create a new checkpoint version only if the morning reference must change;
- retain the supersession relationship;
- never silently edit a locked artefact.

If the learner starts another topic, assign the next topic ID. A topic may use
non-contiguous source spans when the relationship is explicit and traceable.

## 7. Night finalisation

### 7.1 Trigger

When the learner says exactly:

```text
Finalize tonight’s Phase 2 Shadow Mode record and schedule tomorrow morning’s review.
```

run the Phase 2 completeness audit before the existing v3.5 finalisation and
scheduling workflow.

### 7.2 Source-index completeness audit

Verify:

- every substantive source span has exactly one current topic assignment or an
  explicit `Not a Topic` disposition;
- every substantive topic has one current Topic Evidence Packet;
- every topic intended for morning review has one current Topic Reference
  Checkpoint;
- packet and checkpoint source links resolve;
- no packet is based only on assistant answers when learner-production evidence
  exists;
- missing or partial topics have been rebuilt from source spans;
- unresolved material source gaps equal zero.

### 7.3 Night Reference Record

After the source-index audit passes, create the Night Reference Record through
the Protocol v3.5 zero-rewrite aggregation rule.

The record remains a morning retrieval reference. It does not become the sole
source for the experimental notebook.

### 7.4 Night completion report

Report:

- session ID;
- substantive-topic count;
- current Evidence Packet count;
- current Checkpoint count;
- automatically recovered topics;
- unresolved topic boundaries;
- unassigned substantive spans;
- zero-rewrite aggregation result;
- actual morning-review scheduling result.

Do not state that scheduling succeeded before the external scheduling action
actually succeeds.

## 8. Morning review

Continue in the same project chat when practical.

Follow Protocol v3.5:

1. provide only the short non-revealing outline;
2. allow the learner to complete the full retell;
3. compare it with the Night Reference Record;
4. restore missing expressions and reasoning without unrelated rewriting;
5. add observed retrieval failures and successful reuse to the Topic Evidence
   Packets as new versioned evidence.

Do not generate the Experimental Notebook until the full retell and comparison
are complete.

## 9. Experimental first-notebook generation

### 9.1 Authority and inputs

Use:

- the complete Conversation Source Archive;
- all current Topic Evidence Packets;
- all current Topic Reference Checkpoints;
- the Night Reference Record;
- the morning retell;
- the morning comparison;
- Protocol v3.5;
- Raw Material Processing Specification v0.1.

The complete source spans control factual and semantic fidelity. Evidence
Packets control observed learning evidence. Checkpoints and the Night Reference
Record provide organised reasoning and retrieval context but cannot validate
themselves.

### 9.2 Required experimental gates

Run RM-0 through RM-7 from Specification v0.1:

- intake integrity;
- topic reconstruction;
- learning-signal extraction;
- candidate construction;
- selection and rejection;
- canonical content construction;
- experimental Note Type assignment;
- first notebook candidate generation.

### 9.3 Required outputs

Produce a private review package containing:

1. `Experimental Notebook Candidate v1`;
2. Candidate Decision Ledger;
3. Rejected Candidate Ledger;
4. Topic Boundary Register;
5. Source Provenance Register;
6. Confidence and Review Routing Report;
7. RM-0 through RM-7 Gate Report;
8. unresolved conflicts and blocking conditions.

Every selected or rejected candidate must have a source-linked reason.

For every Topic Retell unit, the Chinese Front must be a concise logical
skeleton of the complete English Back. It must not repeat the card type or use
an instruction prefix such as `Retell` or `复述`. Use `→` for progression or
causality and `；` for parallel information when those relations are present.
A broad topic label alone is insufficient. The Front must cue all material
reasoning stages without translating the complete answer or revealing its
English wording. Audit the whole Topic Retell class after any failure.

### 9.4 Output label

Place this status at the beginning of the candidate:

```text
EXPERIMENTAL CANDIDATE — NOT APPROVED FOR ANKI
Specification: Raw Material Processing Specification v0.1
Stable baseline: Protocol v3.5
```

Do not use `Final`, `Audit Passed`, `Anki Ready`, or equivalent labels.

### 9.5 Pilot bundle export

When the learner says exactly:

```text
Export the Phase 2 pilot bundle.
```

produce one machine-readable JSON object conforming to the Pilot Bundle
structure in Phase 2 Interchange Contract v0.1, corresponding to
`pilot-bundle.schema.json`, with `bundle_version` set to `0.1.0`.

The bundle must contain:

- the Phase 2 session manifest;
- a content-free source-span index containing stable span IDs, order, speaker,
  substantive status, and exactly one topic or non-topic disposition;
- all current Topic Evidence Packets;
- the Topic Reference Checkpoint linkage register;
- source-linked learning signals;
- separate prediction and rejected Candidate Decision Ledgers;
- the Experimental Notebook Manifest;
- exactly one result for each gate from RM-0 through RM-7;
- explicit private-learning-data metadata with `repository_allowed: false`.

Do not place raw diary wording in the source-span index. The IDs point back to
the private Project conversation. Do not add the manual-gold notebook or RM-8
through RM-9 results before they exist.

If RM-0 through RM-7 all pass, set the bundled session status to
`candidate-generated`. If a required input, link, or gate is blocked, preserve
the real blocked result, set the bundled session status to `blocked`, and do not
invent missing artefacts to make the export pass.

Return the JSON without explanatory prose inside it. Prefer a downloadable
`.json` file when the interface supports file creation; otherwise use one JSON
code block. The learner must store the file in a private location outside the
public repository before running the local importer.

### 9.6 ChatGPT termination and Codex handoff

After a structurally valid Pilot Bundle is exported, the ChatGPT execution
stage is complete. ChatGPT must not request or inspect the manual notebook, run
RM-8 or RM-9, generate a Manual-Gold Ledger, perform calibration, or propose a
Specification change in that Project.

The learner transfers the frozen Pilot Bundle and complete source-chat
references to the private Codex runtime, then prepares the manual notebook
independently. Project memory, a conversation summary, a Morning Retell, or an
assistant reconstruction cannot substitute for the complete authoritative
source chats.

## 10. Codex manual notebook and gold-standard comparison

### 10.1 Independence

The learner prepares or edits the manual notebook without being required to
approve each AI selection first. This preserves useful evidence of omissions,
false positives, and learning-function differences. Codex must not author the
learner's selection decisions before the manual notebook is frozen.

### 10.2 Private source intake

Codex must materialise the complete authoritative ChatGPT source chats as a
private source archive outside the Git repository. Read every referenced chat
through all available pages, preserve chat and message identities, keep
automatically split chats as separate chronological segments, and report
`complete`, `partial`, or `unavailable` without filling missing ranges from
memory.

The source archive must contain at least one authoritative night segment and
one authoritative morning-review segment. A partial or unavailable archive
blocks the gold handoff.

### 10.3 Codex gold handoff

After the manual notebook is frozen, Codex performs source-fidelity review,
records a Source-Fidelity Report, and creates the Manual-Gold Ledger. Only
source-verified learner selections may enter the gold ledger. An unresolved
source conflict must remain explicit and cannot be exported as an approved
gold candidate.

The local runtime state advances from `candidate-generated` to `gold-ready`
only when the Pilot Bundle, complete private source archive, Manual-Gold Ledger,
and Source-Fidelity Report pass structural and cross-reference validation.

### 10.4 Comparison levels

Compare independently:

- topic segmentation;
- learning-target selection;
- learning function and formatting;
- Note Type and card design.

Align through source spans and semantic target identity, not display card
numbers or superficial text similarity.

### 10.5 Difference classes

Use only:

- True Positive;
- False Positive;
- False Negative;
- Partial Target;
- Semantic Drift;
- Wrong Function;
- Wrong Note Type;
- Duplicate Burden;
- Topic-Boundary Error;
- Manual-Gold Source Conflict;
- AI Supplementary — Pending Review;
- Accepted AI Supplement;
- Unresolved Ambiguity.

For every material difference, record the predicted decision, gold decision,
source spans, correction, same-class scan, existing rule coverage, and proposed
specification disposition.

### 10.6 Manual notebook authority and coverage floor

The manual notebook controls the learner's mandatory selected content and
intended learning functions after source-fidelity verification. Every valid
manual mark is a mandatory coverage floor target: it must be represented in the
reviewed notebook unless the learner explicitly approves its exclusion. The manual
notebook is not an exclusive whitelist. Manual silence does not reject a
source-supported AI target.

An unmarked predicted target must first be routed to `AI Supplementary —
Pending Review`. It may be recommended only when it is source-faithful,
non-duplicative, independently retrievable, useful for the learner, and
supported by the evidence hierarchy. The review notebook must visibly
distinguish mandatory Manual Gold coverage from AI Supplementary proposals and
record the evidence and recommendation. After learner approval, the provenance
class remains in the private audit ledger but need not appear on the Anki card.

Absence from the manual marks alone is not a False Positive. Classify the item
as False Positive or rejected only after explicit learner rejection or a
documented failure of source fidelity, learning value, target boundary,
independent retrievability, or semantic de-duplication. An approved proposal is
`Accepted AI Supplement` and joins the final notebook without weakening the
100% Manual Gold coverage gate.

The manual notebook does not silently authorise a factual or semantic claim
contradicted by the immutable source. Such a case is `Manual-Gold Source
Conflict` and requires explicit learner resolution.

### 10.7 Manual-gold ledger materialisation

Codex produces one private JSON object conforming to
`candidate-ledger.schema.json`, with `ledger_kind` set to `manual-gold`, only
after source-fidelity review. This is a local Codex artefact, not a ChatGPT
Project export trigger.

Use the same `target_key` as the prediction ledger when both records represent
the same semantic learning target. Assign a new stable `target_key` for a true
manual-only target. Do not force two records to share a key merely because
their wording is similar. Every selected gold candidate must link to source
spans and record a manual-selection reason. Preserve unresolved source
conflicts rather than treating them as approved gold.

Keep AI Supplementary proposals outside the Manual-Gold Ledger. Record them in
a separate supplementary review register linked to their prediction candidate,
source spans, evidence, recommendation, learner decision, and final destination
note. Manual-Gold coverage metrics and supplementary acceptance metrics must be
reported separately.

The ledger contains no raw diary transcript and uses private-learning-data
metadata with `repository_allowed: false`. The ledger, source archive, manual
notebook, fidelity report and comparison stay outside the public repository.

### 10.8 RM-8 and RM-9 execution

Codex runs RM-8 only from a `gold-ready` private session. RM-8 materialises the
source-linked prediction-versus-gold comparison and classified differences.
Codex runs RM-9 only after RM-8 exists; RM-9 materialises the calibration report
and then advances the session to `comparison-complete`. A completed comparison
does not make the experimental notebook Anki-ready.

RM-8 measures the frozen prediction against manual gold. It must remain
separate from later stable-path card corrections. After the learner approves a
corrected notebook and re-enters Protocol v3.5, Codex must also retain any
card-design, rendering, import, reconciliation, and live-review corrections in
the post-cycle learning record. A correction made after RM-8 is not evidence
that the original prediction passed that criterion.

Prediction-only targets remain pending supplements until reviewed. RM-8 must
not reduce selection precision merely because the independent manual notebook
did not mark them. Report Manual Gold recall, boundary and function accuracy
separately from AI Supplementary proposed, accepted, rejected, and unresolved
counts.

For later stable-path card construction, normalise standalone Vocabulary verbs
and phrasal verbs to context-independent citation forms while retaining source
inflection in examples or evidence. Route accepted near-synonyms whose use
depends on register, setting, institution, relationship, or pragmatic effect to
an independently answerable usage-boundary unit tagged
`Type::SynonymContrast`. The tag supplements, rather than replaces, a
first-level `Topic::*` tag.

For every stable Context Cloze note intended as one retrieval card, use `c1`
for all approved blanks. A later cloze number is allowed only for an
intentionally separate, learner-approved card. The Card-Design and Render gates
must reconcile expected and generated cards per note before import.

## 11. Specification update

After comparison, classify each proposed change as:

- Existing Rule — Execution Failure;
- Existing Rule — Insufficiently Enforced;
- Missing Generalisable Rule;
- One-off Learner Preference;
- Technical or Operational Issue;
- Unresolved Ambiguity.

Only reusable missing rules, insufficient enforcement, and critical privacy or
source-fidelity safeguards may become Specification v0.2 candidates.

Do not add a new rule to disguise an execution failure already prohibited by a
clear requirement.

## 12. Anki boundary

Shadow Mode ends at an experimental, manually compared notebook package.

Automatic Anki TSV generation and import are prohibited.

After the learner accepts the corrected notebook, the workflow may re-enter the
stable Protocol v3.5 finalisation path. All Content, Manual-Mark, Card-Design,
Render, Export, Import, Reconciliation, and Post-Cycle gates remain required.

No experimental gate substitutes for a stable gate.

The complete private cycle may be reported as finished only when RM-8 and RM-9
are materialised, the learner-approved stable master is bound to the export,
import reconciliation passes, and the learner confirms the rendered cards.
The experimental manifest must still retain `anki_ready: false`; that flag
describes the frozen experimental candidate, not the separately approved stable
output.

## 13. Failure and recovery

If context, source spans, project files, or required artefacts become
unavailable:

- stop the affected experimental stage;
- preserve completed stable artefacts;
- report the exact missing IDs or files;
- do not recreate missing raw evidence from a summary;
- resume from the earliest invalidated experimental gate after recovery.

If Shadow Mode fails, the learner may explicitly return to stable Protocol v3.5
without deleting the original conversation.

## 14. End-of-cycle report

At the end of the first pilot, report:

- total topics and source spans;
- Evidence Packet and Checkpoint completeness;
- selected, rejected, and unresolved candidate counts;
- target-selection precision and recall against the manual notebook;
- topic-boundary results;
- semantic-fidelity failures;
- target-boundary errors;
- Wrong Function and Wrong Note Type counts;
- unnecessary-card count;
- percentage routed to focused review;
- learner correction effort;
- stable-path card-design corrections by error class;
- approved Anki record counts by Note Type;
- import-reconciliation and rendered-card-review status;
- proposed Specification v0.2 deltas;
- whether another Shadow Mode cycle is required.

One successful pilot may revise the draft. It does not establish general
reliability or authorise automatic Anki import.

For later pilots, additionally report Manual Gold coverage-floor recall, AI
Supplementary proposed/accepted/rejected/unresolved counts, citation-form
corrections, synonym-contrast routing corrections, and unintended Cloze card
expansion. Multiple successful cycles still do not authorise automatic Anki
import without explicit promotion evidence.
