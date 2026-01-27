---
title: "AI Essentials: Task Environments (PEAS and Properties)"
date: 2026-01-26
tags: [AI, Task-Environments, PEAS, Rational-Agents, Environments]
confidence: 0.87
source: handwritten
---

## Task Environment Definition

A **task environment** is the problem specification for which the agent is a solution.

### PEAS Framework
- **P**erformance measure
- **E**nvironment
- **A**ctuators
- **S**ensors

**Example: Automated Taxi Driver**
- **P**: Safe, legal, maximize profits
- **E**: Roads, traffic, pedestrians, customers
- **A**: Steering, accelerator, brakes, signals
- **S**: Cameras, LiDAR, speedometer, GPS

## Properties of Task Environments

### Observability
- **Fully Observable**: Task agent's sensors can detect all aspects of the environment relevant to the agent's choice of action.  
  *Example*: Chess
- **Partially Observable**: Access only to info they can perceive with their senses.  
  *Example*: Self-driving car

### Determinism
- **Deterministic**: When an agent picks its action, the immediate result is known with certainty.
- **Non-deterministic**: Agent can pick an action, but the outcome is uncertain (multiple states of the environment after executing that action).  
  *Example*: Games with chance
- **Stochastic**: Probabilistic; quantify how likely each possible outcome is.

### Episodic vs. Sequential
- **Episodic**: Agent processes self-contained episodes. Perceives, then makes action choice; choice of action is not dependent on any previous action.
- **Sequential**: Current decision affects all future decisions. Agent may need to predict multiple actions in the future to find the most desirable one.

### Static vs. Dynamic
- **Static**: Unchanged while agent makes decision.  
  *Example*: Crossword
- **Dynamic**: Environment changes while agent is thinking.  
  *Example*: Self-driving car

### Discrete vs. Continuous
- **Discrete**: Environment represented using a discrete number of distinct states.  
  - Limited number of defined actions
- **Continuous**: Need to think about state representation of environment or way we handle time.

### Agent Type
- **Single Agent**: Only one agent trying to come up with the solution.  
  *Example*: Crossword
- **Multi Agent**: Environment is deterministic except for actions of another agent. In competitive multi-agent environments, design strategies for playing against other agents.  
  *Example*: Chess