---
title: "AI Essentials: Rational Agents"
date: 2026-01-26
tags: [AI, Rational Agents, Agents, Performance Measure, Rational Behavior]
confidence: 0.85
source: handwritten
---

## Agent Definition

An **agent** is something that can **perceive its environment** and **act on it**.

- **Sensors**: Receive percepts (e.g., eyes, ears).
- **Actuators**: Perform actions (e.g., hands, mouth).
- **Percept**: Signal received from sensors.

Example: Humans.

## Agent Function and Program

- **Agent function**: Maps a sequence of percepts to a sequence of actions.
- **Agent program**: Runs on physical architecture to produce the agent function.

## Rational Behavior

A **rational agent** behaves to **do the right thing** based on **consequentialism**—evaluating behavior by its **consequences**[1].

- In economics, **rational choice theory**: Individuals make decisions based on available information (cannot be omniscient).
- Social behaviors emerge from self-interested individual decisions.
- Individuals pick the most desirable alternative.

**Computational limitations** make complete rationality unachievable.

## Performance Measure

**Performance measure**: Criteria for success of an agent's behavior; gives a score based on consequences.

### Example: Roomba
| Objective | Score |
|-----------|-------|
| Each clean square at time \( T \) | +1 point |
| Each move | -1 point (reduce # of moves) |
| More than \( k \) dirty squares | -1000 points |

**Design performance measures** for desired outcomes, not how the agent should behave.

## Rational Agent Decision Process

For each possible percept sequence, a rational agent selects action \( a \) that **maximizes the expected value** of its performance measure (doesn't need to know actual outcome).