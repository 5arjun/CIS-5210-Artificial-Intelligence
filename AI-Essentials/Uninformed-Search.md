---
title: "Uninformed vs Informed Search Strategies and Evaluation Dimensions"
date: 2026-02-03
tags: [Search-Strategies, Uninformed-Search, Informed-Search, Search-Algorithms, Complexity-Analysis]
confidence: 0.79
source: handwritten
---

## Search Strategies Overview

**Uninformed Search**: All non-goal nodes in frontier look equally good.

**Informed Search**: Some non-goal nodes can be ranked above others.

**Review**: Strategy = order of tree expansion, implemented by different queue structures (LIFO, FIFO, priority).

## Dimensions for Evaluation

- **Completeness**: Always find the solution?
- **Optimality**: Finds a least cost solution first?
- **Time Complexity**: # of nodes generated (worst case)
- **Space Complexity**: # of nodes simultaneously in memory (worst case)

## Time/Space Complexity Variables

- \( b \): max branching factor of search tree
- \( d \): depth of shallowest goal node
- \( m \): max length of any path in state space (potentially \( \infty \))
