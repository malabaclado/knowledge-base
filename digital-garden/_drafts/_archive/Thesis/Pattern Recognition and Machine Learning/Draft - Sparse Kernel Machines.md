In the previous chapter, we explored algorithms based on **nonlinear kernels**. One significant limitation of such algorithms is that the *kernel function* $k(\text{x}_{n}, \text{x}_m)$ must be evaluated for all possible pairs $\text{x}_{n}$ and $\text{x}_{m}$ of training points, which can be **computationally infeasible during training** and can lead to **excessive computation times** when making predictions for new data points.

In this chapter, we look at kernel-based algorithms that have *sparse* solutions, so that predictions for new inputs depend only on the kernel fuction evaluated at a subset of the training data points.

---
Need to review: [[Lagrange Multipliers]]

---
# Maximum Margin Classifiers
Consider the *two-class classification problem*:
$$y(\text{x}) = \text{w}^{T} \thinspace \phi(\text{x}) +b$$
where
- $\phi(\text{x})$ ➡ fixed feature-space transformation
- $b$ ➡*bias parameter*



*Target dataset* ➡ $N$ input vectors: $\text{x}_{1}, \text{x}_{2},..., \text{x}_{N}$
*Target values* ➡ $t_{1}, t_{2},..., t_{n}$ wheere $t_{n} \in \{-1,1\}$
*Goal* ➡ classify new data $\text{x}$ according to the sign of $y(\text{x})$


> ***Note:*** **assume that the training set is linearly separable**
> Which implies that: there exists $\text{w}$ and $b$ such that $\text{w}^{T} \phi(\text{x}) + b$ satisfies:
> - $y(\text{x}_{n}) >0$ for points with $t_{n}= +1$,
> - $y(\text{x}_{n}) <0$ for points with $t_{n}= -1$,
> - $t_{n} y(\text{x})_{n} = 0$ for all training data points.

---

![[Pasted image 20220123201552.png]]

*The **margin** is deﬁned as the perpendicular distance between the decision boundary and the closest of the data points, as shown on the left ﬁgure. Maximizing the margin leads to a particular choice of decision boundary, as shown on the right. The location of this boundary is determined by a subset of the data points, known as **support vectors**, which are indicated by the circles.*

---
*(7.2)* The distance of a point $\text{x}_n$ to the decision surface is given by the equation: 
$$\frac{t_{n} y(x_{n})}{||\text{w}||} = \frac{t_{n} (\text{w}^{T}\phi (x_{n}) +b)}{||\text{w}||}$$
*(7.3)* The optimizatio problem that maximizes the margin is given by:
$$\arg \max_{\text{w}, b} \{ \frac{1}{||\text{w}||} \min [t_{n} (\text{w}^{T} \phi(x_{n})+b)]\} $$

Apply rescaling: $\text{w} \to \kappa \text{w}$ and $b \to \kappa b$.

*(7.4)* Let $$t_{n} (\text{w}^{T} \phi(x_{n})+b) = 1$$

*(7.5)* All data points satisfy this constraint: $$t_{n} (\text{w}^{T} \phi(x_{n})+b)  \geq 1, \space n=1,...,N$$
*(7.6)* The optimization problem now reduces to $$\arg \min_{\text{w} ,b} \frac{1}{2}||w||^{2}$$ under the following constraints given in *(7.5)*









---
# Thoughts, Comments, Further Study
- Perceptron algorithm??
- Moivation for maximum margin solution: *computational learning theory*, also known as *statistical learning theory*.
- Parzen density estimator
- Analogy: **Support vectors** are made up of a subset of the dataset that acts as structural supports to the decision boundary. 
![[Pasted image 20220123203254.png|400]]
- Learn about *quadratic programming problem*

