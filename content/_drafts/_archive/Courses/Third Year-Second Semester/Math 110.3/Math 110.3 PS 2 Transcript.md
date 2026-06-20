###### I. Explain clearly why the given statement is false
1. There is a field with 36 elements.
	
	Every finite field is of order $p^n$ for some prime $p$ but $36=2^23^2$ cannot be expressed as a power of a prime, hence, there cannot exist a field with 36 elements.
2. There exists a degree 4 irreducible polynomial in $\mathbb{C}[x]$.
	
	Every polynomial $f(x)$ in $\mathbb{C}[x]$ can be expressed as a product of linear polynomials since $\mathbb{C}$ is an algebraically closed field. Thus, there does not exist a degree 4 irreducible polynomial in $\mathbb{C}$.
3. All the zeros of $x^3 − 2$ are found in $\mathbb{Q}(\sqrt[3]{2})$.


	$$\begin{align}
	(\sqrt[3]{2}i)^3-2&=-2(-i)
	\end{align}

4. The element $π^5$ is transcendental over $\mathbb{Q}(\pi^3)$.

	Let $\alpha=\pi^5$,

	$$\begin{align}
	\alpha&=\pi^5\\
	\alpha^3&=\pi^{15}\\
	\alpha^3-\pi^{15}&=0
	\end{align}$$
	
	The polynomial $f(x)=x^3-\pi^{15} \in \mathbb{Q}(\pi^3)[x]$ is zero at $\alpha=\pi^5$. Hence, $\pi^5$ is algebraic over  $\mathbb{Q}(\pi^3)$ which makes the statement false.
	

###### II. Do as asked.
1. Give the smallest extension of $Q$ that contains the zeros of $x^4-7x^2+10$.

	**Solution:** The zeros of $x^4-7x^2+10=(x^2-2)(x^2-5)$ are $\sqrt{2}$ and $\sqrt{5}$ . Hence, the smallest extension of $\mathbb{Q}$ that contains these zeroes is $\mathbb{Q}(\sqrt{2},\sqrt{5})$.

2. Let p be a prime. Give all the subfields of $F_{p^{20}}$ and sketch its subfield lattice.

	**Solution:** The subfields of $\mathbb{F}_{p^{20}}$ are  of the form $\mathbb{F}_{p^m}$ where $m|20$. These are: $\mathbb{F}_{p^{20}}$, $\mathbb{F}_{p^{10}}$, $\mathbb{F}_{p^{5}}$,$\mathbb{F}_{p^{4}}$, $\mathbb{F}_{p^{2}}$, and $\mathbb{F}_{p}$.
	
	The lattice diagram is as follows: *insert image here*

3. Let $a=\sqrt{3+2\sqrt{2}}$. Show that $[\mathbb{Q}(a):\mathbb{Q}]=2$.



4. Let $\alpha=\sqrt[4]{2}i$. Give polynomials of degree 1,2 and 4 over $\mathbb{C}, \mathbb{R}$ and $\mathbb{Q}$, respectively, that have $\alpha$ as zero.

	The $irr(\alpha,\mathbb{C})=x-\sqrt[4]{2}i$ is the smallest irreducible polynomial in $\mathbb{C}$ that have zero of $\alpha$. In $\mathbb{C}$, we have the following polynomials that has a zero at $\alpha$:
	
	degree 1: $x-\sqrt[4]{2}i$
	degree 2: $x^2-\sqrt[4]{2}ix$
	degree 3: $x^4-\sqrt[4]{2}ix^3$
	
	Now considering only real coefficients,
	
	$$\begin{align}
	\alpha&=\sqrt[4]{2}i \\
	\alpha^2&=-\sqrt{2}\\
	\alpha^2+\sqrt{2}&=0
	\end{align}$$
	
	So the smallest degree irreducible polynomial with zero $\alpha$ in $\mathbb{R}$ is $irr(\alpha,\mathbb{R})=x^2+\sqrt{2}$ which is a degree 2 polynomial. Thus, there is no degree 1 polynomial in $\mathbb{R}$ that have a zero $\alpha$. A degree 4 polynomial with zero $\alpha$ in $\mathbb{R}$ could be $(x^4+\sqrt{2}x^2)$.
	
	This time, considering only rational coefficients,

	$$\begin{align}
	\alpha&=\sqrt[4]{2}i \\
	\alpha^4&=2\\
	\alpha^4-2&=0
	\end{align}$$
	
	Thus, the smallest degree irreducible polynomial with zero $\alpha$ in $\mathbb{Q}$ is given by $irr(\alpha,\mathbb{Q})=x^4-2$ which is a degree 4 polynomial. Hence, there is no degree 1 or degree 2 polynomial in $\mathbb{Q}$ for which $\alpha$ is a zero.
	
	
	
