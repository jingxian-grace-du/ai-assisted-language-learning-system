#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PRIVATE_CLASSIFICATION = {
    "classification": "private-learning-data",
    "repository_allowed": False,
    "retention_policy": "learner-controlled",
}
EXPERIMENTAL_LABEL = "EXPERIMENTAL CANDIDATE — NOT APPROVED FOR ANKI"
REQUIRED_RM_GATES = {f"RM-{number}" for number in range(8)}
SESSION_STATES = {
    "initialized", "night-open", "night-finalized", "morning-complete",
    "candidate-generated", "gold-ready", "comparison-complete", "blocked",
}
ALLOWED_TRANSITIONS = {
    "initialized": {"night-open", "blocked"},
    "night-open": {"night-finalized", "blocked"},
    "night-finalized": {"morning-complete", "blocked"},
    "morning-complete": {"candidate-generated", "blocked"},
    "candidate-generated": {"gold-ready", "blocked"},
    "gold-ready": {"comparison-complete", "blocked"},
    "comparison-complete": set(),
    "blocked": set(),
}


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def require_external_root(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    if resolved == REPOSITORY_ROOT or REPOSITORY_ROOT in resolved.parents:
        raise SystemExit(
            "RM-PRIVATE-PATH-IN-REPOSITORY: private session data must remain outside the repository"
        )
    return resolved


def repository_fixture(value: dict) -> bool:
    privacy = value.get("privacy", {})
    return privacy.get("classification") == "synthetic" and privacy.get("repository_allowed") is True


def require_private_input_path(path: Path, value: dict) -> Path:
    resolved = path.expanduser().resolve()
    if not repository_fixture(value):
        require_external_root(resolved.parent)
    return resolved


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid JSON {path}: {error}") from error
    if not isinstance(value, dict):
        raise SystemExit(f"expected JSON object: {path}")
    return value


def artefact_directories() -> dict[str, str]:
    return {
        "source_archive": "source",
        "topic_evidence_packets": "evidence-packets",
        "checkpoints": "checkpoints",
        "learning_signals": "signals",
        "candidate_ledgers": "ledgers",
        "pilot_bundles": "bundles",
        "comparison_reports": "comparisons",
        "calibration_reports": "calibration",
        "state_transitions": "transitions",
    }


def init_session(args: argparse.Namespace) -> None:
    private_root = require_external_root(Path(args.private_root))
    session_id = args.session_id or f"EOD-{date.today().isoformat()}-S01"
    session_root = private_root / "sessions" / session_id
    if session_root.exists() and any(session_root.iterdir()):
        raise SystemExit(f"session already exists and is not empty: {session_root}")

    directories = artefact_directories()
    session_root.mkdir(parents=True, exist_ok=True)
    for relative in directories.values():
        (session_root / relative).mkdir(exist_ok=True)

    manifest = {
        "manifest_version": "0.1.0",
        "session_id": session_id,
        "mode": "phase-2-shadow",
        "protocol": {
            "stable": "3.5",
            "experimental": "raw-material-processing-v0.1",
            "profile": "3.6-draft-shadow-mode",
        },
        "status": "initialized",
        "artefacts": directories,
        "privacy": PRIVATE_CLASSIFICATION,
    }
    write_json(session_root / "session-manifest.json", manifest)
    print(session_root)


def validate_privacy(value: dict, label: str) -> list[str]:
    privacy = value.get("privacy")
    if not isinstance(privacy, dict):
        return [f"{label}: missing privacy metadata"]
    if privacy.get("classification") == "private-learning-data" and privacy.get("repository_allowed") is not False:
        return [f"{label}: private data must set repository_allowed=false"]
    if privacy.get("classification") not in {"private-learning-data", "synthetic", "aggregate-non-reconstructive"}:
        return [f"{label}: unsupported privacy classification"]
    return []


def validate_ledger(ledger: dict, label: str) -> list[str]:
    errors = []
    required = {"ledger_id", "session_id", "ledger_kind", "specification", "candidates", "privacy"}
    missing = sorted(required - set(ledger))
    if missing:
        errors.append(f"{label}: missing {', '.join(missing)}")
        return errors
    if ledger["specification"] != "raw-material-processing-v0.1":
        errors.append(f"{label}: unsupported specification")
    if not isinstance(ledger.get("candidates"), list):
        return errors + [f"{label}: candidates must be an array"]
    seen_ids = set()
    seen_keys = set()
    for index, candidate in enumerate(ledger["candidates"]):
        prefix = f"{label}.candidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{prefix}: expected object")
            continue
        for field in (
            "candidate_id", "target_key", "topic_id", "signal_ids", "learning_function",
            "note_type", "decision", "decision_reasons", "confidence", "source_span_ids",
        ):
            if field not in candidate:
                errors.append(f"{prefix}: missing {field}")
        candidate_id = candidate.get("candidate_id")
        target_key = candidate.get("target_key")
        if candidate_id in seen_ids:
            errors.append(f"{prefix}: duplicate candidate_id {candidate_id}")
        seen_ids.add(candidate_id)
        if target_key in seen_keys:
            errors.append(f"{prefix}: duplicate target_key {target_key}")
        seen_keys.add(target_key)
        if not candidate.get("source_span_ids"):
            errors.append(f"{prefix}: RM-SIGNAL-UNSUPPORTED no source spans")
        if not candidate.get("decision_reasons"):
            errors.append(f"{prefix}: decision requires a reason")
    errors.extend(validate_privacy(ledger, label))
    return errors


