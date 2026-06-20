---
tags: 
alias: 
creation-date: Sunday 10th July 2022
last-modified-date: Sunday 10th July 2022 15:20:18
---



Support vector regression is the application of SVM to regression tasks.

Unlike the linear regression, whose objective function minimizes the mean squared error, the objective function of SVR is to minimize the coefficients - specifically the L2 norm of the coefficient vector. 

## SVR in simple terms
1. 


---
## Simple SVR

The objective function of support vector regression:
$$\text{min} \frac{1}{2} ||w||^{2}$$
subject to the constraint: $|y_{i} - w_{i}x_{i} \leq \epsilon|$

![[Pasted image 20220710155702.png]]

## SVR with slack variables

Objective function with slack variable:
$$\text{min} \frac{1}{2}||w||^{2} + C \sum_{i=1}^{n}|\xi_{i}|$$
subject to: $|y_{i}- w_{i}x_{i}| \leq \epsilon  + |\xi_{i}|$

![[Pasted image 20220710155637.png]]