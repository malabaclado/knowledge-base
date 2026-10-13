
(1) Prove that for any complex numbers $z$ and $w$ we have $|zw| = |z||w|$.

Solution:  Let $z=a+bi, \space w = c+di$ for some $a,b,c,d \in \mathbb{R}$. We have $|z| = \sqrt{a^2 + b^2}$ and $|w| = \sqrt{c^2 + d^2}$.

$$\begin{align}
|zw| &= |(a+bi)(c+di)|\\
&= |(ac-bd)+i(ad+bc)|\\
&= \sqrt{(ac-bd)^2+(ad+bc)^2}\\
&= \sqrt{a^2c^2 +b^2d^2 + a^2d^2+b^2c^2}\\
&= \sqrt{a^2(c^2+d^2)+b^2(c^2+d^2)}\\
&= \sqrt{(a^2+b^2)(c^2+d^2)}\\
&= \sqrt{(a^2+b^2)} \sqrt{(c^2+d^2)}\\
&= |z||w|
\end{align}$$

---

(2) Prove that any complex number of modulus 1 is of the form $e^{i\theta}$ for some $\theta \in \mathbb{R}$.

Solution: Suppose $z \in \mathbb{C}$ with polar coordinates $(r,\theta)$, where $r,\theta \in \mathbb{R}$. Suppose $|z|=1$. Then $r=1$ and that:

$$z = \cos \theta + i \sin \theta$$

Using following result from (5) of Lecture 2.5:
$$e^{iy}=\cos y + i\sin y$$

we get: $$z = \cos \theta + i \sin \theta=e^{i\theta}, \space\theta\in \mathbb{R}$$

---
(3)	 Let $P(z)$ be a polynomial with real coefficients. Show that zeros of P come in conjugate pairs. In addition, show that if P is of odd degree then P must have a real zero.

Solution: Denote the coefficients of P(z) as $a_i\in \mathbb{R},, \space i=0,1,...,n$.

Suppose $c \in \mathbb{C}$ is a zero of $P(z)$.  Then 
$$P(c) = a_0 +a_1c +a_2c^2 +,...,+a_nc^n=0$$

Note that $\overline{a_i}=a_i$ for all coefficients $a_i \in \mathbb{R}$ of P so that the product $\overline{a} \overline{z} = \overline{az}$ for any $z\in \mathbb{C}$. In addition, we have the property $\overline{z}^k =\overline{z^k}$ for any $k\in \mathbb{N}$.

Let $\bar{c}$ be the complex conjugate of $c$. Then,

$$\begin{align}
P(\overline{c}) &= a_0 +a_1\overline{c} +a_2\overline{c}^2 +,...,+a_n\overline{c}^n\\
&= \overline{a_0} +\overline{a_1 c} +\overline{a_2 c^2} +,...,+\overline{a_n c^n}\\
&= \overline{a_0 +a_1c +a_2c^2 +,...,+a_nc^n}\\
&= \overline{P(c)}\\
&= \overline{0}\\
&=0
\end{align}$$

Therefore, for any zero $c$  of $P(z)$, the conjugate $\overline{c}$ is also a zero of $P(z)$.

