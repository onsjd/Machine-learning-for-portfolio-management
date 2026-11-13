# Old work — historical research notebooks

These intermediate notebooks document the development of the project. **They are not the submission and are not required by the final notebook.**

Use [Final_Research_Notebook.ipynb](../Final_Research_Notebook.ipynb) for the complete submitted study and the latest robustness checks.

| Notebook | Historical role |
|---|---|
| `01_market_regimes.ipynb` | Initial price exploration and K-Means/GMM regimes |
| `02_portfolio_comparison.ipynb` | Initial portfolio comparison |
| `03_fred_regimes_portfolios.ipynb` | FRED macroeconomic extension |
| `04_news_sentiment.ipynb` | News cleaning and sentiment exploration |
| `05_sentiment_regimes_portfolios.ipynb` | Initial sentiment-conditioned allocation |

The notebooks and saved outputs are preserved unchanged. Their conclusions and specifications may differ from the final consolidated study.

## Optional historical execution

Their relative data paths assume the repository root as the working directory, not this folder. From the root, `python run_notebooks.py` runs 01–03. To run another historical notebook explicitly, use, for example, `python run_notebooks.py old_work/04_news_sentiment.ipynb`. Running historical notebooks can regenerate files under `data/` and `results/`; use a separate copy if preserving those snapshots matters. For interactive Jupyter execution, set the kernel working directory to the repository root before running cells.
