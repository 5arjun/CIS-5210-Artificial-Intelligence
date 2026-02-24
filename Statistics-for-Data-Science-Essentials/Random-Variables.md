---
title: "Statistics for Data Science: Random Variables Notes"
date: 2026-02-24
tags: [Random-Variables, Probability, Discrete-Random-Variables, Continuous-Random-Variables, Gaussian-Distribution, Exponential-Distribution]
confidence: 0.67
source: handwritten
---

## Random Variables: Informal Definition

A **random variable** is a variable which takes multiple real values assigned probabilities.

- Denoted as \( X \), with values \( x_i \) and probabilities \( P_i \)
- \( x = x_1, P_1 \)
- \( x = x_2, P_2 \)
- \( 0 \leq P_i \leq 1 \)

## Random Variables: Formal Definition

A random variable \( X \) is a mapping \( X: S \to \mathbb{R} \), where \( S \) is a set of **probabilistic outcomes**.

**Example:**
- \( S = \{ \text{heads}, \text{tails} \} \)
- \( P(\text{heads}) = \frac{1}{2} \)
- \( X(\text{heads}) = 0 \), \( P = \frac{1}{2} \)
- \( X(\text{tails}) = 1 \), \( P = \frac{1}{2} \)

## Types of Random Variables

Random variables exist in 2 forms:

1. **Discrete** (like coin flip example above)
2. **Continuous** - defined through the **probability density function (pdf)**

### Continuous Random Variables (PDF)

- \( P(X = c) = 0 \) for any single point \( c \)
- \( \int P(x) \, dx = 1 \)
- \( P(X \in [a,b]) = \int_a^b P(x) \, dx \)

## Examples

### Gaussian Distribution

\[
P(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
\]

**Gaussian distribution** with parameters \( \mu \) (mean) and \( \sigma \) (standard deviation).

### Exponential Distribution

\[
P(x) = \lambda e^{-\lambda x} \quad \text{if } x \geq 0
\]

\[
P(x) = 0 \quad \text{if } x < 0
\]