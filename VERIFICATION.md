# Verification

The Python code cells of all three notebooks were rerun successfully on 2026-11-08 using the bundled data, in an isolated copy of the project.

- PASS: 01_market_regimes.ipynb
- PASS: 02_portfolio_comparison.ipynb
- PASS: 03_fred_regimes_portfolios.ipynb

Embedded assertions cover chronological cutoffs, portfolio budgets and caps, initial transaction costs, cost sensitivity, aligned test dates, finite returns and signal lags. This verifies execution and the embedded checks; it does not establish an investable trading performance or point-in-time data availability.

The original executed notebook outputs and result snapshots are preserved.
