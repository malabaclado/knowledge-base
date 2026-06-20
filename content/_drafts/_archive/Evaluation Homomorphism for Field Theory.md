⬅ [[Polynomial Rings MOC]]
# Evaluation Homomorphism for Field Theory

> ==Theorem.==
> Suppose F is a subfield of field E and $\alpha \in E$.
> 
> The mapping $\phi_{\alpha}: F[x] \to E$ given by $$\phi_{\alpha}(a_0+a_1x+,...,a_nx^n)=a_0+a_1\alpha+,...,a_n \alpha^n$$


Remarks:
1. This mapping takes a polynomial as input then evaluates it at $\alpha$.
2. $\phi_{\alpha}(f(x))$ is called the ==value== and is denoted by $f(\alpha)$.
3. $\alpha$ is a ==zero== of f(x) iff $f(\alpha)=0$
4. The range of $\phi_{\alpha}$ is given by the set $$\{f(\alpha): f(x) \in F[x]\}$$
5. The kernel of $\phi_{\alpha}$ is given by $$\{f(x)\in F[x] | f(\alpha)=0=\}$$