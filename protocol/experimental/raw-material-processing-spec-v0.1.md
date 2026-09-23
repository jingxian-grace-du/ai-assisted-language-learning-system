# Raw Material Processing Specification v0.1

- Status: Experimental draft
- Pilot clarification: 0.1.3 (coverage floor, lexical citation forms, contrast
  routing, and single-card Cloze enforcement)
- Protocol relationship: Phase 2 extension candidate
- Export authority: None
- Automatic Anki import: Prohibited

## 1. Purpose

This specification defines an experimental, traceable process for converting a
long English Oral Diary conversation into a first structured learning-notebook
candidate.

Version 0.1 is a hypothesis to be calibrated against a separately stored manual
notebook. It does not claim that topic reconstruction, target selection, or
Note Type assignment is mature. Its first purpose is to make every decision
observable so errors can be classified and converted into reusable rules.

## 2. Non-goals

Version 0.1 does not:

- replace the learner's final authority;
- treat generated content as its own evidence;
- depend on model memory of an entire long conversation;
- use the Night Reference Record as a substitute for the raw source;
- copy assistant answers mechanically and call them raw material;
- automatically export or import unreviewed Anki notes;
- promise a fixed target-selection accuracy;
- store private source content in the public repository.

## 3. Four-artifact source architecture

Long conversations must not depend on one model context window or one summary.
The system maintains four distinct artefacts with different jobs.

### 3.1 Conversation Source Archive

The archive is the immutable, complete session event stream. It preserves:

- speaker identity;
- exact turn order;
- exact source text or audio-transcript reference;
- timestamps or stable sequence positions;
- corrections, acceptances, rejections, and later supersession;
- session and turn hashes where available.

This is the highest-fidelity raw material. It remains private and outside the
repository. The pipeline reads it through an explicit external data location.

### 3.2 Topic Evidence Packet

When a topic is provisionally closed, the system creates a packet containing
references to the complete relevant source spans, not copied excerpts alone.

The packet records:

- provisional topic identity and title;
- first and last source-span IDs;
- every non-contiguous span included in the topic;
- learner production spans;
- assistant response spans;
- explicit wording questions;
- descriptions of unknown concepts;
- hesitation, self-correction, inaccurate substitution, and retrieval signals;
- expressions proposed by the assistant;
- learner acceptance, rejection, reuse, or correction evidence;
- substantive reasoning and Guidance candidates;
- unresolved boundary or authority conflicts.

This packet is the primary input for learning-target extraction. It must retain
the learner's production evidence because assistant answers alone cannot show
what the learner struggled to express.

### 3.3 Topic Reference Checkpoint

The checkpoint supports next-morning retrieval and reasoning reconstruction. It
is a derived, locked reference assembled according to the existing checkpoint
rules. It may consolidate useful assistant reasoning and grounded learner
points, but it is not the raw source and does not replace the Topic Evidence
Packet.

Every checkpoint must link to its Topic Evidence Packet and source-span set.

### 3.4 Night Reference Record

The Night Reference Record is the zero-rewrite concatenation of current locked
Topic Reference Checkpoints. It supports morning review. It is not used as the
sole source for first-notebook learning-target extraction.

## 4. Long-conversation resilience

### 4.1 Incremental capture

After every completed turn, persist the turn to the Conversation Source Archive
before performing semantic processing. A model response or summary is not proof
that the source was captured.

### 4.2 Provisional topic boundaries

The pipeline maintains an open-topic state. A topic may be provisionally closed
by an explicit trigger or by strong boundary evidence. Closure creates the
Topic Evidence Packet and Topic Reference Checkpoint independently.

### 4.3 Topic trigger

The existing topic-lock trigger remains useful because it reduces end-of-night
context pressure. Its meaning changes from “remember this summary” to “freeze
the source-span membership, evidence packet, and derived checkpoint for this
topic.”

### 4.4 Nightly completeness audit

