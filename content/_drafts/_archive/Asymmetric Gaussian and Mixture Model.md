---
tags:
alias:
creation-date: Thursday 8th September 2022
last-modified-date: Thursday 8th September 2022 08:42:11
---

# Asymmetric Gaussian and Mixture Model

## Asymmetric Gaussian Distribution 
Let $z$ be a random variable. We say $z$ has Asymmetric Gaussian distribution if its probability density function $p(z)$ follows $$ p(z)= \mathcal{A}(z; \mu, \sigma^{2}, r) = \frac{2}{\sqrt{2\pi}} \frac{1}{\sqrt{\sigma^{2}}(r+1)} \begin{cases}
\exp(- \frac{(z - \mu)^{2}}{2\sigma^{2}}) \quad &, \text{if } z>\mu  \\
\exp(\frac{(z-\mu)^{2}}{2r\sigma^{2}}) \quad &, \text{otherwise}
\end{cases}$$ where $\mu$ is the mean, $\sigma^2$ is the variance and $r$ is the asymmetric component. We call the distribution 'univariate asymmetric Gaussian' (UAG). We note that UAG is an extension of the Gaussian distribution with asymmetric component and we can see that the UAG with $r=1$ is exactly the Gaussian distribution. 

![[Pasted image 20220908093002.png]]

The asymmetric component $r$ denotes the amount of *slant* or asymmetry of the distribution in the left side of the mean as illustrated in the picture. (Photo from [[katoAsymmetricGaussianIts2002]]). 


## Asymmetric Gaussian Mixture Model
Now, we'll define the Asymmetric [[Gaussian Mixture Model]] using the finite mixture model. 