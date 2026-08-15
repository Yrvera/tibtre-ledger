# Tibtre — the Yrvera contribution currency

Yrvera is built by its contributors, and tibtre is how the project remembers who built it.

## What is one tibtre?

**1 tibtre ≈ 1 focused hour of high-quality work on something the project genuinely needs.**

Tibtre is granted for *accepted results*, not for time spent. When a contribution is accepted, the reviewer estimates how many hours of quality work it represents and grants that many tibtre. You never report your own hours.

## What is tibtre worth?

Today, two things:

1. **Recognition.** Your balance is public in [`BALANCES.md`](BALANCES.md), and your name goes in the project credits.
2. **Governance.** Roadmap polls and feature votes in the Discord are weighted by tibtre. Contributors steer the project — with one fairness cap: no single person's weight ever counts for more than 25% of a vote, so early large holders guide but never rule. (Exact mechanics are executable — [`voteweight.py`](voteweight.py); with 4 or fewer voters the cap makes a poll one-person-one-vote.)

**Tibtre has no monetary value and no promise of future monetary value.** However, it is the founders' stated intent that **if this project ever forms a legal entity or distributes money, this ledger will be the primary basis for allocation.** Early contributors are provably first in line.

## How do you earn it?

**There is nothing to apply for and nothing to claim.** Do work you believe helps, submit it, get valued — that's the whole process. And tibtre itself is **opt-out**: if you'd rather contribute without being scored at all, say so — your work is just as welcome, and nothing about it gets a number. Contribute anything the project needs, through whichever channel suits you:

| Category | Examples | Where to submit |
|---|---|---|
| `code` | Engine features, bug fixes, tooling | GitHub pull request |
| `research` | Verified gamemd.exe research, parity findings | GitHub pull request or Discord |
| `art` | Sprites, UI art, loading screens, logos, videos | Discord `#submissions` |
| `maps` | Maps and scenarios | Discord `#submissions` |
| `playtesting` | Structured playtest reports, reproducible bug reports | Discord `#submissions` |
| `docs` | Guides, wiki pages, translations | GitHub pull request or Discord |
| `community` | Sustained moderation, onboarding, events | Granted by maintainers |
| `recruit` | Bringing in a contributor who ships | Automatic when their first grant lands — they name you when joining |

You do **not** need a GitHub account. Post your work in the Discord and a maintainer records the grant for you.

## How grants happen

1. You submit work (PR, Discord post, however fits).
2. Accepted work gets **two independent valuations**: a maintainer gives one, and the project's AI reviewer computes one from the public [grading rubric](docs/grading-rubric.md). Your grant is their **average**, rounded to the nearest 0.5 — and both numbers are recorded, so you always see how yours was reached. If the two valuations disagree badly, they're openly reconciled before anything is recorded.
3. On your first grant you're assigned a **contributor ID** (random, like `T-9C41`), DM'd to you — keep that message. The grant is recorded as one row in [`LEDGER.csv`](LEDGER.csv): date, ID, amount, category, and a note carrying what the work was and the full computation.
4. Every grant is public. The ledger is append-only and its full history is auditable.

Work in hard or urgent domains is naturally worth more hours of "quality work" — the reviewer's estimate reflects difficulty, not just clock time.

**The same rules bind everyone — maintainers and founders included.** Their contributions are graded by the same rubric, recorded in the same public ledger, and open to the same disputes as anyone else's.

## Your name is yours to control

The public ledger only ever contains your contributor ID. How you *appear* — in the balances and in credits — is up to you, via [`CONTRIBUTORS.csv`](CONTRIBUTORS.csv):

- Use your Discord handle, a pseudonym, or any name you like.
- Set no display name at all and appear only as your ID.
- Optionally list a public **contact** (portfolio, website, profile link — shown beside your balance). A link is strongly preferred over a raw email: public repos get scraped by spammers, and like everything committed, old values persist in history.
- Change or remove your display name or contact at any time by asking a maintainer — this never touches ledger history, so your balance and grants are unaffected. (GitHub users can also just open a PR editing their own row — your commitment proves the row is yours. The ledger itself is never edited via PR.)

Who is behind each ID is known only to the maintainers, recorded privately. Your assignment DM is your receipt: between it and the maintainers' records, you can always prove which ID is yours — which matters if the allocation intent described above is ever exercised.

And you don't have to trust either of those: every ID carries a public **cryptographic commitment** — a salted hash of your stable platform identity (your Discord or GitHub *numeric* user ID, which never changes even when your username does), recorded in [`CONTRIBUTORS.csv`](CONTRIBUTORS.csv) and pinned in git history the day it was assigned. Your assignment message includes your **salt**; keep it. (Prefer that nobody else ever sees it? Generate the commitment yourself — run `identity.py new` locally and send us only the hash.) Revealing your identity + salt lets *anyone* verify your claim with [`identity.py`](identity.py) — no maintainer, registry, or platform needs to exist for the proof to work, and nobody (including future maintainers) can quietly reassign your ID to someone else. The commitment reveals nothing about you on its own.

### If you want to disappear later

- **Instantly:** ask a maintainer to blank your display name — every current page then shows only your ID. Your balance and grants are untouched, because the ledger never contained your name.
- **From history too:** old versions of the contributors file live in this repository's public history. On request we will rewrite that history to purge your name and ask GitHub to clear its caches. Honest caveat: public repositories can be copied by anyone at any time — we can purge every copy *we* control, but not copies strangers may have made before your request.
- **Your submitted work:** we remove attribution on request, always. Work that has already shipped in the game or been merged stays licensed and shipped — that can't be undone — but we'll stop showcasing it where practical.

## Licensing of submissions

By submitting work to Yrvera you license the project to use, modify, and distribute it under the project's license (or CC-BY 4.0 with attribution for standalone art). You keep ownership of your work; the project keeps the right to ship it.

## Disputes and corrections

If you think a grant is wrong (yours or anyone's), raise it with a maintainer. A second reviewer decides. Corrections are appended to the ledger as new rows — history is never rewritten.

## Changes to this policy

Policy changes are announced in the Discord before they take effect. The ledger and its rules exist to be boring, predictable, and fair.
