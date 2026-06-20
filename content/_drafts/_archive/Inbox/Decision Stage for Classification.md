---
tags: type/concept
alias: null
creation-date: Friday 29th July 2022
last-modified-date: Friday 29th July 2022 20:02:29
---

# Decision Stage for Classification


## Two-Stage Process
1. *inference stage*
	->using the training data, learn a model for the posterior probabilities $p(C_k|\textbf{x})$
2. *decision stage*
	-> make optimal class assignments based on posterior probabilities
	
	
==Note that the optimal class is based on posterior probabilities.==
	


## Three Approaches to Making Decision (Classification)
*Approach A*: First solve the inference problem of determining the class-conditional densities $p(\textbf{x},|C_k)$ for each $C_k$, infer prior class probabilities $p(C_k)$. Use Bayes' theorem to find the posterior class probabilities $p(C_k|\textbf{x})$. Having posterior class probablities, use decision theory to determine class membership.


*Approach B*: Discriminative models. Solve the inference problem of determining posterior class probabilities $p(C_k|\textbf{x})$ then use decision theory to assign each new $\textbf{x}$ to a new class.

*Approach C*: Find a function $f(\textbf{x})$ that maps each new input $\textbf{x}$ to a class label.

Notes:
- Approach A is computationaly demanding and needs a lot of data.
- Approach B just does the job well.
- Approach C is the most simple - if you only want to classify.

However, there are instances when you want to determine the posterior class probabilities of your data. 
