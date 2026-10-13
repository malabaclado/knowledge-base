
I.
1. False. There are only 16 polynomials of degree 4 over $\mathbb{Z}_2$. Let $f(x)=ax^4 + bx^3 +cx^2 +dx +e$. Fix $e=1$, there are only two integer choices for each coefficient b,c,d and e $\Rightarrow 2\times2\times2\times2=16$.
2. False. Let $f(x),g(x) \in R[x]$, $\deg fg = \deg f+\deg g \Longleftrightarrow R[x]$ is an integral domain. But $\mathbb{Z}_6[x]$ is not an integral domain.
3. False. Consider $6x+1$. This is not a unit of $\mathbb{Z}_{12}$ but is a unit in $\mathbb{Z}_{12}[x]$. Indeed, $(6x+1)(6x+1)=1$ in $\mathbb{Z}_{12}[x]$.
4. True. $\phi_i(f(x))=f(i)=(i)^4+(i)^2+1=1-1+1=1$ which is also the identity in $\mathbb{C}$.
5. False. Consider $2x^2+10$. This is reducible over $\mathbb{Z}$, since $2x^2+10=2(x^2+5)$ and 2 is nonunit. But this is irreducible in $\mathbb{Q}[x]$ since $2x^2+10$ does not have a factor of order 1 in $\mathbb{Q}[x]$.
6. False. By third crtiterion of Eisenstein's theorem is not satisfied since $p^2=4$ divides $a_0=4$.
7. False. $x^2+4=(x-2i)(x+2i)$ in $\mathbb{C}$ and by theorem, $\langle x^2+4\rangle \subseteq \langle x-2i\rangle$. Thus, the statement is false.
8. False. Consider $x^2-1\in \langle x^2-1 \rangle$ and $x^2+1 \in \langle x^2+1\rangle$, the sum $(x^2-1) + (x^2+1)=2x^2 \in \langle x^2-1 \rangle+\langle x^2+1\rangle$ but $2x^2\not \in \langle x^4-1 \rangle$.
9. False. Because 3 cannot be an expressed as a sum of two integer squares.
10. False. Consider the prime number $2\in \mathbb{Z}$. In $\mathbb{Z}_i$, 2 is reducible since $2=(1-i)(1+i)$.


II
1. First, we'll look at zeros of $f(x)$ in $\mathbb{Z}_5$.

$$\begin{align}
f(0) &= (0)^5+3(0)^4+(0)^2+(0)+4=4\\
f(1) &= (1)^5+3(1)^4+(1)^2+(1)+4=10=0\\
f(2) &= (2)^5+3(2)^4+(2)^2+(2)+4=90=0\\
f(3) &= (3)^5+3(3)^4+(3)^2+(3)+4=502=2\\
f(4) &= (4)^5+3(4)^4+(4)^2+(4)+4 = 1816=1
\end{align}$$

By Factor Theorem, $f(x)$ have factors $(x-1)$ and $(x-2)$. Dividing $f(x)$ by $(x-1)=(x+4)$ and $(x-2)=(x+3)$, we get: $$x^3-4x^2+x-3$$

==(Show that $x^3-4x^2+x-3$ is irreducible)==

2. A. Let $p=2$. Reducing the coefficients of $g(x)$ mod 2, we get: $$\bar{g}(x)=x^3+x^2+x+1$$
We have $\deg g = \deg \bar{g}$. But $\bar{g}(x)$ is reducible in  $\mathbb{Z}_2=\{0,1\}$. Indeed, 

$$\begin{align} 
\bar{g}(0) &= (0)^3+(0)^2+(0)+1 = 1\\
\bar{g}(1) &= (1)^3+(1)^2+(1)+1 = 4 = 0
\end{align}$$

Hence, Mod 2 irreducibility Test cannot be used to show irreducibility of $g(x)$ over $\mathbb{Q}$.

2. B. Let $p=3$. Reducing the coefficients of $g(x)$ mod 3, we get: $$\bar{g}(x)=2x^3+x^2+5$$ Again, we have $\deg g = \deg \bar{g}$. Now we'll check for zeros of $\bar{g}(x)$ in $\mathbb{Z}_3$: 

$$\begin{align}
\bar{g}(0) &= 2(0)^3+(0)^2+5= 5=2 \\
\bar{g}(1) &= 2(1)^3+(1)^2+5 = 8 = 2\\
\bar{g}(0) &= 2(2)^3+(2)^2+5 = 25 = 2
\end{align}$$