###### III. Let $F=\mathbb{Q}(\sqrt{3}+i)$
1. Show that $F=\mathbb{Q}(\sqrt{3},i)$.

	We would want to show that $\mathbb{Q}(\sqrt{3},i)=\mathbb{Q}(\sqrt{3}+i)$.
	
	Note that $\sqrt{3}+i \in \mathbb{Q}(\sqrt{3},i)$ so that $\mathbb{Q}(\sqrt{3}+i)\subseteq \mathbb{Q}(\sqrt{3},i)$.
	
	Thus, we have the subfield relationship as follows:
	
	$$\mathbb{Q} \leq \mathbb{Q}(\sqrt{3}+i)\leq \mathbb{Q}(\sqrt{3},i)$$
	
	We know that $[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}]=4$ since it can be constructed by adjoining $i$ to the field  $\mathbb{Q}(\sqrt{3})$ using the polynomial $x^2+1$ and that $\deg(i,\mathbb{Q}(\sqrt{2}))=2$ and $\deg(\sqrt{2},\mathbb{Q})=2$ so that 
	
	$$[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}]=[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}(\sqrt{3})][\mathbb{Q}(\sqrt{3}):\mathbb{Q}]=(2)(2)=4$$
	
	Now let
	$$\begin{align}
	\alpha&=\sqrt{3}+i\\
	\alpha^2&= 3-2\sqrt{3}i-1\\
	\alpha^2-2&=-2\sqrt{3}i\\
	(\alpha^2-2)^2&=-12\\
	\alpha^4-4\alpha^2+16=0
	\end{align}$$
	
	Then the $irr(\sqrt{3}+i,\mathbb{Q})=x^4-4x^2+16$ and $\deg(\sqrt{3}+i,\mathbb{Q})=4$ so that 
	
	$$[\mathbb{Q}(\sqrt{3}+i):\mathbb{Q}]=4$$
	
	By theorem, we have $$[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}]=[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}(\sqrt{3}+i)][\mathbb{Q}(\sqrt{3}+i):\mathbb{Q}]$$
	
	But we have shown above that $[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}]=[\mathbb{Q}(\sqrt{3}+i):\mathbb{Q}]=4$ which leaves $$[\mathbb{Q}(\sqrt{3},i):\mathbb{Q}(\sqrt{3}+i)]=1$$
	
	Which implies that $\mathbb{Q}(\sqrt{3},i)=\mathbb{Q}(\sqrt{3}+i)$.
	
	
	

2. List all the proper subfields of F containing $\mathbb{Q}$. Sketch the subfield lattice of F.

	As mentioned above, we construct $F=\mathbb{Q}(\sqrt{3},i)$ by adjoining $i$ to the field $\mathbb{Q}(\sqrt{3})$. Thus, $\mathbb{Q}(\sqrt{3})$ and $\mathbb{Q}$ are the proper subfields of F. The subfield lattice is as shown below:
	
	*insert image here*

3. Give an extension E of F such that $[E:F]=3$. Give a basis for E over F.

	We'll construct such field by adjoining $F=\mathbb{Q}(\sqrt{3},i)$ with $\sqrt[3]{5}$. The smallest degree irreducible polynomial for $\sqrt[3]{5}$ over $F=\mathbb{Q}(\sqrt{3},i)$ is given by $x^3-5$. Thus $$[\mathbb{Q}(\sqrt{3},\sqrt[3]{5},i):\mathbb{Q}(\sqrt{3},i)]=\deg(\sqrt[3]{5},\mathbb{Q}(\sqrt{3},i))=3$$
	
	The field $\mathbb{Q}(\sqrt{3},\sqrt[3]{5},i)$ is a vector space of degree 12 and with basis: 
	
	$$\{1,\space 3^\frac{1}{3},\space i,\space 5^\frac{1}{3},\space 5^\frac{2}{3},\space 3^\frac{1}{3}i,\space 5^\frac{1}{3}i,\space 5^\frac{2}{3},\space3^\frac{1}{3}5^\frac{1}{3},\space 3^\frac{1}{3}5^\frac{2}{3},\space3^\frac{1}{3}5^\frac{1}{3}i,\space 3^\frac{1}{3}5^\frac{2}{3}i\}$$

###### IV. Let $a=\bar{\mathbb{Z}}_3$ be a zero of the irreducible polynomial $f(x)=x^2+2x+2$ in $\mathbb{Z}_3[x]$.

1. Give all the elements of the set $\mathbb{Z}_3(a)$.

	The elements of  $\mathbb{Z}_3(a)$ is are $\{ 0,1,2,a,2a,1+a,1+2a,2+a,2+2a\}$