At night finalisation, operate on the source archive index rather than asking a
model to recall the chat. Verify:

- every substantive source span belongs to one current topic or has an explicit
  non-topic disposition;
- every substantive topic has one current evidence packet;
- every topic intended for morning review has one current checkpoint;
- overlapping and non-contiguous topic spans are recorded explicitly;
- missing or partial packets are rebuilt from the archive;
- checkpoint aggregation changes no locked checkpoint content.

### 4.5 Recovery

If the active model context cannot contain the complete conversation, process
source spans in bounded chunks. Each chunk produces only indexed observations;
the final topic and candidate decisions operate on the accumulated registers.
No chunk summary may delete its underlying source references.

## 5. Experimental processing pipeline

### Gate RM-0 — Intake integrity

Inputs:

- Conversation Source Archive;
- current Topic Evidence Packets;
- Topic Reference Checkpoints;
- Night Reference Record when available;
- morning retell and comparison when available;
- current experimental specification version.

Pass conditions:

- every input has a stable ID and version;
- all private inputs resolve outside the repository;
- source order is complete;
- speaker attribution is present;
- no derived artefact is presented as the raw source.

### Gate RM-1 — Topic reconstruction

Identify candidate topics using changes in event, person, question, time,
location, communicative purpose, reasoning centre, or explicit learner intent.

For every boundary, record:

- supporting source-span IDs;
- boundary evidence;
- confidence;
- whether adjacent material was continued, split, merged, or left unresolved.

Do not force every conversational turn into a substantive topic.

### Gate RM-2 — Learning-signal extraction

Extract observable signals before deciding what becomes a card. Initial signal
types are:

- unknown-concept description;
- explicit wording question;
- first-language insertion;
- hesitation or abandoned formulation;
- self-correction;
- inaccurate substitution;
- understandable but unnatural production;
- morning-recall failure;
- learner acceptance of a proposed expression;
- learner reuse of a proposed expression;
- explicit retention request;
- manual mark;
- reusable reasoning or Guidance candidate.

Each signal must point to source evidence. Linguistic sophistication without a
learner signal is insufficient by itself.

### Gate RM-3 — Candidate construction

Create a candidate only after signal extraction. A candidate records:

- proposed target;
- canonical source meaning;
- relevant source spans;
- topic;
- signal IDs;
- intended learning function;
- communicative relevance;
- reusability;
- evidence of a mastery gap;
- source confidence;
- expected review cost;
- possible redundancy;
- unresolved conflicts.

### Gate RM-4 — Selection and rejection

Classify each candidate as:

- selected;
- suggested for review;
- rejected;
- unresolved conflict.

Every rejection requires a reason. Initial rejection reasons include:

- no demonstrated learning need;
- low future reuse value;
- incidental one-session detail;
- already covered by an approved target;
- assistant-created sophistication without learner evidence;
- insufficient context;
- unsupported semantic inference;
- duplicate retrieval purpose;
- review burden exceeds learning value.

Card quotas must not determine selection.

### Gate RM-5 — Canonical content construction

Build topic-level canonical content before adding card markup.

Permitted transformations:

- grammar and spelling correction;
- naturalisation that preserves meaning;
- removal of non-material spoken redundancy;
- consolidation of genuinely repeated material;
- restoration of directly supported omitted context;
- organisation into coherent reasoning units.

Every transformation must retain provenance. It may not change actor, event,
object, causality, chronology, polarity, certainty, qualification, stance, or
material factual detail.

### Gate RM-6 — Experimental Note Type assignment

Assign a proposed Note Type by retrieval purpose:

- Context Cloze for local retrieval in meaningful context;
- Topic Retell for complete discourse or reasoning reconstruction;
- Vocabulary for independently answerable lexical or concise expression work;
- Guidance for complete reusable advice, principles, and reasoning intended for
  repeated reflection.

Record why the selected Note Type is preferable and why plausible alternatives
were rejected. Apply the existing paired-note, Vocabulary-answerability, and
Guidance-alignment requirements.

