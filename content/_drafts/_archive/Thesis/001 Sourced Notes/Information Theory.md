
**Outline**
- Information Theory
	- Entropy of a random variable 
	- Noiseless Coding Theorem
	- Multiplicity
	- Differential Entropy
	- Conditional Entropy

- Relative Entropy and Mutual Information
	- Relative Entropy / Kullback-Leibler divergence / KL divergence
	- Jensen's Inequality
	- Mutual information between two variables

---
**Question:** Consider a discrete random variable $x$, how much information is received when we observe a specific value for this variable?

**Answer:** The amount of information can be viewed as the ‘degree of surprise’ on learning the value of x. 

- If we are told that a highly improbable event has just occurred, we will have received more information than if we were told that some very likely event has just occurred, and if we knew that the event was certain to happen we would receive no information.

Our measure of information content will therefore *depend on the probability distribution* $p(x)$, and we therefore look for a quantity $h(x)$ that is a monotonic function of the probability $p(x)$ and that expresses the information content.

We should note that:
1. If two events x and y are unrelated, then the information gain from observing both of them should be the sum of the information gained from each of them separately.
2. Two unrelated events will be independent

Taking the above conditions into account, the form of $h(x)$ should satisfy:
1. $h(x,y) = h(x) + h(y)$ 
2. $p(x,y) = p(x)p(y)$  	*independence*

From these two relationships, one can show that $h(x)$ must be given by the logarithm of $p(x)$: $$h(x) = -\log_{2}p(x)$$

Now suppose that a sender wishes to transmit the value of a random variable to a receiver. The average amount of information that they transmit in the process is obtained by taking the expectation of $h(x)$ with respect to the distribution $p(x)$ and is given by $$H[x] = -\sum\limits_x p(x)\log_2p(x)$$

This quantity is known as the entropy of the random variable $x$.


**Note that low probability events x correspond to high information content**


> **Noiseless Coding Theorem** states that the entropy os a lower bound on the number of bits needed to transmit the state of a random variable.

Interpretation of Entropy:
- average amount of information needed to specify th state of a random variable.

### Differential Entropy

We can extend the definition of entropy to include distributions over continuous variables.


$$H[x] = -\int p(x)\ln p(x)dx$$

The discrete and continuous forms of the entropy differ by a quantity $\ln \Delta$, which diverges to the limit $\Delta \to 0$. This reflects the fact that to specify a continuous variable very precisely requires a large number of bits.

In the case of discrete distributions, the maximum entropy configuration corresponded to an *equal distribution of probabilities across the possible  
states of the variable*. In the case of continuous variables, the distribution that maximizes the differential entropy is the Gaussian distribution.

If we evaluate the differential entropy of the Gaussian distribution we obtain $$H[x]=\frac{1}{2}\{1 + \ln(2\pi \sigma^2)\}$$

Observations:
1. The entropy increases as the distribution becomes broader  (i.e., as $\sigma^2$ increases)
2. Unlike the discrete entropy, the differential entropy can be negative.

### Conditional Entropy
Suppose we have a joint distribution $p(x, y)$ from which we draw pairs of values of $x$ and $y$. If a value of $x$ is already known, then the additional information needed to specify the corresponding value of $y$ is given by $−\ln p(y|x)$. Thus the average  
additional information needed to specify $y$ can be written as $$H[y|x] = -\int \int p(y,x) \ln p(y|x)dy dx$$


The conditional entropy satisfies the following relation $$H[x,y] = H[y|x] + H[x]$$
Thus the information needed to describe $x$ and $y$ is given by the sum of the information needed to describe $x$ alone plus the additional information required to specify $y$ given x.

---
**Relative Entropy and Mutual Information**
Consider some unknown distribution $p(\text{x})$, and suppose that we ahve modelled this distribution using an *approximating distribution* $q(\text{x})$. 

If we use $q(\text{x})$ to construct a coding scheme for the purpose of transmitting values of $\text{x}$ to a receiver, then the additional amount of information (in nats) required to specify the value of $\text{x}$ as a result of using $q(\text{x})$ instead of the true distribution $p(\text{x})$ is given by $$KL(p||q) = -\int p(\text{x}) \ln \{\frac{q(\text{x})}{p(\text{x})}\}d\text{x}$$ 

This quantity is known as the **relative entropy** or the **Kullback-Leibler divergence** or the **KL divergence** between the distributions $p(\text{x})$ and $q(\text{x})$.

*Note that the relative entropy is not symmetric, ie. $KL(p||q) \neq KL(q||p)$*

> **Proposition.** The **KL divergence** satisfies $KL(p||q) \geq 0$ with equality if and only if $p(\text{x}) = q(\text{x})$.

---

Consider a joint distribution between two sets of variables $\text{x}$ and $\text{y}$ given by $p(\text{x},\text{y})$. 

If the variables are independent, then their joint distribution satisfy the property $$p(\text{x},\text{y}) = p(\text{x})p(\text{y})$$

If the variables are not independent, we can gain some idea of whether they are 'close' to being independent by considering the Kullback-Leibler divergence between the joint distribution and the product of marginals, given by $$I[x,y] = KL(p(\text{x},\text{y})||p(\text{x})p(\text{y}))$$

This quantity is known as the **mutual infomation** between variables $\text{x}$ and $\text{y}$.

> **Corollary.** The quantity $I(\text{x},\text{y}) \leq 0$ with equality if, and only if, $\text{x}$ and $\text{y}$ ae independent.

> **Proposition.** The mutual information is related to conditional entropy. $$I[\text{x},\text{y}]= H[\text{x}] - H[\text{x}|\text{y}] = H[\text{y}] - H[\text{y}|\text{x}]$$

Thus we can view the mutual information as the reduction in the uncertainty about $\text{x}$   by virtue of being told the value of $\text{y}$ (or vice versa). From a Bayesian perspective, we can view $p(\text{x})$ as the prior distribution for $\text{x}$ and $p(\text{x}|\text{y})$ as the posterior distribution after we have observed new data $\text{y}$. The mutual information therefore represents  
the reduction in uncertainty about $\text{x}$ as a consequence of the new observation $\text{y}$.