---
tags: chapter
alias: null
creation-date: Thursday 4th August 2022
last-modified-date: Thursday 4th August 2022 14:34:44
---

# Maximum likelihood for the Gaussian
Given a dataset in which the observations $\{\text{x}_{n}\}$ are assumed to be drawn independently from a multivariate [[Gaussian Distribution]]. We estimate the parameters by maximum likelihood. 

The log-lilkelihood function is given by:
![[Pasted image 20220804143804.png]]

Using the derivative of log-likelihood wrt mean $\mu$:
![[Pasted image 20220804144010.png]]

and setting this derivative to zero, we obtain the solution for the maximum likelihood estimate of the mean given by: 
![[Pasted image 20220804144104.png]]



Using the same method, the maximum likelihood estimate for the covariance is:
![[Pasted image 20220804144157.png]]

---
Note: We see that the expectation of the maximum likelihood estimate for the mean is equal to the true mean. However, the maximum likelihood estimate for the covariance has an expectation that is less than the true value, and hence it is biased.

![[Pasted image 20220804144319.png]]

---
[[📕 Pattern Recognition and Machine Learning (Bishop) 1]]