def validate_bundle(bundle: dict) -> list[str]:
    errors: list[str] = []
    required = {
        "bundle_version", "bundle_id", "session_manifest", "source_span_index",
        "topic_evidence_packets", "checkpoint_register", "learning_signals",
        "candidate_ledgers", "experimental_notebook_manifest", "gate_results", "privacy",
    }
    missing = sorted(required - set(bundle))
    if missing:
        return [f"bundle: missing {', '.join(missing)}"]
    if bundle.get("bundle_version") != "0.1.0":
        errors.append("bundle: unsupported bundle_version")
    errors.extend(validate_privacy(bundle, "bundle"))

    manifest = bundle.get("session_manifest", {})
    session_id = manifest.get("session_id")
    if manifest.get("mode") != "phase-2-shadow":
        errors.append("bundle.session_manifest: mode must be phase-2-shadow")
    if manifest.get("protocol", {}).get("stable") != "3.5":
        errors.append("bundle.session_manifest: stable protocol must be 3.5")
    if manifest.get("status") not in {"candidate-generated", "blocked"}:
        errors.append("bundle.session_manifest: exported bundle status must be candidate-generated or blocked")
    errors.extend(validate_privacy(manifest, "bundle.session_manifest"))

    source_index = bundle.get("source_span_index", {})
    if source_index.get("session_id") != session_id:
        errors.append("source_span_index: session ID differs")
    errors.extend(validate_privacy(source_index, "source_span_index"))
    span_ids: set[str] = set()
    span_orders: set[int] = set()
    topic_assignments: set[str] = set()
    spans = source_index.get("spans", [])
    if not isinstance(spans, list) or not spans:
        errors.append("source_span_index: spans must be a non-empty array")
        spans = []
    for index, span in enumerate(spans):
        label = f"source_span_index.spans[{index}]"
        if not isinstance(span, dict):
            errors.append(f"{label}: expected object")
            continue
        span_id = span.get("span_id")
        order = span.get("order")
        if not span_id or span_id in span_ids:
            errors.append(f"{label}: missing or duplicate span_id")
        span_ids.add(span_id)
        if not isinstance(order, int) or order < 1 or order in span_orders:
            errors.append(f"{label}: order must be unique positive integer")
        span_orders.add(order)
        has_topic = bool(span.get("topic_id"))
        has_disposition = bool(span.get("non_topic_disposition"))
        if has_topic == has_disposition:
            errors.append(f"{label}: requires exactly one topic_id or non_topic_disposition")
        if has_topic:
            topic_assignments.add(span["topic_id"])
        if "content" in span:
            errors.append(f"{label}: source text is prohibited in the content-free index")

    packets = bundle.get("topic_evidence_packets", [])
    packet_ids: set[str] = set()
    packet_topic_ids: set[str] = set()
    checkpoint_ids_from_packets: set[str] = set()
    signal_ids_from_packets: set[str] = set()
    if not isinstance(packets, list) or not packets:
        errors.append("topic_evidence_packets: expected non-empty array")
        packets = []
    for index, packet in enumerate(packets):
        label = f"topic_evidence_packets[{index}]"
        if packet.get("session_id") != session_id:
            errors.append(f"{label}: session ID differs")
        if packet.get("packet_id") in packet_ids:
            errors.append(f"{label}: duplicate packet_id")
        packet_ids.add(packet.get("packet_id"))
        packet_topic_ids.add(packet.get("topic_id"))
        checkpoint_ids_from_packets.add(packet.get("checkpoint_id"))
        signal_ids_from_packets.update(packet.get("signal_ids", []))
        missing_spans = set(packet.get("source_span_ids", [])) - span_ids
        if missing_spans:
            errors.append(f"{label}: unresolved source spans {sorted(missing_spans)}")
        errors.extend(validate_privacy(packet, label))
    if topic_assignments != packet_topic_ids:
        errors.append("topic coverage differs between source index and current evidence packets")

    checkpoint_register = bundle.get("checkpoint_register", {})
    if checkpoint_register.get("session_id") != session_id:
        errors.append("checkpoint_register: session ID differs")
    errors.extend(validate_privacy(checkpoint_register, "checkpoint_register"))
    checkpoint_ids: set[str] = set()
    for index, link in enumerate(checkpoint_register.get("links", [])):
        label = f"checkpoint_register.links[{index}]"
        checkpoint_ids.add(link.get("checkpoint_id"))
        if link.get("packet_id") not in packet_ids:
            errors.append(f"{label}: unresolved packet_id")
        if set(link.get("source_span_ids", [])) - span_ids:
            errors.append(f"{label}: unresolved source spans")
    if checkpoint_ids_from_packets != checkpoint_ids:
        errors.append("checkpoint coverage differs between packets and checkpoint register")

    signals = bundle.get("learning_signals", [])
    signal_ids: set[str] = set()
    for index, signal in enumerate(signals):
        label = f"learning_signals[{index}]"
        signal_id = signal.get("signal_id")
        if signal_id in signal_ids:
            errors.append(f"{label}: duplicate signal_id")
        signal_ids.add(signal_id)
        if signal.get("topic_id") not in packet_topic_ids:
            errors.append(f"{label}: unresolved topic_id")
        if set(signal.get("source_span_ids", [])) - span_ids:
            errors.append(f"{label}: unresolved source spans")
        errors.extend(validate_privacy(signal, label))
    if signal_ids_from_packets - signal_ids:
        errors.append(f"packets reference unresolved signals {sorted(signal_ids_from_packets - signal_ids)}")

    ledgers = bundle.get("candidate_ledgers", [])
    ledger_ids: set[str] = set()
    ledger_kinds: set[str] = set()
    for index, ledger in enumerate(ledgers):
        label = f"candidate_ledgers[{index}]"
        errors.extend(validate_ledger(ledger, label))
        if ledger.get("session_id") != session_id:
            errors.append(f"{label}: session ID differs")
        ledger_ids.add(ledger.get("ledger_id"))
        ledger_kinds.add(ledger.get("ledger_kind"))
        for candidate_index, candidate in enumerate(ledger.get("candidates", [])):
            if set(candidate.get("source_span_ids", [])) - span_ids:
                errors.append(f"{label}.candidates[{candidate_index}]: unresolved source spans")
            if set(candidate.get("signal_ids", [])) - signal_ids:
                errors.append(f"{label}.candidates[{candidate_index}]: unresolved signal IDs")
    if ledger_kinds != {"prediction", "rejected"}:
        errors.append("candidate_ledgers: exactly prediction and rejected ledgers are required")

    gates = bundle.get("gate_results", [])
    gate_ids = {gate.get("gate_id") for gate in gates}
    gate_result_ids = {gate.get("result_id") for gate in gates}
    if gate_ids != REQUIRED_RM_GATES:
        errors.append(f"gate_results: expected RM-0 through RM-7, received {sorted(gate_ids)}")
    for index, gate in enumerate(gates):
        if not gate.get("checks"):
            errors.append(f"gate_results[{index}]: checks cannot be empty")

    notebook = bundle.get("experimental_notebook_manifest", {})
    if notebook.get("session_id") != session_id:
        errors.append("experimental_notebook_manifest: session ID differs")
    if notebook.get("label") != EXPERIMENTAL_LABEL or notebook.get("anki_ready") is not False:
        errors.append("experimental_notebook_manifest: RM-EXPERIMENTAL-ANKI-BOUNDARY")
    if set(notebook.get("ledger_ids", [])) != ledger_ids:
        errors.append("experimental_notebook_manifest: ledger IDs do not match bundle ledgers")
    if set(notebook.get("gate_result_ids", [])) != gate_result_ids:
        errors.append("experimental_notebook_manifest: gate result IDs do not match bundle gates")
    errors.extend(validate_privacy(notebook, "experimental_notebook_manifest"))
    return errors


