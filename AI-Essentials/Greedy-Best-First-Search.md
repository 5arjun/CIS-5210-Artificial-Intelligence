---
title: "AI Essentials: Greedy Best-First Search and Heuristics"
date: 2026-02-10
tags: [Heuristic-Search, Greedy-Best-First, Uninformed-Search, Search-Algorithms, AI-Essentials]
confidence: 0.86
source: handwritten
---

## Heuristics

- **Heuristic**: Rule of thumb, simplification, or educated guess.
- **Heuristic knowledge**: Useful but not necessarily correct.
- **Heuristic algorithms**: Use heuristic knowledge to solve a problem.
- **Heuristic function** \( h(n) \): Takes a state \( n \) and returns an estimate of the distance from \( n \) to the goal.

The performance of heuristic search algorithms very much depends on the quality of the heuristic function.

## Uniform-Cost Search (UCS)

- UCS is a **complete** algorithm.
- It will find a solution in a finite amount of time.

## Greedy Best-First Search

**Basic idea**: Select node for expansion with minimal evaluation function \( f(n) \), where \( f(n) \) includes the estimated heuristic \( h(n) \) of remaining distance to the goal.

- **Implementation**: Priority queue.
- Exactly like UCS, but with \( f(n) = h(n) \) replacing \( g(n) \).
- Expands node that's estimated to be closest to the goal.
- Completely ignores \( g(n) \): cost to get to node.

### Properties

- **Optimal?** No, not guaranteed to find best path.
- **Complete?** No, can get stuck in loops.