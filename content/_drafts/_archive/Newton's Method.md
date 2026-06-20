# Newton's Method

The Newton's method is a special case of the Fixed-Point Iteration method.


This is also called as Newton-Raphson Method

Iterative Formula:
![[Pasted image 20210331130144.png]]

---
##### Geometric Intuition
![[Pasted image 20210331130421.png]]


---

##### Necessary conditions for Newton's Method to converge:
Recall: [[Taylor's Theorem of order n]]


1. $f(x) \in C^2[a,b]$ -> f(x) must be continuously differentiable up to second degree on the interval [a,b].


---
##### Convergence of Newton's Method
TL;DR Newton's method is quadratically convergent.


==**Theorem**== Let be twice continuously differentiable and f(r)=0. If $f'(r)\neq 0$, then Newton's method is **locally**  and **quadratically convergent** to r. The error $e_i$ at step $i$ satisfies $$\lim_{i\to \infty} \frac{e_{i+1}}{e_i^2}=M$$ where $$M=\frac{f''(r)}{2f'(r)}$$

---
##### Stopping criteria
1. $|X_N-X_{N-1}|<\epsilon$
2. $\frac{|X_N-X_{N-1}|}{X_N}<\epsilon$


---
Related: [[Secant Method]]