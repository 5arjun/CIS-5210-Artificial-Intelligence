---
title: "AI Fundamentals: Task Environments and PEAS Framework"
date: 2026-01-26
tags: [AI, Task-Environments, PEAS, Rational-Agents, Environments]
confidence: 0.79
source: handwritten
---

## Task Environment Definition

A **task environment** is the problem specification for which the agent is a solution.

### PEAS Framework
- **P**: Performance measure
- **E**: Environment
- **A**: Actuators
- **S**: Sensors

**Example: Automated taxi driver**
- **P**: Safe, legal, maximize profits
- **E**: Roads, traffic, pedestrians, customers
- **A**: Steering, accelerator, brakes, signals
- **S**: Cameras, LiDAR, speedometer, GPS

## Properties of Task Environments

### Observability
- **Fully Observable**: Task agent's sensors can detect all aspects of the environment relevant to the agent's choice of action.  
  *Ex: Chess*
- **Partially Observable**: Access only to information they can perceive with their sensors.  
  *Ex: Self-driving car*

### Determinism
- **Deterministic**: When an agent picks its action, the immediate result is known with certainty.
- **Non-deterministic**: Agent can pick an action, but the outcome is uncertain (multiple possible states).  
  *Ex: Games with chance*
- **Stochastic**: Probabilistic; quantifies likelihood of each possible outcome.

### Decision Structure
- **Episodic**: Agent processes self-contained episodes. Perception leads to action; choice independent of previous actions.
- **Sequential**: Current decision affects future decisions. Agent may need to predict multiple future actions to find the most desirable one.

### Dynamics
- **Static**: Environment unchanged while agent makes decision.  
  *Ex: Crossword*
- **Dynamic**: Environment changes while agent is thinking.  
  *Ex: Self-driving car*

### State and Action Space
- **Discrete**: Environment represented by discrete number of distinct states; limited number of defined actions.
- **Continuous**: Requires consideration of state representation or time handling.

### Agent Count
- **Single Agent**: Only one agent solving the problem.  
  *Ex: Crossword*
- **Multi-Agent**: Environment deterministic except for actions of other agents. In competitive settings, design strategies against opponents.  
  *Ex: Chess*