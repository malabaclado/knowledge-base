> [!Theorem] 
> **Characterization of Extension Fields**
> Let $E$ be an extension of $F$ and let $\alpha \in E$ . 
> - If $\alpha$ is algebraic over $F$, then $F(α) \cong F[x]/  \langle irr(α, F) \rangle$
> - If $\alpha$ is transcendental over $F$, then $F(\alpha) \cong F[x]$

## Proof
We'll prove this theorem using direct proof. We adapt 2 cases: one where $\alpha$ is algebraic and the other when $\alpha$ is transcendental.

**Case 1**
Suppose $\alpha$ is algebraic over $F$. Then $$\ker \phi_{\alpha}=\langle irr(\alpha,F)\rangle$$

Where $\langle irr(\alpha,F)\rangle$ is a maximal ideal. This implies that $F[x]/\langle irr(\alpha,F)\rangle$ is a field and by [[First Isomorphism Theorem]], $$F[x]/\langle irr(\alpha,F)\rangle \cong Im\phi_{\alpha} $$


**Case  2^[This is still incomplete]**
Suppose $\alpha$ is transcendental over $F$. Then $$\ker \phi_{\alpha}=\{0\}$$

since there does not exist a nonzero polynomial $f(x)$ such that $f(\alpha)=0$. 

Consider the evaluation homomorphism $\phi_{\alpha}:F[x] \to E$ which maps $f(x)$ to $f(\alpha)$. Now we have the image: $$\phi_{\alpha}(F[x]) = F[\alpha]$$

Unlike in the algebraic case, here $F[\alpha]$ is just an integral domain instead a field. We can work around this by extending this domain to a field where $$F[x] \subseteq F(\alpha)$$
where $F(\alpha)$ is the smallest extension of $F$ containing $\alpha$

---
#### Some Examples
1. $\sqrt{2}\in \mathbb{R}$ is algebraic over $\mathbb{Q}$ with $irr(\sqrt{2},\mathbb{Q})=x^2-2$

	- Now, $$\mathbb{Q}(\sqrt{2}) \cong \mathbb{Q}[x]/\langle x^2-2 \rangle$$ where the elements $$a+bx+\langle x^2-2 \rangle \in \mathbb{Q}[x]/\langle x^2-2 \rangle$$ is associated with $$a+b\sqrt{2} \in \mathbb{Q}(\sqrt{2})$$

2. $i \in \mathbb{C}$ is algebraic over $\mathbb{R}$ with $irr(i,\mathbb{R})=x^2+1$

	- Now we have $$\mathbb{R}(i) \cong \mathbb{R}[x]/\langle x^2+1 \rangle$$
	
	- The field $\mathbb{R}(i)$ whose elements $a+bi$ are associated with the elements $a+bx+\langle x^2+1 \rangle$ of $\mathbb{R}[x]/\langle x^2+1 \rangle$ 
	
3. $\pi \in \mathbb{R}$ is transcendental over $\mathbb{Q}$.
	- Since $\pi$ is transcendental over $\mathbb{Q}$. Then $$\ker \phi_{\pi}=\{0\}$$ and that $\phi_{\pi}$ is one-to-one.
	
	- Now we form the **field of  rational forms** $\mathbb{Q}(\pi)$ such that $$\mathbb{Q}[x] \subseteq \mathbb{Q}(\pi)$$ whose elements are $$\frac{f(\pi)}{g(\pi)}$$ where $f, g\in \mathbb{Q}[x]$ and $g(x)\neq 0$
