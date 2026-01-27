---
title: "AI Essentials: Task Environments and PEAS Framework"
date: 2026-01-26
tags: [AI, Task-Environments, PEAS, Rational-Agents, Environments]
confidence: 0.85
source: handwritten
---

## Task Environment

A **task environment** is the problem specification for which the agent is designed.

### PEAS Framework
- **P**: Performance measure
- **E**: Environment
- **A**: Actuators
- **S**: Sensors

**Example: Automated Taxi Driver**
- **P**: Safe, legal, maximize profits
- **E**: Roads, traffic, pedestrians, customers
- **A**: Steering, accelerator, brakes, signals
- **S**: Cameras, LiDAR, speedometer, GPS

## Properties of Task Environments

### Observability
- **Fully Observable**: Task agent's sensors can detect all aspects of the environment relevant to the agent's choice of action.  
  *Example: Chess*
- **Partially Observable**: Access only to information they can perceive with their senses.  
  *Example: Self-driving car*

### Determinism
- **Deterministic**: When an agent picks its action, the immediate result is known with certainty.
- **Non-deterministic**: Agent picks an action, but outcome is uncertain (multiple possible states).  
  *Example: Games with chance*
- **Stochastic**: Probabilistic; quantifies likelihood of each possible outcome.

### Task Type
- **Episodic**: Agent processes self-contained episodes. Perception leads to action; choice independent of previous actions.
- **Sequential**: Current decision affects all future decisions. Agent may need to predict multiple future actions to find the most desirable one.