def validate_source_archive(archive: dict, expected_session_id: str | None = None) -> list[str]:
    errors: list[str] = []
    required = {"archive_id", "session_id", "segments", "completeness", "privacy"}
    missing = sorted(required - set(archive))
    if missing:
        return [f"source archive: missing {', '.join(missing)}"]
    if expected_session_id and archive.get("session_id") != expected_session_id:
        errors.append("source archive: session ID differs")
    errors.extend(validate_privacy(archive, "source archive"))

    segments = archive.get("segments")
    if not isinstance(segments, list) or not segments:
        return errors + ["source archive: segments must be a non-empty array"]
    segment_ids: set[str] = set()
    sequences: set[int] = set()
    message_ids: set[str] = set()
    authoritative_roles: set[str] = set()
    for segment_index, segment in enumerate(segments):
        label = f"source archive.segments[{segment_index}]"
        segment_id = segment.get("segment_id")
        sequence = segment.get("sequence")
        if not segment_id or segment_id in segment_ids:
            errors.append(f"{label}: missing or duplicate segment_id")
        segment_ids.add(segment_id)
        if not isinstance(sequence, int) or sequence < 1 or sequence in sequences:
            errors.append(f"{label}: sequence must be a unique positive integer")
        sequences.add(sequence)
        if segment.get("authoritative"):
            authoritative_roles.add(segment.get("role"))
            if segment.get("complete") is not True:
                errors.append(f"{label}: authoritative segment is incomplete")
        messages = segment.get("messages")
        if not isinstance(messages, list) or not messages:
            errors.append(f"{label}: messages must be a non-empty array")
            continue
        orders: set[int] = set()
        for message_index, message in enumerate(messages):
            prefix = f"{label}.messages[{message_index}]"
            message_id = message.get("message_id")
            order = message.get("order")
            if not message_id or message_id in message_ids:
                errors.append(f"{prefix}: missing or duplicate message_id")
            message_ids.add(message_id)
            if not isinstance(order, int) or order < 1 or order in orders:
                errors.append(f"{prefix}: order must be unique within the segment")
            orders.add(order)
            if message.get("speaker") not in {"learner", "assistant", "system-event"}:
                errors.append(f"{prefix}: unsupported speaker")
            if not isinstance(message.get("content"), str) or not message["content"]:
                errors.append(f"{prefix}: content is required")

    if not ({"night-diary", "night-continuation"} & authoritative_roles):
        errors.append("source archive: no authoritative night source segment")
    if "morning-review" not in authoritative_roles:
        errors.append("source archive: no authoritative morning-review segment")
    completeness = archive.get("completeness", {})
    checked = set(completeness.get("checked_segment_ids", []))
    if checked != segment_ids:
        errors.append("source archive: completeness coverage differs from segments")
    if completeness.get("status") == "complete" and completeness.get("missing_ranges"):
        errors.append("source archive: complete archive cannot declare missing ranges")
    if completeness.get("status") != "complete":
        errors.append("source archive: completeness status must be complete for gold handoff")
    return errors