2. Find the other zero of $f(x)$ in $\mathbb{Z}_3(a)$.

	Since $f(a)=a^2+2a+2=0$, then
	
	$$\begin{align}
	a^2&=-2x-2\\
	&=a+1
	\end{align}$$
	
	This result is critical to our computations in this item as well as in items IV. 3 and IV.4.

	$$\begin{align}
	(1+2a)^2+2(1+2a)+2&=1+4a+4a^2+2+4a+2\\
	&=1+a+a^2+2+a+2\\
	&=1+a+(a+1)+2+a+2\\
	&=6+3a\\
	&=0
	\end{align}$$

	Hence, the other zero of $f(x)$ is $(1+2a)$.

3. By trial and error, give the two zeros in $\mathbb{Z}_3(a)$ for each of $g(x) = x^2 + 1$ and $h(x) = x^2 + x + 2$, the other two monic irreducible quadratic polynomials over $\mathbb{Z}_3$.


	$$\begin{align}
	g(1+2a)&=(1+2a)^2 + 1\\
	&=1+4a+4a^2+1\\
	&=a+a+a^2+1\\
	&=1+2a+(a+1)+1\\
	&=3a+3\\
	&=0
	\end{align}$$
	
	$$\begin{align}
	g(2+2a)&=(2+2a)^2 + 1\\
	&=4+8a+4a^2+1\\
	&=1+2a+a^2+1\\
	&=1+2a+1+a+1\\
	&=3+3a\\
	&=0
	\end{align}$$
	
	$$\begin{align}
	h(2+a)&=(2+a)^2+(2+a)+2\\
	&=4+4a+a^2+2+a+2\\
	&=1+a+a+1+2+a+2\\
	&=3a+6\\
	&=0
	\end{align}$$
	
	$$\begin{align}
	h(2a)&=(2a)^2+(2a)+2\\
	&=4a^2+2a+2\\
	&=a^2+2a+2\\
	&=a+1+2a+2\\
	&=3a+3\\
	&=0
	\end{align}$$
	
	Therefore, the $(1+2a)$ and $(2+2a)$ are the zeros of $g(x)$ in $\mathbb{Z}_3(a)$. While $(2+a)$ and $(2a)$ are the zeros of $h(x)$ in $\mathbb{Z}_3(a)$.
	
	
	
4. Express each nonzero element of $\mathbb{Z}_3(a)$ as a power of $a$.

	In this item, we repeatedly use the above result : $a^2=a+1$.

	$$\begin{align}
	a^1&=a\\
	a^2&=a^2=1+a\\
	a^3&=a(1+a)=a+a^2=a+1+a=1+2a\\
	a^4&=(1+a)^2=1+2a+a^2=1+2a+a+1=2\\
	a^5&=a^4(a)=2a\\
	a^6&=a^4a^2=2(1+a)=2+2a\\
	a^7&=a^4a^3=2(1+2a)=2+4a=2+a\\
	a^8&=(a^4)^2=(2)^2=4=1
	\end{align}$$
	
	

###### V. Let E be a field whose elements are the distinct zeros of $x^{16} − x$ in $\bar{\mathbb{Z}}_2$.
1. If $\alpha \in E$ is a generator of the multiplicative group $E^{∗}$ , give the subgroup of $E^{∗}$ with 5 elements. (Write the elements in the subgroup as powers of $\alpha$.)

	Since the elements of $E$ are the zeros of the polynomial $x^{2^4}-x \in \mathbb{Z}_2[x]$, then $E=\mathbb{F}_{2^4}$ which is a field of order 16. By theorem, the multiplicative group $E^*=\mathbb{F}_{2^4}^*$ is a cyclic group of order 15. 
	
	Suppose $\alpha$ is a generator of $E^*$. We can form a subgroup of $E^*$ with 5 elements given by:

$$\{\alpha^3, \alpha^6, \alpha^9, \alpha^{12}, \alpha^{15}=1\}$$

2. Give all the primitive 15th roots of unity in E. (Give the roots as powers of $\alpha$.)

	The number of primitive 15th roots of unity in E is given by the Euler-Phi function:
	
	$$\phi(15)=\phi(3)\phi(5)=2\cdot 4=8$$
	
	These are the elements $\alpha^m$ where $m$ is relatively prime prime to 15 which are precisely the elements: $\{\alpha, \alpha^2, \alpha^4, \alpha^7, \alpha^8, \alpha^11,\alpha^{11}, \alpha^{13},\alpha^{15} \}$
	

3. If $\beta \in E\backslash\mathbb{Z}_2$  such that $f(\beta) = 0$ for some degree 3 polynomial $f(x)$ over $\mathbb{Z}_2$, determine $\deg(\beta,\mathbb{Z}_2)$.

