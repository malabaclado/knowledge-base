⬅ [[Polynomial Rings MOC]]
# Polynomial Ring over R

> ==Definition.== (Polynomial Ring over R)
> Let R be a ring. A polynomial over a ring R is a formal sum $$f(x)=\sum_{i=0}^{\infty}a_ix^i=a_0+a_1x+a_2x^2+...$$
> where $a_i \in R$ for all i  and $a_i \neq 0$ for at most a finite number of values of i.


Remarks:
1. In this chapter, we'll generally talk about f(x) as polynomials (not as a function/mapping).
2. $a_i$ are called *coefficients* while $x$ is called *indeterminate.*
3. All elements $a\in R$ are called *constant polynomial*. We call $0\in R$ the zero polynomial. ==The degree of constant polynomials is 0, while the degree of the zero polynomial is undefined.==

---

> ==Definition.== (Equality, Sum and Product of Polynomials)
> 1. We say f(x) and g(x)are equal iff $a_i=b_i$ for all i.
> 2. The sum f(x) + g(x)  is given by $$f(x)+g(x)=\sum_{i=0}^{\infty}(a_i+b_i)x^i$$
> 3. The product of f(x) and g(x) is defined as $f(x)g(x)=\sum_{i=0}^{\infty}c_ix^i$ where $$c_n=\sum_{j=0}^n a_jb_{n-j}$$

---
> ==Theorem.== The Polynomial Ring R[x]
> The set of polynomials R[x] with coefficients from ring R is a ring under addition and multiplication of polynomials.


Remarks.
1. In this ring, the zero element is the zero polynomial $0\in R$. 
2. If $f(x)=\sum a_ix^1=$ then its inverse $-f(x)=\sum (-a_i)x^i$.
3. If the ring R is commutative, then R[x] is also commutative.
4. If the ring R has unity 1, then R[x] also has unity 1.
5. If the ring R is an integral domain, then R[x] is an integral domain.