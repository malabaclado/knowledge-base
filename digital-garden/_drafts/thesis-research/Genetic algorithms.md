---
tags:
alias:
creation-date: Tuesday 17th January 2023
last-modified-date: Tuesday 17th January 2023 14:52:24
---

# Genetic algorithms
Genetic algorithms borrow inspiration from biological evolution, where fitter individuals are more likely to pass on their genes to the next generation. 

**Fitness**
An individual's fitness for reproduction is inversely related to the value of the objective function at that point. 

**Chromosome**
The design point associated with an individual is represented as a *chromosome*. At each generation, the chromosomes of the fitter individuals are passed on to the next generation after undergoing the genetic operations of crossover and mutation.

There are several ways to represent chromosomes. The simplest is the *binary string chromosome*, a representation that is similar to the way DNA is encoded. (Eg. A random binary string of length *d*) 

Sometimes, the binary string might not represent a valid point in the design space. Another representation uses real values. Such *real-valued chromosomes* are vectors in $\mathbb{R}^d$  that directly corresponds to points in the design space. 

## Steps in Genetic Algorithm

1. Initialization - initialize chromosomes at random positions in the search space
2. Selection 
	- This is the process of choosing whch chromosomes to use as parents for the next generation. 
	- There are multiple ways to approach this: 
		- *truncation selection* - choose parents from the best *k* chromosomes in the population
		- *tournament selection* - select the fittest out of k randomly chosen chromosomes in the population 
		- *roulette wheel selection* - each parent is chosen with a probability proportional to its performance relative to the population.
3. Crossovers 
	- Crossover combines chromosomes of parents to form children.
	- If new chromosomes were produced only through crossover, many traits that were not present in the initial random population  could never occur, and the most-fit would saturate the population.