Since $\bar{g}(x)$ does not have any zero in $\mathbb{Z}_3$, by theorem, $\bar{g}(x)$ is irreducible in $\mathbb{Z}_3$. Hence, by Mod 3 Irreducibility Test, $g(x)$ is irreducible over $\mathbb{Q}$.

3. $$\langle x^5+2x^3\rangle \subset \langle x^4+2x^2 \rangle \subset \langle x^3+2x\rangle \subset \langle x^2+1\rangle \subset \langle x+1\rangle $$
4. A. Note that $N(\alpha) = 5^2+12^2=169$ , $N(\beta) = 8^2+1^2 = 65$ and $N(\alpha)>N(\beta)$.

Let $q,r \in \mathbb{Z}_i$ such that $\alpha=q\beta+r$.
$$q=\frac{\alpha}{\beta}=\frac{-5+12i}{8-i} = \frac{-52+91i}{65} \approx -1+i$$
$$\begin{align}
r &= \alpha -q\beta\\
  &= -5+12i -(-1+i)(8-i)\\
  &= 2+3i
\end{align}$$

Now let $q_1, r_1 \in \mathbb{Z}_i$ such that $\beta=q_1r+r_1$.
$$q_1=\frac{\beta}{r}=\frac{8-1}{2+3i}=\frac{13-26i}{13}=1-2i$$
which leaves $r_1=0$. By Euclidean Algorithm, we have $\gcd(\alpha, \beta)=2+3i$

Going back to the equation $\alpha=q\beta+r$, we get $r=\alpha-q\beta$ and hence: 
$$\begin{align}
2+3i &= (-5+12i)-(-1+i)(8-i)\\
\Rightarrow2+3i &= (1)(-5+12i) + (1-i)(8-i)
\end{align}$$

We have written the gcd as linear combination of $\alpha$ and $\beta$ with coefficients $1$ and $1-i$ respectively. 

B. Since the $2+3i$ is a divisor of $\alpha=-5+12i$,
$$\frac{-5+12i}{2+3i}= \Bigg(\frac{-5+12i}{2+3i}\Bigg)\Bigg(\frac{2-3i}{2-3i}\Bigg)=\frac{26+39i}{12}=2+3i$$ 

which gives the factorization
$$\alpha=-5+21i=(2+3i)(2+3i)$$

The norm of $2+31$, $N(2+3i)=2^2+3^2=13$ is a prime number. By theorem, $(2+3i)$ is irreducible in $\mathbb{Z}_i$.

III.
1. Let $$f(x)=a_nx^n+a_{n-1}x^{n-1}+...+a_1x+a_0,$$ be a primitive polynomial. Suppose $$g(x)=b_mx^m+b_{m-1}x^{m-1}+...+b_1x+b_0,$$  is a nonprimitive polynomial with content $k\neq 1$. Let $$\bar{g}(x)=b'_mx^m+b'_{m-1}x^{m-1}+...+b'_1x+b'_0,$$  such that $g(x)=k\bar{g}(x)$. Note that $\bar{g}(x)$ is primitive and that $f(x)\bar{g}(x)$ is also primitive. Now $$f(x)g(x)=kf(x)\bar{g}(x)=k\sum_{i=0}^{\infty} c_ix^i$$ where $c_n(x)= \sum_{j=0}^n	a_nb'_{n-i}$. Since, $f(x)\bar{g}(x)$ is primitive, $\gcd(c_0,c_1,...,c_{n-1},c_{n})=1$. Now, the set of coefficients of $f(x)g(x)$ have greatest common divisor $\gcd(kc_0,kc_1,...,kc_{n-1},kc_{n})=k$. Hence, $f(x)g(x)$ is nonprimitive.
2. Let D be an integral domain. 
- (i) For $a\in D$, $a=1\cdot a$. Since 1 is a unit in D, then a~a.
- (ii) Suppose a~b. Then there exists a unit $u\in D$ such that $a=ub \Longrightarrow u^{-1}a=b$. Since $u^{-1}$ is a unit, then b~a.
- (iii) Suppose a~b and b~c. Then there exists units $u,v \in D$ such that $a=ub$  and $b=vc$ which implies $a=uvc$. We say that $uv$ is a unit since it is a product of two units.  Therefore, a~c.



