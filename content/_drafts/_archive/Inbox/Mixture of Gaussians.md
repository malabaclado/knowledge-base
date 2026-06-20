---
tags: null
alias: null
creation-date: Tuesday 23rd August 2022
last-modified-date: Tuesday 23rd August 2022 10:23:04
---

# Mixture of Gaussians
The Gaussian mixture distribution can be written as a linear superposition of Gaussians in the form $$p(\text{x}) = \sum_{k=1}^{K}\pi_{k}\mathcal{N}(\text{x}|\mu_{k}, \Sigma_{k})$$

Let's introduce a K-dimensional binary random variable $\text{z}$ having a 1-of-K representation in which a particular element $z_{k}$ is equal to 1 and all other elements are equal to 0. 


> [!NOTE] Remark
> 	Note that the values of $z_{k}$ satisfy $z_{k} \in \{0,1\}$ and $\sum_{k} z_{k}=1$


Define the joint distribution $p(\text{x}, \text{z})$ in terms of the marginal distribution $p(\text{z})$ and conditional distribution $p(\text{x}| \text{z})$.

The marginal distribution over $\text{z}$ is specified in terms of the mxing coefficient $\pi_{k}$ such that $$p(z_{k}=1)=\pi_{k}$$ where the parameters $\{\pi_{k}\}$ must satisfy:
1. $0\leq \pi_{k} \leq 1$
2. $\sum_{k=1}^{K}\pi_{k}=1$

This conditions show that the marginal distribution is a valid probability. 

Because $\text{z}$ uses a 1-of-K representation, we can also write this distribution in the form: $$p(\text{z}) = \prod_{k=1}^{K} \pi_{k}^{z_{k}}$$

The conditional distribution of $\text{x}$ given a particular value for $\text{z}$ is a Gaussian $$p(\text{x}|z_{k}=1) = \mathcal{N}(\text{x}|\mu_{k}, \Sigma_{k})$$ which can also be written in  the form $$p(\text{x}| \text{z}) = \prod_{k=1}^{K} \mathcal{N}(\text{x}| \mu_{k}, \Sigma_{k})$$

