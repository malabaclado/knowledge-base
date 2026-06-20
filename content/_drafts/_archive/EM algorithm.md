---
tags:
alias:
creation-date: Thursday 1st September 2022
last-modified-date: Thursday 1st September 2022 14:24:01
---

# EM algorithm
The goal of the EM algorithm is to find the maximum likelihood solutions for models having latent variables. 

***Why use expectation?*** (Further reading:[[📕 Pattern Recognition and Machine Learning (Bishop)]] Section 9.4)

Denote the set of all observed data by $X$, where the $n$th row represents $\text{x}_{n}^T$. Similarly, denote the set of all latent variables by $Z$, with a corresponding row $\text{z}_{n}^{T}$

The set of all model parameters is denoted by $\theta$ and so the likelihood function is given by: $$\ln p(X|\theta)=\ln \{\sum_{Z} p(X,Z|\theta)\}$$
Note that the summation over the latent variables appears inside the logarithm. The presence of the sum prevents the logarithm from acting directly on the joint distribution which results in complicated expression for the maximum likelihood. 

Suppose that for each observation in $X$, we were told the corresponding value of the latent variable $Z$, such as knowning the class labels of data points in a classification problem. We shall call $\{X,Z\}$ the complete data set and we shall refer to the actual observed data $X$ as incomplete. 

Given the complete data set $\{X,Z\}$, the likelihood function simply takes the form $\ln p(X,Z|\theta)$. However, in practice, we are only given the incomplete data set $X$. The EM algorithm is a numerical method for estimating the parameters that maximizes the complete-data log likelihood function. 

**The EM algorithm**  (Bishop, p. 441)
In the E step, we use the current parameter $\theta^\text{old}$ to find the posterior distribution of the latent variables given by $p(Z|X, \theta^\text{old})$ . Then, we use this posterior distribution to find the expectation of the complete-data log likelihood, denoted by $\mathcal{Q}(\theta, \theta^\text{old})$ evaluated for some parameter value $\theta$. 

In the M step, we determine the revised parameter estimate $\theta^{\text{new}}$ by maximizing this function. $$\theta^{\text{new}} = \arg \max_{\theta} \mathcal{Q}(\theta,\theta^{\text{old}})$$ 
In each step, we are increasing the complete-data log likelihood. The algorithm converges when the increase in the expectation of the complete-data log likelihood $\mathcal{Q}(\theta, \theta^\text{old})$ passes below a certain threshold or when the increase in the parameter passes below a certain threshold. 

***Proof of convergence of EM algorithm***
