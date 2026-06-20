---
tags: [thesis]
alias:
creation-date: Tuesday 30th August 2022
last-modified-date: Tuesday 30th August 2022 11:22:09
---

# Latent Variable Model of the Gaussian Mixture Model
Here we show that the [[Gaussian Mixture Model]] can be formulated with an explicit latent variable. 


> [!NOTE] Recall
> Recall that the [[Gaussian mixture distribution]] can be written as a linear superposition of Gaussians and has the form: $$p(\text{x})=\sum_{k=1}^{K}\pi_{k}\mathcal{N}(\text{x} | \mu_k,\Sigma_{k})$$

Let's introduce a *K-dimensional binary random variable* $\text{z}$ having a 1-of-K representation in which a particular element $z_k$ is equal to one and the rest are equal to zero. 


> [!NOTE] Example 
> $$\text{z} = [0,0,0,1,0,0,0]$$

> [!NOTE] Remarks
> - The values $z_{k}$ satisfy $z_{k}\in \{0,1\}$ and $\sum_{k}z_{k}=1$.
> - There are $K$ possible states for vector $\text{z}$ depending on which element is non-zero. 

We shall define the joint distribution $p(\text{x}, \text{z})$ in terms of the marginal distribution $p(\text{z})$ and the conditional distribution $p(\text{x}|\text{z})$ : $$p(\text{x}, \text{z})= p(\text{z})  p(\text{x}|\text{z})$$
**The Marginal Distribution**
The marginal distribution over $\text{z}$ is specified in terms of the mixing coefficients $\pi_k$ such that $$p(z_{k}=1)=\pi_{k}$$
where the parameters $\{\pi_{k}\}$ must satisfy $$0 \leq \pi_{k} \leq 1$$ together with $$\sum_{k=1}^{K} \pi_{k}=1$$
so that it is a valid probability distribution . 

Because $\text{z}$ uses a 1-of-K representation, we can write the marginal distribution in the form $$p(\text{z}) = \prod_{k=1}^{K} \pi_{k}^{z_{k}}$$

> [!NOTE] Remark
> Note that $p(\text{z}) = \prod_{k=1}^{K} \pi_{k}^{z_{k}}=\pi_{k}$ since all values of $\text{z}$ are $0$ except $z_{k}$. 


**The Conditional Distribution** 
The conditional distribution of $\text{x}$ given a particular value for $\text{z}$ is a Gaussian $$p(\text{x}|z_{k}=1)=\mathcal{N}(\text{x}| \mu_{k}, \Sigma_{k})$$
which can also be written in the form: $$p(\text{x}|\text{z})= \prod_{k=1}^{K} \mathcal{N}(\text{x}|\mu_{k}, \Sigma_{k})^{z_{k}}$$

> [!NOTE] Recall
> Recall that the marginal distribution of $\text{x}$, $p(\text{x})$ can be obtained by summing the joint distribution over all the possible states of $\text{z}$:$$p(\text{x}) = \sum_{z} p(\text{z}) p(\text{x}|\text{z})$$
	
This gives us: $$p(\text{x})= \sum_{k=1}^{K} \pi_{k} \mathcal{N} (\text{x}| \mu_{k}, \Sigma_{k})$$
which is the form of the Gaussian mixture. **This shows that the gaussian mixture can be expressed using a latent variable.** 

---

Another quantity that plays an important role is the conditional probability of $\text{z}$ given $\text{x}$. Let's denote this quantity by $\gamma(z_k)$. We can calculate this quantity by Bayes' Theorem.

$$\begin{align*}
	\gamma(z_{k}) = p(z_{k}=1|\text{x}) &= \frac{p(\text{x}|z_{k}=1) p(z_{k})}{\sum^{K}_{j=1} p(\text{x}|z_{j}=1) p(z_{j}=1)}\\
&= \frac{\pi_{k} \mathcal{N}(\text{x}|\mu_{k}, \Sigma_{k})}{\sum^{K}_{j=1} \pi_{j} \mathcal{N}(\text{x}|\mu_{j}, \Sigma_{j})}
\end{align*}$$



> [!NOTE] Remarks
> - We shall view $\pi_{k}$ as the prior probability of $z_{k}=1$ and the quantity $\gamma(z_{k})$ as the corresponding posterior probability once we have observed $\text{x}$. 
> - The quantity $\gamma(z_{k})$ is also called the **responsibility**.