For Vocabulary headwords and phrasal-verb answers, use the context-independent
citation form rather than copying an incidental tense from the source. Use the
base form for verbs and phrasal verbs (`connect`, `hold back`), the natural
singular citation form for count nouns, and parallel grammatical forms in a
synonym set. Preserve the actually observed inflected form in the example or
source evidence. Keep the inflected form as the answer only when tense, aspect,
voice, participial use, or a fixed expression is itself the approved learning
target.

When several accepted expressions overlap but differ by register, setting,
institution, relationship, or pragmatic effect, do not flatten them into an
unqualified synonym list. Create an independently answerable usage-boundary or
synonym-contrast unit and propose the `Type::SynonymContrast` tag. State the
shared meaning, the boundary for each expression, and at least one natural-use
contrast. The tag classifies the retrieval task; it does not replace the
ordinary `Topic::*` tag or create a fifth Note Type.

For a Context Cloze reasoning unit intended to be retrieved as one card, assign
every approved blank the same `c1` index. Use `c2` or a later index only when a
card is intentionally separate and the learner has approved that
split. Before export, count the generated cards per note and treat an
unintended multi-card expansion as a Card-Design gate failure.

For every Topic Retell Front, construct a concise Chinese logical skeleton of
the complete Back rather than a broad topic label. Do not repeat the Note Type
or add an instruction label such as `Retell` or `复述`; the card template already
communicates the retrieval task. Use `→` for progression or causality and `；`
for parallel information when those relations are present. The cue must cover
the answer's material reasoning stages without becoming a complete translation
or revealing the English wording. A broad-topic-only cue fails RM-6 even when
the Back itself is correct.

### Gate RM-7 — First notebook candidate

Produce:

- the structured notebook candidate;
- a candidate decision ledger;
- a rejected-candidate ledger;
- source-provenance links;
- confidence and review-routing status;
- automatic structural and semantic gate results.

The output must be labelled Experimental Candidate. It may not be called Final,
approved, or ready for Anki.

Before RM-7 passes, audit every Topic Retell Front for redundant task labels,
logical-stage coverage, relationship markers, translation leakage, and
alignment with the complete Back. One failure triggers a same-class scan of all
Topic Retell Fronts in the candidate.

Also audit every proposed Vocabulary answer for citation-form normalisation and
every proposed synonym set for missing usage boundaries. These checks operate
on the frozen prediction; later learner corrections remain post-RM-8 evidence
and must not be backfilled into the historical prediction.

### Gate RM-8 — Shadow comparison

After the learner prepares or confirms the manual notebook, compare it with the
experimental candidate at four independent levels:

1. topic segmentation;
2. learning-target selection;
3. target function and formatting;
4. Note Type and card design.

Do not compare only final card counts or text similarity.

Execution boundary: RM-8 runs in the private Codex runtime, not in the ChatGPT
Diary Project. It requires the frozen Pilot Bundle, a complete private archive
of every authoritative night and morning source-chat segment, the independently
prepared manual notebook, a source-fidelity report, and a structurally valid
Manual-Gold Ledger. This changes the execution location only; it does not alter
the semantic comparison criteria in this specification.

### Gate RM-9 — Calibration record

For every material difference, record:

- source spans;
- predicted decision;
- gold-standard decision;
- error class;
- same-class scan result;
- correction applied;
- whether an existing rule already covered it;
- whether it is a reusable rule, enforcement problem, one-off preference, or
  unresolved ambiguity.

Execution boundary: Codex materialises RM-9 only after RM-8 exists. Private
source, notebook, ledger and comparison content remain outside the repository;
only generalisable protocol changes, non-reconstructive aggregate results and
synthetic tests may enter the public project.

## 6. Gold-standard comparison model

The manual notebook is the calibration authority for the learner's mandatory
selected content and learning functions, subject to explicit source-fidelity
checks. It defines a 100% coverage floor, not an exclusive whitelist. It cannot
authorise a meaning that contradicts the immutable source without a recorded
learner correction.

