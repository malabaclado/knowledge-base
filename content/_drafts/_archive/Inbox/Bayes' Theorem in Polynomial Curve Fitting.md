---
tags: 
alias: 
creation-date: Wednesday 24th August 2022
last-modified-date: Wednesday 24th August 2022 10:55:19
---
Bayes' Theorem is the use of probability to represent uncertainty. 

We shall discuss Bayes' theorem in the context of polynomial curve fitting. 

Suppose we have...
- $p(\text{w})$ : our assumptions to $\text{w}$; the prior 
- $p(\mathcal{D}|\text{w})$ : the effect of the observed data $\mathcal{D}$ 

Using Bayes' Theorem: $$p(\text{w}| \mathcal{D}) = \frac{p(\mathcal{D}|\text{w}) p(\text{w})}{p(\mathcal{D})}$$we can evaluate the uncertainty in $\text{w}$ after observing $\mathcal{D}$ in the form of a posterior probability $p(\text{w}, \mathcal{D})$ .

> [!NOTE] Remarks
> - The quantity $p(\mathcal{D} |\text{w})$ is called the **likelihood function**. It expresses how probable the observed data set is for different settings of parameter vector $\text{w}$. 
> - Note that the likelihood function is not a probability distribution over $\text{w}$ , and its integral wrt to $\text{w}$ does not necessarily equal to 1.

![[Pasted image 20220824112501.png]]
