# LLM Output Arbitration System

Multi-agent AI workflow that generates answers, critiques them from multiple perspectives, and produces a final quality verdict.

## Overview

This project demonstrates agent orchestration using OpenAI, LangGraph, structured outputs, and arbitration logic.

A generator agent creates an answer.

Three critic agents evaluate:

- Factual accuracy
- Logical consistency
- Completeness

An arbitrator agent combines the scores and determines whether the answer should be approved, revised, or rejected.

---

## Architecture

```text
START
  ↓
Generator Agent
  ↓
Factual Critic
  ↓
Logic Critic
  ↓
Completeness Critic
  ↓
Arbitrator
  ↓
END
```

---

## Features

- OpenAI API integration
- Multi-agent architecture
- LangGraph workflow prototype
- Pydantic structured outputs
- Memory storage
- Arbitration engine
- Modular agent design

---

## Example

Question:

```text
What is the capital of Canada?
```

Generated Answer:

```text
The capital of Canada is Ottawa.
```

Critiques:

```json
[
  {
    "agent": "factual_critic",
    "score": 8
  },
  {
    "agent": "logic_critic",
    "score": 7
  },
  {
    "agent": "completeness_critic",
    "score": 6
  }
]
```

Final Verdict:

```json
{
  "average_score": 7.0,
  "verdict": "needs_revision"
}
```

---

## Tech Stack

- Python
- OpenAI API
- LangGraph
- Pydantic
- GitHub

---

## Learning Objectives

This project demonstrates:

- Agent orchestration
- Agent evaluation
- LLM quality assurance
- Structured AI outputs
- Workflow design
- Memory integration

---

## Future Improvements

- Full LangGraph orchestration
- Persistent memory database
- Human-in-the-loop review
- Parallel critic execution
- Dashboard visualization
