---
tags:
alias:
creation-date: Friday 21st May 2021
last-modified-date: Thursday 22nd September 2022 16:48:01
---

# Thm. Extension Field as a Vector Space

> Theorem. (**Extension Field as a Vector Space**)
> Let E be an extension field of a field F and $\alpha\in E$ be algebraic element over F. If $\deg(\alpha,F)=n$, then $F(\alpha)$ is an n-dimesional vector space over F with bases $\{1,\alpha,\alpha^2,...,\alpha^{n-1}\}$. Furthermore, every element $\beta\in F(\alpha)$ is algebraic over F and $\deg(\beta	,F)\leq \deg(\alpha,F)$

#### Remarks

---
#### Proof of Theorem
The theorem says two things:
1.  If $\deg(\alpha,F)=n$, then $F(\alpha)$ is an n-dimesional vector space over F with bases $\{1,\alpha,\alpha^2,...,\alpha^{n-1}\}$
2.  Every element $\beta\in F(\alpha)$ is algebraic over F and $\deg(\beta	,F)\leq \deg(\alpha,F)$

Note that item 1 can be shown using the proof for [[Thm. Charactetization of Simple Extension Elements]]. We only need to show item 2.

Let $\beta$ be an element of $F$. Then the set $\{1,\beta,\beta^2,...,\beta^n\}$ is an $n+1$ set. Hence, it is linearly dependent since $F(\alpha)$ is only n-dimensional. By linear dependence, we have $b_i$'s in $F$ not all zero such that $$b_0+b_i\beta +b_2\beta^2+,...,+b_n\beta^n=0$$

This means that $\beta$ is a zero of the polynomial $$f(x)=b_0+b_1x+b_2x^2+,...,+b_nx^n$$
Therefore, $\beta$ is algebraic over $F$. 

---
#### Some Examples
1. By theorem, $\mathbb{R}(i)=\mathbb{C}$ is a vector space over $\mathbb{R}$ with basis $\{1,i\}$.

	**Show that all elements of $\mathbb{C}$ are algebraic over $\mathbb{R}$**:
	Let $\alpha = a+bi$ be chosen arbitrarily where $a,b,\in \mathbb{R}$.


---
#### Reference
- Math 110.3 Video 7.1
- Math 110.3 Lecture 7 Extension Fields Part 3