Suppose $P(z)$ is a polynomial of degree $m\in \mathbb{N}$ where $m$ is an odd number. By the Fundamental Theorem of Algebra, P(z) has $m$ complex roots. We just proved that for any zero $c$  of $P(z)$, the conjugate $\overline{c}$ is also a zero of $P(z)$. But since is $m$ odd, at least one of these complex root $c'$ that have no pair and thus, it must be that case that $c'=\overline{c'}$ which would only happen when $c'$ is a real number. Indeed, whenever $P(z)$ is of odd degree then $P(z)$ must have a real zero.

---
(4) For any $z \in \mathbb{C}$, define
$$\sin z = \frac{1}{2i}(e^{iz}-e^{-iz}), \qquad \cos z = \frac{1}{2} (e^{iz}+e^{-iz})$$

Show that:

A. $\sin^2 z  + \cos^2 z = 1$

$$\begin{align}
\sin ^2z  &= \Big( \frac{1}{2i}(e^{iz}-e^{-iz})\Big) \Big(\frac{1}{2i}(e^{iz}-e^{-iz}) \Big)\\
&= -\frac{1}{4} (e^{2iz}-2+e^{-2iz})\\
&= -\frac{1}{4} (e^{2iz}+e^{-2iz}) + \frac{1}{2}
\end{align}$$

$$\begin{align}
\cos ^2z  &= \Big( \frac{1}{2}(e^{iz}+e^{-iz})\Big) \Big(\frac{1}{2}(e^{iz}+e^{-iz}) \Big)\\
&= \frac{1}{4} (e^{2iz}+2+e^{-2iz})\\
&= \frac{1}{4} (e^{2iz}+e^{-2iz}) + \frac{1}{2}
\end{align}$$

$$
\sin ^2z +\cos ^2z  = \Big( -\frac{1}{4} (e^{2iz}+e^{-2iz})  + \frac{1}{4} (e^{2iz}+e^{-2iz}) + \frac{1}{2} + \frac{1} {2}\Big) =1
$$

B. $\sin 2z = 2\sin z \cos z$

$$\sin 2z = \frac{1}{2i}(e^{2iz}-e^{-2iz})$$

We have a difference of two squares: $(e^{2iz}-e^{-2iz})= (e^{iz}-e^{-iz})(e^{iz}+e^{-iz})$.

$$\begin{align}
\sin 2z &= \frac{1}{2i} (e^{iz}-e^{-iz})(e^{iz}+e^{-iz})\\
&= 2 \Big(\frac{1}{2i} \Big) \Big( \frac{1}{2}\Big)(e^{iz}-e^{-iz})(e^{iz}+e^{-iz})\\
&= 2\Big[ \frac{1}{2i} (e^{iz}-e^{-iz})\Big] \Big[ \frac{1}{2} (e^{iz}+e^{-iz})\Big]\\
&= 2 \sin z \cos z
\end{align}$$

C. $\frac{\partial}{\partial z} \sin z = \cos z$

$$\begin{align}
\frac{\partial}{\partial z} \sin z &= \Big[\frac{1}{2} \Big(  \frac{\partial}{\partial x} - i \frac{\partial}{\partial y}\Big) \Big] \Big[\frac{1}{2i}(e^{iz}-e^{-iz}) \Big]\\
&= \frac{1}{4i} \Big( \frac{\partial}{\partial x} e^{iz}- \frac{\partial}{\partial x} e^{-iz}-  i\frac{\partial}{\partial y}e^{iz} + i\frac{\partial}{\partial y} e^{iz}\Big)\\
&= \frac{1}{4i} \Big( ie^{iz} + ie^{-iz}+ ie^{iz} + ie^{-iz}\Big)\\
&= \frac{1}{4i} \Big( 2ie^{iz} + 2ie^{-iz} \Big)\\
&= \frac{2i}{4i} \Big( ie^{iz} + ie^{-iz}\Big)\\
&= \frac{1}{2i}\Big( ie^{iz} + ie^{-iz}\Big)\\
&= \cos z
\end{align}$$

---
(5) Find all holomorphic functions $f=u+iv$ with $u(x,y)=x^2-y^2$.

Solution: 
$$\begin{align}
\Delta u &= \frac{\partial^2}{\partial x^2} u + \frac{\partial^2}{\partial y^2} u\\
&= \frac{\partial}{\partial x} (2x)+ \frac{\partial}{\partial y} (-2y)\\
&= 2 - 2 \\
&= 0
\end{align}$$

This ensures that $u(x,y)$ is harmonic. Now, we'll find a function $v(x,y)$ that satisfies the Cauchy-Riemann equations:

$$\frac{\partial v}{\partial y} = \frac{\partial u }{\partial x} = 2x$$
$$\frac{\partial v}{\partial x} = -\frac{\partial u }{\partial y} = 2y$$

Now, $$v(x,y) = \int{\frac{\partial v}{\partial y}}dy=\int{2xdy} =2xy + \phi(x)$$

Then $$\frac{\partial }{\partial x}v(x,y) = \frac{\partial }{\partial x}(2xy + \phi(x)) = 2y + \phi'(x) = 2y$$

Thus, we have $\phi'(x)=0$ and $\phi(x)=C$ where  $C$ is a constant.

Therefore, we have $$v(x,y)= 2xy + C$$ and 
$$f(z) = x^2-y^2 + i(2xy + C)$$ where $C$ is a constant.

---
(6) We know that if a function $f = u+vi$ is holomorphic, the it is harmonic (from (11) Lecture 3). In addition, if $f$ is harmonic, then both $u,v$ are also harmonic. By contrapositive of both of these statements, we say that if either the real part $u(x,y)$ or the imaginary part $v(x,y)$ is of a function $f$ is non-hamonic, then $f$ is non-holomorphic.

We will show that no holomorphic function $f = u+iv$ with real part $u(x,y)=x^2+y^2$ exists by showing that $u(x,y)$ is not harmonic.


$$\begin{align}
\Delta u(x,y) &= \frac{\partial^2}{\partial x^2} u(x,y) + \frac{\partial^2}{\partial y^2}u(x,y) \\
&= \frac{\partial^2}{\partial x^2} (x^2+y^2) + \frac{\partial^2}{\partial y^2} (x^2+y^2)\\
&= \frac{\partial}{\partial x} (2x)+ \frac{\partial}{\partial y} (2y)\\
&= 2+2\\
&= 4 \\
\end{align}$$

Since $\Delta u(x,y) \neq 0$ , $u(x,y)$ is indeed not harmonic. Thus, proving the statement.

(7) Is the function $f(z) =|z$| holomorphic?

Solution: Let $z= x+iy$. Then , the polynomial $$f(z)= \sqrt{x^2+y^2}$$
have a real part $u(x,y)=\sqrt{x^2+y^2}$ and imaginary part $v(x,y)=0$  such that $f=u+iv$.


Note that the function $f$ does not satisfy the Cauchy-Riemann Equations. Indeed,
$$\frac{\partial v}{\partial y} = 0 \neq \frac{2x}{\sqrt{x^2+y^2}}=\frac{\partial u }{\partial x} $$
$$\frac{\partial v}{\partial x} = 0 \neq -\frac{2y}{\sqrt{x^2+y^2}}=-\frac{\partial u }{\partial y} $$

And thus, $f$ is non-holomorphic.