---
title: "A* Search Essentials"
date: 2026-02-13
tags: [A-Star-Search, Admissible-Heuristics, Search-Algorithms, Heuristic-Search, AI-Search]
confidence: 0.80
source: handwritten
---

## A* Search Overview

A* Search avoids expanding paths that are already expensive, but expands the **most promising first**.

- **f(n) = g(n) + h(n)**
  - **g(n)**: actual cost so far to reach node
  - **h(n)**: estimated cost to get from current node to goal
  - **f(n)**: estimated total cost of path through n to goal

**Implementation**: Frontier queue as priority queue by increasing f(n).

## Key Concept: Admissible Heuristics

**A heuristic h(n) is admissible if it never overestimates the cost to reach the goal** [optimistic].

**Theorem**: If h(n) is admissible, A* using h(n) is optimal.

**? Should h(n) ≤ true cost?**

## Relaxed Problems

A problem with **fewer restrictions** on the actions than the original.

The cost of an optimal solution to a relaxed problem is an **admissible heuristic** for the original problem.

## Defining Heuristics h(n)

Cost of an exact solution to a relaxed problem (fewer restrictions on operators).

## Dominance: Metric on Better Heuristics

h₂(n) **dominates** h₁(n) if for every node in the search graph, it has a **higher remaining estimate** and both are still admissible.

## Properties of A* Search

- Expands nodes in a different order than Uniform-Cost Search (UCS).
- UCS only checks path cost so far; expands equally in all directions.
- A* expands mainly toward goal but hedges bets to ensure optimality.

**Comparison**:

| Algorithm              | f(n) Formula | Behavior |
|------------------------|--------------|----------|
| **Greedy Best-First** | f(n) = h(n) | Ignores path cost; expands options closest to goal. |
| **UCS**               | f(n) = g(n) | Searches only by path cost; expands lowest path cost. |
| **A***                | f(n) = g(n) + h(n) | Balances path cost and heuristic for optimality. |

## A* Applications

- Pathing/routing problems (e.g., Google Maps)
- Video games
- Robot motion planning
- Resource planning problems

A* Search uses heuristics to **prune the search space** so the use of space is effective.

A well-designed heuristic has a **branching factor close to 1**.