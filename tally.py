"""Regenerate BALANCES.md from LEDGER.csv + CONTRIBUTORS.csv.

The ledger is keyed by contributor ID (random, like T-83DE). Display names live
in CONTRIBUTORS.csv and are optional - an ID with no display name is shown as
the ID itself (pseudonymous contributor). If a contact URL is set, the display
name renders as a link.

Usage: python tally.py
"""

import csv
from pathlib import Path

HERE = Path(__file__).parent
LEDGER = HERE / "LEDGER.csv"
CONTRIBUTORS = HERE / "CONTRIBUTORS.csv"
BALANCES = HERE / "BALANCES.md"


def fmt(amount: float) -> str:
    return f"{amount:g}"


def load_contributors() -> dict[str, dict[str, str]]:
    info: dict[str, dict[str, str]] = {}
    with CONTRIBUTORS.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = row["id"].strip()
            if cid:
                info[cid] = {
                    "name": row["display_name"].strip(),
                    "contact": (row.get("contact") or "").strip(),
                }
    return info


def main() -> None:
    info = load_contributors()
    balances: dict[str, float] = {}
    grants = 0
    with LEDGER.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = row["id"].strip()
            if not cid:
                continue
            balances[cid] = balances.get(cid, 0) + float(row["tibtre"])
            grants += 1

    def shown(cid: str) -> str:
        entry = info.get(cid, {})
        name = entry.get("name") or cid
        contact = entry.get("contact", "")
        if contact.startswith("http"):
            return f"[{name}]({contact})"
        if contact:
            return f"{name} ({contact})"
        return name

    ranked = sorted(balances.items(), key=lambda kv: (-kv[1], shown(kv[0]).lower()))

    lines = [
        "# Tibtre balances",
        "",
        f"Generated from [`LEDGER.csv`](LEDGER.csv) - {grants} grant(s), "
        f"{fmt(sum(balances.values()))} tibtre in circulation. "
        "Do not edit by hand; run `python tally.py`.",
        "",
        "| # | Contributor | Tibtre |",
        "|---|---|---|",
    ]
    if ranked:
        for i, (cid, balance) in enumerate(ranked, start=1):
            lines.append(f"| {i} | {shown(cid)} | {fmt(balance)} |")
    else:
        lines.append("| - | *no grants yet* | 0 |")
    lines.append("")

    BALANCES.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {BALANCES.name}: {len(ranked)} contributor(s), {grants} grant(s).")


if __name__ == "__main__":
    main()
