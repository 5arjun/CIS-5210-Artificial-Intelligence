---
title: "AI Essentials: Tree Search vs Graph Search"
date: 2026-02-02
tags: [Search-Algorithms, Tree-Search, Graph-Search, Search-Problems, AI-Essentials]
confidence: 0.82
source: handwritten
---

## Tree Search

Tree search enumerates in some order all possible paths from the initial state.

- **Root** = initial state
- Nodes in search tree generated through **transition model**
- Treats different paths to same node as distinct

## Problem: Repeated States

Failure to detect repeated states can turn a linear problem into exponential.

## Graph Search

Simple modification from tree search: Check to see if a node has been visited before adding to search queue.

- Must keep track of all possible states (can use a lot of memory)

## Graph vs Tree Pseudocode

**Underlined code is only for graph search.**

```
function GRAPH/TREE-SEARCH(problem) returns a solution, or failure
    initialize the frontier using the initial state of problem
    initialize the explored set to be empty
    loop do
        if the frontier is empty then
            return failure
        choose a leaf node and remove it from frontier
        if the node contains a goal state then
            return the corresponding solution
        add the node to the explored set
        expand the chosen node, adding the resulting nodes to the frontier
            only if not in frontier or explored set
```

## TODO Items

- No explicit TODO items identified in the notes.