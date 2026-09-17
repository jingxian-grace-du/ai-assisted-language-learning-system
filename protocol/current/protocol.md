# English Oral Diary Protocol v3.5

> Status: privacy-reviewed legacy baseline for Phase 1 migration.
> This baseline preserves the v3.5 normative meaning while replacing
> machine-specific storage paths and removing non-portable internal citation tokens.
> New front-pipeline requirements will be developed separately before being merged
> into a future protocol version.

Source SHA-256: `1ba8cc2c3b35c4909973a1771b07b61bb9c779f7d66d18fea0e9d65b00417f90`

<a id="legacy-p0002"></a>

Status

<a id="legacy-p0003"></a>

Validated full-cycle version, upgraded with non-redundant learning-dimension tags, controlled Type expansion, immutable Topic Reference Checkpoints, nightly missing-topic recovery, manual-mark ledgers, context-first synonym consolidation, minimal-card post-manual revision, first-level-only Topic tags, global error-class audits, conversation-global Protocol release auditing, master-notebook archiving and database-verified Anki import. Version 3.5 adds authoritative-source fallback when manual notebooks are absent, source-fidelity controls against semantic rewriting, atomic bidirectional Guidance mapping with linked updates, underline-only blank rendering, a mandatory post-cycle learning audit and bounded metadata-assisted Anki import.

<a id="legacy-p0004"></a>

This protocol becomes the default workflow whenever the user says:

<a id="legacy-p0005"></a>

English oral diary

<a id="legacy-p0006"></a>

Its purpose is to turn daily spoken English into:

<a id="legacy-p0007"></a>

corrected spoken output;

<a id="legacy-p0008"></a>

next-day active retrieval;

<a id="legacy-p0009"></a>

context-based Anki cards;

<a id="legacy-p0010"></a>

long-term spaced repetition.

<a id="legacy-p0012"></a>

## 1. Core Principles

<a id="legacy-p0013"></a>

### 1.1 Preserve the user’s English

<a id="legacy-p0014"></a>

When correcting the oral diary:

<a id="legacy-p0015"></a>

preserve the original sentence structure whenever possible;

<a id="legacy-p0016"></a>

correct grammar, spelling, collocations and naturalness;

<a id="legacy-p0017"></a>

do not rewrite unnecessarily;

<a id="legacy-p0018"></a>

when English has a shorter or more native expression, present it separately rather than silently replacing the whole sentence.

<a id="legacy-p0019"></a>

### 1.2 Separate speaking, retrieval and memory work

<a id="legacy-p0020"></a>

The three stages have different purposes:

<a id="legacy-p0021"></a>

Night: expression and correction;

<a id="legacy-p0022"></a>

Morning: retrieval and reconstruction;

<a id="legacy-p0023"></a>

Anki: long-term memory and repeated practice.

<a id="legacy-p0024"></a>

They should not be collapsed into one session.

<a id="legacy-p0025"></a>

### 1.3 Learn expressions inside meaningful context

<a id="legacy-p0026"></a>

Do not create isolated words or phrases as Context Cloze or Topic Retell notes. Vocabulary notes are the explicit exception when they provide evidence-based lexical reinforcement, sense distinction or a concise expression test.

<a id="legacy-p0027"></a>

The minimum useful learning unit is:

<a id="legacy-p0028"></a>

a word, phrase or speaking pattern inside a complete context

<a id="legacy-p0029"></a>

Several related sentences may be combined into one card when they form one coherent reasoning unit.

<a id="legacy-p0030"></a>

### 1.4 Review Notebook is an editing stage

<a id="legacy-p0031"></a>

The Review Notebook is not intended to become a separate study resource.

<a id="legacy-p0032"></a>

Its purposes are only to:

<a id="legacy-p0033"></a>

let the user review and modify proposed cards;

<a id="legacy-p0034"></a>

verify the language and contexts;

<a id="legacy-p0035"></a>

prepare clean Anki notes;

<a id="legacy-p0036"></a>

serve as the single source for the final import files.

<a id="legacy-p0037"></a>

The user is expected to study primarily through Anki, not repeatedly read the Review Notebook.

<a id="legacy-p0039"></a>

## 2. Night Session

<a id="legacy-p0040"></a>

Trigger

<a id="legacy-p0041"></a>

The user says:

<a id="legacy-p0042"></a>

English oral diary

<a id="legacy-p0043"></a>

This starts the night phase.

<a id="legacy-p0044"></a>

### Step 1 — Free Speaking

<a id="legacy-p0045"></a>

The user speaks freely about one or more topics.

<a id="legacy-p0046"></a>

During this stage:

<a id="legacy-p0047"></a>

use English only unless the user explicitly requests Chinese;

<a id="legacy-p0048"></a>

do not interrupt unnecessarily;

<a id="legacy-p0049"></a>

allow the user to finish each idea;

<a id="legacy-p0050"></a>

do not force the conversation into predefined topics.

<a id="legacy-p0051"></a>

### Step 2 — Minimal Correction

<a id="legacy-p0052"></a>

For every section, correct in this order:

<a id="legacy-p0053"></a>

grammar;

<a id="legacy-p0054"></a>

spelling;

<a id="legacy-p0055"></a>

collocations;

<a id="legacy-p0056"></a>

naturalness;

<a id="legacy-p0057"></a>

optional concise native alternatives.

<a id="legacy-p0058"></a>

Preserve the user’s original organisation and meaning.

<a id="legacy-p0059"></a>

### Step 3 — Lock Each Topic Reference

<a id="legacy-p0060"></a>

When the user says exactly:

<a id="legacy-p0061"></a>

Lock this topic reference.

<a id="legacy-p0062"></a>

Close the current substantive topic and generate its final Topic Reference Checkpoint. The Checkpoint is the locked reference for that topic and the only content source later permitted in the Night Reference Record.

<a id="legacy-p0063"></a>

Topic Reference Source Order

<a id="legacy-p0064"></a>

Build the Checkpoint primarily by selecting and consolidating the assistant’s useful substantive answers from the complete current-topic span. Use earlier assistant answers when they contain unique useful material, and use the user’s actual dialogue only to restore an important, directly supported point that the assistant omitted.

<a id="legacy-p0065"></a>

Do not reconstruct the Checkpoint primarily from the user’s raw speech, and do not invent new advice, experience, interpretation or conclusion. Delete process language, generic praise, offers to continue and repetition with no unique value. If an earlier answer conflicts with a later user-confirmed answer, retain the latest confirmed version.

<a id="legacy-p0066"></a>

Dialogue-Recovery Test

<a id="legacy-p0067"></a>

A point recovered from the user’s dialogue must be explicit, directly relevant to the topic, valuable for later retrieval or reasoning, absent from the useful assistant answers, and restorable without changing the user’s meaning. Internally record it as User-dialogue recovery with the omitted-point reason.

<a id="legacy-p0068"></a>

Notebook-Style Predictive Formatting

<a id="legacy-p0069"></a>

Format the Checkpoint to imitate the user’s approved manual notebooks. Bold marks complete Guidance content. Italic and underline mark the smallest words, collocations, reusable expressions, sentences or passages intended for active learning. When formatting overlaps, bold defines the Guidance range while italic or underline inside it defines the exact memory target.

<a id="legacy-p0070"></a>

Predict markings from direct evidence in the current topic and repeated patterns in the most recent approved notebooks. Prefer corrected production failures, direct wording questions, hesitation, inaccurate substitutions, reusable chunks, important reasoning patterns and actionable guidance. Do not mark language merely because it is advanced or polished.

<a id="legacy-p0071"></a>

Checkpoint Audit and Lock

<a id="legacy-p0072"></a>

Before locking, inspect the full topic span rather than only recent messages. Confirm that all substantive assistant answers were reviewed, unique early material was not lost, user-dialogue recovery is grounded, rejected or superseded material is excluded, duplicate material is consolidated without loss, and bold/italic/underline boundaries match their defined learning functions.

<a id="legacy-p0073"></a>

Assign a stable identifier such as TRC-YYYY-MM-DD-T01 and record the topic title, conversation range, version and whether it was user-triggered or recovered during the nightly audit. A locked Checkpoint is immutable. Later correction creates a new version; it never silently edits the locked text.

<a id="legacy-p0074"></a>

### Step 4 — Finalise the Night Reference Record

<a id="legacy-p0075"></a>

Either of these exact triggers ends the night session:

<a id="legacy-p0076"></a>

Finalize tonight’s Night Reference Record and schedule tomorrow morning’s review.

<a id="legacy-p0077"></a>

End tonight’s diary and schedule tomorrow morning’s review.

<a id="legacy-p0078"></a>

First build a topic map for the complete night conversation. For every substantive topic, record its conversation span, core question, whether it has a complete Checkpoint, and one status: Covered, Missing Trigger, Partial Checkpoint, Merged Incorrectly or Not a Topic.

<a id="legacy-p0079"></a>

For every Missing Trigger or Partial Checkpoint, return automatically to the complete Step 3 workflow: review the full topic span, select useful assistant answers, restore only grounded omissions from the dialogue, predict notebook formatting, audit the result and create a locked Checkpoint marked Auto-recovered during nightly topic audit.

<a id="legacy-p0080"></a>

Do not finish the audit until every substantive topic has exactly one current valid Checkpoint, Missing Trigger and Partial Checkpoint both equal zero, and no substantive dialogue segment remains unassigned. Ask the user only when a topic boundary or source conflict would materially change the result and cannot be resolved from the conversation.

<a id="legacy-p0081"></a>

Night Reference Record — Zero-Rewrite Aggregation

<a id="legacy-p0082"></a>

Create the Night Reference Record only by concatenating the current locked Checkpoints in conversation order. Apart from the record title, date, Topic numbering, separators, source metadata and review-scheduling statement, do not rewrite, polish, shorten, merge, correct, reorder or change any Checkpoint text or formatting.

<a id="legacy-p0083"></a>

If a locked Checkpoint appears wrong, report the possible error and create a new version only through the Checkpoint workflow; never repair it silently during aggregation.

<a id="legacy-p0084"></a>

Report the detected substantive-topic count, previously locked count, automatically recovered count, partial checkpoints repaired, unresolved boundaries and confirmation that aggregation changed zero Checkpoint text. Then schedule the single next-morning review and state the actual date, time, topic coverage and active-task status only after scheduling succeeds.

<a id="legacy-p0085"></a>

Do not generate Review Notebook, Anki notes, card-selection tables or approval vocabulary lists during the night session. Card creation waits until the morning retell is complete.

<a id="legacy-p0086"></a>

### Step 5 — Reopening a Closed Diary

<a id="legacy-p0087"></a>

If the user remembers another topic after saying “End tonight’s diary” but before the morning review begins, treat it as a continuation of the same night diary.

<a id="legacy-p0088"></a>

The user may say:

<a id="legacy-p0089"></a>

Reopen tonight’s diary.

<a id="legacy-p0090"></a>

continue in the same chat rather than creating a new diary;

<a id="legacy-p0091"></a>

preserve all previously locked topics;

<a id="legacy-p0092"></a>

retain the earlier Night Reference Record as a superseded snapshot while preserving every immutable locked Checkpoint;

<a id="legacy-p0093"></a>

accept, correct and lock the additional topic using the normal night-session rules;

<a id="legacy-p0094"></a>

re-run the missing-topic audit and rebuild the Night Reference Record only by zero-rewrite aggregation of every current locked Checkpoint;

<a id="legacy-p0095"></a>

update or replace the existing morning-review task and never create duplicate reviews for the same diary;

<a id="legacy-p0096"></a>

treat the diary as permanently closed only when the morning review begins; and

<a id="legacy-p0097"></a>

if the morning review has already begun, treat later material as a new diary.

<a id="legacy-p0098"></a>

After adding all topics, the user may say:

<a id="legacy-p0099"></a>

End tonight’s diary and reschedule tomorrow morning’s review.

<a id="legacy-p0100"></a>

After scheduling or rescheduling, explicitly state the review date and time, confirm that every added topic is included, and confirm whether only one active review task exists. Never claim that a task was updated unless the scheduling action actually succeeded.

<a id="legacy-p0102"></a>

## 3. Morning Review at 08:30

<a id="legacy-p0103"></a>

### Step 1 — Short Outline

<a id="legacy-p0104"></a>

The 08:30 automation starts the morning review by providing only a short English outline of the previous diary.

<a id="legacy-p0105"></a>

The outline should contain:

<a id="legacy-p0106"></a>

topic headings;

<a id="legacy-p0107"></a>

a few retrieval cues;

<a id="legacy-p0108"></a>

no complete corrected sentences;

<a id="legacy-p0109"></a>

no answer text.

<a id="legacy-p0110"></a>

Its purpose is to trigger memory, not reveal the diary.

<a id="legacy-p0111"></a>

### Step 2 — Full Retell

<a id="legacy-p0112"></a>

The user reconstructs the full diary from memory.

<a id="legacy-p0113"></a>

During the retell:

<a id="legacy-p0114"></a>

do not interrupt unless clarification is necessary;

<a id="legacy-p0115"></a>

allow the user to complete the full reasoning;

<a id="legacy-p0116"></a>

pay attention to expressions that are forgotten, hesitant or replaced by less accurate wording.

<a id="legacy-p0117"></a>

### Step 3 — Comparison

<a id="legacy-p0118"></a>

Compare the morning retell with the final Night Reference Record assembled from the previous night’s locked Topic Reference Checkpoints.

<a id="legacy-p0119"></a>

Restore:

<a id="legacy-p0120"></a>

missing information;

<a id="legacy-p0121"></a>

forgotten expressions;

<a id="legacy-p0122"></a>

inaccurate collocations;

<a id="legacy-p0123"></a>

grammar that changed during recall;

<a id="legacy-p0124"></a>

the original logical sequence.

<a id="legacy-p0125"></a>

Do not introduce unrelated rewrites or new expressions at this stage.

<a id="legacy-p0126"></a>

### Step 4 — Use Retell Performance as a Selection Signal

<a id="legacy-p0127"></a>

Morning performance helps determine what should become an Anki note.

<a id="legacy-p0128"></a>

Strong Context Cloze candidates include expressions that were:

<a id="legacy-p0129"></a>

forgotten;

<a id="legacy-p0130"></a>

produced hesitantly;

<a id="legacy-p0131"></a>

replaced by a less natural expression;

<a id="legacy-p0132"></a>

understood passively but not produced actively.

<a id="legacy-p0133"></a>

