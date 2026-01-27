---
title: "AI Essentials: Task Environments"
date: 2026-01-26
tags: [AI, Task-Environments, Rational-Agents, PEAS, Multi-Agent]
confidence: 0.76
source: handwritten
---

## AI Essentials / Task Environments (2/2)

### Properties of Task Environments

#### b) Partially Observable vs Fully Observable
- **Fully Observable (LA)**: Environment is unchanged while agent makes decision.  
  *Example*: Crossword puzzle
- **Partially Observable**: Environment changes while agent is thinking.  
  *Example*: Self-driving car

#### Discrete vs Continuous
- **Discrete**: Environment can be represented using a discrete number of distinct states, limited number of defined actions.  
  *Example*: Crossword puzzle (one agent solving)
- **Continuous**: Need to think about state representation of environment or way we handle time.

#### Single Agent vs Multi-Agent
- **Single Agent**: Only one agent is trying to come up with the solution.  
  *Example*: Crossword puzzle
- **Multi-Agent**: Environment is deterministic except for actions of another agent. In competitive multi-agent environments, design strategies for playing against other agents.  
  *Example*: Chess