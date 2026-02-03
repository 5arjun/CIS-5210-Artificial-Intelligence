---
title: "Uninformed vs Informed Search Strategies and Evaluation Dimensions"
date: 2026-02-03
tags: [Search-Strategies, Uninformed-Search, Informed-Search, Search-Algorithms, Complexity-Analysis]
confidence: 0.79
source: handwritten
---

## Search Strategies Overview

**Uninformed Search**: All non-goal nodes in frontier look equally good.[1]

**Informed Search**: Some non-goal nodes can be ranked above others.[1]

**Review**: Strategy = order of tree expansion, implemented by different queue structures (LIFO, FIFO, priority).[1]

## Dimensions for Evaluation

- **Completeness**: Always find the solution?[1]
- **Optimality**: Finds a least cost solution first?[1]
- **Time Complexity**: # of nodes generated (worst case)[1]
- **Space Complexity**: # of nodes simultaneously in memory (worst case)[1]

## Time/Space Complexity Variables

- \( b \): max branching factor of search tree[1]
- \( d \): depth of shallowest goal node[1]
- \( m \): max length of any path in state space (potentially \( \infty \))[1]