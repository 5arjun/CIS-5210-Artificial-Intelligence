---
title: "AI Essentials: Search Algorithms Comparison"
date: 2026-02-04
tags: [Breadth-First-Search, Depth-First-Search, Iterative-Deepening-Search, Uninformed-Search, Search-Algorithms]
confidence: 0.84
source: handwritten
---

## Breadth-First Search (BFS)

Expand shallowest unexpanded node.

### Implementation
- Frontier is FIFO queue.
- Put successors at end of frontier successor list.

### Properties
- **Complete?** Yes (if \( b \) is finite).
- **Time complexity:** \( O(b^d) \), where:
  - \( b \): max branching factor of tree.
  - \( d \): depth of least-cost solution.
- **Space complexity:** \( O(b^d) \), where \( m \): max depth of state space.
- **Optimal?** Yes if cost = 1 per step (usually not).

## Depth-First Search (DFS)

Expand deepest unexpanded node.

### Implementation
- Frontier is LIFO queue.
- Put successors at front of frontier.

### Properties
- **Complete?** No, fails in infinite depth spaces.
- **Time:** \( O(b^m) \), \( m \) = max depth.
- **Space:** \( O(bm) \) (linear).
- **Optimal?** No.

## Depth vs Breadth Trade-offs

- Space is restricted.
- Many possible solutions with long paths, wrong paths terminate quickly.
- Search can be fine-tuned quickly.
- Possible infinite paths.
- Some solutions have short paths.
- Can quickly discard unlikely paths.

## Depth-Limited Search

Depth-First Search but with limited depth \( l \):
- Nodes at depth \( l \) have no successors (no infinite path problem).

### Properties
- If \( l = d \) (by luck): optimal.
- If \( l < d \): incomplete.
- If \( l > d \): not optimal.
- **Time:** \( O(b^l) \).
- **Space:** \( O(bl) \).

## Iterative Deepening Search

Uses Depth-Limited Search as subroutine with increasing \( l \).

### Properties
- **Complete:** Yes.
- **Optimal:** Yes (if cost per step = 1).
- **Time:** \( O(b^d) \).
- **Space:** \( O(bd) \).

## Summary Table

| Algorithm          | Complete | Time     | Space   | Optimal          |
|--------------------|----------|----------|---------|------------------|
| **Breadth-First** | Yes     | \( b^d \) | \( b^d \) | Yes (cost=1)    |
| **Depth-First**   | No      | \( b^m \) | \( bm \)  | No              |
| **Depth-Limited** | No      | \( b^l \) | \( bl \)  | No              |
| **Iterative Deepening** | Yes | \( b^d \) | \( bd \)  | Yes (cost=1)    |