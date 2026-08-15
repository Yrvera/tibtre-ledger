# tibtre-ledger

Home of **tibtre**, the contribution currency of the Yrvera cooperative. This repository holds the policy, the append-only ledger, the generated balances, and the tooling that makes every number in the system independently verifiable.

## Why tibtre exists

Yrvera is built by its contributors, and the founding idea is that it should *belong* to them. Tibtre is how that idea is made concrete before it matters:

- **Preemptive fairness.** If Yrvera ever forms a legal entity or ever has income to distribute, the hard question — *who built this, and how much?* — is already answered: publicly, verifiably, from day one. This ledger is the stated basis for any such allocation.
- **A real say, today.** Decisions about Yrvera's direction are weighted by tibtre — capped so no single holder can ever dominate ([`voteweight.py`](voteweight.py)).
- **A permanent record.** Contributions are valued by public rules ([the rubric](docs/grading-rubric.md)), recorded forever, and verifiable by anyone — including by the contributor themselves, without trusting anyone ([`identity.py`](identity.py)).

One tibtre ≈ one hour of high-quality work on something Yrvera genuinely needs — quality and value both count, and both are priced by the public rules. Nothing to apply for: contribute, get valued, get recorded.

## Map

| File / folder | What it is |
|---|---|
| `RULES.md` | The policy: what tibtre is, how it's earned, what it's worth |
| `LEDGER.csv` | Append-only grant ledger, keyed by contributor ID — the single source of truth |
| `CONTRIBUTORS.csv` | ID → public display name (optional, changeable; empty = pseudonymous) |
| `BALANCES.md` | Generated balances table — run `python tally.py` after editing the ledger |
| `tally.py` | Regenerates `BALANCES.md` from `LEDGER.csv` |
| `voteweight.py` | Computes counted poll weights under the 25% per-person cap (`--demo` for examples) |
| `identity.py` | Generates/verifies the public identity commitments — prove an ID is yours without trusting anyone |
| `docs/granting-guide.md` | Step-by-step guide for approvers recording a grant |
| `assets/` | Archive of accepted community artwork and other non-code artifacts |

## Conventions

- The ledger is **append-only**: never edit or delete past rows. Corrections get a new row (negative amounts are allowed, with a note explaining why).
- The ledger contains **contributor IDs only** (random, like `T-83DE`), never names. Display names live in `CONTRIBUTORS.csv` and may be edited or emptied at any time without touching history.
- The ID → real person mapping lives in the **separate private folder** (`../vera20k-tibtre-private/`), which must never be published.
- Every change is committed to git — the commit history *is* the audit trail.
- All future tibtre-related documentation goes in `docs/`.
- Accepted artwork goes in `assets/`, named `YYYY-MM-DD_T-XXXX_short-title.ext` (ID, never name — filenames are public and permanent).

