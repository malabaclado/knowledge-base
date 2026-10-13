---
tags: molecule
alias: null
creation-date: Friday 29th July 2022
last-modified-date: Friday 29th July 2022 20:22:07
---

# Basic Polynomial Curve Fitting

The goal of polynomial curve fitting is to fit a dataset to a polynomial function in the form of:
$$y(x,w) = w_{0}+ w_{1}x + w_{2}x^{2}+...+w_{M}x^{M} = \sum^{M}_{j=0} w_{j}x^{j} $$
To do this, we minimize the error function (usually sum of squares):
$$E(w) = \frac{1}{2} \sum^{N}_{n=1} \{y(x_{n},w) - t_{n}\}$$

![[Pasted image 20220730115927.png]]
