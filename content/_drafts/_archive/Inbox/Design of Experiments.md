---
tags:
  - design-of-experiments
aliases: 
creation-date: Wednesday 13th September 2023
---

Design of experiment is a systematic way of finding an answer to a question.

1. Formulate a question (Research question/Hypothesis)
2. Find the appropriate method/design
3. Analyze and produce the results
4. Make a contextual conclusion (explain the results in the context of the experiment)

# Concepts in DOE
## **Fixed Factor**
Consider the problem of testing a new fertilizer. So we have:
- Factor: Fertilizer
- Levels: 2 (New and Old Fertilizer)
If we have a fixed number of levels, then we call the factor a **Fixed Factor.** Here, the *Fertilizer* is a fixed factor.

In fixed factor ANOVA, we compare means.

## **Random Factor**
Suppose we want to test a new fertilizer on 40 different states. It is impractical to actually do the experiment on all states and compare them pairwise. Instead, it is more convenient to pick just a handful of states, say 3. Then we have:
- Factor: States
- Factor(*States*) level: 3 (State 1, State 2, State 3) *Note that states are picked randomly.*
Since the states are randomly picked, then we call the factor *States* a **Random Factor**.

In random factor ANOVA, we compare variances.

