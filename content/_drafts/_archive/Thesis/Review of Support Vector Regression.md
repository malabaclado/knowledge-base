---
tags:
alias:
creation-date: Friday 2nd December 2022
---
# Outline for discussion of SVR
- [ ] Intro to SVR and regression task in machine learning
	- [ ] Advantages of SVR (sparsity, kernel based, maxium margin-based)
- [ ] Mathematics of support vector regression
	- [ ] Hard SVM
	- [ ] Soft SVM
	- [ ] Dual formulation and Lagrange multipliers
---
# Introduction to SVR and regression task in machine learning

The regression problem is a machine learning problem wherein the model returns a continuous-valued output rather than a finite set. A regression model, in other words, estimates a continuous-valued function.

Support Vector Regression is a non-linear kernel-based regression method that tries to find the best regression hyperplane with the smallest structural risk.

An important property of support vector machines is that the determination of the model parameters corresponds to a convex optimization problem, and so any local solution is also a global optimum. 

Support Vector Regression (SVR) is achieved by introducing an $\varepsilon$-insensitive region around the function, known as the $\varepsilon$-tube. This tube reformulates the optimization problem in order to find the curve that best approximates the continuous-valued function while balancing model complexity and prediction error. More specifically, SVR is formulated as an optimization problem by first defining a convex $\varepsilon$-insensitive loss function to be minimized and then locating the flattest tube that contains the majority of the training instances. As a result, a multiobjective function is built from the loss function and the geometrical properties of the tube.

# The Mathematics of Support Vector Regression
Given a training dataset $T$ comprised of $N$ observations:$$\text{T} =\{(\text{x}_{1},y_{1}), (\text{x}_{2}, y_{2}),...,(\text{x}_{N}, y_{N}) \} $$where  $\text{x}_{i} \in \mathbb{R}^{n}$ , $y_{i} \in\mathbb{R}$  and $i=1,2,...,N$.  We call $\mathcal{X} = \{\text{x}_{1},, \text{x}_{2},...,\text{x}_{N}\}$ the *input space* or the *domain set* and $\mathcal{Y}=\{y_{1},y_{2},...,y_{N}\}$ the *output space* or the *label set*. 

The goal of the regression task is to predict the output value $y$ for a new input value of $\text{x}$. The simplest linear model for regression is one that involves a linear combination of the input space:
$$\begin{align*}
f(\text{x}) &= \text{w}^{T}_{1} \text{x}_{1}, \text{w}^{T}_{2} \text{x}_{2}, ..., \text{w}^{T}_{N} \text{x}_{N} + b\\
&= \sum_{i=1}^{N} \text{w}^{T} \text{x}_{i} + b\\
&=  \langle \text{w}, \text{x}\rangle + b
\end{align*}$$

Where $\text{w}_{i}\in i=1,...,N$  are the weight vectors. The parameter $b$ allows for any fixed offset in the data. It is known as the *bias parameter*. 

## Hard Margin SVR
SVR formulates this function approximation problem as an optimization problem whose goal is to determine the flattest tube centered on the surface while reducing the prediction error, or the difference between the predicted and desired output. In this context, flatness implies looking for a small $\mathrm{w}$. One method to achieve this is to minimize the norm $||\mathrm{w}||$. ==In addition, it should happen that the predictions are within $\varepsilon$ distance from the target values.== 
$$y_{i} -f(\mathrm{x}) \leq \varepsilon \text{ or } f(\mathrm{x})-y_{i} \leq \varepsilon$$

 Using Equation 2.1, we have the following optimization problem:



$$\begin{align} 
	\text{minimize } &\frac{1}{2}||\text{w}||^{2} \\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon\end{cases}
\end{align}$$

<mark style="background: #D2B3FFA6;">Support Vector Regression (SVR) approaches this function estimation problem as an optimization problem that seeks to minimize an $\varepsilon$-insensitive loss function. The quantity $\varepsilon$ is known as the margin of tolerance which is the distance.</mark>

