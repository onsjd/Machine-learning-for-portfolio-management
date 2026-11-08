## Observed results from this execution

| Strategy | CAGR | Volatility | Sharpe rf=0 | Max drawdown |
|---|---:|---:|---:|---:|
| Equal weight | 12.96% | 17.36% | 0.79 | -25.33% |
| Markowitz | 13.69% | 11.87% | 1.14 | -17.07% |
| KMeans price | 13.29% | 12.89% | 1.04 | -16.55% |
| GMM price | 14.52% | 13.08% | 1.11 | -19.38% |
| KMeans price_fred | 13.37% | 12.91% | 1.04 | -16.60% |
| GMM price_fred | 10.79% | 12.55% | 0.88 | -19.10% |

Incremental FRED effect relative to the same algorithm on commodity features only:

- KMeans price_fred minus KMeans price: Sharpe difference +0.004; approximate paired interval [-0.180, 0.141].
- GMM price_fred minus GMM price: Sharpe difference -0.225; approximate paired interval [-0.571, 0.084].

A change in ranking is a result of this exploratory specification, not proof that FRED indicators improve future investable performance. The original two notebooks are retained; use this third notebook for the fair common-sample comparison.