Source-supported prediction targets not marked in the manual notebook remain
AI Supplementary candidates pending focused learner review. Manual silence is
not a rejection. Keep mandatory-gold coverage and supplementary review in
separate registers during audit; the provenance distinction may be removed from
the visible Anki card after approval while remaining in private audit metadata.

### 6.1 Alignment unit

Align prediction and gold standard through source spans and semantic target
identity, not display card numbers. One predicted unit may map to multiple gold
units or the reverse.

### 6.2 Selection outcomes

- True positive: predicted and retained by the gold standard.
- AI Supplementary — Pending Review: predicted, not manually marked, and not yet
  explicitly accepted or rejected.
- Accepted AI Supplement: prediction-only target approved after evidence,
  fidelity, de-duplication, usefulness, and retrievability review.
- False positive: predicted and explicitly rejected by the learner or rejected
  by a documented evidence, fidelity, value, boundary, retrievability, or
  duplication failure; absence from manual marks alone is insufficient.
- False negative: omitted by prediction but added by the gold standard.
- Partial target: underlying target is correct but scope is too broad or narrow.
- Semantic drift: output changes the authoritative meaning.
- Wrong function: target selected but assigned the wrong learning function.
- Wrong Note Type: learning function is accepted but card format is unsuitable.
- Duplicate burden: target is covered but creates unnecessary repeated review.
- Topic-boundary error: content is incorrectly split, merged, or assigned.

### 6.3 Metrics

Report separately:

- topic-boundary precision and recall;
- target-selection precision and recall;
- Manual Gold mandatory-coverage recall;
- AI Supplementary proposed, accepted, rejected, and unresolved counts;
- semantic-fidelity failure count;
- target-boundary error count;
- learning-function accuracy;
- Note Type accuracy;
- unnecessary-card count;
- unresolved-conflict count;
- percentage routed to human review;
- learner correction effort.

No metric may be described as percentage improvement in English ability.

## 7. Rule promotion

A difference does not automatically become a protocol rule.

Promote a change only when it is:

- a missing generalisable rule supported by evidence;
- an existing rule whose enforcement or wording is insufficient;
- or a critical source-fidelity, privacy, or irreversible-state safeguard.

Do not promote:

- an execution failure already prohibited by a clear rule;
- a one-off content preference;
- an annotation inconsistency with no resolved authority;
- a workaround tied only to one interface version.

Every promoted rule requires a stable ID, source evidence, intended validator,
failure state, and regression test that contains no private diary content.

## 8. Confidence and review routing

Version 0.1 uses qualitative states until calibrated evidence supports numeric
thresholds.

- High: strong direct learner evidence, clear source meaning, clear learning
  function, and no authority conflict.
- Medium: plausible value but incomplete evidence, competing Note Types, or
  uncertain target boundary.
- Low: assistant judgement dominates, reuse value is speculative, or source
  context is insufficient.

High-confidence content remains in Shadow Mode during v0.1. Medium-confidence
content requires focused review. Low-confidence content is omitted from the
candidate notebook but retained in the rejected-candidate ledger when useful for
calibration.

## 9. Privacy and storage

All archives, evidence packets, checkpoints, notebook candidates, manual gold
standards, comparisons, and calibration records are private learning data and
remain outside the repository.

The public repository may contain only schemas, validators, aggregate
non-reconstructive metrics, abstract error codes, and content-free or wholly
synthetic tests.

## 10. Exit criteria for v0.1

Version 0.1 remains experimental until at least one complete private cycle has:

- preserved a complete source archive;
- generated evidence packets without source loss;
- produced a traceable first notebook candidate;
- completed manual-gold comparison;
- classified every material difference;
- rerun all affected error classes;
- proposed only evidence-supported specification deltas.

One cycle is sufficient to revise the draft, not to claim general reliability or
permit automatic Anki import.
