# Glossary

Definitions for the modeling table  
`NHL Skater Cap Hit.csv`  
and closely related project terms.

Unless noted, values are **per player season**.  
Chart labels use plain English via `viz_labels.py` (`lab()` / `labs()`).

**Sources:** NHL API / NHL Edge, [HockeyStats](https://hockeystats.com/stats), Spotrac team cap sheets.  
**Sample (EDA + model):** skaters, `GP >= 10`, CapHit present (2310 player seasons in the public CSV).

Season keys in CSV files are hyphenated (`23-24`). Charts and prose often show slash form (`23/24`).

---

## Identity and filters

| Metric | Meaning |
|--------|---------|
| `playerId` | NHL player id (preferred join key with `Season`) |
| `Player` | Display name |
| `Season` | Season key, e.g. `23-24` |
| `Team` | Team abbrev. For multi-club seasons, **last** club in NHL `teamAbbrevs` (not the first) |
| `Season_id` | Numeric season index for the model |
| `Pos_group` | Position group used in modeling (`C` / `W` / `D`; L/R wings folded into `W`) |
| `S/C` | Shot side: `L` or `R` |
| `Age` | Age in floor years for that season |
| `heightInInches` | Height (inches) |
| `weightInPounds` | Weight (pounds) |
| `GP` | Games played |

---

## Target and pay

| Metric | Meaning |
|--------|---------|
| `CapHit` | Contractual cap hit for that season, stored in **millions of USD** on the lean table |
| `CapHit_pct` | `CapHit / SalaryCap` for that season (**model target**). Share of the league salary cap |
| Salary cap | Implied from `CapHit / CapHit_pct` in the table (e.g. `25-26` = $95.5M) |

**Units tip:** model and SHAP often use **percentage points (pp)** of `CapHit_pct`. At a $95.5M cap, **1 pp ≈ $0.95M**. Dollar residuals in the notebook also use each row’s implied cap (`CapHit / CapHit_pct`).

**CapHit policy:** full contractual hit for the deal season. Not mid-season retain splits or accrued dead-cap shards. `AAV` is not kept on the model tables.

---

## Contract

| Metric | Meaning |
|--------|---------|
| `Is_ELC` | Entry-level style flag (rule-based): CapHit in ELC band, length 2 or 3, age under 25, not UFA. Audited against false post-ELC flags |
| `ContractLength` | Years on the current deal (ELC length is usually 3; slides do not inflate length) |
| `YearsRemaining` | `ExpiryYear − season_end_year`. **0** in the final year of the deal. One-year deals ⇒ YR = 0. Always YR ≤ ContractLength |

---

## Role and ice time

| Metric | Meaning |
|--------|---------|
| `TOI/GP` | Ice time per game (**minutes** on the lean table) |
| `Depth_TOI_rank` | Ice time rank on the team (within season / team / position group) |
| `PP TOI` | Power play ice time |
| `PK TOI` | Penalty kill ice time |

---

## Value (HockeyStats WAR)

| Metric | Meaning |
|--------|---------|
| `WAR_per_GP` | HockeyStats wins above replacement / GP |
| `EVO WAR` | Even-strength offense WAR component |
| `EVD WAR` | Even-strength defense WAR component |
| `PP WAR` | Power play WAR component |
| `PK WAR` | Penalty kill WAR component |

HockeyStats WAR is the value layer in this project (not Evolving-Hockey GAR).

---

## Offense and on-ice

| Metric | Meaning |
|--------|---------|
| `pointsPerGame` | Points per game |
| `ixG` | Individual expected goals (season total) |
| `shots` | Shots on goal (season total) |
| `xGF%` | On-ice expected goals for share (HockeyStats on-ice in join is **5v5**) |
| `OZ Start%` | Offensive zone start share |
| `DZ Start%` | Defensive zone start share |
| `xG_diff` | Expected goals difference (on-ice) |

---

## Defense and physical

| Metric | Meaning |
|--------|---------|
| `Hits` | Hits delivered |
| `HitsT` | Hits taken |
| `BkS` | Blocked shots |
| `TkA` | Takeaways |
| `GvA` | Giveaways |
| `penaltyMinutes` | Penalty minutes |

---

## Team context

| Metric | Meaning |
|--------|---------|
| `Team_pointPct` | Team points percentage |
| `Team_GF_pct` | Team goals for share |
| `Team_PP%` | Team power play percentage |
| `Team_PK%` | Team penalty kill percentage |

Joined from the player’s `Team` (last club when traded).

---

## NHL Edge

| Metric | Meaning |
|--------|---------|
| `nhl_edge_skatingSpeedMax_mph` | Top skating speed (mph) |
| `nhl_edge_burstsOver20` | Skating bursts over 20 mph (season count) |
| `nhl_edge_topShotSpeed_mph` | Top shot speed (mph) |
| `nhl_edge_totalDistanceSkated_mph` | Skating distance (NHL Edge field as stored) |
| `nhl_edge_distanceMaxGame_mph` | Max skating distance in a game (NHL Edge field as stored) |
| `nhl_edge_zoneTime_offensiveZonePctg` | Share of time in the offensive zone |

---

## Derived in notebooks (not always a CSV column)

| Metric | Meaning |
|--------|---------|
| `bursts_per_60` | `nhl_edge_burstsOver20 / (TOI/GP * GP) * 60`. Intensity rate; used in EDA. Not a default model feature |
| `CapHit_pct_pred` | Model predicted share of salary cap |
| `residual_pct` / `residual_pp` | Actual share minus predicted share |
| `residual_M` | Residual in roughly $M using implied salary cap |
| length effect (pp) | Sum of SHAP for `ContractLength`, in percentage points of cap share |
| everything else (pp) | Sum of SHAP for all other features |

---

## Reading residuals

| Sign | Meaning |
|------|---------|
| Negative | Actual cap share lower than expected (possible under / bargain relative to profile) |
| Positive | Actual cap share higher than expected (possible over relative to profile) |

Residuals are a comps / reevaluation signal, not a claim that a club overpaid or underpaid as a fact.  
On ELC, prefer **next-contract potential** over underpaid today.
