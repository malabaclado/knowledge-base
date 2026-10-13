# Review of Calculus

The [[Intermediate Value Theorem ]] and the [[Mean Value Theorem]] are important for solving equations in Chapter 1. [[Taylor’s Theorem]] is important for understanding interpolation in Chapter 3 and becomes of paramount importance for solving differential equations inChapters 6, 7, and 8.


---
### [[Intermediate Value Theorem]]

**Intuition.** If f is a continuous function on [a,b], then all values y between f(a) and f(b) have corresponding value c in the interval [a,b]


![[Pasted image 20210330125507.png]]

**Theorem Statement.** Let $f$ be a continuous function on the interval $[a,b]$, then $f$ realizes every value  from $f(a)$ to $f(b)$. More precisely, if $f(a) \leq y \leq f(b)$, then there exists $c$ with $a\leq c\leq b$ such that $f(c)=y$.

---
### [[Continuous Limits Theorem]]

Intuition: Limits may be brought inside values in continuous functions


Theorem Statement. Let f be a continuous function in a neighborhood of $x_0$, and assume $\lim_{n\to\infty} x_n=x_0$. Then $$\lim_{n\to \infty}f(x_n)=f(\lim_{n\to \infty}x_n)=f(x_0)$$

---
### [[Mean Value Theorem]]
Let $f$ be a continuously differentiable function on the interval $[a,b]$. Then there exists a number $c$ in $[a,b]$ such that $$f'(c)=\frac{f(b)-f(a)}{b-a}$$


[[Rolle's Theorem]] is a special case of this theorem.

### [[Rolle's Theorem]]
Let $f$ be a continuously differentiable function on the interval $[a,b]$. If $f(a)=f(b)$ then there exists a number $c$ in $[a,b]$ such that $f'(c)=0$.


---
Tags: #course/math-171 #topic/math/numerical-analysis #type/lecture-note