---
tags:
alias:
creation-date: Wednesday 31st August 2022
last-modified-date: Wednesday 31st August 2022 14:55:14
---

Suppose we have a set of observations $\{\text{x}_1,\text{x}_2,...,\text{x}_{N}\}$ that we wish to model using a mixture of Gaussians. We'll represent this data set as an $N\times D$ dimensional matrix $X$ whose nth row is given by $\text{x}_n^T$ 

Let $Z$ be a $N\times K$ dimensional matrix corresponding to the latent variables. 

We assume that the data points are drawn independently from the distribution.

The log-likelihood function is given by: $$\ln \mathcal{L}(X|\pi, \mu, \Sigma)= \sum_{n=1}^{N} \{\sum_{k=1}^{K} \pi_{k}\mathcal{N}(\text{x}_{n}|\mu_{k}, \Sigma_{k}) \}$$
Maximizing the log likelihood function for a [[Gaussian Mixture Model]] turns out to be a complicated problem. We'll solve this problem using a numerical method known as the EM algorithm.

**EM for Gaussian Mixtures**
1. Choose the initial values for means, covariances and mixing coeffiicients. 
2. **E-step.** Use the current values to evaluate the posterior probabilities (or responsibilities)
3. **M-step** Use the responsibilities to re-estimate the means, covariances and mixng coefficients. 

Each step that update the parameters resulting from an E-step, followed by an M-step is guaranteed to increase the log likelihood function. The algorithm is deemed to have converge when he change in the log likelihood function (or alternatively in the parameters), falls below some threshold. 