A passage may still qualify for Topic Retell even when all its individual vocabulary was recalled correctly, if organising the full explanation remains difficult.

<a id="legacy-p0135"></a>

## 4. Sources Used to Build the Review Notebook

<a id="legacy-p0136"></a>

The assistant should use all relevant materials together:

<a id="legacy-p0137"></a>

the final zero-rewrite Night Reference Record;

<a id="legacy-p0138"></a>

the morning retell;

<a id="legacy-p0139"></a>

the comparison between the two;

<a id="legacy-p0140"></a>

the user’s own organised notes;

<a id="legacy-p0141"></a>

expressions the user has underlined or explicitly marked as uncertain;

<a id="legacy-p0142"></a>

previously identified Core Expressions and Native Chunks.

<a id="legacy-p0143"></a>

User Formatting Semantics

<a id="legacy-p0144"></a>

When the user supplies an organised note, interpret its formatting as follows:

<a id="legacy-p0145"></a>

Italic text normally marks words, collocations, synonyms or phrases that the user does not know well or cannot yet use confidently. Italic is a mandatory active-memory mark, not a lower-priority annotation.

<a id="legacy-p0146"></a>

Underlined text normally marks expressions, sentences or passages the user wants to remember actively. These may include vocabulary, collocations, proverbs, complex sentences, concise summaries or familiar language whose use in the current context deserves deliberate practice. Underline and italic both define mandatory memory targets; their usual scope differs, but neither may be omitted or weakened.

<a id="legacy-p0147"></a>

Bold text marks the complete useful advice, principle or Guidance content that the user wants to revisit and internalise. Bold alone is primarily for familiarisation and reflection. When italic or underline appears inside bold content, the inner italic or underlined span is the exact mandatory memory target and must control the Chinese blank and English answer/highlight boundary.

<a id="legacy-p0148"></a>

Formatting may overlap. When one item is both italic, underlined or bold, preserve every applicable learning function instead of forcing it into only one category.

<a id="legacy-p0149"></a>

All materially marked content is high-priority source material. Preserve it wherever possible, while allowing unmarked transcript text to be shortened, merged or omitted when it is not needed for context.

<a id="legacy-p0150"></a>

Italic and underlined language should first be embedded in its original or reconstructed complete context. Marking does not automatically justify an isolated card.

<a id="legacy-p0151"></a>

Predictive Marking

<a id="legacy-p0152"></a>

When the user has not supplied formatting, predict italic, underline and bold by combining direct evidence from the current diary with patterns learned from previously approved notebooks. The purpose is to reduce later manual marking, not to eliminate user authority.

<a id="legacy-p0153"></a>

Evidence Priority

<a id="legacy-p0154"></a>

## 1. explicit user formatting, manual Cloze edits and direct instructions are authoritative;

<a id="legacy-p0155"></a>

## 2. observable production difficulty is strong evidence, including Chinese insertion, “How do you say…?”, repeated hesitation, self-correction, inaccurate substitution and morning-recall failure;

<a id="legacy-p0156"></a>

## 3. previously confirmed targets and their word families are strong historical evidence; and

<a id="legacy-p0157"></a>

## 4. linguistic rarity, sophistication or the assistant’s judgment alone is weak evidence and must not determine selection by itself.

<a id="legacy-p0158"></a>

Predict Italic — Unfamiliar Lexical Material

<a id="legacy-p0159"></a>

Predict italic for a word, collocation, synonym or short expression when evidence suggests that the user understands it incompletely or cannot yet retrieve and use it confidently.

<a id="legacy-p0160"></a>

Prioritise expressions requested through Chinese insertion or a direct wording question, repeatedly attempted with hesitation, forgotten during retell, replaced by an inaccurate expression, or belonging to an already confirmed target family.

<a id="legacy-p0161"></a>

Do not mark a word merely because it is advanced, uncommon or stylistically impressive.

<a id="legacy-p0162"></a>

Predict Underline — Complete Expressions Worth Active Recall

<a id="legacy-p0163"></a>

Predict underline when the learning value lies in reconstructing a complete expression rather than recognising one unfamiliar word.

<a id="legacy-p0164"></a>

Strong candidates include proverbs, culturally specific sayings, long or structurally demanding sentences, concise high-level summaries, reusable cause–effect or contrast patterns, difficult Chinese-to-English formulations, contextually important uses of otherwise familiar words, and representative statements of the user’s values or experience.

<a id="legacy-p0165"></a>

A sentence may qualify even when every individual word is familiar.

<a id="legacy-p0166"></a>

Do not underline every fluent or polished sentence. The sentence must carry distinctive structural, conceptual, contextual or personal learning value.

<a id="legacy-p0167"></a>

Predict Bold — Guidance

<a id="legacy-p0168"></a>

Predict bold for self-contained advice, principles or frameworks that the user may want to reread and apply in future situations.

<a id="legacy-p0169"></a>

Strong candidates contain an actionable step, decision rule, emotional-regulation sequence, boundary-setting principle, safety reminder, useful cognitive reframe or broadly reusable distinction.

<a id="legacy-p0170"></a>

Generic reassurance, praise, emotional mirroring or an observation with no practical implication should not become Guidance merely because it sounds supportive.

<a id="legacy-p0171"></a>

Multi-Label Prediction

<a id="legacy-p0172"></a>

One passage may be predicted as more than one formatting class when its learning functions genuinely overlap. The Guidance coverage rule below determines whether separate Anki notes are still needed.

<a id="legacy-p0173"></a>

Confidence and Review Load

<a id="legacy-p0174"></a>

High-confidence predictions are formatted and included automatically in Review Notebook v1.

<a id="legacy-p0175"></a>

Medium-confidence predictions are placed in a short Suggested Candidates section for quick confirmation and are not exported until approved.

<a id="legacy-p0176"></a>

Low-confidence predictions are omitted unless later user behaviour provides stronger evidence.

<a id="legacy-p0177"></a>

The assistant should prefer a small number of meaningful medium-confidence candidates over a long speculative list.

<a id="legacy-p0178"></a>

Preference Calibration

<a id="legacy-p0179"></a>

Use each approved notebook as a calibration example. This is an explicit preference record, not a claim that the underlying model has been permanently retrained.

<a id="legacy-p0180"></a>

Keeping a predicted mark is positive evidence; deleting it is negative evidence.

<a id="legacy-p0181"></a>

Adding an omitted mark reveals a coverage blind spot.

<a id="legacy-p0182"></a>

Changing italic, underline or bold corrects the predicted learning function.

<a id="legacy-p0183"></a>

Narrowing, expanding or splitting a Cloze corrects target-span boundaries.

<a id="legacy-p0184"></a>

Future predictions should prioritise the most recent repeated user decisions over generic language-learning heuristics.

<a id="legacy-p0185"></a>

Two-Stage Preference Calibration

<a id="legacy-p0186"></a>

Treat notebook development as two separate learning and review stages. Do not mix their error signals.

<a id="legacy-p0187"></a>

Stage A — Content Selection and Synthesis Calibration

<a id="legacy-p0188"></a>

Compare the assistant’s predicted content notebook with the user’s independently organised or marked notebook. Learn what content the user retains, omits, combines, marks as unfamiliar, underlines for active recall, or bolds as Guidance.

<a id="legacy-p0189"></a>

Stage A answers: what should be learned, what should be preserved, and how the diary should be organised by topic and complete reasoning unit. Material content may still be added, removed, merged or reorganised at this stage.

<a id="legacy-p0190"></a>

When Stage A is approved, freeze the selected English content and reasoning units as the authoritative content source.

<a id="legacy-p0191"></a>

Stage B — Card-Design Calibration

<a id="legacy-p0192"></a>

Convert the frozen content into Context Cloze, paired Topic Retell, Vocabulary and Guidance notes. Compare the assistant’s card notebook with the user’s final card edits.

<a id="legacy-p0193"></a>

Stage B learns card-type choice, Cloze boundaries, contrast-pair handling, synonym grouping, Chinese blank placement, Guidance highlight span and technical Anki formatting. It must not silently reopen Stage A or introduce new learning content unless the user explicitly identifies a content omission.

<a id="legacy-p0194"></a>

Track two distinct quality measures: content-coverage accuracy for Stage A and card-conversion accuracy for Stage B.

<a id="legacy-p0195"></a>

Source Authority and Version Control

<a id="legacy-p0196"></a>

For one diary, use this authority order: the user’s current explicit instruction; the latest user-edited or explicitly confirmed notebook; the original organised or manually marked notebook as a deletion and meaning check; when the manual-notebook stage is absent, the complete corresponding source span in the original conversation; the locked Topic Reference Checkpoint or Night Reference Record only after source-fidelity verification; previously confirmed targets and approved notebooks; protocol inference; and general linguistic judgement. A later checked notebook supersedes an earlier manual version only where the user intentionally changed it. Assistant-generated notebook text, card English and Chinese translations are derivative outputs and may not validate themselves or override an available authoritative source.

<a id="legacy-p0197"></a>

The final Night Reference Record made from immutable Checkpoints is the morning review reference. The original conversation may be consulted only to audit an omission, trace a source or resolve an explicit review issue; it must not be used to silently generate a different morning reference.

<a id="legacy-p0198"></a>

Authoritative-Source Fidelity Rule

<a id="legacy-p0199"></a>

Every generated note must remain semantically faithful to its highest available authoritative source. Preserve the same actor, event, object, causal relation, chronology, polarity, certainty, qualification, stance and material factual detail. Naturalisation may correct grammar, remove non-material oral redundancy or change retrieval format, but it must not convert reported speech into the user’s own conclusion, generalise a specific event, add a motive, evaluation, diagnosis or fact, or otherwise replace the original claim with a different one.

<a id="legacy-p0200"></a>

For every final note, record the authoritative source and source span, then compare card English with that source, Chinese prompt or translation with the card English, and the Chinese again with the authoritative source. Any material mismatch is a Source-Fidelity FAIL. When a manual notebook exists it controls the selected content and meaning; when that stage is absent, return to the complete original-conversation span. Use Unresolved Conflict rather than assistant inference when authoritative sources materially disagree.

<a id="legacy-p0201"></a>

Manual Mark Ledger

<a id="legacy-p0202"></a>

Before card creation, create one ledger row for every material bold, italic and underlined source item, including overlapping formats. Record a stable ID, exact source text, formatting function, source sentence, smallest intended answer, proposed Note Type and coverage status.

<a id="legacy-p0203"></a>

Do not claim complete manual coverage unless marked-item total equals covered-item total, uncovered items equal zero, over-expanded targets equal zero and under-expanded targets equal zero. For every merged or indirectly represented item, record the destination card and reason.

<a id="legacy-p0204"></a>

Manual-Coverage Enforcement Layer

<a id="legacy-p0205"></a>

Ledger-before-cards rule. Build and freeze the complete Manual Mark Ledger before generating any candidate note. A ledger reconstructed retrospectively from already generated cards, a category summary or a card-range mapping is invalid for Gate 1 and cannot support a coverage claim.

<a id="legacy-p0206"></a>

Atomic mark identifiers. Assign each material bold, italic, underlined or overlapping source span a stable atomic ID tied to its source paragraph and run position, such as MN-P00-R03-U01. Each row must record the exact source text, formatting function, complete source sentence, smallest intended answer, proposed Note Type, destination card, destination field, actual tested text, coverage status and any merge, substitution or exclusion reason.

<a id="legacy-p0207"></a>

Technical definition of coverage. Mere appearance in visible context, ordinary prose, a ledger, an audit explanation or Suggested Candidates does not count as coverage. Italic and underlined material is covered only when it is an actual Context Cloze deletion, a Vocabulary Back answer or the exact highlighted answer corresponding to a Guidance Front blank. Bold material is covered only when its complete advice, actionable logic, conditions and conclusion are preserved in a Guidance Back. Italic or underlined material inside bold content must satisfy both complete-Guidance coverage and exact minimal-answer highlighting.

<a id="legacy-p0208"></a>

Permitted coverage statuses. Use only Directly Covered; Covered in Merged Unit; Covered by Exact Equivalent; Excluded — User Approved; Unresolved Conflict; or Uncovered. Covered in Merged Unit must identify the destination card and field and explain how the complete learning function survives. Covered by Exact Equivalent must record both expressions and the equivalence reason. Excluded — User Approved requires an explicit user decision; assistant judgment alone is insufficient.

<a id="legacy-p0209"></a>

Manual-source conflict rule. When manual marking conflicts with the Night Reference Record, an earlier draft or assistant interpretation, do not delete or weaken the manual target automatically. Record Unresolved Conflict, trace the source and resolve it from existing authoritative evidence only when the correction is technical and cannot alter the user’s selection. Otherwise request the user’s decision. A belief that an earlier assistant may have misunderstood the user is not by itself sufficient grounds for exclusion.

<a id="legacy-p0210"></a>

Deterministic coverage equation. Before first submission and every later finalisation, verify that marked-item total equals Directly Covered plus Covered in Merged Unit plus Covered by Exact Equivalent plus Excluded — User Approved. Pass only when Uncovered, Unresolved Conflict, under-expanded targets, over-expanded targets, incomplete bold Guidance and Guidance-alignment errors all equal zero.

<a id="legacy-p0211"></a>

Build-blocking validator. The deterministic coverage equation and zero-error conditions are a build gate, not narrative self-certification. If any required value is missing or non-zero, do not generate or label a document as Final, Audit Passed or fully covered. A draft may be produced only with an explicit FAIL status and a complete unresolved-item list.

<a id="legacy-p0212"></a>

Mandatory first-submission audit summary. State the atomic marked-item total; separate bold, italic, underline and overlapping counts; directly covered, merged, exact-equivalent and user-approved-exclusion counts; uncovered and unresolved-conflict counts; under- and over-expanded counts; final note count; and validator result PASS or FAIL. Do not replace these counts with a general statement that all material marks were assigned.

<a id="legacy-p0213"></a>

Independent completion states. Report Content Audit, Manual-Mark Audit, Card-Design Audit and Render Audit separately as PASS or FAIL. A notebook may be declared complete only when all four states are PASS. Render success cannot compensate for a failed or unperformed content, manual-mark or card-design audit.

<a id="legacy-p0214"></a>

Audit invalidation and global rescan. If the user identifies one uncovered or weakened manual mark, the previous Manual-Mark Audit automatically becomes invalid. Re-extract every mark from the original manual notebook, rebuild or reconcile the entire atomic ledger, re-run the full error-class scan and recalculate all counts before returning a revision. Fixing only the reported example is prohibited.

