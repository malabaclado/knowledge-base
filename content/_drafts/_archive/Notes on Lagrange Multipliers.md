Consider the following optimization problem: 
$$\begin{align}
&\text{min }  f(x) \\
&\text{subject to }  g(x) = 0
\end{align}$$
The optimal solution can be found by introducing constants $\lambda$ and solving the system $$\frac{\partial}{ \partial x_{i}} \left( f(x) + \sum^{p}_{j=1} \lambda_{i}g_{j}(x) \right) = 0$$
$$g_{j}(x)= c_{j}, 1\leq j \leq p$$

Each $\lambda$ is called a Lagrange multiplier.

Ref: S. Sawyer

----
# Karush-Kuhn-Tucker Conditions
KKT conditions are optimality conditions for inequality constrined optimization problems.

**1. Feasibility**. The constraints are satisfied 
$$\begin{align}
g(x)&\leq 0 \\
h(x) &=0 \\
\end{align}$$
**2. Dual feasibility**. $$\lambda \geq 0$$

**3. Complementary slackness**
$$\lambda g(x)=0$$
**4. Stationarity** $$\nabla f(x) + \sum \lambda \nabla g(x)=0$$

Ref: Algorithms for optimization p178

---
# Definition (Lagrange function)
Given a general optimization problem:
min f(x) subject to g(x)=b, the lagrangean is $$L(x,\lambda)= f(x)-\lambda(g(x)-b)$$

Theorem (Lagrangean sufficiency theorem)
if $x^*$ and $\lambda$ exists such that $x^*$ is feasible for P and $L(x^{*}, \lambda) \leq L(x, \lambda) ,\forall x \in X$, then x is optimal for P.

Ref: Richard Weber (file name:O)

---

Definition (Lagrangean Function)
$$L(x,\lambda, \mu) = f(x) - \lambda g(x) - \mu h(x)$$

Method of Lagrange Multipliers for Constrained Optimization 
Consider the general optimization problem P: 
$$\begin{align}
\text{min } f(x) \\
\text{subject to } g(x) \geq 0 \\
h(x)=0
\end{align}$$

---
See also: [[Thesis Scratchpad]]



Consider the general constrained optimization problem P:
$$\begin{align}
\text{min } f(x) \\
\text{subject to } g(x) \leq 0 \\
h(x)=0
\end{align}$$
Method of Lagrange Multipliers for Constrained Optimization
1. Define the Lagrangean function 
2. Set the gradient of L equal to zero, find the stationary points x*
3. Substitute x* to find the dual function
4. The Lagrangean dual function is defined as:

Conditions for optimality (KKT conditions)

---
See also: [[Thesis Scratchpad]]







