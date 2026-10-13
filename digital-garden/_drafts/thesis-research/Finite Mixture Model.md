---
tags:
alias:
creation-date: Thursday 1st September 2022
last-modified-date: Thursday 1st September 2022 13:58:17
---

- # Finite Mixture Model
  We say that a d-dimensional random variable $X$ follows a $K$-components mixture if its probability function can be written in the following form: $$p(X|\Theta)= \sum_{k=1}^{K}\pi_{k} p(X|\theta^{(k)})$$where $\theta^{(k)}$ is the set of parameters of  the distribution corresponding to component $k$, $\pi_{k}$ are the mixing coefficients which satisfy $0\leq \pi_{k}\leq 1$ for all $k$, and $\sum_{k} \pi_{k}=1$. Whereas $\Theta$ denotes the complete set of parameters fully characterizing the mixture.