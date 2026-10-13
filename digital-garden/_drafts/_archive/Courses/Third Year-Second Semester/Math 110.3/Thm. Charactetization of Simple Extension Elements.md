---
tags:
alias:
creation-date: Tuesday 11th May 2021
last-modified-date: Saturday 16th October 2021 12:52:33
---

# Thm. Charactetization of Simple Extension Elements

> Theorem. (**Charactetization of Simple Extension Elements**)
> Let $\alpha$ be algebraic over $F$ and let $E=F(\alpha)$ be a simple extension  of $F$.
> If the $\deg(\alpha,F)=n$, then all elements $\beta \in E$ can be uniquely expressed as $$\beta = b_0 + b_1\alpha +...+ b_{n-1}\alpha^{n-1}, \quad b_i \in F$$

#### Proof of Theorem
Since $\alpha$ is algebraic, by theorem^[[[Thm. Existence of the Irreducible Polynomial]]], there exists an irreducible polynomial $p(x)$ (that we can always choose to be monic) such that $p(\alpha)=0$. So for $c_i \in F$, we have $$p(\alpha)=\alpha^n + c_{n-1}\alpha^{n-1} +...+c_1\alpha+c_0=0$$ isolating $\alpha^n$ on one side, we get
$$\alpha^n=-c_{n-1}\alpha^{n-1} -...-c_1\alpha-c_0$$

Suppose we take a polynomial $f(x)$ from the simple extension $E$.We present two cases: either $\deg f < n$ or $\deg f \geq n$. 

- Suppose $\deg f < n$. Then $f(\alpha)$ is of the form $$f(\alpha) = a_0 + a_1\alpha +...+a_{n-1}\alpha^{n-1}$$ and we are done.

- Suppose $\deg f \geq n$. Then $f(\alpha)$ is of the form $$f(\alpha) = a_0 + a_1\alpha +...+a_{n-1}\alpha^{n-1}+a_n\alpha^n + a_{n+1}\alpha^{n+1}+...+a_{m}\alpha^{m}, m=\deg f$$ And we have elements of $f(\alpha)$ that are have degree more than or equal to $n$. Now these elements always have a factor $\alpha^n$. In this case, substitute $$\alpha^n=-c_{n-1}\alpha^{n-1} -...-c_1\alpha-c_0$$ and eventually, you'll reduce all elements to be of degree less than or equal to $n$.


**Proof of Uniqueness**
Suppose we can express the polynomial $\beta \in E$ in the form:
$$\begin{align}
\beta &= b_0 +b_1\alpha+...+b_{n-1}\alpha^{n-1} \\
&= d_0 +d_1\alpha +...+ d_{n-1}\alpha^{n-1}
\end{align}$$
By reflexivity, we get:
$$\beta = (b_0 -d_0) + (b_1 -d_1)\alpha +...+(b_{n-1}-d_{n-1})\alpha^{n-1} $$

We know that $\beta({\alpha})=0$, we can think of the above expression as a polynomial $$g(\alpha) =(b_0 -d_0) + (b_1 -d_1)\alpha +...+(b_{n-1}-d_{n-1})\alpha^{n-1}  = 0$$

This was saying that $\alpha$ is a zero of $g(\alpha)$ where $\deg g=n-1$. This is a contradiction because the smallest irreducible polynomial $p(x)$ that we have previously defined is the polynomial of smallest degree whose degree $\deg p = n$.  There cannot exist another nonzero polynomial $g(x)$ such that $g(\alpha)=0$ and degree less than $n$. Therefore, $\beta$ must be uniquely expressed.

#### Some Examples
1. We know that $\deg(i,\mathbb{R})$=2 since $irr(i,\mathbb{R})=x^2+1$.
	- By theorem, the elements of $\mathbb{R}(i)$ are of the form $$a+bi$$ such that $a,b \in \mathbb{R}$.
	- Indeed, these are the elements of the set of complex numbers $\mathbb{C}$.

2. We know that $irr(\sqrt{2},\mathbb{Q})=x^2-2$ so that $\deg(\sqrt{2},\mathbb{Q})=2$.
	- The elements of the simple extension $\mathbb{Q}(\sqrt{2})$ are of the form $$a+b\sqrt{2}$$ where $a,b, \in \mathbb{Q}$

3. Note that $\sqrt{3}$ is not an element of $\mathbb{Q}(\sqrt{2})$. By theorem^[[[Kronecker's Theorem]]] ^[[[Thm. Charactetization of Simple Extension Elements]]], $\mathbb{Q}(\sqrt{2})(\sqrt{3})$ is a simple extension of $\mathbb{Q}(\sqrt{2})$. Its elements are of the form $$a+b\sqrt{3}$$ where $a,b \in \mathbb{Q}(\sqrt{2})$. Hence these take the form $$(c+d\sqrt{2})+(e+f\sqrt{2})\sqrt{3}$$ where $c,d,e,f \in \mathbb{Q}$ which can be reduced to $$c+d\sqrt{2}+e\sqrt{3}+f\sqrt{6}$$
