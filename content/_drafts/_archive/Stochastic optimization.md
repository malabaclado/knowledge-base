---
tags:
alias:
creation-date: Thursday 5th January 2023
last-modified-date: Thursday 5th January 2023 15:48:01
---


# Stochastic optimization

**Stochastic optimization** refers to the use of randomness in the objective function or in the optimization algorithm.

Randomness in the algorithm is used as a strategy, e.g. stochastic or probabilistic decisions. It is used as an alternative to deterministic decisions in an effort to improve the likelihood of locating the global optima or a better local optima.

> Standard stochastic optimization methods are brittle, sensitive to stepsize choice and other algorithmic parameters, and they exhibit instability outside of well-behaved families of objectives.

— Page xiii, [Introduction to Stochastic Search and Optimization](https://amzn.to/34JYN7m), 2003.

Deterministic algorithms may get stuck in local optimums especially on non-linear response surfaces. 

Using randomness in an optimization algorithm allows the search procedure to perform well on challenging optimization problems that may have a nonlinear response surface. This is achieved by the algorithm taking locally suboptimal steps or moves in the search space that allow it to escape local optima.

The randomness used in a stochastic optimization algorithm does not have to be true randomness; instead, pseudorandom is sufficient. A [pseudorandom number generator](https://machinelearningmastery.com/introduction-to-random-number-generators-for-machine-learning/) is almost universally used in stochastic optimization.

## Examples of stochastic optimization algorithms
-   Iterated Local Search
-   Stochastic Hill Climbing
-   Stochastic Gradient Descent
-   Tabu Search
-   Greedy Randomized Adaptive Search Procedure

## Examples of stochastic optimization algorithms inspired by biological/physical processes:

-   Simulated Annealing
-   Evolution Strategies
-   Genetic Algorithm
-   Differential Evolution
-   Particle Swarm Optimization

## Practical considerations for stochastic optimization
- The stochastic nature of the procedure means that any single run of the algorithm will be different. Different source of randomness and decisions made during the search. (In a way, we can say each run cannot be replicated?)
- The pseudorandom number generator used as the source of randomness can be seeded to ensure the same sequence of random numbers is provided each run of the algorithm.
- A given algorithm can be executed many times to control for the randomness of the procedure.
- Any single run of a chosen optimization algorithm alone does not meaningfully represent the global optima of the objective function. Instead, a strategy of repeated evaluation should be used to develop a distribution of optimal solutions.
- The repeated application of a stochastic optimization algorithm on an objective function is sometimes referred to as a **multi-restart strategy** and may be built in to the optimization algorithm itself or prescribed more generally as a procedure around the chosen stochastic optimization algorithm.

---
[A Gentle Introduction to Stochastic Optimization Algorithms - MachineLearningMastery.com](https://machinelearningmastery.com/stochastic-optimization-for-machine-learning/)
