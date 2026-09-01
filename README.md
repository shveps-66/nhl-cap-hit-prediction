# NHL Cap Hit: expected pay vs actual

Build an **expected share of salary cap** for NHL skaters (`CapHit_pct` = CapHit / salary cap), then use residuals (actual minus expected) to flag players who look underpaid or overpaid **relative to the model**.

This is a second look signal for comps and negotiation prep. It is not a market verdict.

Metric definitions: see [GLOSSARY.md](GLOSSARY.md).

Presentation (PDF): [NHL Cap Hit Model.pdf](NHL%20Cap%20Hit%20Model.pdf)

## Why this matters

Cap hit is a fact. Value is a judgment call. The residual

`actual CapHit_pct − predicted CapHit_pct`

is a practical mismatch detector:
- **Negative residual:** actual share is lower than the model expects (possible bargain / under relative to profile)
- **Positive residual:** actual share is higher than expected (possible over relative to profile)

Large gaps need contract context (length, ELC, when the deal was signed). Same-season stats describe expected pay **given that season profile**, not a pure prior-year forecast.

## Project goals

1. Estimate expected cap share from performance, role, team context, and contract stage
2. Flag large pay gaps worth a second look in contract review
3. Explain what drives expected pay with CatBoost and SHAP
4. Treat entry-level under residuals as **next-contract potential**, not underpaid today

## Project structure

```
├── EDA.ipynb                      # contract market exploratory analysis
├── NHL_CapHit_Model.ipynb         # CatBoost, residuals, SHAP, ELC lens
├── NHL Skater Cap Hit.csv         # skater seasons used in the notebooks
├── NHL Cap Hit Model.pdf          # portfolio presentation deck
├── viz_labels.py                  # shared chart labels for EDA
├── requirements.txt
├── GLOSSARY.md                    # metric definitions
└── README.md
```

## Data

| Item | Detail |
|------|--------|
| File | `NHL Skater Cap Hit.csv` |
| Unit | Player season |
| Seasons | 23/24 to 25/26 |
| Train | 23/24 + 24/25 |
| Holdout review | 25/26 |
| Rows | 2310 skater seasons (`GP >= 10`, CapHit present) |
| Sources | Publicly available NHL, HockeyStats, and contract data |

**Team for multi-club seasons:** `Team` = last club in NHL `teamAbbrevs` (not the first). Example: Chinakhov 25/26 → PIT.

CapHit policy: **full contractual** hit for the season (not mid-season retain splits or accrued shards).

## Method (short)

1. Load the modeling table and filter to the GP ≥ 10 sample
2. EDA on contract market structure (length, age, F vs D, end of ELC, performance links)
3. CatBoost on `23/24`+`24/25`; residuals and SHAP on `25/26`
4. Read ELC under residuals as next-contract potential

## Model features (~42)

- Context: `Season_id`, `Pos_group`, `S/C`, Age, height, weight, `GP`
- Role: `TOI/GP`, `Depth_TOI_rank`, `PP TOI`, `PK TOI`
- Contract: `Is_ELC`, `ContractLength`, `YearsRemaining`
- Value: `WAR_per_GP`, EVO / EVD / PP / PK WAR
- Offense / on-ice: points/GP, ixG, shots, xGF%, OZ Start%, xG_diff
- Defense / physical: Hits, HitsT, BkS, TkA, GvA, PIM, DZ Start%
- Team: pointPct, GF%, PP%, PK%
- NHL Edge: max skating mph, bursts over 20, top shot mph, distance metrics, OZ time share

**Not in the model:** `plusMinus`, `AAV` (CapHit / CapHit_pct only).

## Holdout results (`25/26`)

| Metric | Value |
|--------|-------|
| RMSE (`CapHit_pct`) | 0.01123 |
| MAE (`CapHit_pct`) | 0.00801 |
| R² | 0.8575 |
| MAE ≈ $M | ~0.77 |
| Features | ~42 |

Salary cap in `25/26` is **$95.5M**. Rough talk track: **1 pp of cap share ≈ $0.95M**.

Contract length is the strongest single lever (price-band anchor). Performance, role, ELC / years left still move expected share a lot after that.

## Notebook map

### `EDA.ipynb`

Cap-hit size, contract length, age and pay, signing age, F vs D, end of ELC, performance scatters, and Spearman links with `CapHit_pct`.

### `NHL_CapHit_Model.ipynb`

1. Fit + holdout metrics
2. League residuals (under / over)
3. Drivers: importance, SHAP, contract length vs everything else
4. Entry-level as next-contract potential
5. Summary

## How to run

```bash
# from this project folder
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook EDA.ipynb
jupyter notebook NHL_CapHit_Model.ipynb
```

Run each notebook top to bottom. Both read `NHL Skater Cap Hit.csv`.

## Key libraries

- pandas, numpy
- scikit-learn, CatBoost
- matplotlib, seaborn, shap

## Limitations

- Same-season stats describe expected pay given that season profile. Many deals were signed earlier.
- Entry-level pay is largely CBA-capped. A large ELC under residual is a **next-deal lens**, not underpaid today.
- Goalies are out of this skater model.
- Residuals are a starting point for comps, not a claim that a club overpaid or underpaid as a fact.
- `Is_ELC` is rule-based and was audited; cheap post-ELC deals with ELC-like CapHit are a known trap.

## Author

Valentin Shepelev  
Hockey analytics content: [TikTok @vs__hockey](https://www.tiktok.com/@vs__hockey)
