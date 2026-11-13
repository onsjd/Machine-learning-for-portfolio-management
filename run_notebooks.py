"""Run historical notebook Python cells from the repository root (no Jupyter needed)."""
import argparse
import json
import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebooks", nargs="*", default=[
        "old_work/01_market_regimes.ipynb", "old_work/02_portfolio_comparison.ipynb",
        "old_work/03_fred_regimes_portfolios.ipynb"])
    args = parser.parse_args()
    os.chdir(root)
    for name in args.notebooks:
        path = root / name
        namespace = {"__name__": "__main__", "display": lambda *args, **kwargs: None}
        notebook = json.loads(path.read_text(encoding="utf-8"))
        for i, cell in enumerate(notebook["cells"], 1):
            if cell["cell_type"] == "code":
                exec(compile("".join(cell["source"]), f"{name}:cell-{i}", "exec"), namespace)
                plt.close("all")
        print(f"PASS {name}", flush=True)

if __name__ == "__main__":
    main()
