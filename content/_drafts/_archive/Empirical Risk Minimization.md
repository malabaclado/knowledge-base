---
tags: type/concept 
alias:
creation-date: Friday 2nd December 2022
last-modified-date: Wednesday 1st February 2023 10:33:16
---

Empirical Risk Minimization refers to the method of minimizing the *empirical error* (aka empirical risk). The empirical error is the error that the predictor makes based on the training set.

>  The empirical error is also sometimes called the generalization error. The reason is that actually, in most problems, we don’t have access to the whole domain **_X_** of inputs, but only our training subset **_S_**. We want to generalize based on **_S_**, also called inductive learning. This error is also called the **risk,** hence the term risk in empirical risk minimization. If this reminded you of mini-batch gradient descent, you would be correct. This concept is basically ubiquitous in modern machine learning.
>  
>  -[Learning Theory: Empirical Risk Minimization - TDS](https://towardsdatascience.com/learning-theory-empirical-risk-minimization-d3573f90ff77)


ERM is very prone to [[overfitting]]. A common solution to the problem of overfitting is to apply the ERM learning rule over a restricted search space. However, this might cause the model to have stronger bias. 

The bias-complexity trade off is an active interest in machine learning.