def validate_fidelity_report(
    report: dict,
    *,
    session_id: str,
    archive_id: str,
    span_ids: set[str],
    gold_candidate_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    required = {
        "report_id", "session_id", "source_archive_id", "manual_notebook_id",
        "status", "checks", "conflict_ids", "reviewed_at", "privacy",
    }
    missing = sorted(required - set(report))
    if missing:
        return [f"source fidelity report: missing {', '.join(missing)}"]
    if report.get("session_id") != session_id:
        errors.append("source fidelity report: session ID differs")
    if report.get("source_archive_id") != archive_id:
        errors.append("source fidelity report: archive ID differs")
    if report.get("status") not in {"pass", "unresolved-conflicts-preserved"}:
        errors.append("source fidelity report: status is not eligible for gold handoff")
    errors.extend(validate_privacy(report, "source fidelity report"))
    checks = report.get("checks")
    if not isinstance(checks, list) or not checks:
        return errors + ["source fidelity report: checks must be a non-empty array"]
    check_ids: set[str] = set()
    reported_conflicts = set(report.get("conflict_ids", []))
    seen_conflicts: set[str] = set()
    for index, check in enumerate(checks):
        label = f"source fidelity report.checks[{index}]"
        check_id = check.get("check_id")
        if not check_id or check_id in check_ids:
            errors.append(f"{label}: missing or duplicate check_id")
        check_ids.add(check_id)
        unresolved_spans = set(check.get("source_span_ids", [])) - span_ids
        if unresolved_spans:
            errors.append(f"{label}: unresolved source spans {sorted(unresolved_spans)}")
        candidate_id = check.get("gold_candidate_id")
        if candidate_id and candidate_id not in gold_candidate_ids:
            errors.append(f"{label}: unresolved gold_candidate_id")
        if check.get("status") == "fail":
            errors.append(f"{label}: failed source-fidelity check")
        conflict_id = check.get("conflict_id")
        if check.get("status") == "unresolved" and not conflict_id:
            errors.append(f"{label}: unresolved check requires conflict_id")
        if conflict_id:
            seen_conflicts.add(conflict_id)
    if seen_conflicts != reported_conflicts:
        errors.append("source fidelity report: conflict IDs do not match unresolved checks")
    if report.get("status") == "pass" and reported_conflicts:
        errors.append("source fidelity report: pass cannot retain conflicts")
    return errors


def record_transition(session_root: Path, manifest: dict, target: str, operation: str) -> None:
    current = manifest.get("status")
    if target not in SESSION_STATES or target == "initialized":
        raise SystemExit(f"RM-STATE-TRANSITION-INVALID: invalid target state: {target}")
    if operation == "manual-transition" and target not in ALLOWED_TRANSITIONS.get(current, set()):
        raise SystemExit(f"RM-STATE-TRANSITION-INVALID: invalid state transition: {current} -> {target}")
    if current == target:
        return
    transitions_dir = session_root / manifest["artefacts"]["state_transitions"]
    sequence = len(list(transitions_dir.glob("*.json"))) + 1
    transition = {
        "transition_id": f"TRANS-{manifest['session_id']}-{sequence:03d}",
        "session_id": manifest["session_id"],
        "from": current,
        "to": target,
        "operation": operation,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "privacy": PRIVATE_CLASSIFICATION,
    }
    write_json(transitions_dir / f"{sequence:03d}.json", transition)
    manifest["status"] = target
    write_json(session_root / "session-manifest.json", manifest)


def transition_session(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    if args.to in {"gold-ready", "comparison-complete"}:
        raise SystemExit(
            "RM-STATE-TRANSITION-INVALID: gold-ready and comparison-complete "
            "are produced only by validated Codex workflow commands"
        )
    record_transition(session_root, manifest, args.to, "manual-transition")
    print(f"SESSION_STATE session={manifest['session_id']} status={manifest['status']}")


def import_bundle(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    bundle_path = Path(args.bundle).expanduser().resolve()
    bundle = load_json(bundle_path)
    require_private_input_path(bundle_path, bundle)
    errors = validate_bundle(bundle)
    if bundle.get("session_manifest", {}).get("session_id") != manifest.get("session_id"):
        errors.append("bundle session ID differs from destination session")
    if errors:
        raise SystemExit("RM-BUNDLE-CONTRACT-INVALID:\n- " + "\n- ".join(errors))

    directories = manifest["artefacts"]
    write_json(session_root / directories["pilot_bundles"] / "pilot-bundle.json", bundle)
    write_json(session_root / directories["source_archive"] / "source-span-index.json", bundle["source_span_index"])
    for index, packet in enumerate(bundle["topic_evidence_packets"], start=1):
        write_json(session_root / directories["topic_evidence_packets"] / f"packet-{index:03d}.json", packet)
    write_json(session_root / directories["checkpoints"] / "checkpoint-register.json", bundle["checkpoint_register"])
    for index, signal in enumerate(bundle["learning_signals"], start=1):
        write_json(session_root / directories["learning_signals"] / f"signal-{index:03d}.json", signal)
    for ledger in bundle["candidate_ledgers"]:
        write_json(session_root / directories["candidate_ledgers"] / f"{ledger['ledger_kind']}-ledger.json", ledger)
    write_json(session_root / "experimental-notebook-manifest.json", bundle["experimental_notebook_manifest"])
    write_json(session_root / "rm-gate-results.json", {"results": bundle["gate_results"]})

    gate_statuses = {gate.get("status") for gate in bundle["gate_results"]}
    target = "candidate-generated" if gate_statuses == {"pass"} else "blocked"
    record_transition(session_root, manifest, target, "bundle-import-sync")
    print(f"PILOT_BUNDLE_IMPORTED session={manifest['session_id']} status={manifest['status']}")


def import_source_archive(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    archive_path = Path(args.archive).expanduser().resolve()
    archive = load_json(archive_path)
    require_private_input_path(archive_path, archive)
    errors = validate_source_archive(archive, manifest.get("session_id"))
    if manifest.get("status") not in {"candidate-generated", "gold-ready"}:
        errors.append("source archive: session must have a frozen candidate before handoff")
    if errors:
        raise SystemExit("RM-SOURCE-ARCHIVE-INVALID:\n- " + "\n- ".join(errors))
    destination = session_root / manifest["artefacts"]["source_archive"] / "conversation-source-archive.json"
    write_json(destination, archive)
    print(
        f"SOURCE_ARCHIVE_IMPORTED session={manifest['session_id']} "
        f"segments={len(archive['segments'])} status={archive['completeness']['status']}"
    )


def validate_manual_gold(
    ledger: dict,
    *,
    session_id: str,
    span_ids: set[str],
    signal_ids: set[str],
    topic_ids: set[str],
) -> list[str]:
    errors = validate_ledger(ledger, "manual-gold ledger")
    if ledger.get("session_id") != session_id:
        errors.append("manual-gold ledger: session ID differs")
    if ledger.get("ledger_kind") != "manual-gold":
        errors.append("manual-gold ledger: ledger_kind must be manual-gold")
    for index, candidate in enumerate(ledger.get("candidates", [])):
        label = f"manual-gold ledger.candidates[{index}]"
        if candidate.get("decision") != "selected":
            errors.append(f"{label}: approved gold candidate must be selected")
        if candidate.get("confidence") != "manual":
            errors.append(f"{label}: approved gold candidate confidence must be manual")
        if candidate.get("semantic_fidelity") != "pass":
            errors.append(f"{label}: semantic_fidelity must be pass")
        unresolved = set(candidate.get("source_span_ids", [])) - span_ids
        if unresolved:
            errors.append(f"{label}: unresolved source spans {sorted(unresolved)}")
        unresolved_signals = set(candidate.get("signal_ids", [])) - signal_ids
        if unresolved_signals:
            errors.append(f"{label}: unresolved signal IDs {sorted(unresolved_signals)}")
        if candidate.get("topic_id") not in topic_ids:
            errors.append(f"{label}: unresolved topic_id")
    return errors


def import_gold(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    errors: list[str] = []
    if manifest.get("status") != "candidate-generated":
        errors.append("gold handoff: session status must be candidate-generated")

    bundle_path = session_root / manifest["artefacts"]["pilot_bundles"] / "pilot-bundle.json"
    archive_path = session_root / manifest["artefacts"]["source_archive"] / "conversation-source-archive.json"
    if not bundle_path.is_file():
        errors.append("gold handoff: frozen Pilot Bundle is missing")
    if not archive_path.is_file():
        errors.append("gold handoff: complete private source archive is missing")
    if errors:
        raise SystemExit("RM-GOLD-HANDOFF-INVALID:\n- " + "\n- ".join(errors))

    bundle = load_json(bundle_path)
    archive = load_json(archive_path)
    errors.extend(validate_source_archive(archive, manifest.get("session_id")))
    span_ids = {item["span_id"] for item in bundle["source_span_index"]["spans"]}
    signal_ids = {item["signal_id"] for item in bundle["learning_signals"]}
    topic_ids = {item["topic_id"] for item in bundle["topic_evidence_packets"]}

    gold_path = Path(args.gold).expanduser().resolve()
    fidelity_path = Path(args.fidelity_report).expanduser().resolve()
    gold = load_json(gold_path)
    fidelity = load_json(fidelity_path)
    require_private_input_path(gold_path, gold)
    require_private_input_path(fidelity_path, fidelity)
    errors.extend(
        validate_manual_gold(
            gold,
            session_id=manifest["session_id"],
            span_ids=span_ids,
            signal_ids=signal_ids,
            topic_ids=topic_ids,
        )
    )
    gold_candidate_ids = {item.get("candidate_id") for item in gold.get("candidates", [])}
    errors.extend(
        validate_fidelity_report(
            fidelity,
            session_id=manifest["session_id"],
            archive_id=archive["archive_id"],
            span_ids=span_ids,
            gold_candidate_ids=gold_candidate_ids,
        )
    )
    if errors:
        raise SystemExit("RM-GOLD-HANDOFF-INVALID:\n- " + "\n- ".join(errors))

    ledgers_dir = session_root / manifest["artefacts"]["candidate_ledgers"]
    comparisons_dir = session_root / manifest["artefacts"]["comparison_reports"]
    write_json(ledgers_dir / "manual-gold-ledger.json", gold)
    write_json(comparisons_dir / "source-fidelity-report.json", fidelity)
    record_transition(session_root, manifest, "gold-ready", "codex-gold-handoff")
    print(
        f"MANUAL_GOLD_IMPORTED session={manifest['session_id']} "
        f"candidates={len(gold['candidates'])} status={manifest['status']}"
    )


def validate_session(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    errors = []
    if manifest.get("mode") != "phase-2-shadow":
        errors.append("manifest mode must be phase-2-shadow")
    if manifest.get("protocol", {}).get("stable") != "3.5":
        errors.append("stable protocol must be 3.5")
    errors.extend(validate_privacy(manifest, "manifest"))
    expected_directories = set(artefact_directories())
    if set(manifest.get("artefacts", {})) != expected_directories:
        errors.append("manifest artefact directory contract is incomplete")
    for relative in manifest.get("artefacts", {}).values():
        if not (session_root / relative).is_dir():
            errors.append(f"missing artefact directory: {relative}")

    for ledger_path in sorted((session_root / "ledgers").glob("*.json")):
        errors.extend(validate_ledger(load_json(ledger_path), ledger_path.name))
    for notebook_path in sorted(session_root.glob("experimental-notebook-manifest*.json")):
        notebook = load_json(notebook_path)
        if notebook.get("label") != EXPERIMENTAL_LABEL or notebook.get("anki_ready") is not False:
            errors.append(f"{notebook_path.name}: RM-EXPERIMENTAL-ANKI-BOUNDARY")
    bundle_path = session_root / manifest.get("artefacts", {}).get("pilot_bundles", "bundles") / "pilot-bundle.json"
    bundle = None
    if bundle_path.is_file():
        bundle = load_json(bundle_path)
        errors.extend(validate_bundle(bundle))

    source_archive_path = session_root / manifest.get("artefacts", {}).get("source_archive", "source") / "conversation-source-archive.json"
    source_archive = None
    if source_archive_path.is_file():
        source_archive = load_json(source_archive_path)
        errors.extend(validate_source_archive(source_archive, manifest.get("session_id")))

    ledgers_dir = session_root / manifest.get("artefacts", {}).get("candidate_ledgers", "ledgers")
    gold_path = ledgers_dir / "manual-gold-ledger.json"
    fidelity_path = session_root / manifest.get("artefacts", {}).get("comparison_reports", "comparisons") / "source-fidelity-report.json"
    if gold_path.is_file() != fidelity_path.is_file():
        errors.append("gold handoff requires both manual-gold ledger and source-fidelity report")
    if gold_path.is_file() and fidelity_path.is_file() and bundle and source_archive:
        gold = load_json(gold_path)
        fidelity = load_json(fidelity_path)
        span_ids = {item["span_id"] for item in bundle["source_span_index"]["spans"]}
        signal_ids = {item["signal_id"] for item in bundle["learning_signals"]}
        topic_ids = {item["topic_id"] for item in bundle["topic_evidence_packets"]}
        errors.extend(
            validate_manual_gold(
                gold,
                session_id=manifest["session_id"],
                span_ids=span_ids,
                signal_ids=signal_ids,
                topic_ids=topic_ids,
            )
        )
        errors.extend(
            validate_fidelity_report(
                fidelity,
                session_id=manifest["session_id"],
                archive_id=source_archive["archive_id"],
                span_ids=span_ids,
                gold_candidate_ids={item.get("candidate_id") for item in gold.get("candidates", [])},
            )
        )

    if manifest.get("status") in {"gold-ready", "comparison-complete"}:
        if not source_archive_path.is_file():
            errors.append("gold-ready session is missing the private source archive")
        if not gold_path.is_file() or not fidelity_path.is_file():
            errors.append("gold-ready session is missing validated gold handoff artefacts")
    if manifest.get("status") == "comparison-complete":
        comparisons_dir = session_root / manifest["artefacts"]["comparison_reports"]
        calibration_dir = session_root / manifest["artefacts"]["calibration_reports"]
        for required_path in (
            comparisons_dir / "gold-comparison.json",
            comparisons_dir / "rm-8-result.json",
            calibration_dir / "calibration-report.json",
            calibration_dir / "rm-9-result.json",
        ):
            if not required_path.is_file():
                errors.append(f"comparison-complete session is missing {required_path.name}")

    if errors:
        print("SESSION_VALIDATION_FAIL")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print(f"SESSION_VALIDATION_PASS session={manifest.get('session_id')} status={manifest.get('status')}")


def status(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    directories = manifest.get("artefacts", {})
    bundle_path = session_root / directories.get("pilot_bundles", "bundles") / "pilot-bundle.json"
    bundle = load_json(bundle_path) if bundle_path.is_file() else None
    source_archive_path = session_root / directories.get("source_archive", "source") / "conversation-source-archive.json"
    gold_path = session_root / directories.get("candidate_ledgers", "ledgers") / "manual-gold-ledger.json"
    comparisons_dir = session_root / directories.get("comparison_reports", "comparisons")
    calibration_dir = session_root / directories.get("calibration_reports", "calibration")
    summary = {
        "session_id": manifest.get("session_id"),
        "status": manifest.get("status"),
        "bundle_imported": bundle is not None,
        "source_archive_imported": source_archive_path.is_file(),
        "manual_gold_imported": gold_path.is_file(),
        "rm8_complete": (comparisons_dir / "rm-8-result.json").is_file(),
        "rm9_complete": (calibration_dir / "rm-9-result.json").is_file(),
        "counts": {
            "source_spans": len(bundle.get("source_span_index", {}).get("spans", [])) if bundle else 0,
            "topics": len(bundle.get("topic_evidence_packets", [])) if bundle else 0,
            "checkpoints": len(bundle.get("checkpoint_register", {}).get("links", [])) if bundle else 0,
            "learning_signals": len(bundle.get("learning_signals", [])) if bundle else 0,
            "prediction_candidates": next((len(item["candidates"]) for item in bundle.get("candidate_ledgers", []) if item.get("ledger_kind") == "prediction"), 0) if bundle else 0,
            "rejected_candidates": next((len(item["candidates"]) for item in bundle.get("candidate_ledgers", []) if item.get("ledger_kind") == "rejected"), 0) if bundle else 0,
            "rm_gates": len(bundle.get("gate_results", [])) if bundle else 0,
        },
        "anki_ready": bundle.get("experimental_notebook_manifest", {}).get("anki_ready") if bundle else False,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return
    print(f"SESSION_STATUS session={summary['session_id']} status={summary['status']}")
    for name, count in summary["counts"].items():
        print(f"{name}={count}")
    print(f"anki_ready={str(summary['anki_ready']).lower()}")


def selected_by_key(ledger: dict) -> dict[str, dict]:
    return {
        item["target_key"]: item
        for item in ledger["candidates"]
        if item["decision"] in {"selected", "suggested-for-review"}
    }


def build_comparison(prediction: dict, gold: dict, comparison_id: str) -> dict:
    predicted = selected_by_key(prediction)
    approved = selected_by_key(gold)
    outcomes = []
    for key in sorted(predicted.keys() | approved.keys()):
        p = predicted.get(key)
        g = approved.get(key)
        if p and not g:
            outcome, codes = "false-positive", ["RM-TARGET-FALSE-POSITIVE"]
        elif g and not p:
            outcome, codes = "false-negative", ["RM-TARGET-FALSE-NEGATIVE"]
        elif p["learning_function"] != g["learning_function"]:
            outcome, codes = "wrong-function", ["RM-WRONG-FUNCTION"]
        elif p["note_type"] != g["note_type"]:
            outcome, codes = "wrong-note-type", ["RM-WRONG-NOTE-TYPE"]
        elif p.get("boundary_key") != g.get("boundary_key"):
            outcome, codes = "partial-target", ["RM-TARGET-PARTIAL"]
        elif p.get("semantic_fidelity") == "fail":
            outcome, codes = "semantic-drift", ["RM-SEMANTIC-DRIFT"]
        else:
            outcome, codes = "true-positive", []
        record = {"target_key": key, "outcome": outcome, "error_codes": codes}
        if p:
            record["prediction_candidate_id"] = p["candidate_id"]
        if g:
            record["gold_candidate_id"] = g["candidate_id"]
        outcomes.append(record)

    tp = sum(item["outcome"] == "true-positive" for item in outcomes)
    fp = sum(item["outcome"] == "false-positive" for item in outcomes)
    fn = sum(item["outcome"] == "false-negative" for item in outcomes)
    return {
        "comparison_id": comparison_id,
        "session_id": prediction["session_id"],
        "prediction_ledger_id": prediction["ledger_id"],
        "gold_ledger_id": gold["ledger_id"],
        "outcomes": outcomes,
        "metrics": {
            "true_positive": tp,
            "false_positive": fp,
            "false_negative": fn,
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None,
        },
        "privacy": PRIVATE_CLASSIFICATION,
    }


def compare(args: argparse.Namespace) -> None:
    prediction_path = Path(args.prediction).expanduser().resolve()
    gold_path = Path(args.gold).expanduser().resolve()
    output_path = require_external_root(Path(args.output).expanduser().resolve().parent) / Path(args.output).name
    prediction = load_json(prediction_path)
    gold = load_json(gold_path)
    require_private_input_path(prediction_path, prediction)
    require_private_input_path(gold_path, gold)
    errors = validate_ledger(prediction, "prediction") + validate_ledger(gold, "gold")
    if prediction.get("ledger_kind") != "prediction":
        errors.append("prediction ledger_kind must be prediction")
    if gold.get("ledger_kind") != "manual-gold":
        errors.append("gold ledger_kind must be manual-gold")
    if prediction.get("session_id") != gold.get("session_id"):
        errors.append("prediction and gold session IDs differ")
    if errors:
        raise SystemExit("comparison input invalid:\n- " + "\n- ".join(errors))
    result = build_comparison(prediction, gold, args.comparison_id)
    write_json(output_path, result)
    if args.session_root:
        session_root = require_external_root(Path(args.session_root))
        manifest = load_json(session_root / "session-manifest.json")
        if manifest.get("session_id") != prediction["session_id"]:
            raise SystemExit("comparison session differs from destination session")
        if manifest.get("status") != "gold-ready":
            raise SystemExit("comparison requires a Codex-validated gold-ready session")
    print(output_path)


def compare_session(args: argparse.Namespace) -> None:
    session_root = require_external_root(Path(args.session_root))
    manifest = load_json(session_root / "session-manifest.json")
    if manifest.get("status") != "gold-ready":
        raise SystemExit("RM-8-BLOCKED: session must be gold-ready")
    ledgers_dir = session_root / manifest["artefacts"]["candidate_ledgers"]
    source_archive_path = session_root / manifest["artefacts"]["source_archive"] / "conversation-source-archive.json"
    fidelity_path = session_root / manifest["artefacts"]["comparison_reports"] / "source-fidelity-report.json"
    prediction_path = ledgers_dir / "prediction-ledger.json"
    gold_path = ledgers_dir / "manual-gold-ledger.json"
    required_paths = (source_archive_path, fidelity_path, prediction_path, gold_path)
    missing = [path.name for path in required_paths if not path.is_file()]
    if missing:
        raise SystemExit(f"RM-8-BLOCKED: missing {', '.join(missing)}")
    prediction = load_json(prediction_path)
    gold = load_json(gold_path)
    errors = validate_ledger(prediction, "prediction") + validate_ledger(gold, "gold")
    if errors:
        raise SystemExit("RM-8-BLOCKED:\n- " + "\n- ".join(errors))
    result = build_comparison(prediction, gold, args.comparison_id)
    comparisons_dir = session_root / manifest["artefacts"]["comparison_reports"]
    comparison_path = comparisons_dir / "gold-comparison.json"
    write_json(comparison_path, result)
    gate_result = {
        "result_id": f"RESULT-{manifest['session_id']}-RM-8",
        "gate_id": "RM-8",
        "subject_ids": [manifest["session_id"], result["comparison_id"]],
        "status": "pass",
        "checks": [{
            "requirement_id": "EOD-RM-800",
            "status": "pass",
            "evidence_reference": result["comparison_id"],
        }],
        "invalidates_result_ids": [],
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }
    write_json(comparisons_dir / "rm-8-result.json", gate_result)
    print(f"RM8_COMPARISON_COMPLETE session={manifest['session_id']} output={comparison_path}")


def calibration_report(args: argparse.Namespace) -> None:
    comparison_path = Path(args.comparison).expanduser().resolve()
    comparison = load_json(comparison_path)
    require_private_input_path(comparison_path, comparison)
    output_path = require_external_root(Path(args.output).expanduser().resolve().parent) / Path(args.output).name
    counts = Counter(item.get("outcome") for item in comparison.get("outcomes", []))
    blockers = sorted({code for item in comparison.get("outcomes", []) for code in item.get("error_codes", [])})
    report = {
        "report_id": args.report_id,
        "session_id": comparison.get("session_id"),
        "comparison_id": comparison.get("comparison_id"),
        "difference_counts": dict(sorted(counts.items())),
        "proposed_delta_ids": [],
        "next_cycle_required": True,
        "promotion_blockers": blockers or ["PILOT-COUNT-INSUFFICIENT"],
        "privacy": PRIVATE_CLASSIFICATION,
    }
    write_json(output_path, report)
    if args.session_root:
        session_root = require_external_root(Path(args.session_root))
        manifest = load_json(session_root / "session-manifest.json")
        if manifest.get("status") != "gold-ready":
            raise SystemExit("RM-9-BLOCKED: session must be gold-ready")
        if manifest.get("session_id") != comparison.get("session_id"):
            raise SystemExit("RM-9-BLOCKED: comparison session differs")
        comparisons_dir = session_root / manifest["artefacts"]["comparison_reports"]
        if not (comparisons_dir / "rm-8-result.json").is_file():
            raise SystemExit("RM-9-BLOCKED: RM-8 result is missing")
        calibration_dir = session_root / manifest["artefacts"]["calibration_reports"]
        write_json(calibration_dir / "calibration-report.json", report)
        gate_result = {
            "result_id": f"RESULT-{manifest['session_id']}-RM-9",
            "gate_id": "RM-9",
            "subject_ids": [manifest["session_id"], report["report_id"]],
            "status": "pass",
            "checks": [{
                "requirement_id": "EOD-RM-900",
                "status": "pass",
                "evidence_reference": report["report_id"],
            }],
            "invalidates_result_ids": [],
            "evaluated_at": datetime.now(timezone.utc).isoformat(),
        }
        write_json(calibration_dir / "rm-9-result.json", gate_result)
        record_transition(session_root, manifest, "comparison-complete", "codex-calibration-complete")
    print(output_path)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="English Oral Diary Phase 2 structural tooling")
    commands = root.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init-session")
    init.add_argument("--private-root", required=True)
    init.add_argument("--session-id")
    init.set_defaults(handler=init_session)

    validate = commands.add_parser("validate-session")
    validate.add_argument("--session-root", required=True)
    validate.set_defaults(handler=validate_session)

    import_command = commands.add_parser("import-bundle")
    import_command.add_argument("--bundle", required=True)
    import_command.add_argument("--session-root", required=True)
    import_command.set_defaults(handler=import_bundle)

    source_archive = commands.add_parser("import-source-archive")
    source_archive.add_argument("--archive", required=True)
    source_archive.add_argument("--session-root", required=True)
    source_archive.set_defaults(handler=import_source_archive)

    gold_import = commands.add_parser("import-gold")
    gold_import.add_argument("--gold", required=True)
    gold_import.add_argument("--fidelity-report", required=True)
    gold_import.add_argument("--session-root", required=True)
    gold_import.set_defaults(handler=import_gold)

    status_command = commands.add_parser("status")
    status_command.add_argument("--session-root", required=True)
    status_command.add_argument("--json", action="store_true")
    status_command.set_defaults(handler=status)

    transition = commands.add_parser("transition")
    transition.add_argument("--session-root", required=True)
    transition.add_argument("--to", required=True, choices=sorted(SESSION_STATES - {"initialized"}))
    transition.set_defaults(handler=transition_session)

    comparison = commands.add_parser("compare")
    comparison.add_argument("--prediction", required=True)
    comparison.add_argument("--gold", required=True)
    comparison.add_argument("--output", required=True)
    comparison.add_argument("--comparison-id", default="CMP-SYN-001")
    comparison.add_argument("--session-root")
    comparison.set_defaults(handler=compare)

    session_comparison = commands.add_parser("compare-session")
    session_comparison.add_argument("--session-root", required=True)
    session_comparison.add_argument("--comparison-id", required=True)
    session_comparison.set_defaults(handler=compare_session)

    calibration = commands.add_parser("calibration-report")
    calibration.add_argument("--comparison", required=True)
    calibration.add_argument("--output", required=True)
    calibration.add_argument("--report-id", default="CAL-SYN-001")
    calibration.add_argument("--session-root")
    calibration.set_defaults(handler=calibration_report)
    return root


def main() -> None:
    args = parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
