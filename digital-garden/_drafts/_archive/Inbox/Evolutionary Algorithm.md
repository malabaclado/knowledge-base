---
tags:
alias:
creation-date: Friday 12th May 2023
---

In [[computational intelligence]], an evolutionary algorithm is a subset of evolutionary computation, a generic population-based metaheuristic optimization algorithm. 

An evolutionary algorithm uses mechanisms inspired by biological evolution, such as reproduction, mutation, recombination, and selection. Candidate solutions to the optimization problem play the role of individuals in a population, and the fitness function determines the quality of the solutions (see also loss function). Evolution of the population then takes place after the repeated application of the above operators.

Evolutionary algorithms perform well because they do not make any assumption to the fitness landscape (or the search space).

In most real applications of EAs, [[computational complexity]] is a prohibiting factor. This is due to repeated fitness function evaluation. 


# Types of Evolutionary Algorithms 
- [[Genetic algorithms]] - This is the most popular type of EA. One seeks the solution of a problem in the form of strings of numbers by applying operators such as recombination and mutation (sometimes one, sometimes both). 
- Genetic programming - Here the solutions are in the form of computer programs, and their fitness is determined by their ability to solve a computational problem.
	- Examples include: Cartesian genetic programming, gene expression programming, grammatical evolution, linear genetic programming, multi expression programming etc.

# Theoretical Background
These theoretical principles apply to almost all evolutionary algorithms. 
- [[No free lunch theorem]]
- [[Convergence]]
- Virtual Alphabets

# Related Techniques
- Swarm algorithms such as
	- Ant colony optimization - based on the ideas of ant foraging by pheromone communication to form paths.
	- Runner-root Algorithm - inspired by the function of runners and roots of plants in nature.
	- Artificial bee colony algorithm - based on the honeybee foraging behaviour. Primarily proposed for numerical optimization and extended to solve combinatorial, constrained and multi-objective optimization problems.
	- Bees algorithm - based on the foraging behaviour of honeybees. It has been applied in many applications such as routing and scheduling.
	- Cuckoo Search - inspired by the brooding parasitism of the cuckoo species. It also uses Lévy flights, and thus it suits for global optimization problems.
	- Particle Swarm Optimization - based on the ideas of animal flocking behaviour.


---
- [Evolutionary algorithm - Wikipedia](https://en.wikipedia.org/wiki/Evolutionary_algorithm)