# Verification

## Final submission notebook — 13 November 2026

`Final_Research_Notebook.ipynb` was executed from a fresh Python 3.12.15 kernel, top to bottom, twice during this update. The final saved run completed all 26 code cells with no error outputs. Tested package versions are recorded in `environment_used.json`, `requirements.txt` and Section 7.

The original cutoff-invariance checks passed for all 88 decision months; backward-looking price features and independent net-return reconciliation also passed. New checks verify finite allocations, budget constraints and every concentration cap, and reproduce original allocations at the 60% cap and with both conditional moments (absolute tolerance 1e-9).

Section 5.2 reports 12 conditioning-channel comparisons, 12 matched-state-count sentiment comparisons, and all 51 strategy/cap/window combinations. Each cap comparison uses Markowitz under the same cap. All inputs passed the notebook's SHA-256 checks. These are exploratory analyses of previously examined evaluation windows, with conditional block-bootstrap intervals and no multiplicity correction. Successful execution does not establish investability or historical predictor availability.

## Historical verification of notebooks 01–03

The Python code cells of all three notebooks were rerun successfully on 2026-11-08 using the bundled data, in an isolated copy of the project.

- PASS: 01_market_regimes.ipynb
- PASS: 02_portfolio_comparison.ipynb
- PASS: 03_fred_regimes_portfolios.ipynb

Embedded assertions cover chronological cutoffs, portfolio budgets and caps, initial transaction costs, cost sensitivity, aligned test dates, finite returns and signal lags. This verifies execution and the embedded checks; it does not establish an investable trading performance or point-in-time data availability.

The original executed notebook outputs and result snapshots are preserved.
