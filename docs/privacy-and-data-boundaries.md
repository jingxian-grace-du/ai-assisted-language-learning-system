# Privacy and data boundaries

## Non-negotiable boundary

The repository does not need real diary content to explain or implement the learning system. It must not contain, quote, summarise, paraphrase, or allude to a learner's private diary material.

This includes content that has had names removed. Combinations of events, relationships, dates, locations, emotions, and language can remain identifiable.

## Public repository contents

Allowed by default:

- learning philosophy and system documentation;
- abstract protocol rules;
- machine-readable schemas without personal values;
- validators and transformation code;
- tests based on wholly synthetic content;
- aggregate evaluation metrics that cannot reconstruct source material;
- privacy-safe operational documentation.

Prohibited by default:

- raw oral diaries and recordings;
- chat exports or prompts containing session content;
- manual, draft, checked, or final notebooks derived from real sessions;
- Anki exports, packages, collections, or screenshots containing learning content;
- source spans in debugging output;
- model traces, temporary files, caches, or logs containing private text;
- real-life examples disguised through light editing.

## Local processing model

Private data should live outside the repository and be supplied through an explicit local path at runtime. The software should support:

- local-only input and output directories;
- configurable retention;
- minimal logging with content redaction by default;
- stable opaque identifiers instead of source text in reports;
- separate metadata and content stores where practical;
- deletion of temporary processing artefacts;
- a dry-run mode for inspecting intended operations;
- refusal to write private content inside the repository tree.

Referenced ChatGPT chats are private source inputs. Codex may paginate and
materialise them only in an external private session workspace. A Project-memory
summary, retell, screenshot, or model reconstruction is not an acceptable
replacement for missing messages. The public repository may contain the source
archive schema and synthetic tests, but never a real archive instance.

## Synthetic fixtures

Synthetic fixtures may be introduced only when a test cannot be expressed structurally. They must:

- be written from scratch rather than transformed from a real diary;
- contain no distinctive personal history;
- be visibly labelled as synthetic;
- test the smallest relevant behaviour;
- avoid presenting themselves as representative learner testimony.

The foundation release intentionally contains no diary-like fixture.

## Publication checklist

Before the first remote push:

1. inspect tracked and untracked files;
2. scan the complete Git history, not only the working tree;
3. verify ignore rules with representative filenames;
4. search for personal names, notebook titles, local source paths, and copied excerpts;
5. confirm generated reports do not embed source content;
6. establish a private security-reporting contact;
7. document the response to accidental disclosure.

Privacy validation must be a release gate, not an informal final glance.
