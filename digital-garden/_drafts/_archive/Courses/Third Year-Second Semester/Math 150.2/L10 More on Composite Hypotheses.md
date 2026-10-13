

### Details
Source:
- Math 150.2 L10 Composite Hypothesis Lecture Note
- Math 150.2 Class Lecture (May 18)

### Notes
In this lecture we discussed:
- Generalized Likelihood-Ratio Test
- [[Uniformly Most Powerful Test]]
- [[Monotone Likelihood-Ratio]]
- [[Thm. Generating a UMPT from a family with MLR]]

---

First, we defined the [[Generalized Likelihood-Ratio]].

Suppose we have a random sample $X_1, X_2, . . . , X_n$ from the density $f(x; \theta)$, the **Generalized Likelihood-Ratio Test** goes like this:

- Reject $H_0$ if the [[Generalized Likelihood-Ratio]] $\lambda_n < \lambda_0$  where $\lambda_0$ is some constant.

Note that $\lambda$ will tend to be small when $H_0$ is not true.


Next, we discussed the [[Uniformly Most Powerful Test]] which is a test that have the following properties:
1. The supremum of the power function is equal to $\alpha$.
2.  $\Pi_{\Upsilon^*}(\theta) \geq \Pi_{\Upsilon}(\theta)$ for every $\theta \in \Omega - \Omega_0$ and for any test $\Upsilon$ with size less than or equal to $\alpha$.

Note that the symbol $\Pi_{\Upsilon^*}(\theta)$ above is the **power function**.

It is remarked that the **Uniformly Most Powerful Test may or may not exist**. Thus, we develop a theorem that will help us identify when we have a UMPT.

But before we get to the theorem, we'll need the concept of [[Monotone Likelihood-Ratio]].


Next, we'll discuss a theorem that allows us to generate a UMPT from a family of density with MLR.

> **Theorem. (Generating a UMPT from a family with MLR)**
> Assume that the family of densities $\{f(x;\theta) | \theta\in \Omega \}$ has a monotone likelihood-ratio (MLR) in the statistics $T=t(X_1,X_2,...,X_n)$.
> - If the MLR is nondecreasing in T and if $k^*$ is such that $\mathbb{P}[T<k^*]=\alpha$, then the test corresponding to the critical region is a UMPT of size $\alpha$ of $H_0:\theta\leq\theta_0$ versus $H_a:\theta >\theta_0$.
> - If the MLR is nonincreasing in T and if $k^*$ is such that $\mathbb{P}[T>k^*]=\alpha$, then the test corresponding to the critical region is a UMPT of size $\alpha$ of $H_0:\theta\leq\theta_0$ versus $H_a:\theta >\theta_0$.
> 

### Comments
