"""Compute counted voting weights for a tibtre-weighted poll.

Implements the governance rule in RULES.md: votes are weighted by tibtre
balance, but no single person's ballot counts for more than 25% of the final
tally. Because that cap is self-referential (capping one voter shrinks the
tally, which shrinks the cap), the exact rule is:

- 4 or fewer voters: the cap forces equality -> one person, one vote.
- More than 4 voters: a common ceiling C is found (water-filling) such that
  each counted weight is min(balance, C) and nobody exceeds 25% of the
  counted total. At most 3 voters can sit at the cap simultaneously.

Voters with zero tibtre carry no weight. Holding is never capped - only how
much a ballot counts.

Usage:
  python voteweight.py T-83DE T-3BF2 T-9C41            # weights for these voters
  python voteweight.py T-83DE:yes T-3BF2:no            # ...and per-choice totals
  python voteweight.py --demo                          # worked examples
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).parent
LEDGER = HERE / "LEDGER.csv"
CAP = 0.25


def load_balances() -> dict[str, float]:
    balances: dict[str, float] = {}
    with LEDGER.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = row["id"].strip()
            if cid:
                balances[cid] = balances.get(cid, 0) + float(row["tibtre"])
    return balances


def counted_weights(balances: dict[str, float], cap: float = CAP) -> dict[str, float]:
    """Return each voter's counted weight under the per-person cap.

    `balances` holds only the voters who actually cast a ballot.
    """
    voters = {k: v for k, v in balances.items() if v > 0}
    if not voters:
        return {}
    max_equal = int(1 / cap)  # 4 voters at cap 25%
    if len(voters) <= max_equal:
        return {k: 1.0 for k in voters}  # degenerate case: equal weights

    ordered = sorted(voters.values(), reverse=True)
    ceiling = None
    # Try clamping the top k voters (k can be at most 3 at cap 25%: four
    # voters at exactly 25% would already be 100% of the tally).
    for k in range(0, max_equal):
        rest = sum(ordered[k:])
        c = cap * rest / (1 - cap * k)
        top_ok = k == 0 or ordered[k - 1] >= c
        rest_ok = ordered[k] <= c
        if top_ok and rest_ok:
            ceiling = c
            break
    if ceiling is None:  # unreachable with valid input; guard anyway
        ceiling = cap * sum(ordered)
    return {k: min(v, ceiling) for k, v in voters.items()}


def report(votes: dict[str, str | None], balances: dict[str, float]) -> str:
    missing = [v for v in votes if balances.get(v, 0) <= 0]
    weights = counted_weights({v: balances.get(v, 0) for v in votes})
    total = sum(weights.values())
    lines = []
    equal_mode = 0 < len(weights) <= int(1 / CAP)
    if equal_mode:
        lines.append(f"{len(weights)} eligible voter(s) -> equal weights (cap forces one-person-one-vote at <=4 voters)")
    lines.append(f"{'voter':<8} {'balance':>8} {'counted':>9} {'share':>7}")
    for v in sorted(weights, key=lambda x: -weights[x]):
        share = weights[v] / total * 100
        capped = "  (capped)" if not equal_mode and weights[v] < balances[v] else ""
        lines.append(f"{v:<8} {balances[v]:>8g} {weights[v]:>9.2f} {share:>6.1f}%{capped}")
    for v in missing:
        lines.append(f"{v:<8} {'0':>8} {'-':>9} {'-':>7}  (no tibtre: no weight)")
    if any(c for c in votes.values()):
        lines.append("")
        choice_totals: dict[str, float] = {}
        for v, choice in votes.items():
            if choice and v in weights:
                choice_totals[choice] = choice_totals.get(choice, 0) + weights[v]
        for choice, w in sorted(choice_totals.items(), key=lambda kv: -kv[1]):
            lines.append(f"  {choice}: {w:.2f} ({w / total * 100:.1f}%)")
    return "\n".join(lines)


def demo() -> None:
    cases = [
        ("Two voters, one whale - equal (cap degenerate below 5 voters)",
         {"T-A001": 500, "T-A002": 10}),
        ("Five equal voters - nobody near the cap",
         {f"T-A00{i}": 10 for i in range(1, 6)}),
        ("Whale among five - whale clamped to exactly 25% of tally",
         {"T-A001": 1000, "T-A002": 10, "T-A003": 10, "T-A004": 10, "T-A005": 10, "T-A006": 10}),
        ("Three whales among six - multiple voters at the cap",
         {"T-A001": 900, "T-A002": 800, "T-A003": 700, "T-A004": 20, "T-A005": 15, "T-A006": 10}),
    ]
    for title, balances in cases:
        print(f"--- {title}")
        print(report({v: None for v in balances}, balances))
        print()


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        return
    if args[0] == "--demo":
        demo()
        return
    votes: dict[str, str | None] = {}
    for a in args:
        cid, _, choice = a.partition(":")
        votes[cid.strip()] = choice.strip() or None
    print(report(votes, load_balances()))


if __name__ == "__main__":
    main()
