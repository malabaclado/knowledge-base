Consider a set of training data $T$: $$T = \{ (\mathrm{x}_{1}, y_{1}), (\mathrm{x}_{2}, y_{2}), \dots,(\mathrm{x}_{N}, y_{N})\} \subset \mathcal{X} \times \mathbb{R}$$
where $\mathrm{x}_{i} \in \mathbb{R}^{n}$ and $y \in \mathbb{R}$ for $i=1,\dots,N$. We call $\mathcal{X}=\{ \mathrm{x}_{1}, \mathrm{x}_{2},\dots,\mathrm{x}_{N}\}$ the input feature space (or feature dataset), $y_{i}$ as the actual target values, and the set $\{y_{1},y_{2},\dots,y_{N}\}$ the target dataset.

The goal of SVR is to approximate the function $f(\mathrm{x})$ that is at most $\varepsilon$ distance away from the actual targets $y_{i}$ for all training data and at the same time, as flat as possible. The continuous-valued function to be approximated is in the form

$$\begin{equation}
f(\mathrm{x}) = \langle \mathrm{w}, \mathrm{x} \rangle + b
\end{equation}$$

where $\langle \cdot, \cdot \rangle$ denotes the dot product in $\mathcal{X}$, $\mathbf{w}$ is called the weight vector, and $b$ is called the bias term.

SVR formulates this function approximation problem as an optimization problem whose goal is to determine the flattest tube centered on the surface while reducing the prediction error, or the difference between the predicted and desired output. 

In this context, flatness implies minimizing the perpendicular distance between the observations and the regression function. This implies minimizing the norm of $\mathbf{w}$. This leads us to the optimization problem:

$$\begin{align} 
	\text{minimize } &\frac{1}{2}||\text{w}||^{2} \\
	\text{subject to }& \begin{cases} y_{i} - \langle \text{w},\text{x}_{i}\rangle -b \leq \varepsilon\\
		\langle \text{w},\text{x}_{i}\rangle + b - y_{i} \leq \varepsilon\end{cases}
\end{align}$$
An underlying assumption is that the optimization problem has a feasible solution. That is, there exists a function $f(\mathbf{x})$ that approximates all target values with $\varepsilon$-precision. However, this is not always the case, expecially when there are outliers in the data. To address this, we sometimes allow some points to be found outside the $\varepsilon$-insensitive tube. We then introduce slack variables $\xi_{i}, \xi^{*}_{i}$ to penalize these outliers. Our goal now is to minimize $\text{w}$ and the penalty we accept for having points outside the $\varepsilon$-insensitivity tube. With that, we arrive at a new optimization problem:

