

### Details
**Source:**
- A First Course in Abstract Algebra (Fraleigh) 
- Course video 
	- 5.4
	- 6.1 (Existence of Irreducible Polynomial for $\alpha$)
	- 6.2 (Characterization of Extension Fields)
	- 6.3 (Some Examples; Simple Extension)
	- 6.4 (Examples)
	- 7.1 (Algebraic and Finite Extension)

---
### Notes
In this lecture, we defined [[Algebraic and Transcendental Elements]]. We say an element $\alpha$ is algebraic over a field $F$ if it is a zero of some polynomial $f(x)$ over $F$. Otherwise, it is known to be transcendental.

Next, we discuss the theorem: [[Thm. Characterization of Transcendental Elements using Evaluation Homomorphism]]. It says that an element $\alpha$ if and only if the evaluation homomorphism $\phi_{\alpha}:F[x] \to E$ is a one-to-one map.

Recall that if $\alpha$ is algebraic over F, then there exists $f(x) \in F[x]$ such that $f(\alpha)=0$. If this is the case, then there are infinitely many other polynomials over F having $\alpha$ as a zero. Among all these polynomials, the next theorem guarantees that there exists an irreducible one which generates all the others.

We summarize this idea in this theorem: [[Thm. Existence of the Irreducible Polynomial]]. Then we defined the [[Irreducible Polynomial for an element of a field F]].

Next, we examine the extension field $F(\alpha)$. We studied the theorem [[Thm. Characterization of Extension Fields]].  

It says that when $\alpha$ is algebraic, then we get $F(\alpha)$ is a field such that $$F(\alpha) \cong F[x]/  \langle irr(α, F) \rangle$$

However, when $\alpha$ is transcendental, then we only get $F(\alpha)$ an integral domain and that $$F(\alpha) \cong F(x)$$ which means that we just treat $\alpha$ as if it is an indeterminate.

Next, we defined a [[Simple Extension]] and discussed a theorem ([[Thm. Characterization of Extension Fields]]) which characterizes the elements of a simple extension.

