# Anki adapter boundary

The Anki adapter implements validated export and import contracts. It does not
decide what should be learned and may not rewrite learning content.

## Normative adapter responsibilities

- consume only validated canonical export records;
- map each Note Type to its configured matching subdeck;
- preserve approved field order, tags, HTML, and Cloze markup;
- prohibit direct card assignment to the parent deck;
- keep temporary import copies byte-faithful apart from permitted official
  import directives;
- reconcile note counts, card counts, fields, tags, HTML, and deck assignment
  against the canonical export;
- report state changes and failures without embedding private source content in
  repository logs.

## Operational profile

UI-specific steps such as opening an import dialog, selecting a dropdown, or
using a particular Browse command belong to a versioned adapter profile. They
may change with Anki without changing the learning protocol.

The adapter must verify the resulting state rather than treating successful UI
interaction as proof of a correct import.
