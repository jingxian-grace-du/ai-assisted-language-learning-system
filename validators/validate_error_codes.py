#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"^RM-[A-Z0-9]+(?:-[A-Z0-9]+)+$")


def fail(message: str) -> None:
    raise SystemExit(f"ERROR_CODE_FAIL: {message}")


def main() -> None:
    path = ROOT / "protocol/experimental/error-codes.json"
    catalogue = json.loads(path.read_text(encoding="utf-8"))
    codes = catalogue.get("codes")
    if not isinstance(codes, list) or not codes:
        fail("empty catalogue")
    values = [item.get("code") for item in codes]
    if len(values) != len(set(values)):
        fail("duplicate codes")
    for item in codes:
        if not PATTERN.fullmatch(str(item.get("code", ""))):
            fail(f"invalid code: {item.get('code')!r}")
        if item.get("severity") not in {"block", "review", "calibrate"}:
            fail(f"invalid severity for {item['code']}")
        if not str(item.get("stage", "")).startswith("RM-"):
            fail(f"invalid stage for {item['code']}")
        if not str(item.get("meaning", "")).strip():
            fail(f"missing meaning for {item['code']}")
    print(f"ERROR_CODE_PASS count={len(values)}")


if __name__ == "__main__":
    main()
