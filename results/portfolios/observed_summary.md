## Observed results from this execution

| Strategy | CAGR | Volatility | Sharpe (rf=0) | Max drawdown |
|---|---:|---:|---:|---:|
| Equal weight | 12.96% | 17.36% | 0.79 | -25.33% |
| Markowitz | 13.69% | 11.87% | 1.14 | -17.07% |
| KMeans Markowitz | 13.56% | 12.96% | 1.05 | -16.41% |
| GMM Markowitz | 14.10% | 12.54% | 1.12 | -22.08% |

These are net monthly-average price-proxy results for March 2021–December 2025. KMeans Markowitz has a Sharpe difference of -0.09 versus classical Markowitz in this sample. GMM Markowitz has a Sharpe difference of -0.03 versus classical Markowitz in this sample. The paired bootstrap intervals above help assess uncertainty; no robust investment outperformance claim follows from this short proxy experiment.