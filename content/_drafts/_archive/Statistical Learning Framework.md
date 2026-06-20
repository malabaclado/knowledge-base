---
tags:
alias:
creation-date: Wednesday 1st February 2023
last-modified-date: Wednesday 1st February 2023 11:16:06
---



# The learner's input
- Domain set $\mathcal{X}$ : The set of objects that we with to label.
- Label set $\mathcal{Y}$: The set containing the labels for the domain set.
- Training data $S=((x_{1}, y_{1}), ..., (x_{m}, y_{m}))$ : a finite sequence of pairs in $\mathcal{X} \times \mathcal{Y}$ ; a sequence of labeled domain points. Also called the *training set*.

# The learner's output 
The learner outputs a *prediction rule* $h: \mathcal{X} \to \mathcal{Y}$. This function is also called the *predictor*, or a *hypothesis*.


> [!NOTE] Notation
> We use the notation $A(S)$ to denote the hypothesis that a learning algorithm $A$ returns upon receiving the training sequence $S$. 
















