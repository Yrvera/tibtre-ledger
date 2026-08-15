# Tibtre grading rubric — v1.3

*(v1.3: added `recruit` — paid when the recruit's first grant lands. v1.2: dual
valuation — human value + AI value, averaged; bounties demoted to an occasional
tool. v1.1: added "Worth to the project". Forward-only as always.)*

## Who values a grant — human + AI, averaged

Accepted work gets two independent valuations:

1. **The AI reviewer** computes a value strictly from this rubric, showing every
   factor.
2. **A maintainer** gives their value — a rubric computation or an experienced gut
   number, their choice.

The grant is the **average of the two, rounded to the nearest 0.5**, and both inputs
are recorded in the ledger notes (e.g. `H4 + A5 → 4.5`). If the valuations differ by
more than **×1.5**, don't average — that gap usually means the two saw different
scope; reconcile openly first, then record.

Contributors never apply, claim, or pre-register anything. Do the work, submit it,
get valued.

Every grant is **computed, not guessed**:

```
tibtre = base × difficulty × quality      (rounded to nearest 0.5, minimum 0.5)
```

Each factor comes from the tables below. Every grant proposal must show all three
factors with a one-line justification each, so anyone can recompute the number.
Same formula for everyone, no exceptions.

## Base — by category and size

Size is judged on **scope of the accepted work, not effort claimed** — and never on
raw line count (padding a diff doesn't move the size class).

### Code
| Size | Definition | Base |
|---|---|---|
| XS | Typo, one-liner, config tweak | 0.5 |
| S | Contained fix, one file/subsystem | 1.5 |
| M | Feature or fix within one subsystem, incl. tests | 4 |
| L | Multi-subsystem feature or new module | 8 |
| XL | New system end-to-end | 16 |

### Reverse-engineering research
| Work | Base |
|---|---|
| Single verified fact (address/constant/formula, with evidence) | 1 |
| Focused note — one mechanic, verified claims, implementation handoff | 3 |
| Full system doc — verified, with implementation handoff | 8 |

### Art (RA2 assets are countable — frames, facings, damage states)
| Work | Base |
|---|---|
| Cameo/icon | 1 |
| UI element, loading screen, promo art | 3 |
| Building SHP (frames + damage states) | 5 |
| Voxel unit (+turret) | 6 |
| Full unit SHP set (8 facings × walk/attack/die) | 10 |

### Maps
| Work | Base |
|---|---|
| Small skirmish map, playtested | 3 |
| Large or multiplayer-balanced map, playtested | 6 |

### Playtesting
| Work | Base |
|---|---|
| Reproducible bug report (steps + expected vs actual) | 1 |
| Structured session report (following the template) | 2 |

### Docs, translations, community
| Work | Base |
|---|---|
| Guide/wiki page | 2 |
| Translation, per 1000 words | 1.5 |
| Community event organized | 3 |
| Sustained moderation, per month | 2 |
| Recruited a contributor who ships | 2 |

**Recruit rule:** paid only when the recruited person's *first grant is recorded* —
never on the invite itself (invite spam mints nothing). The newcomer names their
recruiter during ID assignment; one recruit grant per new contributor; no
multipliers. If the recruit becomes a major contributor, the recruiter's upside is
handled by the normal impact-bonus machinery.

## Difficulty multiplier — take the single highest that applies

| × | Applies to |
|---|---|
| 1.0 | Routine work |
| 1.5 | Hard domains: deterministic sim internals, renderer/GPU, netcode, RE of unlabeled binary code |
| 2.0 | Items on the current **priority board** (published and updated by maintainers) |

The priority board is how "hard-pressing" becomes math instead of mood: maintainers
post what the project urgently needs; work on those items earns ×2.0 while listed.

## Quality multiplier

| × | Applies to |
|---|---|
| 0.75 | Accepted, but needed significant rework by others |
| 1.0 | Solid — accepted as-is |
| 1.25 | Exceptional — beyond-scope tests/docs/polish |

## Bounties — an occasional tool, never a gate

Maintainers may occasionally pre-price an urgent task: *"implement X = 12 tibtre."*
A completed, accepted bounty pays **exactly** its posted price — no valuations, no
judgment after the fact. Bounties are rare and purely optional: nobody ever needs to
wait for one, claim one, or ask permission to work. Unsolicited work is the normal
path and is valued identically well.

## Worth to the project

Tibtre ultimately tracks **contribution to the project's worth** — what attracts
players, attracts contributors, draws support, or unblocks the work that does. Since
every grant dilutes every other holder, overpaying low-value work is unfair to the
people who added real worth. But worth cannot be *guessed* at grant time without
destroying reproducibility — so it enters at the two moments it is actually knowable:

- **Before work starts:** the priority board (×2.0) and bounty prices are the
  maintainers' declaration of what the project's worth needs most. Value is priced by
  judgment in advance, then paid by formula.
- **After worth proves itself — impact bonuses:** at milestones (a release, a player
  or contributor influx, a donation spike), maintainers review what demonstrably drove
  it and grant bonus tibtre as new ledger rows, category `impact`, each citing its
  observable evidence (e.g., *"replay system — named in the posts that brought 200 new
  members"*). No formula — but no bonus without named, public evidence, and
  comparables discipline applies across impact grants too.

The strongest predictor of worth in this project is **player-visible improvement** —
the same bar the engine uses for parity. When judging priority-board entries and
impact bonuses, ask "does a player feel this?" before "was this hard?".

## Consistency mechanics

- **Show your work.** A grant without its computation is invalid.
- **Comparables.** Each proposal cites the most similar past grant(s) from the ledger;
  deviating more than ~30% from comparables requires explanation or a second reviewer.
- **Versioned, forward-only.** Rubric changes get a new version number and apply only
  to future grants — the ledger is never repriced retroactively.
- **Disputes.** Recompute together; if you still disagree, a second maintainer
  decides; corrections are appended as new ledger rows.

## Worked examples

1. Contained pathfinding bug fix, in the hard sim domain, accepted as-is:
   `1.5 (S code) × 1.5 (hard domain) × 1.0 = 2.5` *(2.25 → nearest 0.5)*
2. Loading screen, routine, exceptional polish:
   `3 (art) × 1.0 × 1.25 = 4`
3. Full verified research doc on a priority-board system:
   `8 × 2.0 × 1.0 = 16`
4. Bounty "fix desync in replay seek" posted at 12: accepted → **12**, computed no further.

## What the math does and doesn't promise

The formula guarantees **consistency, predictability, and auditability** — identical
work earns identical tibtre, and you can price your contribution before you start.
It does not claim the constants are objectively true; they are calibrated judgment,
tuned openly via rubric versions. The human review gate stays because every fully
automated scoring system eventually gets gamed; the formula disciplines the human,
the human sanity-checks the formula.
