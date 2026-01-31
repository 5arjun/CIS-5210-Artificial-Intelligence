---
title: "AI Essentials: Reflex Agents, Problem Solving, and Task Environments"
date: 2026-01-31
tags: [AI-Agents, Search-Problems, Task-Environments, Reflex-Agents, Problem-Solving]
confidence: 0.88
source: handwritten
---

## AI Essentials / Search Problems

### Reflex Agent
- Selects action based on **current percept** (ignores percept history)
- Reacts to immediate surroundings and **does not plan ahead**

### Problem Solving Agent
- Has a **goal** and must plan a sequence of actions to achieve it
- Process of planning a sequence of actions is called **search**

## Impact of Task Environments

Properties of **task environments** change the type of solution needed.

### Example Comparison

| Environment Properties | Solution Type |
|------------------------|---------------|
| **Fully observable**<br>**Deterministic**<br>**Known environment** | Fixed sequence of actions |
| **Partially observable**<br>**OR**<br>**Nondeterministic** | Must recommend different future actions depending on percepts<br>Could be in the form of a **branching strategy** |

## Steps for Problem Solving

1. **Formulate a goal**
2. **Formulate a search problem** (states, actions, performance measure)
3. **Find the solution**