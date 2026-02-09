---
title: "AI Essentials: Uniform-Cost Search"
date: 2026-02-09
tags: [Uninformed-Search, Search-Algorithms, Uniform-Cost-Search, AI-Essentials]
confidence: 0.83
source: handwritten
---

## Uniform-Cost Search

Uniform-Cost Search is a **search tree algorithm** used for weighted graphs, such as map navigation problems.

- **g(N)**: path cost function, representing the cost to reach node \( n \).

### Key Characteristics
- Extension of **Breadth-First Search (BFS)**: expands nodes with the **lowest path cost** first.
- **Implementation**: frontier is a **priority queue** ordered by \( g(n) \).

### Significant Differences from BFS
- Tests if a node is the **goal state** when **selected for expansion**, not when added to the frontier.
- **Updates** a node on the frontier if a **better path** to the same state is found.
- Always enqueues a node **before checking** if it is a goal.

### Comparison Table

| Aspect                  | Breadth-First Search (BFS)              | Uniform-Cost Search (UCS)                  |
|-------------------------|-----------------------------------------|--------------------------------------------|
| **Queue Type**         | FIFO queue (uniform in all directions) | Priority queue (prioritizes lowest path cost) |
| **Expansion Order**    | Level by level                         | Lowest \( g(n) \) first                    |
| **Goal Test Timing**   | When added to frontier                 | When selected for expansion                |
| **Path Updates**       | No updates for better paths            | Updates frontier if better path found      |