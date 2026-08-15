"""Identity commitments: prove a contributor ID is yours without trusting anyone.

When a contributor ID is assigned, a random salt is generated and
SHA-256("<identity>:<salt>") is recorded in that ID's `commitment` field in
CONTRIBUTORS.csv - publicly, pinned by the append-only git history. `<identity>`
is a stable platform identity string:

    discord:<numeric user id>     (Discord snowflake - handles change, this doesn't)
    github:<numeric user id>      (GitHub account id - usernames change, this doesn't)

A contributor may hold several commitments (space-separated in the column), one
per platform identity. The salt goes to the contributor (assignment DM) and to
the maintainers' private registry. A commitment reveals nothing by itself (the
salt blocks brute-forcing enumerable platform IDs), but revealing your identity
string + salt lets ANYONE recompute the hash and verify your claim against what
git history pinned on assignment day. No maintainer, registry, or platform needs
to survive for the proof to work.

Usage:
  python identity.py new github:118310809
      -> prints a fresh salt and the commitment to record

  python identity.py verify T-83DE github:118310809 <salt>
      -> checks the claim against CONTRIBUTORS.csv
"""

import csv
import hashlib
import secrets
import sys
from pathlib import Path

CONTRIBUTORS = Path(__file__).parent / "CONTRIBUTORS.csv"


def commitment(identity: str, salt: str) -> str:
    return hashlib.sha256(f"{identity}:{salt}".encode()).hexdigest()


def cmd_new(identity: str) -> None:
    if ":" not in identity:
        sys.exit("identity must be '<platform>:<numeric id>', e.g. discord:123... or github:123...")
    salt = secrets.token_hex(16)
    print(f"identity:   {identity}")
    print(f"salt:       {salt}")
    print(f"commitment: {commitment(identity, salt)}")
    print("Record the commitment in CONTRIBUTORS.csv (space-separated if the")
    print("contributor already has one); give the salt to the contributor and")
    print("store it in the private registry.")


def cmd_verify(cid: str, identity: str, salt: str) -> None:
    with CONTRIBUTORS.open(newline="", encoding="utf-8-sig") as f:
        rows = {r["id"].strip(): r for r in csv.DictReader(f)}
    row = rows.get(cid)
    if row is None:
        sys.exit(f"FAIL: no contributor {cid} in CONTRIBUTORS.csv")
    recorded = (row.get("commitment") or "").split()
    if not recorded:
        sys.exit(f"FAIL: {cid} has no commitment recorded")
    if commitment(identity, salt) in recorded:
        print(f"OK: the claim checks out - {cid} was assigned to {identity.split(':')[0]} identity {identity}.")
    else:
        sys.exit(f"FAIL: commitment mismatch - this claim does not match {cid}.")


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "new":
        cmd_new(args[1])
    elif len(args) == 4 and args[0] == "verify":
        cmd_verify(args[1], args[2], args[3])
    else:
        print(__doc__.strip())


if __name__ == "__main__":
    main()