![|450](https://slideplayer.com/slide/14537332/90/images/90/Formulation+of+hard-margin+%EF%81%A5-SVR.jpg)

Then we find the regression hyperplane by finding the flattest line inside the tube. The regression line is the flattest line between the margin. We have this optimization problem: 
$$\begin{align*}
	\text{minimize }& \frac{1}{2}||\text{w}||^{2}\\\\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon\end{cases}
\end{align*}$$

To improve the predictions of our SVR model,  we may sometimes allow some data points outside the $\varepsilon$-insensitivity tube. This makes the model more robust and sensitive to outliers. In this soft-margin approach, we use slack variables to penalize the points outside the tube based on their distance. This results to a multi-objective optimization problem.

![|350](https://slideplayer.com/slide/14537332/90/images/91/Formulation+of+soft-margin+%EF%81%A5-SVR.jpg)

We now have the $\varepsilon$-insensitivity loss function defined as:

And the optimization problem: 
$$\begin{align*}
	\text{minimize }& \frac{1}{2}||\text{w}|| ^{2} + \text{C}\sum_{i=1}^{n} (\xi_{i}+ \xi^*_{i})\\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon + \xi_{i}\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon + \xi^{*}_{i}\\
		\xi_{i}, \xi^{*}_{i}\geq 0\end{cases}
\end{align*}$$


## The dual formulation
We'll construct the Lagrange function from the primal objective function and introduce a dual set of variables $\alpha_{i}, \alpha^{*}_{i}, \mu_{i}, \mu^{*}_{i}$. We arrive at the Lagrange function:

$$\begin{align*}
	\text{L} = &\frac{1}{2}||\text{w}|| ^{2} + \text{C}\sum_{i=1}^{N} (\xi_{i}+ \xi^{*}_{i}) - \sum^{N}_{i=1} (\mu_{i} \xi_{i} + \mu_{i}^{*} \xi_{i}^{*}) \\\\
	&-\sum^{N}_{i=1} \alpha_{i}(\varepsilon + \xi_{i} - y_{i} + \langle \text{w},\text{x}_{i}\rangle +b)\\\\
	&-\sum^{N}_{i=1} \alpha_{i}(\varepsilon + \xi_{i} + y_{i} - \langle \text{w},\text{x}_{i}\rangle -b)
\end{align*}$$

Now we take the derivatives of the Lagrange function with respect to $\text{w}, b, \xi_{i} \text{ and } \xi_{i}^{*}$ and setting them to zero:

$$\begin{align*}
	\frac{\partial L}{\partial \text{w}} = 0 &\Rightarrow \text{w} = \sum^{N}_{i=1} (\alpha_{i} - \alpha_{i}^{*}) \text{x}_{i}  \\\\
	\frac{\partial L}{\partial b} = 0 &\Rightarrow \sum^{N}_{i=1}(\alpha_{i}^{*} - \alpha_{i})=0\\\\
	\frac{\partial L}{\partial \xi_{i}} = 0 &\Rightarrow \alpha_{i}+ \mu_{i}= C\\\\
	\frac{\partial L}{\partial \xi_{i}^{*} } = 0 &\Rightarrow \alpha_{i}^{*}+ \mu_{i}^{*} =C
\end{align*}$$

Using these results to eliminate the corresponding variables in the Lagrangian, we arrive at the dual formulation of the optimization problem:

$$\begin{align*}
	\text{maximize } &L=\frac{1}{2}\sum^{N}_{i=1}\sum^{N}_{j=1} (\alpha_{i} - \alpha_{i}^{*})(\alpha_{j}- \alpha_{j}^{*})\langle \text{x}_{i},\text{x}_{j}\rangle\\
  & \qquad - \varepsilon \sum^{N}_{i=1} (\alpha_{i} +\alpha_{i}^{*}) - \sum^{N}_{i=1} y_{i}(\alpha_{i} - \alpha_{i}^{*})\\ \\
	\text{subject to } & \begin{cases} \alpha_{i},\alpha_{i}^{*}\in [0, C]\\
	\sum^{N}_{i=1}(\alpha_{i} - \alpha_{i}^{*}) = 0 \end{cases}
\end{align*}$$


## Kernel trick for non-linearity

## Karush-Kuhn-Tucker Conditions
The Karush-Kuhn-Tucker conditions are necessary conditions for a local solution $x^*$ of the general mathematical programming problem. It generalizes the method of Lagrange multipliers to cases where there are inequality-constraints. It provides a criterion for testing whether a solution which has been found by other methods is an optimal solution.

These results was obtained independently by Karush in 1939 and by H.W. Kuhn and J.W. Tucker in 1951.

**Theorem.** KKT Conditions
Consider the general mathematical programming problem: 
$$\begin{align*}
\text{minimize } &f(x), \quad x\in \mathbb{R}\\
\text{subject to } &g_{i}(x) \leq 0, \quad i=1,...,p\\
&h_{j}(x)=0, \quad j=1,...,q
\end{align*}$$
where $f, g_{i}, h_{j}$ are all continuously differentiable and from the Lagrangian function 
$$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^{p}\lambda_{i}g_{i}(x) + \sum_{j=1}^{q} \mu_{j} h_{j}$$
The Karush-Kuhn-Tucker (KKT) conditions are: 

$$\begin{align*}
\frac{\partial}{\partial x_{k}} L(x, \lambda, \mu) = 0 &, \quad k=1,...,n\\
\lambda_{i}\geq 0 &, \quad i=1,...,p\\
\lambda_{i} g_{i}(x) = 0 &, \quad i=1,...,p\\
g_{i}(x)\leq 0 &, \quad i=1,...,p\\
h_{j}(x)=0 &, \quad j=1,...,q
\end{align*}$$

Citations
- [Karush-Kuhn-Tucker conditions - Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Karush-Kuhn-Tucker_conditions)
- [Karush–Kuhn–Tucker conditions - Wikipedia](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions)
- Numerical optimization (Springer)

## Mercer's Theorem

Mercer's theorem is a representation of a symmetric positive-definite function on a square as a sum of a convergent sequence of product functions. 

**Theorem.** Mercer's theorem
Let $X$ be a compact subset of $\mathbb{R}^{n}$. Assuming that $K$ is a symmetric continuous function such that the integral operator $T_{K}:L_{2}(X) \to L_{2}(x)$, $$(T_{K}f)(\cdot) = \int_{X} K(\cdot, \text{x})f(\text{x})d\text{x}$$
is positive. That is: $$\int_{X \times X} K(\text{x}, \text{z}) f(\text{x})f(\text{z})d\text{x}d\text{z} \geq 0$$
for all $f \in L_{2}(X)$. Then $K(\text{x}, \text{z})$ can be expanded in a uniformly convergent series (on $X \times X$) in terms of function $\phi_{j} \in L_{2}(X)$, normalized in such a way that $||\phi_{j}||_{L_{2}}=1$  and positive eigenvalues associated with $\lambda_{j}\geq 0$, $$K(\text{x}, \text{z}) = \sum_{j-1}^{\infty} \lambda_{j} \phi_{j}(\text{x}) \phi_j(\text{z})$$

Citations 
- Cervantes et. al

Other resource:
- [hilbert spaces - Mercer's Theorem importance (Kernels) - Mathematics Stack Exchange](https://math.stackexchange.com/questions/3063705/mercers-theorem-importance-kernels)
- [Mercer's theorem - HandWiki](https://handwiki.org/wiki/Mercer%27s_theorem#Introduction)


---
# Draft

Suppose we are given a training data $\text{T} =\{(\text{x}_{1},y_{1}), (\text{x}_{2}, y_{2}),...,(\text{x}_{N}, y_{N}) \} \subset \mathcal{X} \times \mathbb{R}$ where  $\text{x}_{i} \in \mathbb{R}^{n}$ , $y_{k} \in\mathbb{R}$  and $k=1,2,...,N$.  We call $\mathcal{X}$ the input feature space and we call $y_{k}$ the actual target values. 

The goal of $\varepsilon$-SVR is to find the function $f(x)$ that is at most $\varepsilon$ distance away from the actual targets $y_i$ for all training data and at the same time, as flat as possible. The continuous-valued function being approximated can be written as: $$f(\text{x}) = \langle \text{w}, \text{x} \rangle + b \qquad (2.1)$$
where $\langle \cdot, \cdot \rangle$ denotes the dot product in $\mathcal{X}$, $\text{w}$ is called the weight vector, and $b$ is called the bias term. 


---
To find the optimal curve, we need to tune $\text{w}$ to be as small as possible. That is, we solve the optimization problem:

$$\begin{align*}
	\text{minimize }& \frac{1}{2}||\text{w}||^{2}\\\\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon\end{cases}
\end{align*}$$

**Soft Margin Slack Variable**

In this model, there is an underlying assumption that there exists a function $f$ such that all $(\text{x}, y)$ pairs are inside the $\varepsilon$-insensitivity tube. However, this is not always the case, especially when you have outliers. Sometimes, we allow some points to be found outside the $\varepsilon$-insensitive tube. We then introduce slack variables $\xi_{i}, \xi^{*}_{i}$ to penalize these outliers. Our goal now is to minimize $\text{w}$ and the penalty we accept for having points outside the $\varepsilon$-insensitivity tube. With that, we arrive at a new optimization problem:

$$\begin{align*}
	\text{minimize }& \frac{1}{2}||\text{w}|| ^{2} + \text{C}\sum_{i=1}^{n} (\xi_{i}+ \xi^*_{i})\\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon + \xi_{i}\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon + \xi^{*}_{i}\\
		\xi_{i}, \xi^{*_{i}}\geq 0\end{cases}
\end{align*}$$

In the objective function, the constant $C$ determines the balance between the flattening the $\text{w}$ vector and penalizing for errors. A very high value of $C$, means that the model has very low tolerance for errors. For that reason, it is called the regularization parameter.

Dual Formulation


---

**Dealing with nonlinear data**

The SVR algorithm also works for non-linear datasets. This is achieved by preprocessing the training data $\text{x}_{i}$ by using a map $\Phi:\mathcal{X} \to \mathcal{F}$. 

Notice that in eq (?) that the SV algorithm only depends on dot products between patterns. The key observation is that we can implicitly map the input space into our desired feature space by the use of functions we call kernel. 

Definition. Kernel function
Let k be a function such that $k(x,x')=\langle \Phi(x), \Phi(x') \rangle$. Then k is known as a kernel function.

The use of kernels allow us to restate the optimization problem as follows:

$$\begin{align*}
	\text{maximize } &L=\frac{1}{2}\sum^{N}_{i=1}\sum^{N}_{j=1} (\alpha_{i} - \alpha_{i}^{*})(\alpha_{j}- \alpha_{j}^{*}) k(x,x')- \varepsilon \sum^{N}_{i=1} (\alpha_{i} +\alpha_{i}^{*}) - \sum^{N}_{i=1} y_{i}(\alpha_{i} - \alpha_{i}^{*})\\ \\
	\text{subject to } & \alpha_{i},\alpha_{i}^{*}\in [0, C]\\
	&\sum^{N}_{i=1}(\alpha_{i} - \alpha_{i}^{*}) = 0
\end{align*}$$

which gives us:

$$\text{w} = \sum_{i=1}^N (\alpha_i - \alpha_i^* ) \Phi(x_i) \quad \text{and}$$ 

$$f(x) = \sum_{i=1}^N (\alpha_i - \alpha_i^* ) k(x_i ,x) +b$$

The difference of eq (?) to the linear case is that $w$ is no longer given explicitly. 

Also note that in the nonlinear setting, the optimization problem corresponds to finding the flattest function in the feature space, not in input space. 

The condition for kernel functions is summarized by Mercer's Theorem, which is outside the scope of this study. 

**The Loss Function**

The $\varepsilon$-insensitive loss function is defined as:
$$|\xi|_{\varepsilon} = \begin{cases} 0\quad \text{, if } |\xi| \leq \varepsilon \\
	2\quad \text{, otherwise}\end{cases}$$

**Computing the bias term b**

... (KKT conditions)


**Kernel Method**
A solution proposed by *Boser, Guyon & Vapnik (1992)* was to map the input feature space into a higher-dimensional space where a linear operator could be found. 

In this case, the computation for the optimal regression function is not done on the feature space, but by the use of a *kernel trick*.

Suppose we transform the input feature space to a higher-dimensional feature space using a mapping $\phi$.

Then the dual objective function will be:
...


Notice that the inner products happens only on the images of the inputs $\mathrm{x}, \mathrm{x'}$. 

A key observation for the development of the kernel trick is to notice that the objective function and the regression function depends on some inner product of two vectors. Now suppose the data is mapped onto a higher dimensional space, the properties of this inner product is preserved by the kernel function.



Definition. Positive Definite Matrix
The real-valued matrix $A$ is called positive definite if $$\mathrm{x}^{T} A\mathrm{x} >0$$for all vectors $\mathrm{x} \in \mathbb{C}^{n}$ where $\mathrm{x}^{T}$ denotes the transpose of $\mathrm{x}$.

The definition of positive definiteness is equivalent to the requirement that the determinants associated with all upper-left submatrices are positive.

Definition. Mercer's Kernel
Let $X=\{x_{1}, ..., x_{n}\}$ be a finite set of $n$ samples from $\mathcal{X}$. The [[Gram matrix]] of $X$ is defined as $$\mathrm{K}(X, \kappa) \in \mathbb{R}^{n \times n}$$(or $\mathrm{K}$ for short), such that $$(\mathrm{K}_{ij}=\kappa (x_{i}, x_{j}))$$If $\forall X \subseteq \mathcal{X}$, the matrix $\mathrm{K}$ is positive definite, then $\kappa$ is called a **Mercer kernel**, or a **positive definite kernel**. 

Theorem. Mercer's Theorem
Let $X=\{x_{1}, ..., x_{n}\}$ be a finite set of $n$ samples from $\mathcal{X}$. If the Gram matrix $\mathrm{K}$ of $\mathrm{X}$ is positive definite, we can compute the eigenvector decomposition of the Gram matrix as: $$\mathrm{K}=\mathrm{U}^{T} \Lambda \mathrm{U} $$ where $\Lambda = diag(\lambda_{1},\dots, \lambda_{n })$.

 

To show this, let $\phi : \mathrm{x}_{i} \to (\sqrt{\lambda_{k}} \mathrm{ x} _{ki})_{t=1}^{n} \in \mathbb{R}^{n}$ for $i=1,\dots, n$. Then $$\langle \phi(\mathrm{x}_{i}) \cdot \phi(\mathrm{x}_{i})\rangle 
= \sum_{t=1}^{n}\lambda_{k} \mathrm{x}_{ki} \mathrm{x}_{kj}
= (\mathrm{V}^T  \Lambda \mathrm{V})_{ij}
= \mathrm{K}_{ij}
=\kappa(\mathrm{x}_{i} \cdot \mathrm{x}_{j})$$
This implies that $\kappa(\mathrm{x}_{i}, \mathrm{x}_{j })$ is a kernel function corresponding to the mapping $\phi$.


---
## References
- Efficient Learning Machines (Awad)
- Pattern Recognition (Bishop)
- Understanding Machine Learning 
- @smola2004
- @kavakloiglu2011
- Kernal and Kernel Methods, Engelhardt, et al.