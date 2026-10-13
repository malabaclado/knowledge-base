#scratchpad 

# Method of Lagrange Multipliers

Consider the general optimization problem: 
$$\begin{align}
\text{min}_{x} &f(\mathrm{x}) \\
\text{subject to } &g(\mathrm{x}) \leq 0, i=1,\dots,m \\
&h(\mathrm{x}) = 0, j=1,\dots,r
\end{align}$$


The Lagrangean is defined as 
$$
L(\mathrm{x}, \lambda, \mu) = f(\mathrm{x}) 
+ \sum_{i=1}^{m} \lambda_{i} g_{i }(\mathrm{x})
+ \sum_{i=1}^{r} \mu_{i} h_{i }(\mathrm{x})
$$


The Lagrange dual function is $$g(\lambda, \mu) = \text{min}_{\mathrm{x}} L(\mathrm{x}, \lambda, \mu)$$

The corresponding dual problem is: 
$$
\begin{align}
&max_{\lambda,\mu} \qquad g(\lambda, \mu) \\
&\text{subject to } \quad \lambda\geq 0
\end{align}
$$



# KKT Conditions
KKT conditions are first-order necessary conditions for a solution in nonlinear programming to be optimal. The KKT approach generalizes the method of Lagrange multipliers to inequality constraints. 

KKT conditions
1. $g(x)\leq 0 ,\quad h(x) =0$
2. $\lambda \geq 0$
3. $\lambda g(\mathrm{x})=0$
4. $\nabla f(x) + \sum \lambda \nabla g(x)=0$


KKT Theorem
If there exists a solution $\mathrm{x}^{*}$  to the primal problem, a solution $(\lambda^{*}, \mu^{*})$ to the dual problem, such that they together satisfy the KKT conditions, then the problem pair has strong duality, and $\mathrm{x}^{*}$, $(\lambda^{*}, \mu^{*})$ is a solution pair to the primal and dual problems.