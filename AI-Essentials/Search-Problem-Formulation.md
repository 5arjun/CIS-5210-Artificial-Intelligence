---
title: "AI Essentials: Search Problem Formulation"
date: 2026-02-02
tags: [Search-Problems, AI-Essentials, State-Space, Vacuum-World, Abstraction]
confidence: 0.85
source: handwritten
---

## Search Problem Definition

1. **States**: a set \( S \)
2. **An Initial State**: \( s_I \in S \)
3. **Actions**: a set \( A \)
4. **Transition Model**:  
   - Set of possible actions from any state. Given a state, which actions can we take?  
   - Result of applying an action from the state to another.
5. **Path Cost** (Performance measure): whether one path costs more than another.
6. **Goal Test**: Goal (\( s_G \))

## Example: Vacuum World

## Solution

- Sequence of actions from initial state to goal state.
- **Optimal Solution**: A solution is optimal if no solution has a lower path cost.

Real world is absurdly complex. State space must be abstracted for problem solving.

- **(Abstract) State** = set (equivalence class) of real world states.
- **(Abstract) Action** = equivalence class of combinations of real world actions.

Abstraction is valid if path between 2 states is reflected in real world.

## Useful Concepts

- **State Space** = set of all states reachable from initial state by any sequence of actions.
- **Path** = sequence of actions leading from one state \( s_i \) to another \( s_k \).
- **Frontier** = those states that are available to expand.
- **Solution** = path from initial state \( s_i \) to \( s_f \) that satisfies goal state.