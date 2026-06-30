# Scoring Rubric

## Overview

This benchmark evaluates the mathematical reasoning performance of Large Language Models (LLMs) using a standardized four-point scoring rubric. Rather than assessing only the final answer, the evaluation considers three independent dimensions:

- **Correctness** – Whether the final answer matches the verified solution.
- **Reasoning Quality** – The logical coherence, clarity, and completeness of the step-by-step reasoning.
- **Programming Correctness / Mathematical Procedure Correctness** – Whether the mathematical procedure, formulas, and solution approach are valid, regardless of the final answer.

This rubric was applied consistently across all evaluated models and benchmark questions to ensure fairness, transparency, and reproducibility.

---

## Scoring Criteria

| Score | Correctness | Reasoning Quality | Programming Correctness |
|------:|-------------|-------------------|---------------------------------------------------------------|
| **0** | Completely incorrect | No meaningful reasoning | Completely invalid solution procedure |
| **1** | Partially correct | Weak reasoning | Significant errors in the mathematical procedure |
| **2** | Mostly correct | Adequate reasoning | Generally valid procedure with minor issues |
| **3** | Fully correct | Strong reasoning | Fully valid and mathematically sound solution procedure |

---

## Evaluation Principle

Each response was independently evaluated across all three dimensions. A response was **not** judged solely on whether the final answer was correct. Models could receive partial credit for demonstrating sound mathematical reasoning or a correct solution procedure even when the final numerical answer was incorrect.

This evaluation framework provides a more comprehensive assessment of mathematical reasoning than traditional accuracy-based evaluation alone.
