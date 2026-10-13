[[Draft - Sparse Kernel Machines]]

# Outline
- **Maximum Margin Classifiers** (*discusses the mechanisms of support vectors and how to maximize the margin*)
	- Overlapping class distributions (*discusses the case that class distributions overlap*)
	- Relation to logistic regression
	- Multiclass SVMs
	- SVMs for regression
	- Computational learning theory
- **Relevance Vector Machines**
	- RVM for regression
	- Analysis of sparsity
	- RVM for classification


---

# Notes

In the previous chapter, we explored algorithms based on **nonlinear kernels**. One significant limitation of such algorithms is that the *kernel function* $k(\text{x}_{n}, \text{x}_m)$ must be evaluated for all possible pairs $\text{x}_{n}$ and $\text{x}_{m}$ of training points, which can be **computationally infeasible during training** and can lead to **excessive computation times** when making predictions for new data points.

In this chapter, we look at kernel-based algorithms that have *sparse* solutions, so that predictions for new inputs depend only on the kernel fuction evaluated at a subset of the training data points.

## Maximum Margin Classifiers
*(7.1)* Consider the 2-class classification problem of the form $$y(\text{x}) = \text{w}^{T} \phi(\text{x}) +b$$

where $\phi (\text{x})$ denotes a fixed *feature-space transformation* and $b$ a *bias parameter*.

The training data set comprises $N$ input vectors $\text{x}_{1}, \text{x}_{2},..., \text{x}_{N}$ with corresponding target values $t_{1}, t_{2},..., t_{N}$ where $t_{n} \in \{-1,1\}$. 

New data points $\text{x}$ are classified according to the sign of $y(\text{x})$.

Assume that the training set is [[linearly separable]] in the feature space.

There may exists many solutions that separate the classes exactly. If there are multiple solutions that ca classify the training data set, then we should find the one that will give the **smallest generalization error**. The support vector machine approaches this problem through the concept of a *margin*, which is defined to be the **smalest distance** between the decision boundary and any of the samples.

In support vector machines the *decision boundary* is chosen to be the one for which the **margin is maximized.**

The perpendicular distance of a point $\text{x}$ from a hyperplane defined by $y(\text{x}) = 0$ where $y(\text{x})$ takes the form of *(7.1)* is given by $$ \frac{|y(\text{x})|}{||\text{w}||}$$

The distance of a point $\text{x}_{n}$ to the decision surface is given by $$\frac{t_{n} y(x_{n})}{||\text{w}||} = \frac{t_{n} (\text{w}^{T}\phi (x_{n}) +b)}{||\text{w}||}$$
The margin is given by the **perpendicular distance to the closest point** $\text{x}_n$. So to find the maximum margin, we need to solve this optimization problem $$\arg \max_{\text{w}, b} \{ \frac{1}{||\text{w}||} \min [t_{n} (\text{w}^{T} \phi(x_{n})+b)]\} $$

Direct solution of this optimization problem would be very complex. 

We reduce the optimization problem to $$\arg \min_{\text{w}, b} \frac{1}{2} ||\text{w}||^{2}$$

subject to the following constraints $$t_{n}(\text{w}^{T} \phi(\text{x}_{n}) +b) \geq 1, \space n=1,...,N$$
This is an example of a *quadratic programming problem* in which we are trying to minimize a quadratic function subject to a set of linear inequality constraints.


*(7.7)* To solve this constrained problem, introduce Lagrange multipliers $a_{n} \geq 0$ for each constraint, giving the Lagrangian function:
$$L(\text{w},b,\text{a}) = \frac{1}{2}||\text{w}||^{2} - \sum^{N}_{n=1}a_{n}\{t_{n}(\text{w}^{T}\phi(\text{x}_{n})+b)-1\}$$ ^f12833

where $\text{a} = (a_{1},...,a_{N})^{T}$

*(7.10)* Eliminating $\text{w}$ and $b$ from $L(\text{w},b,\text{a})$ gives the *dual representation* of the maximum margin problem in which we **maximize** $$\tilde{L}(\text{a}) = \sum^{N}_{n=1}a_{n} - \frac{1}{2}\sum^{N}_{n=1} \sum^{M}_{m=1}a_{n}a_{m}t_{n}t_{m}k(\text{x}_n,\text{x}_{m})$$
subject to the following constraints 
*(7.11)* $$a\geq 0, \quad n=1,...,N$$ *(7.12)* $$\sum^{N}_{n=1}a_{n}t_{n} = 0 $$
Here, the *kernel function* is defined as $$k(\text{x}, \text{x}') = \phi(\text{x})^{T}\phi(\text{x}')$$

