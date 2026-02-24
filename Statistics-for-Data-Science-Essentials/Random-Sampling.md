---
title: "Statistics for Data Science Essentials: Random Sampling"
date: 2026-02-24
tags: [Data-Science, Random-Sampling, Statistics, Confidence-Intervals, Population-Estimation]
confidence: 0.77
source: handwritten
---

## Data Science Overview

Data Science involves the **acquisition, storage, and analysis** of data to effectively extract useful knowledge, information, insights, and patterns.

## Estimating Basic Statistics

Consider the task of estimating the **average height of women** in a population: $\{h_1, h_2, \dots, h_N\}$.

- **Population size**: $N$
- **Goal**: Estimate $\mu = \frac{1}{N} \sum_{i=1}^N h_i$

## Random Sampling

In the real world, choosing from the full $N$ is infeasible for large populations.

- Select a **subset of data uniformly at random** = **random sampling**.
- Let $X_i$ be the $i$-th data point corresponding to an individual chosen uniformly at random from the population.
- Typically, $n \ll N$ (sample size much smaller than population).

```
Population: N
Sample:     n (Xi's chosen independently)
```

## Sample Mean Estimator

Simplest estimator: **Sample mean** $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i \Rightarrow$ estimate for $\mu$.

**Is $\bar{X}$ a good estimate?** If yes, how can we quantify its **performance/error/confidence**, etc.?

## Confidence Interval

**Confidence interval** - range of values within which the true population parameter is likely to lie.