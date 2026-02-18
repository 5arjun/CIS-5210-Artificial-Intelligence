---
title: "Statistics for Data Science Essentials: Discrete Math Review"
date: 2026-02-18
tags: [discrete-mathematics, set-theory, functions, data-science-fundamentals]
confidence: 0.82
source: handwritten
---

## Sets

A **set** is a collection of distinct objects called elements. Sets are typically denoted by capital letters, and elements are contained within curly braces.

Key properties of sets:
- Order of elements doesn't matter
- No element may be repeated
- Example: \(A = \{7, -10, 4.5\}\)

The symbol \(\in\) denotes that something is an element of a set. For example: \(7 \in A\)

## Number Systems

| Number System | Description | Symbol | Examples |
|---|---|---|---|
| Integers | Whole numbers (positive, negative, and zero) | \(\mathbb{Z}\) | 3, 0, -10, 4657 |
| Natural Numbers | Positive integers starting at 1 | \(\mathbb{N}\) | 1, 2, 3, 4, ... |
| Rational Numbers | Numbers represented as a ratio between two integers; includes fractions and decimals | \(\mathbb{Q}\) | \(\frac{1}{2}\), 0.5, 3 |

## Set Builder Notation

Set builder notation defines a set by specifying a property that its elements must satisfy.

Examples:
- \(S = \{x \mid -50 \leq x \leq 200\}\)
- \(\mathbb{Q} = \left\{\frac{m}{n} \mid m, n \in \mathbb{Z}, n \neq 0\right\}\)

## Functions

A **function** describes the relationship between a set of inputs (domain) and a set of outputs (codomain).

Examples:
- \(f(x) = x + 5\)
- \(g(x) = x^2 - 1\)
- \(f(x, y) = 7x + 5y\)

### Piecewise Functions

A piecewise function has different functions or rules depending on the domain.

Example:

\[
f(x) = \begin{cases}
1 & \text{if } x < 0 \\
2x & \text{if } x \geq 0
\end{cases}
\]