<a id="legacy-p0215"></a>

Required Relationship Registers

<a id="legacy-p0216"></a>

Before final card numbering, maintain three internal registers: the Manual Mark Ledger; a synonym/near-synonym register classifying each set as same-slot synonym, related but distinct, grammar mismatch, already covered or unique cue; and a card-coverage register mapping every confirmed target to its exact card and field.

<a id="legacy-p0217"></a>

Protocol Iteration — Conversation-Global Change Coverage Audit

<a id="legacy-p0218"></a>

Before presenting any new Protocol version, review the complete current conversation from the first message relevant to that Protocol iteration through the latest user instruction. Do not audit only the most recent correction or the immediately preceding version.

<a id="legacy-p0219"></a>

Build an internal Conversation Change Ledger with one row for every user-requested modification, user-approved proposal, later correction and explicitly rejected proposal. Record the source turn, requested rule or outcome, current status, destination Protocol section and verification result.

<a id="legacy-p0220"></a>

Use only these statuses: Adopted and Written; Explicitly Rejected or Not Adopted; Superseded by a Later Conflicting Instruction; or Pending Material Ambiguity. User silence is not rejection. User approval of a proposal makes every non-excluded item in that proposal required. A later instruction supersedes only the part with which it actually conflicts and does not cancel unrelated approved changes.

<a id="legacy-p0221"></a>

Include every requested or approved modification in the candidate Protocol unless the user explicitly rejected it, explicitly said not to adopt it, or a later instruction directly superseded it. Preserve every unrelated existing Protocol provision unchanged.

<a id="legacy-p0222"></a>

Before release, compare the Conversation Change Ledger with the candidate DOCX paragraph by paragraph. Pass only when every Adopted and Written item has a verified destination, every excluded item has an explicit user-grounded reason, no required item remains Pending Material Ambiguity, and no unrelated section has changed without authorisation.

<a id="legacy-p0223"></a>

The release report must state the number of requested or approved items, the number written, the number explicitly excluded or superseded, any unresolved items and the exact sections changed. Do not claim that the conversation-global audit passed when any required modification is missing.

<a id="legacy-p0224"></a>

Mandatory End-to-End Gates

<a id="legacy-p0225"></a>

Gate 0 — Lock Inputs. Record the Protocol version, final Night Reference Record, morning retell, latest user-checked notebook, original organised notebook and all previously approved supplemental rules. Resolve version priority before extraction.

<a id="legacy-p0226"></a>

Gate 1 — Extract Manual Formatting. Build the Manual Mark Ledger for every bold, italic, underlined and overlapping span before generating cards. Pass only when extraction is complete.

<a id="legacy-p0227"></a>

Gate 2 — Build Canonical Content. Organise the approved material by topic and complete reasoning unit without card markup. This stage decides content completeness, not Note Type.

<a id="legacy-p0228"></a>

Gate 3 — Build Target Relationships. Complete confirmed-target and word-family propagation, synonym/near-synonym classification, context-first placement and the card-coverage register.

<a id="legacy-p0229"></a>

Gate 4 — Generate Candidate Notes. Decide Context Cloze first, then Guidance, then only the residual necessary Vocabulary. Generate paired Topic Retell from each final canonical Context source after Cloze decisions, and add dedicated Topic Retell only under its independent selection rules.

<a id="legacy-p0230"></a>

Gate 5 — Run Mandatory Audits. Complete manual-mark coverage, semantic redundancy, Guidance three-way alignment, confirmed-target propagation, target-boundary, reverse-cue and independent-retrievability audits. Any failure returns only the affected unit to Gate 3.

<a id="legacy-p0231"></a>

Gate 6 — Produce the First-Submission Audit Report. State the marked-item total and covered total; synonym sets merged; standalone Vocabulary notes and their reasons; similar expressions intentionally not merged and their reasons; unresolved items; and every automatic same-class correction. Request user input only for a genuinely subjective ambiguity.

<a id="legacy-p0232"></a>

Gate 7 — Produce and Render the Final DOCX. Assign final display card numbers only after content and card design pass; render every page and inspect it for clipping, missing glyphs, broken formatting, blank display and highlight alignment.

<a id="legacy-p0233"></a>

Gate 8 — Export and Validate Anki Files. Verify UTF-8 no-header format, field count and order, HTML, Cloze syntax, Tags, Note Type, Deck, row counts and character-identical paired English.

<a id="legacy-p0234"></a>

Gate 9 — Import and Reconcile. Verify the import report and read-only collection state by this run’s counts, Note Type, destination deck, required tags, preserved HTML and parent-deck assignment.

<a id="legacy-p0235"></a>

Gate 10 — Post-Cycle Learning and Protocol Delta Audit. Gate 9 does not end the workflow. Review the complete chat from first notebook generation through Stage A manual-content comparison, Stage B checked-card comparison, same-class corrections, final approval, export and collection reconciliation. Build a Post-Cycle Learning Ledger and classify every material difference as Existing Rule — Execution Failure; Existing Rule — Ambiguous or Insufficiently Enforced; Missing Generalisable Rule; One-off User Preference; or Technical/Operational Issue. Record the reported example, complete same-class scan, automatic linked corrections, current Protocol coverage, proposed destination section and adoption decision. Add only reusable missing or insufficient rules; do not duplicate an adequate rule to disguise an execution failure. Report counts for every class, the exact proposed Protocol deltas and whether a new version is required. Do not declare the full workflow complete before Gate 10 passes.

<a id="legacy-p0236"></a>

Minimal Human Participation Mode

<a id="legacy-p0237"></a>

The default objective is to reduce routine human review to one preference decision for genuinely subjective ambiguity and one final acceptance. Problems resolvable by formatting extraction, full-text search, relationship classification, count reconciliation, field comparison or established rules must be resolved automatically before first delivery and must not be transferred to the user as manual checking work.

<a id="legacy-p0238"></a>

If no material ambiguity remains, do not create an artificial approval checkpoint. Deliver the candidate notebook with its audit report for final acceptance. User authority remains absolute: any later manual edit updates the affected ledger or relationship decision and triggers the corresponding global error-class scan.

<a id="legacy-p0239"></a>

Previous Expression Lists

<a id="legacy-p0240"></a>

Lists such as:

<a id="legacy-p0241"></a>

Core Expressions;

<a id="legacy-p0242"></a>

Native Chunks;

<a id="legacy-p0243"></a>

Worth Remembering;

<a id="legacy-p0244"></a>

are used as coverage checklists.

<a id="legacy-p0245"></a>

They help make sure useful expressions are not missed, but the lists themselves are not converted line by line into cards.

<a id="legacy-p0247"></a>

Marked-Content Extraction and Coverage

<a id="legacy-p0248"></a>

Use the user’s markings as a coverage map rather than converting the source note line by line.

<a id="legacy-p0249"></a>

Reorganise marked material by broad topic and complete reasoning unit, not by the order in which it appeared in the conversation or source note.

<a id="legacy-p0250"></a>

Prefer one coherent contextual passage that naturally contains several related marked expressions, synonyms or sentences.

<a id="legacy-p0251"></a>

Do not mechanically create one card for every marked item. Consolidate related targets when they share one natural context and one retrieval purpose.

<a id="legacy-p0252"></a>

Semantic De-duplication Before Card Creation

<a id="legacy-p0253"></a>

Before assigning Note Types, cluster proposed material by underlying meaning, reasoning sequence and retrieval purpose. Compare across the whole notebook, not only adjacent paragraphs.

<a id="legacy-p0254"></a>

When several passages communicate substantially the same idea and differ mainly in wording, do not create multiple Context Cloze–Topic Retell pairs. Build one coherent source passage or one suitable Vocabulary note that preserves the useful alternatives without repeating the same reasoning burden.

<a id="legacy-p0255"></a>

Use slash-separated alternatives such as `get back at someone / hit back / retaliate` inside one learning slot when the expressions are genuinely interchangeable for the intended meaning and grammatical position.

<a id="legacy-p0256"></a>

Do not use slashes to imply that merely related words are exact synonyms. When related terms differ in meaning, register, grammar or usage, create a Vocabulary distinction card whose Front explicitly asks for the difference.

<a id="legacy-p0257"></a>

If one alternative cannot be inserted naturally into the shared sentence, keep the coherent contextual passage and move the remaining expression to a Vocabulary note instead of creating a near-duplicate passage.

<a id="legacy-p0258"></a>

Preserve a separate card only when it contributes a genuinely different logical stage, example, decision, explanation or retrieval ability.

<a id="legacy-p0259"></a>

Run semantic duplicate checks separately within Context Cloze pairs, dedicated Topic Retell notes, Vocabulary notes and Guidance notes, and also across Note Types.

<a id="legacy-p0260"></a>

If a marked word, synonym or phrase cannot be placed in a natural context without distorting the original meaning, create a standalone Vocabulary note instead of forcing an artificial passage.

<a id="legacy-p0261"></a>

Before finalisation, compare the proposed notebook with all italic, underlined and bold source markings. No marked item may be silently omitted. If an item is excluded, merged or represented indirectly, record the reason during review.

<a id="legacy-p0262"></a>

Marked Notes as an Authoritative Expansion Source

<a id="legacy-p0263"></a>

The user’s organised and formatted notes are not merely a correction layer for the assistant’s first draft. They are an authoritative second-pass coverage source and may reveal useful language, complete reasoning units and guidance that the first automatic selection overlooked.

<a id="legacy-p0264"></a>

Preserve all materially italic, underlined and bold content unless the user removes it or an explicit review decision records why it is represented elsewhere.

<a id="legacy-p0265"></a>

Do not preserve every unmarked sentence. Retain only the surrounding language needed to make the marked material natural, coherent and faithful to the original discussion.

<a id="legacy-p0266"></a>

If marked content belongs to an existing reasoning unit, merge it into or extend that contextual passage rather than creating a fragmented extra card.

<a id="legacy-p0267"></a>

If marked content forms a distinct coherent reasoning unit, create a new Context Cloze and its mandatory identical-content Topic Retell pair.

<a id="legacy-p0268"></a>

If a marked lexical item cannot be embedded naturally without invented or distorted context, create a Vocabulary note.

<a id="legacy-p0269"></a>

If bold material expresses advice, principles or practical reflection, create a Guidance note for familiarisation even when it does not qualify as an active-recall Cloze target.

<a id="legacy-p0270"></a>

Reorganise newly added material by topic, semantic relationship and learning function, not by the order in which the user copied it from the conversation.

<a id="legacy-p0271"></a>

The amount of expansion is determined by marked-content coverage and coherent reasoning units, not by a fixed quota of cards or expressions.

<a id="legacy-p0272"></a>

Context-First Synonym and Vocabulary Decision Order

<a id="legacy-p0273"></a>

For every marked lexical item, first search existing Context Cloze and Guidance situations; then test whether it is a genuine synonym that can be inserted naturally in the same grammatical slot; then check whether it is already learned elsewhere; only after those tests may a standalone Vocabulary note be created.

<a id="legacy-p0274"></a>

Combine genuine same-slot alternatives with slash notation, for example vital / essential / necessary. Preserve a distinction card when related terms differ in meaning or usage. When number, word class, collocation or syntax prevents natural insertion, do not force a slash set; retain a separately answerable Vocabulary note and document the grammatical reason.

<a id="legacy-p0275"></a>

No ordinary Vocabulary note may duplicate a target already actively learned in Context or Guidance. A duplicate is permitted only for an explicit semantic distinction, a different fixed collocation, a direct production cue that cannot be tested naturally in context, or another documented independent retrieval purpose.

<a id="legacy-p0276"></a>

Vocabulary Independent-Retrievability Gate

<a id="legacy-p0277"></a>

Every Vocabulary Front must independently identify one answer, one tightly bounded synonym set or one explicit distinction. Ban collection prompts such as other expressions, other manual marks, supplementary vocabulary or any reference that requires another card. Simulate a learner seeing only the Front; if the expected answer is not bounded and answerable, redesign or split the note.

<a id="legacy-p0278"></a>

Post-Manual-Notebook Minimal-Card Expansion Gate

<a id="legacy-p0279"></a>

A correction or newly marked memory target found by comparing with the user’s manual or checked notebook does not automatically justify a new card. Preserve complete marked-content coverage while treating the smallest coherent final card count as an explicit design objective.

<a id="legacy-p0280"></a>

Apply this mandatory order: correct the answer, Cloze or highlight in an existing card; add the target to an existing natural Context Cloze; extend the same coherent reasoning unit; add a genuine same-slot synonym with slash notation; add an internal target to the existing Guidance; add a distinction to an existing suitable Vocabulary note; and only then consider a new note.

<a id="legacy-p0281"></a>

A new note is permitted only when it contributes unique approved memory content or an independent retrieval ability and integration would distort meaning, break natural context, overload the existing note with a materially different task, or violate another Note-Type rule. The new Front must remain independently answerable, and the coverage register must document why every existing-card option failed.

<a id="legacy-p0282"></a>

After incorporating manual-notebook revisions, rerun whole-notebook semantic de-duplication across all Note Types. If every new target is covered by existing notes, the number of new notes must be zero. Do not equate more marked content with more cards.

<a id="legacy-p0283"></a>

Record a card-count change audit containing: card count before revision; number of new or corrected targets; targets integrated into existing notes; duplicate notes merged or removed; final new-note count; final total; and the integration-failure reason for each permitted new note.

<a id="legacy-p0284"></a>

When an existing Context Cloze canonical English source changes, regenerate its paired Topic Retell from that same source. This paired regeneration is maintenance of one learning unit, not justification for an additional independent note.

<a id="legacy-p0285"></a>

Confirmed-Target Propagation and Cloze Granularity

<a id="legacy-p0286"></a>

A word or expression that the user manually marks or preserves as a Cloze target becomes a confirmed active-recall target for that notebook.

<a id="legacy-p0287"></a>

Search the entire approved notebook, not only the current card, for every occurrence of the confirmed target.

<a id="legacy-p0288"></a>

Cloze every applicable occurrence of a confirmed target in every Context Cloze note in which it appears, even across different cards. Apply this only when the occurrence carries the same intended lexical meaning or word-family learning target; do not propagate a common word mechanically into an unrelated usage merely because the surface form matches.

<a id="legacy-p0289"></a>

Propagate the target to inflectional and derivational forms that actually appear in the approved English content. Examples include clique → cliquey or cliquish, collectivism → collectivist, and exclude → excluded, excluding or exclusionary.

