---
tags: type/concept 
alias: concentration matrix
creation-date: Tuesday 2nd August 2022
last-modified-date: Tuesday 2nd August 2022 09:39:25
---

# Precision matrix
The **precision matrix** of a random vector is the inverse of its [[covariance matrix]].

The precision matrix is sometimes called **concentration matrix**.

> [!NOTE] Formal Definition
> Let $\text{X}$ be a $\text{K} \times 1$ random vector. Let $\text{V}$ be its covariance matrix:
$$Var[\text{X}] = V$$
> 
> If $V$ is invertible, then the precision matrix of $X$ is the $K \times K$ matrix $H$, defined as:
> $$H = V^{-1}$$
> 
> 

In the univariate case: **precision is inversely proportional to variance**: when variance tends to infinity, we have zero precision; on the contrary, when variance tends to zero, we have infinite precision.

The joint probability density function of a multivariate normal random vector is often written in terms of its precision matrix.