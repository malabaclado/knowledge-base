---
tags:
alias:
creation-date: Saturday 24th April 2021
last-modified-date: Wednesday 23rd February 2022 19:52:42
---

 Let $f(x)$ be a nonconstant polynomial in $F[x]$. This theorem says that even if we cannot find a zero for a polynomial in $F[x]$, we can _"extend"_ the field so as to arrive at a zero for that polynomial.

> Theorem. (**Kronecker's Theorem**)
> Let $F$ be a field and let $f(x)$ be a nonconstant polynomial in $F[x]$. Then there exists an extension field $E$ of $F$ and an $\alpha \in E$ such that $f (\alpha) = 0$.


#### Proof of  Theorem
Let $F$ be a field and let $f(x)$ be a nonconstant polynomial in $F[x]$.
<!--ID: 1645617154023-->


By theorem^[*Link a theorem to this*], $f(x)$ has a factorization in $F[x]$. Let $p(x)$ be an irreducible polynomial in the factorization of $f(x)$. 

By theorem^[Link another theorem to this], $\langle p(x) \rangle$ is a maximal ideal in $F[x]$ which implies that $F[x]/\langle p(x) \rangle$ is a field. We now show that this is field is an extension field of $F[x]$. More precisely, we show that $$F[x] \leq F[x]/\langle p(x) \rangle$$.

We do this by the use of the map $\phi:F \to F[x]/\langle p(x) \rangle$ given by $$\phi(a)=a+\langle p(x) \rangle$$

One can show that this map is a homomorphism and is a bijection^[Show this next time]. Thus, we have $F[x]$ embedded into $E=F[x]/\langle p(x) \rangle$. 

Now, we show that there is an element $\alpha\in E$ that is a zero of $f(x)$. It is sufficient to show that $p(\alpha)=0$.

Let us set $\alpha = x+ \langle p(x) \rangle$.

Now consider the evaluation homomorphism $\phi:F[x] \to E$. If $$p(x)=a_0+a_1x+...+a_nx^n$$ where $a_i \in F$, then we have $$\phi_{\alpha}(p(x))= a_0+a_i(x+ \langle p(x) \rangle)+...+a_n(x+ \langle p(x) \rangle)^n$$

But we can compute in $E=F[x]/\langle p(x) \rangle$ by choosing a representative and $x$ is a representative of the coset $\alpha=x+\langle p(x) \rangle$. Therefore, 
$$\begin{align}
p(\alpha) &= a_0 + a_1x+...+a_nx^n + \langle p(x) \rangle\\
&= p(x) + \langle p(x) \rangle \\
&= \langle p(x) \rangle \\
&=0
\end{align}$$

Thus, we have found an element $\alpha \in E$ such that $p(\alpha)= 0$ and therefore, $f(\alpha)=0$.

#### Remarks
- In the proof, we constructed the extension field to be the field $$F[x]/\langle p(x) \rangle$$  where $p(x)$ is an irreducible factor of $f(x)$
- We can think of F as an **embedding** into extension field E

- The **elements** of $E=F[x]/\langle p(x) \rangle$ are additive cosets that are of the form  $$f(x)+\langle p(x) \rangle$$ where $\langle p(x) \rangle$ is a maximal ideal.
	- More specifically, they are polynomials that are of less degree than $p(x)$. 
	- Each element $f(x)+\langle p(x) \rangle$ can be** represented by the remainder **of $p(x)|f(x)$


---
#### Some Examples
 1. $p(x)=x^2+1$ have no zero in $\mathbb{R}$. One can show that $\mathbb{C}$ is an extension field of $\mathbb{R}$ and that $p(x)$ has a zero in $\mathbb{C}$. (See Video 5.2)


2. Let $f(x)=x^4-5x^2 +6$. We have the factorization $f(x)=(x^2-2)(x^2-3)$ in $\mathbb{Q}$. Note that $f(x)$ has no zero in $\mathbb{Q}$. We can construct two extension fields using the irreducible factors of $f(x)$ where one contains a zero for $(x^2-2)$ and the other containing the zero for $(x^2-3)$

3. Consider the field $\mathbb{Z_2}$ and the irreducible polynomial $x^2+x+1 \in \mathbb{Z_2}[x]$. Note that $f(x)$ has no zero in $\mathbb{Z_2}$ but we can form the extension field $\mathbb{Z_2}[x]/ \langle x^2+x+1 \rangle$ where $\alpha = x+\langle x^2+x+1 \rangle$ is the zero of $x^2+x+1$


---
#### Reference
- Math 110.3 Course videos (5.1-5.3)
	- Video 5.1 Kronecker's Theorem and its proof
	- Video 5.2 Example 1: Construction of $\mathbb{C}$ from $\mathbb{R}[x]$
	- Video 5.3 Example 2 and 3