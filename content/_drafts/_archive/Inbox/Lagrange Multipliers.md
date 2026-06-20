---
tags: type/concept
alias: 
creation-date: Sunday 23rd January 2022
last-modified-date: Wednesday 23rd February 2022 19:52:41
---

# Lagrange Multipliers
Source: Appendix E. [[📕 Pattern Recognition and Machine Learning (Bishop) 1]]


**Lagrange multipliers**, also sometimes called undetermined multipliers, **are used to find the stationary points(aka the critical points) of a function of several variables subject to one or more constraints.** 

![[Pasted image 20220811114543.png]]
 
**Maximization with equality constraint**
Consider the problem of maximizing the function $f(x_{1}, x_{2})$ subject to a constraint relating $x_1$ and  $x_{2}$ in the form: $g(x_{1},x_{2})=0$ .

To solve this problem using the Lagrange method, we introduce an additional variable $\lambda$ called *"Lagrange multiplier"*.

Form the Lagrangean function: $$L(\text{x}, \lambda) = f(\text{x}) + \lambda g(\text{x})$$
Then we find the critical points of $L(\text{x}, \lambda)$ with respect to $x_{1}, x_{2}$ and $\lambda$. (Finding critical points invovles differentiating the Lagrangean function).

The constrianed stationarity condition is obtained by settin 




**Maximization with inequality constraint**
There are now two kinds of solution possible:
1. *Inactive*: the constrained stationary point lies in the region where $g(\text{x} )> 0$. 
	- In this case, the function $g(x)$ plays no role and the stationary condition is simply $\nabla f(\text{x}) =0$.
2. *Active*: the constrained stationary point lies on the boundary $g(\text{x}) = 0$.
	- This case is analogous to the equality constraint and corresponds to a stationary point of the Lagrange fucnction with $\lambda \neq 0$. 


---
[5.4 The Lagrange Multiplier Method (econgraphs.org)](https://www.econgraphs.org/textbook/scarcity_and_choice/calculus/lagrange)