<a id="legacy-p0290"></a>

Do not add, rewrite or substitute English merely to manufacture another member of a word family. Propagation applies only to forms already present in the user-approved content.

<a id="legacy-p0291"></a>

Match by meaning and word family, not by an uncontrolled character substring. Do not Cloze an unrelated homonym or a form used with a different intended meaning.

<a id="legacy-p0292"></a>

Use the smallest meaningful retrieval unit. If the difficulty is one word, Cloze that word rather than hiding an unnecessarily long clause. If the learning target is a fixed collocation, idiom, proverb, sentence pattern or summary, preserve the complete meaningful chunk as the Cloze.

<a id="legacy-p0293"></a>

The user’s manual Cloze edits override the assistant’s earlier automatic selection and become evidence for future extraction decisions.

<a id="legacy-p0294"></a>

## 5. Building Review Notebook v1

<a id="legacy-p0295"></a>

Format

<a id="legacy-p0296"></a>

Generate Review Notebook v1 as a directly editable writing document.

<a id="legacy-p0297"></a>

Do not use:

<a id="legacy-p0298"></a>

Markdown checkboxes that cannot be clicked;

<a id="legacy-p0299"></a>

isolated expression tables;

<a id="legacy-p0300"></a>

a separate “Anki: yes/no” checklist;

<a id="legacy-p0301"></a>

instructions requiring the user to copy, paste and resend the content.

<a id="legacy-p0302"></a>

The user should be able to edit the document directly.

<a id="legacy-p0303"></a>

Organisation

<a id="legacy-p0304"></a>

Organise the notebook by broad conversation topic.

<a id="legacy-p0305"></a>

Within each topic:

<a id="legacy-p0306"></a>

combine related sentences into complete reasoning units;

<a id="legacy-p0307"></a>

reunite related material that appeared in different parts of the conversation;

<a id="legacy-p0308"></a>

preserve the logical order of the discussion;

<a id="legacy-p0309"></a>

avoid automatically making each sentence a separate card.

<a id="legacy-p0310"></a>

Before numbering cards, perform a whole-notebook semantic consolidation pass. Merge repeated descriptions of the same idea even when their English wording differs.

<a id="legacy-p0311"></a>

When the merged card contains synonymous alternatives, separate them with `/` inside one retrieval target or place them together on one Vocabulary Back. Do not preserve separate cards merely to preserve paraphrase variants.

<a id="legacy-p0312"></a>

Stable Internal IDs and Late Numbering

<a id="legacy-p0313"></a>

Use stable semantic IDs during extraction and review, such as CTX-T1, GUD-MODERATION or VOC-FAMILIARITY-PROFICIENCY. Perform coverage, consolidation, splitting and deletion before assigning display Card numbers. Generate sequential Card numbers only in the final layout so revisions do not change the identity of unrelated cards.

<a id="legacy-p0314"></a>

Each proposed card should contain:

<a id="legacy-p0315"></a>

Card number;

<a id="legacy-p0316"></a>

Note Type;

<a id="legacy-p0317"></a>

Chinese Prompt or Front appropriate to the selected Note Type;

<a id="legacy-p0318"></a>

complete English context;

<a id="legacy-p0319"></a>

fixed reusable tags.

<a id="legacy-p0320"></a>

Proposed Note Classes

<a id="legacy-p0321"></a>

Review Notebook v1 may contain four note classes, chosen by learning purpose:

<a id="legacy-p0322"></a>

Context Cloze for words, collocations, native chunks and sentence forms inside a meaningful passage;

<a id="legacy-p0323"></a>

Topic Retell for reconstructing the complete logic of a passage; every Context Cloze also receives a paired Topic Retell with identical English content after Cloze markup is removed;

<a id="legacy-p0324"></a>

Vocabulary for evidence-based lexical reinforcement, synonym or sense distinction, concise sentence-level expressions, or a marked item that cannot be embedded naturally in context; and

<a id="legacy-p0325"></a>

Guidance for bold life advice or principles intended for repeated reading and reflection rather than forced verbatim memorisation.

<a id="legacy-p0326"></a>

Marked-Content Placement Hierarchy

<a id="legacy-p0327"></a>

Place each marked item using this order of preference:

<a id="legacy-p0328"></a>

## 1. embed it in an existing natural Context Cloze reasoning unit;

<a id="legacy-p0329"></a>

## 2. extend that reasoning unit when the additional material is logically connected;

<a id="legacy-p0330"></a>

## 3. create a new paired Context Cloze and Topic Retell when it forms an independent coherent unit;

<a id="legacy-p0331"></a>

## 4. create a Vocabulary note when natural contextual integration is not possible, when direct production evidence justifies extra lexical reinforcement, when several synonymous alternatives should be learned together, or when a complete one-sentence expression is unsuitable as a Context Cloze–Topic Retell pair;

<a id="legacy-p0332"></a>

## 5. create a Guidance note when the purpose is reflection and practical internalisation rather than active verbatim recall.

<a id="legacy-p0333"></a>

Do not force one item into only one Note Type when the same non-Guidance passage has genuinely different learning purposes. Guidance is the exception: vocabulary and complete expressions already contained in Guidance do not automatically generate Context Cloze or Topic Retell duplicates.

<a id="legacy-p0334"></a>

Review Actions

<a id="legacy-p0335"></a>

The user may directly:

<a id="legacy-p0336"></a>

edit the English;

<a id="legacy-p0337"></a>

edit the Chinese prompt;

<a id="legacy-p0338"></a>

move or remove Cloze markers;

<a id="legacy-p0339"></a>

combine cards;

<a id="legacy-p0340"></a>

split a card when genuinely necessary;

<a id="legacy-p0341"></a>

delete an entire proposed card;

<a id="legacy-p0342"></a>

change tags;

<a id="legacy-p0343"></a>

add missing material.

<a id="legacy-p0344"></a>

The edited document becomes the authoritative version.

<a id="legacy-p0346"></a>

## 6. Anki Note Types

<a id="legacy-p0347"></a>

Four Note Types are used.

<a id="legacy-p0348"></a>

### 6.1 OralDiary — Context Cloze

<a id="legacy-p0349"></a>

Purpose

<a id="legacy-p0350"></a>

Context Cloze tests local language retrieval:

<a id="legacy-p0351"></a>

words;

<a id="legacy-p0352"></a>

collocations;

<a id="legacy-p0353"></a>

native chunks;

<a id="legacy-p0354"></a>

sentence patterns;

<a id="legacy-p0355"></a>

specific language forms inside a known context.

<a id="legacy-p0356"></a>

The surrounding context and logical structure are supplied. The learner’s task is to retrieve the missing language.

<a id="legacy-p0357"></a>

Construction Rules

<a id="legacy-p0358"></a>

A Context Cloze note should:

<a id="legacy-p0359"></a>

preserve enough context to make the situation meaningful;

<a id="legacy-p0360"></a>

contain one or more connected sentences;

<a id="legacy-p0361"></a>

combine closely related expressions when they belong to the same reasoning unit;

<a id="legacy-p0362"></a>

avoid isolated words and context-free phrase cards;

<a id="legacy-p0363"></a>

hide only genuine learning targets;

<a id="legacy-p0364"></a>

leave enough visible language to support meaningful retrieval.

<a id="legacy-p0365"></a>

Apply confirmed-target propagation before finalising a Context Cloze note;

<a id="legacy-p0366"></a>

keep repeated occurrences and observed word-family forms Clozed across separate notes;

<a id="legacy-p0367"></a>

choose the Cloze span according to the smallest meaningful retrieval unit; and

<a id="legacy-p0368"></a>

