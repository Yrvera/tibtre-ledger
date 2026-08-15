# Granting guide (for approvers)

How to record a tibtre grant, start to finish. Target time: under two minutes.

## 1. Value the grant — two numbers, averaged

1. Get the **AI value**: ask Claude to compute it from the
   [grading rubric](grading-rubric.md) (`base × difficulty × quality`), with factors
   shown and the most similar past grant cited. The exact instruction the AI follows
   is public — [ai-evaluation-prompt.md](ai-evaluation-prompt.md) — so anyone can
   reproduce a valuation with their own Claude.
2. Give **your value** — your own rubric computation or an experienced gut number.
3. Grant = **average, rounded to nearest 0.5**. Record both in the `notes` column,
   e.g. `H4 + A5 → 4.5`.
4. If the two values differ by more than ×1.5, don't average — compare what scope
   each of you saw, agree, then record.

A (rare) posted bounty price wins outright — no valuations. When torn between two
size classes, pick the higher one for newcomers.

## 2. First-time contributor? Assign an ID

1. Generate a random ID: `python -c "import secrets; print('T-'+secrets.token_hex(2).upper())"`
   — re-roll if it already exists in `CONTRIBUTORS.csv` (format `T-XXXX`).
2. Generate their identity commitment: `python identity.py new discord:<numeric id>`
   (or `github:<numeric id>` for GitHub-based contributors) — commitment goes in
   `CONTRIBUTORS.csv` (space-separated if they already hold one), salt goes in the
   registry AND the DM. If the contributor prefers to hold the only copy of their
   salt, they may run `identity.py new` themselves and send just the commitment —
   record it verbatim and leave the registry's salt field empty.
3. Add their row to the **private registry** (see `../vera20k-tibtre-private/`):
   ID, Discord **numeric user ID** (Developer Mode → right-click user → Copy User ID —
   handles change, the number never does), current handle, salt, date.
4. **DM them their ID and their salt** and tell them to keep the message — it's
   their receipt, and the salt makes their identity claim publicly provable via
   `identity.py` without trusting anyone.
5. Ask how they want to appear publicly: their handle, a pseudonym, or nothing
   (ID only) — and whether they want a public contact shown (portfolio/site link
   preferred over raw email; warn that committed values persist in history). Add
   `id,display_name,contact,commitment` to `CONTRIBUTORS.csv` — leave fields
   empty as chosen.
6. Ask **who, if anyone, brought them to the project**. Record the recruiter in the
   private registry notes — and when this newcomer's first grant is recorded, grant
   the recruiter 2 tibtre (`recruit`) in the same batch.

Display-name changes later are just an edit to `CONTRIBUTORS.csv` — never touch the
ledger for a naming matter.

## 3. Secure the artifact

The ledger row must link to something durable:

- **Code / research / docs** — link the merged PR or commit.
- **Artwork / maps / media** — save the file into `assets/` as
  `YYYY-MM-DD_T-XXXX_short-title.ext` (always the ID, never the name — filenames are
  public and forever), then reference that path. Discord message links die
  (deletable, members-only) — don't use them as the only reference.
- **Playtest reports** — paste the report into a file under `assets/` too if it only
  exists as a Discord message.

Check the licensing line applies (it's in RULES.md — submitting = licensing the
project to use the work). If the contributor hasn't seen it, point them to it.

**Privacy scrub before committing — history is forever:** check every file for
personal information before it enters git. Usernames or real names visible in
screenshots, embedded image metadata (EXIF), real names in report text, identifying
paths in logs. Redact first, commit second — an erasure request later is a
history-rewrite; a scrub now is ten seconds.

## 4. Append the ledger row

One row at the END of `LEDGER.csv` — never edit existing rows:

```csv
date,id,tibtre,category,notes
2026-08-14,T-9C41,5,art,loading screen (assets/2026-08-14_T-9C41_loading-screen.png); art3 x1.5 x1.0; H5 + A4.5 -> 5 (rubric v1.3)
```

- `date` — ISO `YYYY-MM-DD`
- `id` — contributor ID from `CONTRIBUTORS.csv`
- `tibtre` — the amount (negative only for corrections, with an explanatory note)
- `category` — `code` / `research` / `art` / `maps` / `playtesting` / `docs` / `community` / `recruit` (paid on the recruit's first grant) / `impact` (retrospective value bonus — evidence required in notes) / `other`
- `notes` — what the work was (PR number or assets filename keeps it traceable),
  the computation, and the H/A values. Required for corrections. Keep names out
  of notes for pseudonymous contributors.

## 5. Regenerate balances and commit

```
python tally.py
git add -A
git commit -m "grant: 5 tibtre to T-9C41 (art)"
```

## 6. Announce

Post the grant to the announcements channel via its webhook (URL lives in the
private folder): ID, amount, category, artifact link, and the computation — name
the contributor **only if they have a public display name**; pseudonymous
contributors are congratulated by DM, and their announcement carries the ID only.

## Corrections

Wrong amount or wrong ID? Append a compensating row (negative amount or a new grant)
with a note pointing at the mistaken row's date+ID. The old row stays.
