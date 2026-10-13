---
aliases: []
tags: [#definition]
---
> **Definition. (Generalized Likelihood-Ratio)**
> Let $L(\theta; x_1,x_2,...,x_n)$ be the likelihood function for a random sample $X_1,X_2,...,X_n$ having joint pdf $f(x_1,x_2,...,x_n; \theta)$ where $\theta \in \Omega$.
> The **generalized likelihood-ratio**, denoted $\lambda$ or $\lambda_n$, is  defined as $$\lambda=\lambda_n=\frac{\sup_{\theta \in \Omega_0}L(\theta; x_1,x_2,...,x_n)}{sup_{\theta \in \Omega} L(\theta; x_1,x_2,...,x_n)}$$

#### Remarks
- Even though the notation $\lambda$ is similar, the generalized likelihood-ratio is different from the simple likelihood-ratio.
-  Since $\Omega_0 \subset \Omega, 0 \leq \lambda \leq1$.
- The denominator is the **likelihood function evaluated at the maximum likelihood estimator** (mle).

---
#### Some Examples

---
#### Related

---
#### Reference
- Math 150.2 L10 Composite Hypothesis Lecture Note
- Math 150.2 Class Lecture (May 18)