do not change the approved English solely to create an additional target. On the rendered card, every revealed Cloze answer must use the shared answer style: light blue (#5BC0EB), bold and underline. Apply the same style in day and night modes.

<a id="legacy-p0369"></a>

Cloze-Span Boundary Rules

<a id="legacy-p0370"></a>

A Cloze deletion should hide exactly the material the learner needs to retrieve while leaving the maximum useful contextual scaffold visible.

<a id="legacy-p0371"></a>

When the learning target is an unfamiliar word, hide only that word in the grammatical form used in the sentence. Do not automatically include a nearby personal pronoun, possessive, proper name, determiner, familiar noun or other context-specific complement.

<a id="legacy-p0372"></a>

For example, prefer `{{c1::interrogating}} her`, `{{c1::offended}} her` and `{{c1::hostility}} towards my boyfriend` when the lexical word itself is the difficulty.

<a id="legacy-p0373"></a>

Retain particles, prepositions, pronoun slots or complements inside the Cloze when they are integral to a fixed expression, phrasal verb, idiom or sentence pattern. Examples include `{{c1::owe her one}}`, `{{c1::sound her out}}`, `{{c1::take her words to heart}}` and `{{c1::put me on trial}}`.

<a id="legacy-p0374"></a>

When one phrase contains two independent learning targets, create separate deletions using the same Cloze number so each target is precise while the card remains one contextual test. For example: `{{c1::redirect}} my attention towards something {{c1::grounding}}`.

<a id="legacy-p0375"></a>

Do not hide generic scaffolding such as something, happened, person, her or my merely because it sits next to an unfamiliar word.

<a id="legacy-p0376"></a>

Use a larger Cloze span only when the entire collocation, idiom, proverb, grammatical pattern, translation or summary sentence is the actual marked learning target.

<a id="legacy-p0377"></a>

A Cloze span must not combine two different recall decisions simply because the words are adjacent.

<a id="legacy-p0378"></a>

Reverse-Cue and Contrast-Pair Protection

<a id="legacy-p0379"></a>

Inspect the visible context for words that reveal a hidden answer through direct synonymy, antonymy, translation, parallel structure or a predictable contrast.

<a id="legacy-p0380"></a>

When a visible counterpart would make the target guessable without real retrieval, hide both sides with the same Cloze number. Example: `That makes the gap feel {{c1::heavier / huge}}, while their path might feel {{c1::lighter}}.`

<a id="legacy-p0381"></a>

Apply the same principle to paired opposites, mirrored comparisons and explicit definition–answer structures. Do not hide a contrast term automatically when it does not reveal the target or is not itself worth learning.

<a id="legacy-p0382"></a>

Run the reverse-cue audit after every manual Cloze edit because a newly added or removed deletion can create an unintended clue elsewhere in the same card.

<a id="legacy-p0383"></a>

Whole-Sentence Target and Card-Type Rule

<a id="legacy-p0384"></a>

Do not make an entire ordinary sentence the sole Cloze deletion when almost no useful contextual scaffold remains.

<a id="legacy-p0385"></a>

A full-sentence Cloze is appropriate only when the complete sentence itself is the confirmed learning target, such as a proverb, culturally specific saying, exact translation, fixed quotation or structurally important summary that still benefits from contextual testing.

<a id="legacy-p0386"></a>

When a one-sentence idea is best recalled from a Chinese cue and does not contain meaningful multi-sentence logic, use a sentence-level Vocabulary note instead of creating a Context Cloze and mandatory Topic Retell pair.

<a id="legacy-p0387"></a>

Do not create Topic Retell solely for one isolated sentence. Topic Retell requires a complete reasoning unit or discourse sequence.

<a id="legacy-p0388"></a>

Chinese Prompt

<a id="legacy-p0389"></a>

The Prompt field must contain a complete Chinese translation of the entire English content in that Context Cloze note.

<a id="legacy-p0390"></a>

The translation should preserve every sentence, logical relationship, example and level of detail. It is not an outline and must not omit information.

<a id="legacy-p0391"></a>

Cloze Numbering

<a id="legacy-p0392"></a>

By default, related targets within one reasoning unit use the same number:

<a id="legacy-p0393"></a>

{{c1::expression one}}

<a id="legacy-p0394"></a>

{{c1::expression two}}

<a id="legacy-p0395"></a>

{{c1::expression three}}

<a id="legacy-p0396"></a>

This produces one card with all related sections hidden.

<a id="legacy-p0397"></a>

Different numbers such as c1, c2 and c3 should be used only when intentionally creating separate cards from one note. Anki creates one card per distinct Cloze number; several deletions using the same number appear together on one card.

<a id="legacy-p0399"></a>

Single English Source for Paired Notes

<a id="legacy-p0400"></a>

A Context Cloze and its paired Topic Retell must be generated from one canonical approved English source field, never edited independently. Context Cloze adds deletion markup to that source; Topic Retell removes the markup. After markup removal, the English text must match character for character. Any English correction regenerates both notes.

<a id="legacy-p0401"></a>

### 6.2 OralDiary — Topic Retell

<a id="legacy-p0402"></a>

Purpose

<a id="legacy-p0403"></a>

Topic Retell tests global spoken organisation:

<a id="legacy-p0404"></a>

logical progression;

<a id="legacy-p0405"></a>

connected expression;

<a id="legacy-p0406"></a>

cause and effect;

<a id="legacy-p0407"></a>

sequencing;

<a id="legacy-p0408"></a>

explanation;

<a id="legacy-p0409"></a>

argument structure;

<a id="legacy-p0410"></a>

the ability to expand a short cue into a coherent spoken passage.

<a id="legacy-p0411"></a>

The primary challenge is not remembering one phrase. It is reconstructing and expressing the complete line of thought.

<a id="legacy-p0412"></a>

Front

<a id="legacy-p0413"></a>

A concise Chinese outline containing:

<a id="legacy-p0414"></a>

the central topic;

<a id="legacy-p0415"></a>

the question or situation to explain;

<a id="legacy-p0416"></a>

a logical sequence only when necessary to make the retrieval target clear.

<a id="legacy-p0417"></a>

The prompt must provide only retrieval cues or a logical outline. It must not be a complete Chinese translation and must not reveal the English wording.

<a id="legacy-p0418"></a>

Back

<a id="legacy-p0419"></a>

One coherent English passage representing the complete reasoning unit.

<a id="legacy-p0421"></a>

### 6.3 OralDiary — Vocabulary

<a id="legacy-p0422"></a>

Purpose

<a id="legacy-p0423"></a>

Vocabulary notes provide focused lexical or sentence-level reinforcement when the learning need is a word, sense, synonym set, contrast set or concise expression rather than reconstruction of a full reasoning passage.

<a id="legacy-p0424"></a>

Front

<a id="legacy-p0425"></a>

Provide a concise Chinese cue and, when useful, a short English definition, usage distinction or evidence label. The cue should identify the intended sense without revealing the answer.

<a id="legacy-p0426"></a>

Back

<a id="legacy-p0427"></a>

Provide the English answer. Genuine synonyms or alternative expressions for one meaning may share one note separated by `/`. Related but non-interchangeable terms may share a distinction note only when the Front explicitly asks the learner to distinguish their meanings or usage.

<a id="legacy-p0428"></a>

Construction Rules

<a id="legacy-p0429"></a>

Use Vocabulary when at least one approved trigger applies: inserted Chinese; “How do you say…?” or an explicit wording question; repeated hesitation or failed self-repair; inaccurate substitution; morning-retell non-retrieval; a confirmed unfamiliar word or expression requiring focused reinforcement; a synonym, antonym, word-family or sense set worth learning together; a concise complete sentence unsuitable for Context Cloze and Topic Retell; or a marked item that cannot be embedded naturally without distortion.

<a id="legacy-p0430"></a>

A Vocabulary note may coexist with a natural Context Cloze when it adds a distinct lexical function supported by direct production evidence, such as synonym consolidation, sense distinction or focused recall. Do not duplicate the same expression merely because it appears in context; record the additional Vocabulary purpose.

<a id="legacy-p0431"></a>

Keep definitions short, sense-specific and consistent with the diary context.

<a id="legacy-p0432"></a>

Vocabulary Evidence and Grouping Rules

<a id="legacy-p0433"></a>

For every Vocabulary candidate, record the evidence used during notebook review: Chinese insertion, direct wording request, hesitation, self-correction, inaccurate production, morning-retell failure, user formatting, confirmed historical target, synonym grouping or card-type conversion.

<a id="legacy-p0434"></a>

The evidence label is review metadata and need not become a permanent Anki field unless the user requests it.

<a id="legacy-p0435"></a>

Group expressions only when one Chinese cue can retrieve them as alternatives or when the Front explicitly tests their distinction. Do not build unrelated vocabulary lists merely to reduce card count.

<a id="legacy-p0436"></a>

Where the same meaning has several natural English forms, present them as `expression A / expression B / expression C` and keep their grammatical forms parallel.

<a id="legacy-p0437"></a>

Where one word is polysemous, create sense-specific cues or separate cards when a single cue would be ambiguous. Do not teach multiple unrelated senses under one vague Front.

<a id="legacy-p0438"></a>

Sentence-level Vocabulary notes are permitted for concise quotations, summary statements or exact translations that would otherwise require hiding the whole sentence in Context Cloze.

<a id="legacy-p0439"></a>

### 6.4 OralDiary — Guidance

<a id="legacy-p0440"></a>

Purpose

<a id="legacy-p0441"></a>

Guidance notes preserve bold advice, principles and useful reflections for repeated reading and practical internalisation. They do not require the learner to reproduce the whole English passage from memory.

<a id="legacy-p0442"></a>

Front

<a id="legacy-p0443"></a>

Provide the complete Chinese translation of the guidance sentence or passage. Cloze-style blanks appear only in the Chinese translation at the concepts corresponding to the selected English emphasis targets.

<a id="legacy-p0444"></a>

Back

<a id="legacy-p0445"></a>

Provide the complete English guidance sentence or passage. Highlight every English answer corresponding to a blank on the Chinese Front in the same shared answer style as Context Cloze: light blue (#5BC0EB), bold and underline.

<a id="legacy-p0446"></a>

Exact Blank-to-Highlight Alignment

<a id="legacy-p0447"></a>

Each Chinese blank and English highlight must test the same minimal semantic unit. Do not highlight surrounding complements, pronouns or contrastive context merely because they occur in the same phrase.

<a id="legacy-p0448"></a>

If the Chinese blank is the verb “揭示”, highlight only `reveals`; leave `them, not me` visible as contextual support.

<a id="legacy-p0449"></a>

If the answer is an approved synonym set, one Chinese blank may correspond to one slash-separated highlighted set. Otherwise, each blank should have one clearly identifiable highlighted answer in the same logical order.

<a id="legacy-p0450"></a>

After generating or editing Guidance, audit the number, order, meaning and span of Chinese blanks against the light-blue bold-underlined English answers.

<a id="legacy-p0451"></a>

Construction Rules

<a id="legacy-p0452"></a>

Preserve the full meaning of the advice; do not turn guidance into a decontextualised slogan.

<a id="legacy-p0453"></a>

Blank only the concepts worth noticing. The card is for attentive rereading, not high-pressure verbatim recall.

<a id="legacy-p0454"></a>

A Guidance note is a hybrid coverage card: its Chinese Front blanks test the selected concepts and vocabulary, while its complete English Back supports sentence-level reconstruction and retelling practice. Italic or underlined material occurring inside Guidance is therefore considered covered by that Guidance note.

<a id="legacy-p0455"></a>

Do not create a separate Context Cloze merely because an unfamiliar word appears inside Guidance.

<a id="legacy-p0456"></a>

Do not create a separate Topic Retell merely because the Guidance passage is a complete sentence or coherent passage.

<a id="legacy-p0457"></a>

Create another note only when the same material has been independently selected from non-Guidance diary content for a distinct learning purpose; its presence in Guidance alone is never sufficient reason.

<a id="legacy-p0458"></a>

## 7. Topic Retell Selection Rules

<a id="legacy-p0459"></a>

Use the following rules to select dedicated Topic Retell notes in addition to the mandatory paired Topic Retell created for every Context Cloze. Generate a dedicated Topic Retell note when one or more of the following conditions apply.

<a id="legacy-p0460"></a>

Rule 1 — Several Sentences Are Needed

<a id="legacy-p0461"></a>

The idea cannot be explained properly in one sentence.

<a id="legacy-p0462"></a>

It requires several connected sentences to communicate a complete point.

<a id="legacy-p0463"></a>

Examples include:

<a id="legacy-p0464"></a>

cause → effect;

<a id="legacy-p0465"></a>

situation → problem → consequence;

<a id="legacy-p0466"></a>

problem → solution;

<a id="legacy-p0467"></a>

observation → explanation → example;

<a id="legacy-p0468"></a>

concern → options → decision;

<a id="legacy-p0469"></a>

chronological stages;

<a id="legacy-p0470"></a>

contrast between two situations.

<a id="legacy-p0471"></a>

This applies even when every sentence uses simple vocabulary.

<a id="legacy-p0472"></a>

Rule 2 — The Logical Order Must Be Retrieved

<a id="legacy-p0473"></a>

Generate Topic Retell when the order of ideas is part of what needs to be learned.

<a id="legacy-p0474"></a>

Removing or rearranging the stages would make the explanation:

<a id="legacy-p0475"></a>

incomplete;

<a id="legacy-p0476"></a>

unclear;

<a id="legacy-p0477"></a>

less persuasive;

<a id="legacy-p0478"></a>

logically weaker.

<a id="legacy-p0479"></a>

Rule 3 — Familiar Words Need Contextual Application

<a id="legacy-p0480"></a>

Generate Topic Retell when the individual words are familiar, but the learner needs practice using those simple words together to explain a specific situation.

<a id="legacy-p0481"></a>

The learning target is the complete explanation rather than isolated vocabulary.

<a id="legacy-p0482"></a>

Rule 4 — The Passage Has Both Vocabulary and Discourse Value

<a id="legacy-p0483"></a>

A passage may contain several unfamiliar expressions while also requiring a coherent, progressive explanation.

<a id="legacy-p0484"></a>

In that case, generate both:

<a id="legacy-p0485"></a>

Context Cloze for the expressions;

<a id="legacy-p0486"></a>

Topic Retell for the full reasoning.

<a id="legacy-p0487"></a>

These are not considered duplicate cards because they test different language abilities.

<a id="legacy-p0488"></a>

Do Not Generate Topic Retell When

<a id="legacy-p0489"></a>

one sentence can fully communicate the idea;

<a id="legacy-p0490"></a>

the content is merely a list of unrelated examples;

<a id="legacy-p0491"></a>

the passage contains no meaningful logical progression;

<a id="legacy-p0492"></a>

only one word or collocation needs to be learned;

<a id="legacy-p0493"></a>

several sentences merely repeat the same point without adding a new logical stage.

<a id="legacy-p0494"></a>

Unit of Selection

<a id="legacy-p0495"></a>

Select Topic Retell notes by complete reasoning unit, not automatically by:

<a id="legacy-p0496"></a>

diary topic;

<a id="legacy-p0497"></a>

paragraph length;

<a id="legacy-p0498"></a>

number of sentences.

<a id="legacy-p0499"></a>

One broad topic may produce:

<a id="legacy-p0500"></a>

no Topic Retell notes;

<a id="legacy-p0501"></a>

one Topic Retell note;

<a id="legacy-p0502"></a>

several Topic Retell notes containing independent lines of reasoning.

<a id="legacy-p0504"></a>

## 8. Paired Context Cloze and Topic Retell Notes

<a id="legacy-p0505"></a>

Mandatory Pairing Rule

<a id="legacy-p0506"></a>

Guidance notes are not Context Cloze notes and do not require a paired Topic Retell. Their bilingual blank-and-answer format is treated as sufficient combined lexical and sentence-level coverage.

<a id="legacy-p0507"></a>

Every Context Cloze note must have one corresponding Topic Retell note. Topic Retell notes selected independently under Section 7 are retained in addition to these mandatory pairs.

<a id="legacy-p0508"></a>

Before adding a paired Topic Retell, check whether the same English passage already has a Topic Retell note. If it does, keep the existing pair and do not create a third duplicate note.

<a id="legacy-p0509"></a>

Core Principle — Form Changes, Content Does Not

<a id="legacy-p0510"></a>

Paired cards test different abilities, but they must create only a change of retrieval format. They must never introduce any new learning content or additional memory burden.

<a id="legacy-p0511"></a>

The English source content must be exactly identical in both notes in:

<a id="legacy-p0512"></a>

wording;

<a id="legacy-p0513"></a>

grammar;

<a id="legacy-p0514"></a>

sentence order;

<a id="legacy-p0515"></a>

paragraph order;

<a id="legacy-p0516"></a>

examples;

<a id="legacy-p0517"></a>

logical relationships;

<a id="legacy-p0518"></a>

level of detail.

<a id="legacy-p0519"></a>

The Topic Retell Back must be produced by removing only the Cloze markup from the Context Cloze Text. No other English edit is permitted.

<a id="legacy-p0520"></a>

Permitted Format Differences

<a id="legacy-p0521"></a>

Context Cloze

<a id="legacy-p0522"></a>

uses OralDiary — Context Cloze;

<a id="legacy-p0523"></a>

contains selected {{c1::...}} deletions;

<a id="legacy-p0524"></a>

uses a complete Chinese translation of the entire English passage in the Prompt field;

<a id="legacy-p0525"></a>

may receive a qualifying Type tag only when the note has an independent cross-deck learning purpose that passes the Type admission rules in Section 9.

<a id="legacy-p0526"></a>

Paired Topic Retell

<a id="legacy-p0527"></a>

uses OralDiary — Topic Retell;

<a id="legacy-p0528"></a>

contains no Cloze markup;

<a id="legacy-p0529"></a>

uses a concise Chinese outline or logical cue in the Front field, not a complete translation;

<a id="legacy-p0530"></a>

uses the unchanged English passage in the Back field;

<a id="legacy-p0531"></a>

does not receive a Type tag merely because it is a Topic Retell note; its Note Type and destination deck already identify that format.

<a id="legacy-p0532"></a>

Strict Prohibitions

<a id="legacy-p0533"></a>

Do not paraphrase either English version;

<a id="legacy-p0534"></a>

do not add or remove sentences;

<a id="legacy-p0535"></a>

do not add explanations, examples or transitions;

<a id="legacy-p0536"></a>

do not simplify or upgrade the English;

<a id="legacy-p0537"></a>

do not introduce new vocabulary or memory targets;

<a id="legacy-p0538"></a>

do not change sentence or paragraph order;

<a id="legacy-p0539"></a>

do not create a third note when a valid pair already exists.

<a id="legacy-p0540"></a>

Paired-Card Validation

<a id="legacy-p0541"></a>

Before export, compare the Context Cloze Text after mechanically removing all Cloze markup with the paired Topic Retell Back. The two resulting English strings must match exactly, including punctuation and HTML paragraph breaks.

<a id="legacy-p0542"></a>

## 9. Tag and Deck Structure

<a id="legacy-p0543"></a>

Deck

<a id="legacy-p0544"></a>

Use one stable parent deck with four fixed subdecks:

<a id="legacy-p0545"></a>

English Oral Diary

<a id="legacy-p0546"></a>

English Oral Diary::Context Cloze

<a id="legacy-p0547"></a>

English Oral Diary::Topic Retell

<a id="legacy-p0548"></a>

English Oral Diary::Vocabulary

<a id="legacy-p0549"></a>

English Oral Diary::Guidance

<a id="legacy-p0550"></a>

Context Cloze, Topic Retell, Vocabulary and Guidance cards must be imported into their matching subdecks. Anki does not assign cards to subdecks automatically from their Note Type. The parent deck is used to study all oral-diary cards together.

<a id="legacy-p0551"></a>

Do not create daily decks such as:

<a id="legacy-p0552"></a>

2026-07-29

<a id="legacy-p0553"></a>

2026-07-30

<a id="legacy-p0554"></a>

Do not create ordinary decks for every small topic or expression type.

<a id="legacy-p0555"></a>

Anki recommends using decks for broad categories rather than narrow topics such as individual lessons or vocabulary categories.

<a id="legacy-p0556"></a>

Source Date

<a id="legacy-p0557"></a>

Store the diary date as metadata:

<a id="legacy-p0558"></a>

Source Date: YYYY-MM-DD

<a id="legacy-p0559"></a>

The date is used for traceability, not as the main study structure.

<a id="legacy-p0560"></a>

Non-Redundant Tag Principle

<a id="legacy-p0561"></a>

A tag is permitted only when it enables a useful classification or review grouping that cannot already be obtained from deck, Note Type, fields, SourceDate or the card’s other approved tags.

<a id="legacy-p0562"></a>

Do not add Source::OralDiary. The Oral Diary deck and Note Types already identify the source, so this tag has no independent filtering value.

<a id="legacy-p0563"></a>

Topic Tags

<a id="legacy-p0564"></a>

Use only broad, reusable first-level Topic categories.

<a id="legacy-p0565"></a>

Examples:

<a id="legacy-p0566"></a>

Topic::Career

<a id="legacy-p0567"></a>

Topic::Growth

<a id="legacy-p0568"></a>

Topic::Housing

<a id="legacy-p0569"></a>

Topic::Identity

<a id="legacy-p0570"></a>

Topic::Language

<a id="legacy-p0571"></a>

Topic::Productivity

<a id="legacy-p0572"></a>

Topic::Relationships

<a id="legacy-p0573"></a>

Topic::Society

<a id="legacy-p0574"></a>

Topic::Wellbeing

<a id="legacy-p0575"></a>

Topic::Work

<a id="legacy-p0576"></a>

When a future card belongs to one of these primary categories, reuse the existing first-level tag. Do not create Topic::<PrimaryCategory>::<SecondaryCategory> or any deeper Topic hierarchy.

<a id="legacy-p0577"></a>

First-Level Topic Tag Rule

<a id="legacy-p0578"></a>

Every Topic tag must have exactly the form Topic::<PrimaryCategory>. The only default primary categories are Career, Growth, Housing, Identity, Language, Productivity, Relationships, Society, Wellbeing and Work. A new primary category requires explicit user approval.

<a id="legacy-p0579"></a>

A card that genuinely spans more than one broad subject may receive multiple first-level Topic tags, but use the smallest number of categories that accurately describes it. Never create a secondary Topic tag merely to describe a specific card; retain learning-function metadata under the existing Type tags.

<a id="legacy-p0580"></a>

Before final Notebook approval, TSV export and post-import validation, tokenize every Topic tag and confirm that it contains exactly Topic plus one primary category. The number of Topic tags with a secondary or deeper level must be zero. Type tags remain single-level under Type and must independently pass the admission rules below.

<a id="legacy-p0581"></a>

Do not create a new tag merely because:

<a id="legacy-p0582"></a>

the date changed;

<a id="legacy-p0583"></a>

a slightly different example was discussed;

<a id="legacy-p0584"></a>

the card contains one specific type of argument.

<a id="legacy-p0585"></a>

Type Tags

<a id="legacy-p0587"></a>

#### Purpose

<a id="legacy-p0589"></a>

Type tags describe an optional learning task or linguistic relationship that cuts across dates, Topics, decks and Note Types. They must not restate the card format, source, destination deck or the fact that a card contains vocabulary.

<a id="legacy-p0591"></a>

Type is not a required field. A card with no additional independent filtering value receives no Type tag. Type coverage rate is never a quality target.

<a id="legacy-p0593"></a>

#### Prohibited Redundant Type Tags

<a id="legacy-p0595"></a>

Do not create or retain Type::CoreExpression, Type::TopicRetell or Type::Guidance. These repeat information already supplied by the learning target, Note Type or deck. Do not create Type::Vocabulary; Vocabulary is already a deck and Note Type, and this tag was not part of the established collection.

<a id="legacy-p0597"></a>

Do not mechanically rename Type::NativeChunk. Re-evaluate the actual learning objective of every affected card under the admission gate; remove the old tag when no qualifying independent review dimension remains.

<a id="legacy-p0599"></a>

#### Type Admission Gate

<a id="legacy-p0601"></a>

A Type tag may be assigned only when all conditions are true: it represents a stable and reusable learning dimension; it does not duplicate deck, Note Type, SourceDate, first-level Topic, fields or an existing Type; the user could reasonably want to review this set across Topics, dates and decks; the membership boundary is clear; the feature is an explicit memory target rather than something merely present in the card; and no current Type can contain it without losing useful distinction.

<a id="legacy-p0603"></a>

Apply the decisive question: ‘Can this tag retrieve a group of cards with a shared, independent learning purpose that the existing card design cannot retrieve?’ If the answer is no, do not assign or create the tag.

<a id="legacy-p0605"></a>

#### Actual-Match-First Creation

<a id="legacy-p0607"></a>

Do not pre-create an inventory of empty Type tags. Audit the actual cards first and create only the Type categories for which qualifying members currently exist. Candidate concepts such as SynonymContrast, AntonymContrast, Collocation, Register, UsageBoundary, WordFamily, GrammarPattern, DiscourseFunction and Pronunciation are examples, not a mandatory fixed taxonomy.

<a id="legacy-p0609"></a>

A candidate Type normally requires at least two cards with the same independent learning purpose. A single card remains untyped unless an exceptional long-term retrieval need is explicit; record the exception and its reason in the audit ledger.

<a id="legacy-p0611"></a>

#### Controlled Automatic Expansion

<a id="legacy-p0613"></a>

For future cards, first try to match an existing Type. If none fits, automatically create a new Type only when the candidate passes every admission condition, normally has at least two actual qualifying cards, and cannot be merged with an existing Type without reducing filtering value. Otherwise leave the card untyped.

<a id="legacy-p0615"></a>

Type tags use one level only: Type::<LearningDimension>. Do not create third-level subdivisions such as Type::SynonymContrast::Adjective. New names must describe the learning task, not a particular word, topic, date or card.

<a id="legacy-p0617"></a>

#### Assignment and Set Audit

<a id="legacy-p0619"></a>

Assign Type from the card’s actual tested objective, not from words that happen to appear. Slash-separated alternatives do not automatically qualify as SynonymContrast; use that Type only when synonym relationship, distinction, interchangeability or usage boundary is itself a learning target. Likewise, the presence of a phrase does not automatically qualify as Collocation.

<a id="legacy-p0621"></a>

Use one primary Type per card by default. Permit two only when the card contains two genuinely independent review dimensions and each passes the gate separately.

<a id="legacy-p0623"></a>

After automatic assignment or migration, inspect the complete set returned by each Type. Remove false members whose qualifying phenomenon is merely incidental. Confirm that every surviving Type retrieves a coherent cross-Topic, cross-date or cross-deck learning set.

<a id="legacy-p0624"></a>

Avoid Over-Specific Tags

<a id="legacy-p0625"></a>

Do not create temporary labels such as:

<a id="legacy-p0626"></a>

Planning-Chunk

<a id="legacy-p0627"></a>

Risk-Language

<a id="legacy-p0628"></a>

Cost-Language

<a id="legacy-p0629"></a>

Decision-Making

<a id="legacy-p0630"></a>

Productivity-Chunk

<a id="legacy-p0631"></a>

unless a future recurring learning need passes every Type admission condition. Recurrence alone is not sufficient.

<a id="legacy-p0632"></a>

A useful tag must provide an independent review grouping. Topic categories require explicit user approval; Type categories may expand automatically only through the controlled admission gate above.

<a id="legacy-p0634"></a>

## 10. User Review and Finalisation

<a id="legacy-p0635"></a>

### Step 1 — User Edits Review Notebook v1

<a id="legacy-p0636"></a>

The user reviews the editable document and makes changes directly.

<a id="legacy-p0637"></a>

### Step 2 — Assistant Reads the Edited State

<a id="legacy-p0638"></a>

Do not ask the user to copy and paste the edited content back into the conversation.

<a id="legacy-p0639"></a>

Use the edited writing document as the current source of truth.

<a id="legacy-p0640"></a>

### Step 3 — Final Quality Check

<a id="legacy-p0641"></a>

Check every card for:

<a id="legacy-p0642"></a>

Language

<a id="legacy-p0643"></a>

spelling;

<a id="legacy-p0644"></a>

grammar;

<a id="legacy-p0645"></a>

punctuation;

<a id="legacy-p0646"></a>

collocations;

<a id="legacy-p0647"></a>

word forms;

<a id="legacy-p0648"></a>

natural phrase usage;

<a id="legacy-p0649"></a>

internal consistency.

<a id="legacy-p0650"></a>

Marked-Content Coverage

<a id="legacy-p0651"></a>

all italic, underlined and bold source markings have been represented, merged transparently or explicitly accounted for;

<a id="legacy-p0652"></a>

Vocabulary notes have an approved evidence-based purpose: natural-context fallback, focused non-retrieval reinforcement, synonym or sense grouping, or sentence-level card-type conversion; and

<a id="legacy-p0653"></a>

Guidance notes preserve the full advice and distinguish familiarisation from verbatim recall.

<a id="legacy-p0654"></a>

Confirmed-Target Consistency

<a id="legacy-p0655"></a>

build a target register from the user’s manual markings and approved Cloze edits;

<a id="legacy-p0656"></a>

record the target lemma or expression, all observed inflectional or derivational forms, and the cards in which they occur;

<a id="legacy-p0657"></a>

confirm that every applicable occurrence is Clozed across the complete notebook;

<a id="legacy-p0658"></a>

confirm that Cloze spans are neither broader nor narrower than the intended learning unit; and

<a id="legacy-p0659"></a>

confirm that no English was added or rewritten merely to expand a target family.

<a id="legacy-p0660"></a>

Cloze-Boundary and Expansion Audit

<a id="legacy-p0661"></a>

each deletion isolates the intended unfamiliar word or meaningful chunk without unnecessarily hiding personal pronouns or familiar contextual scaffolding;

<a id="legacy-p0662"></a>

pronouns, particles, prepositions and complements remain inside a deletion only when they are integral to the tested expression;

<a id="legacy-p0663"></a>

independent lexical targets inside one sentence use separate same-number deletions where appropriate;

<a id="legacy-p0664"></a>

all materially marked source content is represented through an existing context, an expanded context, a new paired reasoning unit, Vocabulary or Guidance;

<a id="legacy-p0665"></a>

new cards created from the user’s notes add genuine language or reasoning coverage rather than duplicating the same function; and

<a id="legacy-p0666"></a>

unmarked transcript material has not been copied merely to increase card count.

<a id="legacy-p0667"></a>

Semantic Redundancy Audit

<a id="legacy-p0668"></a>

compare every card with all other cards by underlying meaning, not only wording;

<a id="legacy-p0669"></a>

merge cards whose reasoning and retrieval purpose are substantially the same, preserving useful alternatives with slash notation;

<a id="legacy-p0670"></a>

confirm that any remaining similar cards test genuinely different logic or skills; and

<a id="legacy-p0671"></a>

apply the same audit to Guidance, where repeated advice should be consolidated into one complete card.

<a id="legacy-p0672"></a>

Card-Type Suitability Audit

<a id="legacy-p0673"></a>

confirm that a Context Cloze leaves enough scaffold for local retrieval;

<a id="legacy-p0674"></a>

move an isolated whole-sentence target to Vocabulary unless it qualifies under the explicit full-sentence exception;

<a id="legacy-p0675"></a>

confirm that every Topic Retell contains real discourse progression rather than one sentence; and

<a id="legacy-p0676"></a>

confirm that Vocabulary duplicates have documented lexical reinforcement or distinction value.

<a id="legacy-p0677"></a>

Reverse-Cue Audit

<a id="legacy-p0678"></a>

check antonyms, synonyms, parallel clauses, definitions and translations that remain visible and could reveal a Cloze answer;

<a id="legacy-p0679"></a>

hide the revealing counterpart with the same Cloze number when necessary; and

<a id="legacy-p0680"></a>

re-run this audit after the user edits any Cloze span.

<a id="legacy-p0681"></a>

Guidance Alignment Audit

<a id="legacy-p0682"></a>

verify that every Chinese blank maps to the exact minimal English highlight, with no extra words highlighted;

<a id="legacy-p0683"></a>

verify that the highlighted answers appear in the same logical order as the Chinese blanks; and

<a id="legacy-p0684"></a>

verify that slash-separated highlighted alternatives truly answer the same blank.

<a id="legacy-p0685"></a>

Guidance-internal vocabulary has not generated a separate Context Cloze solely because it is unfamiliar;

<a id="legacy-p0686"></a>

a complete Guidance passage has not generated a Topic Retell solely because it is coherent or sentence-length;

<a id="legacy-p0687"></a>

any additional note sharing Guidance content has an independent non-Guidance source and a clearly distinct learning purpose; and

<a id="legacy-p0688"></a>

high-, medium- and low-confidence predictive markings were handled according to the approved review threshold.

<a id="legacy-p0689"></a>

Anki Syntax

<a id="legacy-p0690"></a>

every opening {{c1:: has a matching }};

<a id="legacy-p0691"></a>

each Context Cloze note contains at least one valid Cloze deletion;

<a id="legacy-p0692"></a>

Cloze numbering matches the intended number of cards;

<a id="legacy-p0693"></a>

the correct Note Type is assigned;

<a id="legacy-p0694"></a>

required fields are present;

<a id="legacy-p0695"></a>

tags use the fixed naming system;

<a id="legacy-p0696"></a>

paired Context Cloze and Topic Retell notes match exactly.

<a id="legacy-p0697"></a>

Vocabulary and Guidance notes contain exactly four export fields in the approved order;

<a id="legacy-p0698"></a>

every Guidance Back highlights the English answers corresponding to the Chinese Front blanks; and

<a id="legacy-p0699"></a>

every Guidance highlight uses the smallest answer span and does not accidentally include visible contextual support;

<a id="legacy-p0700"></a>

every slash-separated Vocabulary or Cloze set contains valid semantic alternatives or an explicitly requested distinction;

<a id="legacy-p0701"></a>

no visible synonym or antonym gives away a hidden target on the same card;

<a id="legacy-p0702"></a>

Guidance highlighting uses valid HTML that survives TSV import.

<a id="legacy-p0703"></a>

Anki Cloze syntax only functions correctly with a Cloze Note Type, and the Cloze text must contain valid deletion markup.

<a id="legacy-p0704"></a>

Error-Class Global Scan

<a id="legacy-p0705"></a>

When the user identifies one error, first abstract its error class and scan the whole notebook before returning a revision. A Guidance mismatch triggers all-Guidance alignment review; an uncovered mark triggers the complete ledger and word-family review; a duplicate Vocabulary note triggers cross-type lexical review; an unusable Front triggers all-card independent-retrievability review; and a synonym correction triggers the full synonym register review.

<a id="legacy-p0706"></a>

The revision report must identify the reported example, abstract error class, full scan scope, every additional same-class correction and the reason similar items were intentionally left unchanged.

<a id="legacy-p0707"></a>

Guidance Three-Way Alignment Gate

<a id="legacy-p0708"></a>

For every Guidance note, build an internal ordered mapping of Chinese blank, minimal English answer and exact English highlight span. Chinese blank count, answer count and highlight count must be identical; order and meaning must match; highlighted text must equal the answer with no extra or missing words. Slash alternatives answer one blank. Perform both directions independently: each Chinese blank must lead to exactly one minimal English answer and highlight, and every English highlight must lead back to exactly one corresponding Chinese blank. Perform a semantic back-translation check rather than relying on position alone. Resolve meaning and target-boundary conflicts from the authority order above, using the original conversation when the manual-notebook stage is absent.

<a id="legacy-p0709"></a>

Guidance Atomic Linked-Update Rule

<a id="legacy-p0710"></a>

Treat authoritative source, complete English Guidance, minimal English answer, exact English highlight, complete Chinese translation, Chinese blank range and rendered underline as one atomic linked unit. A change to any member automatically invalidates the previous Guidance Alignment PASS and requires source-fidelity, forward-mapping, reverse-mapping and rendered-display audits to run again.

<a id="legacy-p0711"></a>

if the Chinese blank or its semantic range changes, automatically recalculate the minimal English answer and highlight, then check visible English for answer leakage;

<a id="legacy-p0712"></a>

if the English answer or highlight changes, automatically verify and minimally revise the corresponding complete Chinese translation and blank range;

<a id="legacy-p0713"></a>

if the complete English Guidance changes, first revalidate it against the authoritative source, then regenerate the complete Chinese translation and rebuild every blank–answer–highlight mapping; and

<a id="legacy-p0714"></a>

if the Chinese translation changes, revalidate it against both the authoritative source and complete English, then propagate any changed semantic boundary to the English answer and highlight.

<a id="legacy-p0715"></a>

Guidance Underline-Only Blank Display Gate

<a id="legacy-p0716"></a>

On every Guidance Front, remove the tested Chinese answer completely and show only a continuous underline at its original position. Do not leave the answer, partial characters, brackets, initials, English hints, highlighted HTML or other answer-revealing characters visible. Validate every blank, not a sample, in the DOCX, exported Front field and final Anki rendering. Any visible answer residue or non-underline blank makes Card-Design Audit and Render Audit FAIL.

<a id="legacy-p0717"></a>

Two-Way Target-Boundary Gate

<a id="legacy-p0718"></a>

Check both omission and overreach. Every manual target must be fully represented, and no answer may include unmarked surrounding words unless they are indispensable to a fixed expression or grammatical production target. Document every justified expansion.

<a id="legacy-p0719"></a>

Source-Fidelity and No-Semantic-Rewrite Gate

<a id="legacy-p0720"></a>

Apply the authoritative-source fidelity rule to every Context Cloze, Topic Retell, Vocabulary and Guidance note before finalisation. Verify source-to-English, English-to-Chinese and Chinese-back-to-source equivalence. Card-format conversion, translation, consolidation and naturalisation may not change the underlying claim. One mismatch invalidates the Content Audit for the affected unit and triggers a whole-notebook scan for the same semantic-drift class.

<a id="legacy-p0721"></a>

Finalisation Stop Conditions

<a id="legacy-p0722"></a>

Do not declare a final notebook while any marked item is unaccounted for, any note fails authoritative-source fidelity, any Guidance forward or reverse mapping differs, any linked update remains stale, any Guidance Front reveals more than underline at a tested position, any Vocabulary Front is not independently answerable, any duplicate lacks a documented purpose, any synonym set remains unclassified, any confirmed occurrence remains unaudited, paired English differs, DOCX pages remain unrendered or expected Anki import counts do not reconcile. Do not declare the complete diary workflow finished until the post-cycle learning and Protocol delta audit also passes.

<a id="legacy-p0723"></a>

### Step 4 — Preserve Approved Content

<a id="legacy-p0724"></a>

During the final check:

<a id="legacy-p0725"></a>

correct actual language errors;

<a id="legacy-p0726"></a>

correct broken Anki formatting;

<a id="legacy-p0727"></a>

do not make stylistic upgrades that the user did not request;

<a id="legacy-p0728"></a>

do not replace accepted expressions with new alternatives;

<a id="legacy-p0729"></a>

do not add examples;

<a id="legacy-p0730"></a>

do not add new memory targets;

<a id="legacy-p0731"></a>

keep every unmentioned and unaffected section exactly unchanged.

<a id="legacy-p0732"></a>

The final check is proofreading and technical validation, not another rewriting stage.

<a id="legacy-p0733"></a>

Stage Isolation

<a id="legacy-p0734"></a>

Once Stage A content is approved, Stage B may merge semantically duplicate card presentations and change Note Type, Cloze span, prompt, synonym grouping or highlight formatting, but it must not silently remove a unique approved learning target or invent new diary content.

<a id="legacy-p0735"></a>

If Stage B exposes a genuine content omission, flag it explicitly and reopen only the affected content unit rather than rewriting the entire notebook.

<a id="legacy-p0736"></a>

### Step 5 — Produce Final Review Notebook

<a id="legacy-p0737"></a>

The corrected document becomes:

<a id="legacy-p0738"></a>

Final Review Notebook — Anki Notes

<a id="legacy-p0739"></a>

Final Master Notebook Archive

<a id="legacy-p0740"></a>

Every user-confirmed Final Review Notebook that serves as the source for Anki files must be stored in the single canonical folder ${EOD_PRIVATE_DATA_ROOT}/final-confirmed-notebooks. The master filename format is YYYY-MM-DD - Topic.docx, using the diary source date and a concise stable topic title.

<a id="legacy-p0741"></a>

Generate every TSV and later correction from that archived master notebook only. Working drafts, checked intermediates and rendered QA files remain outside the master folder. If the confirmed content changes, replace it through a new explicitly confirmed master version; do not silently edit the archived source after export.

<a id="legacy-p0742"></a>

It is the only source used to generate the import files.

<a id="legacy-p0744"></a>

## 11. Anki Export

<a id="legacy-p0745"></a>

Note Types

<a id="legacy-p0746"></a>

Use four separate Anki Note Types:

<a id="legacy-p0747"></a>

OralDiary — Context Cloze

<a id="legacy-p0748"></a>

OralDiary — Topic Retell

<a id="legacy-p0749"></a>

OralDiary — Vocabulary

<a id="legacy-p0750"></a>

OralDiary — Guidance

<a id="legacy-p0751"></a>

The Context Cloze type must be based on Anki’s special Cloze Note Type. A regular Front/Back Note Type cannot correctly process Cloze filters.

<a id="legacy-p0752"></a>

Default Export Files

<a id="legacy-p0753"></a>

Generate four separate UTF-8 tab-separated files:

<a id="legacy-p0754"></a>

English_Oral_Diary_Context_Cloze.tsv

<a id="legacy-p0755"></a>

English_Oral_Diary_Topic_Retell.tsv

<a id="legacy-p0756"></a>

English_Oral_Diary_Vocabulary.tsv

<a id="legacy-p0757"></a>

English_Oral_Diary_Guidance.tsv

<a id="legacy-p0758"></a>

Separate files reduce Note Type mapping errors during import.

<a id="legacy-p0759"></a>

Context Cloze Fields

<a id="legacy-p0760"></a>

Confirmed field order:

<a id="legacy-p0761"></a>

Text

<a id="legacy-p0762"></a>

Back Extra (empty)

<a id="legacy-p0763"></a>

Prompt

<a id="legacy-p0764"></a>

SourceDate

<a id="legacy-p0765"></a>

Tags

<a id="legacy-p0766"></a>

Topic Retell Fields

<a id="legacy-p0767"></a>

Confirmed field order:

<a id="legacy-p0768"></a>

Front

<a id="legacy-p0769"></a>

Back

<a id="legacy-p0770"></a>

SourceDate

<a id="legacy-p0771"></a>

Tags

<a id="legacy-p0772"></a>

Vocabulary Fields

<a id="legacy-p0773"></a>

Required field order:

<a id="legacy-p0774"></a>

Front

<a id="legacy-p0775"></a>

Back

<a id="legacy-p0776"></a>

SourceDate

<a id="legacy-p0777"></a>

Tags

<a id="legacy-p0778"></a>

Guidance Fields

<a id="legacy-p0779"></a>

Required field order:

<a id="legacy-p0780"></a>

Front

<a id="legacy-p0781"></a>

Back

<a id="legacy-p0782"></a>

SourceDate

<a id="legacy-p0783"></a>

Tags

<a id="legacy-p0784"></a>

Line Breaks

<a id="legacy-p0785"></a>

When paragraph breaks are needed inside an imported field, use HTML line breaks such as:

<a id="legacy-p0786"></a>

<br><br>

<a id="legacy-p0787"></a>

and enable HTML in fields during import.

<a id="legacy-p0788"></a>

In Guidance Back fields, encode the selected English answers as `<span class="guidance-answer" style="color:#5BC0EB"><b><u>answer</u></b></span>`. Enable HTML in fields so the light-blue, bold and underlined emphasis is preserved.

<a id="legacy-p0789"></a>

Anki’s text-import documentation warns that escaped multiline fields may not work correctly when Cloze deletions span multiple lines, while HTML line breaks are supported when HTML is enabled.

<a id="legacy-p0790"></a>

Tags

<a id="legacy-p0791"></a>

Include tags in a dedicated field and map that field to Tags during import. Anki’s text importer supports importing tags from a field. Tags remain required metadata for filtering, custom study and targeted review, but they must not be placed in any Front or Back Template and must not be displayed during ordinary card review.

<a id="legacy-p0792"></a>

Deck Destination

<a id="legacy-p0793"></a>

Import Context Cloze into:

<a id="legacy-p0794"></a>

English Oral Diary::Context Cloze

<a id="legacy-p0795"></a>

Import Topic Retell into:

<a id="legacy-p0796"></a>

English Oral Diary::Topic Retell

<a id="legacy-p0797"></a>

Import Vocabulary into:

<a id="legacy-p0798"></a>

English Oral Diary::Vocabulary

<a id="legacy-p0799"></a>

Import Guidance into:

<a id="legacy-p0800"></a>

English Oral Diary::Guidance

<a id="legacy-p0801"></a>

Do not import any file into the parent deck and do not create dated decks. Each file must be mapped to the matching Note Type and subdeck.

<a id="legacy-p0802"></a>

Confirmed Anki Setup and Import Procedure

<a id="legacy-p0803"></a>

One-Time Deck Setup

<a id="legacy-p0804"></a>

Create the parent deck English Oral Diary.

<a id="legacy-p0805"></a>

Create the subdecks English Oral Diary::Context Cloze, English Oral Diary::Topic Retell, English Oral Diary::Vocabulary and English Oral Diary::Guidance.

<a id="legacy-p0806"></a>

One-Time Context Cloze Note Type Setup

<a id="legacy-p0807"></a>

Clone Anki’s built-in Cloze Note Type and name it OralDiary — Context Cloze. Do not build it from Basic.

<a id="legacy-p0808"></a>

Use these fields in this order: Text; Back Extra; Prompt; SourceDate.

<a id="legacy-p0809"></a>

Front Template: display {{Prompt}}, then {{cloze:Text}}.

<a id="legacy-p0810"></a>

Back Template: display {{Prompt}}, {{cloze:Text}} and optional {{Back Extra}}. Do not include {{SourceDate}} or {{Tags}}; both remain stored as metadata and available for filtering.

<a id="legacy-p0811"></a>

One-Time Topic Retell Note Type Setup

<a id="legacy-p0812"></a>

Clone Anki’s Basic Note Type and name it OralDiary — Topic Retell.

<a id="legacy-p0813"></a>

Use these fields in this order: Front; Back; SourceDate.

<a id="legacy-p0814"></a>

Front Template: display {{Front}}.

<a id="legacy-p0815"></a>

Back Template: display {{Front}} and {{Back}}. Do not include {{SourceDate}} or {{Tags}}; both remain stored as metadata and available for filtering.

<a id="legacy-p0816"></a>

One-Time Vocabulary Note Type Setup

<a id="legacy-p0817"></a>

Create by cloning Anki’s Basic Note Type. Use fields in this exact order:

<a id="legacy-p0818"></a>

## 1. Front

<a id="legacy-p0819"></a>

## 2. Back

<a id="legacy-p0820"></a>

## 3. SourceDate

<a id="legacy-p0821"></a>

Front Template

<a id="legacy-p0822"></a>

{{Front}}

<a id="legacy-p0823"></a>

Back Template

<a id="legacy-p0824"></a>

{{FrontSide}}

<a id="legacy-p0825"></a>

<hr id=answer>

<a id="legacy-p0826"></a>

{{Back}}

<a id="legacy-p0827"></a>

<div class="source-date">{{SourceDate}}</div>

<a id="legacy-p0828"></a>

One-Time Guidance Note Type Setup

<a id="legacy-p0829"></a>

Create by cloning Anki’s Basic Note Type. Use fields and templates identical to OralDiary — Vocabulary. The Back field itself contains the approved HTML emphasis for the English answers. In Styling, ensure `.guidance-answer` and legacy purple Guidance spans render as #5BC0EB, bold and underlined so existing and newly imported Guidance notes share the same appearance.

<a id="legacy-p0830"></a>

Export Requirements

<a id="legacy-p0831"></a>

Generate four UTF-8 tab-separated files without a header row. A header row would be imported as a false note.

<a id="legacy-p0832"></a>

Canonical TSV and Temporary Import-Copy Boundary

<a id="legacy-p0833"></a>

The archived export files remain the four validated no-header TSVs and are the only canonical import data. When Anki’s import interface cannot be set reliably, a temporary byte-faithful copy may add only official import directives that select an already existing Note Type, already existing destination subdeck, HTML mode, field names and Tags column. It must not create, clone, rename or modify any Note Type, deck, field, template or styling, and it must not alter card data. Before import, verify the resolved existing names and mappings; after import, reconcile the existing object IDs, exact field values, tags and destination deck against the canonical TSV. The temporary copy never replaces the canonical file and remains an implementation artefact only.

<a id="legacy-p0834"></a>

Context Cloze TSV column order: Text; empty Back Extra; Prompt; SourceDate; Tags.

<a id="legacy-p0835"></a>

Vocabulary TSV column order: Front; Back; SourceDate; Tags.

<a id="legacy-p0836"></a>

Guidance TSV column order: Front; Back; SourceDate; Tags.

<a id="legacy-p0837"></a>

Topic Retell TSV column order: Front; Back; SourceDate; Tags.

<a id="legacy-p0838"></a>

Convert paragraph breaks inside fields to <br><br> and enable Allow HTML in fields during import.

<a id="legacy-p0839"></a>

Context Cloze Import

<a id="legacy-p0840"></a>

Open the Context Cloze TSV in Anki.

<a id="legacy-p0841"></a>

Select Note Type OralDiary — Context Cloze.

<a id="legacy-p0842"></a>

Select deck English Oral Diary::Context Cloze.

<a id="legacy-p0843"></a>

Map Text → column 1, Back Extra → column 2, Prompt → column 3, SourceDate → column 4, and Tags → column 5.

<a id="legacy-p0844"></a>

Add the approved first-level Topic tag and only those optional Type tags that pass the Type admission rules; do not add a global source tag.

<a id="legacy-p0845"></a>

Enable Allow HTML in fields and import.

<a id="legacy-p0846"></a>

Vocabulary Import

<a id="legacy-p0847"></a>

Open the Vocabulary TSV in Anki.

<a id="legacy-p0848"></a>

Select Note Type OralDiary — Vocabulary.

<a id="legacy-p0849"></a>

Select deck English Oral Diary::Vocabulary.

<a id="legacy-p0850"></a>

Map Front → column 1, Back → column 2, SourceDate → column 3, and Tags → column 4.

<a id="legacy-p0851"></a>

Add the approved first-level Topic tag and only those optional Type tags that pass the Type admission rules; do not add a global source tag.

<a id="legacy-p0852"></a>

Enable Allow HTML in fields and import.

<a id="legacy-p0853"></a>

Guidance Import

<a id="legacy-p0854"></a>

Open the Guidance TSV in Anki.

<a id="legacy-p0855"></a>

Select Note Type OralDiary — Guidance.

<a id="legacy-p0856"></a>

Select deck English Oral Diary::Guidance.

<a id="legacy-p0857"></a>

Map Front → column 1, Back → column 2, SourceDate → column 3, and Tags → column 4.

<a id="legacy-p0858"></a>

Add the approved first-level Topic tag and only those optional Type tags that pass the Type admission rules; do not add a global source tag.

<a id="legacy-p0859"></a>

Enable Allow HTML in fields and import.

<a id="legacy-p0860"></a>

Topic Retell Import

<a id="legacy-p0861"></a>

Open the Topic Retell TSV in Anki.

<a id="legacy-p0862"></a>

Select Note Type OralDiary — Topic Retell.

<a id="legacy-p0863"></a>

Select deck English Oral Diary::Topic Retell.

<a id="legacy-p0864"></a>

Map Front → column 1, Back → column 2, SourceDate → column 3, and Tags → column 4.

<a id="legacy-p0865"></a>

Add the approved first-level Topic tag and only those optional Type tags that pass the Type admission rules; do not add a global source tag.

<a id="legacy-p0866"></a>

Enable Allow HTML in fields and import.

<a id="legacy-p0867"></a>

Post-Import Check

<a id="legacy-p0868"></a>

Confirm that the parent deck total equals the sum of all four subdecks and that the parent itself contains no directly assigned cards.

<a id="legacy-p0869"></a>

Confirm that each of the four subdeck counts equals the number of rows in its matching TSV.

<a id="legacy-p0870"></a>

If cards were accidentally imported into the parent deck, filter them by Note Type in Browse, select all matching cards, use Cards → Change Deck, and move each type to its correct subdeck.

<a id="legacy-p0871"></a>

Database-Level Import Reconciliation

<a id="legacy-p0872"></a>

After import, verify both the Anki result report and the collection state: this run’s added or updated note count by Note Type, card count by destination deck, first-level Topic-tag compliance, optional Type-tag admission compliance, absence of Source::OralDiary, expected field count, preserved Guidance HTML and absence of notes assigned directly to the parent deck. Do not rely only on the import dialog when a read-only collection check is available.

<a id="legacy-p0873"></a>

## 12. First Import Validation

<a id="legacy-p0874"></a>

Because the first live Anki import is part of establishing the system, complete one validation round.

<a id="legacy-p0875"></a>

After importing, check:

<a id="legacy-p0876"></a>

the deck is correct;

<a id="legacy-p0877"></a>

the intended Note Type was selected;

<a id="legacy-p0878"></a>

Chinese prompts display correctly;

<a id="legacy-p0879"></a>

paragraph breaks display correctly;

<a id="legacy-p0880"></a>

Cloze deletions work;

<a id="legacy-p0881"></a>

notes using only c1 generate one card;

<a id="legacy-p0882"></a>

Topic Retell Front and Back map correctly;

<a id="legacy-p0883"></a>

hierarchical tags are stored, searchable and usable for filtered review, but do not display on the Front or Back of any card;

<a id="legacy-p0884"></a>

Chinese and English punctuation are not corrupted;

<a id="legacy-p0885"></a>

Vocabulary Front/Back and definitions map correctly;

<a id="legacy-p0886"></a>

Guidance Fronts show the complete Chinese translation with the intended blanks;

<a id="legacy-p0887"></a>

Guidance Backs show the complete English passage and the corresponding answers in light blue (#5BC0EB), bold and underline;

<a id="legacy-p0888"></a>

the four subdeck counts add up to the parent deck total, with no notes assigned directly to the parent;

<a id="legacy-p0889"></a>

confirmed targets and their observed word-family forms are Clozed consistently across all Context Cloze notes;

<a id="legacy-p0890"></a>

repeated contextual appearances of the same target remain separate intentional tests rather than being removed as duplicates;

<a id="legacy-p0891"></a>

Cloze spans do not unnecessarily include personal pronouns, proper names or familiar contextual complements;

<a id="legacy-p0892"></a>

every item added from the user’s marked notes has a documented placement in Context Cloze, Topic Retell, Vocabulary or Guidance;

<a id="legacy-p0893"></a>

Guidance content has not produced automatic Context Cloze or Topic Retell duplicates;

<a id="legacy-p0894"></a>

repeated imports do not create unexpected duplicates.

<a id="legacy-p0895"></a>

If any import problem appears:

<a id="legacy-p0896"></a>

identify whether it comes from the file, field mapping, Note Type or Anki settings;

<a id="legacy-p0897"></a>

correct only the export implementation;

<a id="legacy-p0898"></a>

do not change the learning-content rules unless the problem genuinely concerns card design.

<a id="legacy-p0899"></a>

After the first successful import, lock the confirmed field mapping and export settings into the next protocol version.

<a id="legacy-p0901"></a>

## 13. Daily Workflow Summary

<a id="legacy-p0902"></a>

Night

<a id="legacy-p0903"></a>

English oral diary

<a id="legacy-p0904"></a>

↓

<a id="legacy-p0905"></a>

Free speaking

<a id="legacy-p0906"></a>

↓

<a id="legacy-p0907"></a>

Minimal correction

<a id="legacy-p0908"></a>

↓

<a id="legacy-p0909"></a>

Lock each topic as a formatted Topic Reference Checkpoint

<a id="legacy-p0910"></a>

↓

<a id="legacy-p0911"></a>

Nightly missing-topic audit and zero-rewrite Night Reference Record aggregation

<a id="legacy-p0912"></a>

Morning at 08:30

<a id="legacy-p0913"></a>

Short outline

<a id="legacy-p0914"></a>

↓

<a id="legacy-p0915"></a>

Full retell

<a id="legacy-p0916"></a>

↓

<a id="legacy-p0917"></a>

Comparison with corrected reference

<a id="legacy-p0918"></a>

↓

<a id="legacy-p0919"></a>

Restore missing expressions and logic

<a id="legacy-p0920"></a>

↓

<a id="legacy-p0921"></a>

Generate editable Review Notebook v1

<a id="legacy-p0922"></a>

↓

<a id="legacy-p0923"></a>

Compare predicted content with the user’s organised or marked notebook

<a id="legacy-p0924"></a>

↓

<a id="legacy-p0925"></a>

Complete Stage A content-selection calibration

<a id="legacy-p0926"></a>

↓

<a id="legacy-p0927"></a>

Freeze the authoritative content source

<a id="legacy-p0928"></a>

Card Review

<a id="legacy-p0929"></a>

User edits cards directly

<a id="legacy-p0930"></a>

↓

<a id="legacy-p0931"></a>

Compare the generated Anki notebook with the user’s final card edits

<a id="legacy-p0932"></a>

↓

<a id="legacy-p0933"></a>

Complete Stage B card-design calibration

<a id="legacy-p0934"></a>

↓

<a id="legacy-p0935"></a>

Consolidate semantic duplicates and run card-type, reverse-cue, Vocabulary-evidence and Guidance-alignment audits

<a id="legacy-p0936"></a>

↓

<a id="legacy-p0937"></a>

Assistant reads edited state

<a id="legacy-p0938"></a>

↓

<a id="legacy-p0939"></a>

Language and Anki-format quality check

<a id="legacy-p0940"></a>

↓

<a id="legacy-p0941"></a>

No unrequested rewriting

<a id="legacy-p0942"></a>

↓

<a id="legacy-p0943"></a>

Final confirmed master notebook archived as YYYY-MM-DD - Topic.docx

<a id="legacy-p0944"></a>

Anki

<a id="legacy-p0945"></a>

Generate Context Cloze TSV

<a id="legacy-p0946"></a>

+

<a id="legacy-p0947"></a>

Generate Vocabulary TSV

<a id="legacy-p0948"></a>

+

<a id="legacy-p0949"></a>

Generate Guidance TSV

<a id="legacy-p0950"></a>

+

<a id="legacy-p0951"></a>

Generate Topic Retell TSV

<a id="legacy-p0952"></a>

↓

<a id="legacy-p0953"></a>

Import each Note Type into its corresponding English Oral Diary subdeck

<a id="legacy-p0954"></a>

↓

<a id="legacy-p0955"></a>

Validate first import

<a id="legacy-p0956"></a>

↓

<a id="legacy-p0957"></a>

Run Gate 10 post-cycle learning and Protocol delta audit

<a id="legacy-p0958"></a>

↓

<a id="legacy-p0959"></a>

Only then declare the complete workflow finished

<a id="legacy-p0960"></a>

↓

<a id="legacy-p0961"></a>

Anki manages the review schedule

<a id="legacy-p0963"></a>

## 14. Default Automation Instruction

<a id="legacy-p0964"></a>

At 08:30, the morning automation should initiate the following workflow:

<a id="legacy-p0965"></a>

Use the final Night Reference Record assembled without rewriting from locked Topic Reference Checkpoints as the sole morning reference. Do not regenerate the reference from the raw night conversation. Start the morning review for the most recent English Oral Diary. First provide only a short English topic outline without revealing corrected sentences. Ask the user to retell the full diary. After the retell is complete, compare it with the previous corrected version, restore missing expressions without introducing new rewrites, and generate an editable context-based Review Notebook following the English Oral Diary Protocol. When the user supplies formatted notes, interpret italic, underline and bold according to this Protocol, complete the marked-content coverage check, and select Context Cloze, paired Topic Retell, Vocabulary and Guidance notes by their defined learning purposes. After the user reviews the notebook, treat the user’s Cloze edits as confirmed targets and run the global target-family and Cloze-granularity checks before producing the final notebook or TSV files. Treat the marked notes as an authoritative expansion source, apply the placement hierarchy, and complete the Cloze-boundary audit so unfamiliar lexical items are not unnecessarily combined with pronouns or other familiar scaffolding. When no formatted notes are available, predict italic, underline and bold using the evidence hierarchy, confidence thresholds and preference calibration rules. Treat Guidance as sufficient combined coverage for its internal vocabulary and complete English passage, and do not generate Context Cloze or Topic Retell duplicates solely from Guidance content. Use the two-stage calibration model: first finalise and freeze content selection, then calibrate card design. Before finalising cards, consolidate semantically duplicate passages and Guidance, group genuine synonym alternatives with slash notation, create evidence-based Vocabulary reinforcement for Chinese insertion, wording questions, hesitation, inaccurate production or retell failure, move unsuitable whole-sentence Cloze targets to Vocabulary, hide revealing antonym or synonym counterparts, and verify exact Chinese-blank-to-English-highlight alignment. After Gate 9 import reconciliation, run Gate 10 across the complete chat, separately summarise Stage A and Stage B learning, classify each difference as execution failure, insufficient enforcement, missing reusable rule, one-off preference or technical issue, and state whether a Protocol update is required. Do not announce full completion before this audit passes.

<a id="legacy-p0966"></a>

The Review Notebook is generated only after the user completes the retell.

<a id="legacy-p0968"></a>

## 15. Default Trigger Behaviour

<a id="legacy-p0969"></a>

Whenever the user says:

<a id="legacy-p0970"></a>

English oral diary

<a id="legacy-p0971"></a>

the assistant should automatically follow this protocol unless the user explicitly requests a different mode.

<a id="legacy-p0972"></a>

If the user says:

<a id="legacy-p0973"></a>

按 Protocol 来

<a id="legacy-p0974"></a>

resume this workflow from the appropriate stage without restarting completed steps. If Gate 9 has passed but Gate 10 has not, continue automatically with the post-cycle learning and Protocol delta audit.

<a id="legacy-p0975"></a>

If the user says:

<a id="legacy-p0976"></a>

Reopen tonight’s diary.

<a id="legacy-p0977"></a>

resume the same night diary in the same chat, preserve all immutable locked Checkpoints, accept and lock additional topics, then re-run the missing-topic audit and rebuild the Night Reference Record only through zero-rewrite aggregation. Update or replace the existing morning-review task without creating a duplicate.

<a id="legacy-p0978"></a>

If the user says:

<a id="legacy-p0979"></a>

Lock this topic reference.

<a id="legacy-p0980"></a>

run the complete Topic Reference Checkpoint workflow for the full current-topic span, including assistant-answer selection, grounded dialogue recovery, predictive notebook formatting, audit, stable-ID assignment and immutable locking.

<a id="legacy-p0981"></a>

If the user says either:

<a id="legacy-p0982"></a>

Finalize tonight’s Night Reference Record and schedule tomorrow morning’s review.

<a id="legacy-p0983"></a>

or:

<a id="legacy-p0984"></a>

End tonight’s diary and schedule tomorrow morning’s review.

<a id="legacy-p0985"></a>

audit the full night for missing or partial topics, automatically build any required Checkpoints through the same locking workflow, concatenate all current locked Checkpoints without content changes, report the audit counts and schedule only one morning review.

<a id="legacy-p0986"></a>

If the user says:

<a id="legacy-p0987"></a>

End tonight’s diary and reschedule tomorrow morning’s review.

<a id="legacy-p0988"></a>

audit and finalise the complete diary, including every topic added after reopening; generate any missing Checkpoint through the normal locking workflow; aggregate all current Checkpoints without content changes; and reschedule the single morning-review task. Confirm the review date and time, topic coverage, zero-rewrite status and active-task status only after scheduling succeeds.
