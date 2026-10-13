---
status: finished
---

Let $\alpha \in \mathbb{Z}_3$ be a zero of the irreducible polynomial $p(x)=x^2+x+2 \in \mathbb{Z}_3[x]$.

1. Give all the elements of $\mathbb{Z}_3(\alpha)$.

	**Solution:** Since $\deg(\alpha, \mathbb{Z})=2$, then the elements of $\mathbb{Z}_3(\alpha)$ are sum of two terms of the form $$a+b\alpha$$ where $a,b \in \mathbb{Z}_3$
	
	Thus, $$\mathbb{Z}_3(\alpha)=\{0,1,2,\alpha,2\alpha,1+\alpha,1+2\alpha,2+\alpha,2+2\alpha\}$$

2. Find the other zero of $p(x)$ in  $\mathbb{Z}_3(\alpha)$.
	- Note that since $\alpha^2+\alpha+2=0$, then $\alpha^2=-\alpha-2=2\alpha+1$. Then,
	$$\begin{align}
	p(2+2\alpha) &= (2+2\alpha)^2 +2+2\alpha +2\\
	&= 1+2\alpha+\alpha^2+2\alpha+1\\
	&=2+\alpha+(2\alpha+1)\\
	&= 3\alpha+3\\
	&=0
	\end{align}$$
	
	Hence, $2+2\alpha$ is the other zero of $p(x)$.


3. Prove that $\alpha$ is a generator of $\mathbb{Z}_3(\alpha)^*$.

Here we show that all elements of $\mathbb{Z}_3(\alpha)*=\{1,2,\alpha,2\alpha,1+\alpha,1+2\alpha,2+\alpha,2+2\alpha\}$ is a power of $\alpha$.


$\alpha^1 = \alpha$
$\alpha^2 = -\alpha-2=2\alpha+1$
$\alpha^3=(2\alpha+1)(\alpha)=2\alpha^2+\alpha=2\alpha+2$
$\alpha^4=(2\alpha+2)(\alpha)=2\alpha^2+2\alpha=\alpha+2+2\alpha=2$
$\alpha^5 = 2\alpha$
$\alpha^6 =2\alpha^2=\alpha+2$
$\alpha^7=(\alpha+2)\alpha=\alpha^2+2\alpha=2\alpha+2\alpha+1=\alpha+1$
$\alpha^8=(\alpha+1)\alpha=2\alpha+1+\alpha=1$

Indeed, $\alpha$ generates $\mathbb{Z}_3(\alpha)^*$.

4. Express $x^9-x$ as a product of irredicuble polynomials over $\mathbb{Z}_3$.
	
	**Solution:** Consider the elements of the extension field $\mathbb{Z}_3(\alpha)$.  We'll check if any of these elements is a zero of the factorization of $x^9-x$.
	
	It is easy to see that 0,1 and 2 are zeros of $x^9-x$. Dividing $x^9-x$ by $x$, $x-1$ and $x-2$, we get 
	
	$$x^9-x=x(x-1)(x-2)(x^6+x^4+x^2+1)$$

	Note that $irr(\alpha,\mathbb{Z}_3)=p(x)=x^2+x+2$ and that $\alpha^2+\alpha+2=0$. Hence, $$\alpha^2=-\alpha -2=2\alpha+1$$


	We'll show that $(1+\alpha)$ is a zero of $x^6+x^4+x^2+1$.
	$$\begin{align}
	(1+\alpha)^6+(1+\alpha)^4+(1+\alpha)^2+1 &=(1+2\alpha)+(2)+(2+\alpha)+1 \\
	&= 0
	\end{align}$$
	
	Now, let
	$$\begin{align}
	x-(1+\alpha) &=0\\
	x&=1+\alpha\\
	x^2 &=1+2\alpha+\alpha^2\\
	x^2+2x+2 &= 1+2\alpha+\alpha^2 + 2(1+\alpha) +2\\
	&=\alpha^2+4\alpha+5\\
	&=\alpha^2+\alpha+2\\
	&=0
	\end{align}$$
	
	We have $irr(1+\alpha,\mathbb{Z}_3)=x^2+2x+2$.
	Dividing ($x^6+x^4+x^2+1$) by ($x^2+2x+2$), we arrive at the factorization: 
	
	$$x^9-x=x(x-1)(x-2)(x^2+2x+2)(x^4-2x^3+x-1)$$
	
	We claim that $(2+\alpha)$ is a zero of $(x^4-2x^3+x-1)$. To verify:
	
	$$\begin{align}
	(2+\alpha)^4-2(2+\alpha)^3+(2+\alpha)-1&= (1)-2(1+2\alpha)+\alpha-1 \\
	&=1-2-\alpha+\alpha+1\\
	&=0
	\end{align}$$
	
Now we find the irreducible polynomial for $(2+\alpha)$. Let 

$$\begin{align}
x-(2+\alpha)&=0\\
x&=2+\alpha\\
x^2&=2\\
x^2+1&=2+1\\
&=0
\end{align}$$

Hence we have $irr(2+\alpha,\mathbb{Z}_3)=x^2+1$.

Dividing $(x^4-2x^3+x-1)$ by $(x^2+1)$, we get the factorization:

$$x^9-x=x(x-1)(x-2)(x^2+2x+2)(x^2+1)(x^2+x+2)$$

where the last polynomial is $irr(\alpha,\mathbb{Z}_2)=p(x)=x^2+x+2$. The above factorization are all irreducible polynomials.

	
	

---
5. Determine $irr(2\alpha,\mathbb{Z}_3)$

**Solution:** Let 
$$\begin{align}
x-2\alpha&=0 \\
x&=2\alpha \\
x^2 &= 4\alpha^2=\alpha^2 \\
2x^2&=\alpha^2+\alpha^2=\alpha^2+2\alpha+1\\
2x^2+x+1 &= \alpha^2+2\alpha+1 +2\alpha  + 1\\
&=\alpha^2+\alpha+2\\
&=0
\end{align}$$

Hence we have $irr(2\alpha,\mathbb{Z}_3)$