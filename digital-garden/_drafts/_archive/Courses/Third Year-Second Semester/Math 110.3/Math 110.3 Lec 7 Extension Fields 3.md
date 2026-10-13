
### Details
Source:
- Math 110.3 Videos 7.1 - 7.5

### Notes
**Video 7.1**
Suppose E is an extension field of F. In this section, we examine how E can be viewed as a vector space over F. This means that a field extension will have a basis and that elements of this extension are linear combinations of these basis elements where the coefficients are coming from the base field F. We are particularly interested in a field extension with a finite basis, hence an extension E of finite degree n over F. To start, we present a theorem that deals with the simple extension F(α) of F where α is algebraic over F.

[[Thm. Extension Field as a Vector Space]]




> Definition (Algebraic Extentions)
> An extension field E of a field F is an algebraic extension of F if every element of E is algebraic over F.

> Definition (Finite Extension)
> If an extension field E of F is of finite dimension n as a vector space over F, then we say that E is a finite extension of degreen n over F and we write $[E:F]=n$ to say that the degree of E over F is n.

Remark: Given fields $E$ and $F$ where $F\leq E$
- $[E:F]=1 \Leftrightarrow E=F$
- If $[E:F]>1$, then $F$ is a proper subfield of $E$.

Examples

> Theorem
> A finite extension field E of F is an algebraic extension of F.

Remark:
- The converse of the theorem is not true.


> Theorem
> Let K be a finite  extension of E and E be a finite extension of F. Then K is a finite extension of F and $$[K:F]=[K:E][E:F]$$

Corollaries
- For $i = {1, 2, . . . , r}$, let $F_i$ be a field. Suppose $F_{j+1}$ is a finite extension of $F_j$ for $j = {1, 2, . . . , r − 1}$, then $F_r$ is a finite extension of $F_1$ and $$[F_r:F_1]=[F_r:F_{r-1}][F_{r-1}:F_{r-2}]...[F_2:F_1]$$
- Let $\alpha \in E$ be algebraic over F. If $\beta \in F(\alpha)$, then $\deg(\beta,F)| \deg(\alpha,F)$.


> Theorem.
> Let E be an algebraic extension of F.There exits a finite numebr of elements $\alpha_1,\alpha_2,...,\alpha_k$ such thet $E=F(\alpha_1,\alpha_2,...,\alpha_k)$ if and only if E is a finite extension of F.

> Definition (Algebraic Closure)
> Let $E$ be an extension field of $F$. The set $\bar{F}_E=\{\alpha \in E : \alpha is algebraic over F\}$ is called the algebraic closure of $F$ in $E$.

Remark
- $\bar{F}_E$ is a subfield of $E$.

> Definition (Algebraically Closed)
> A field F is algebraically closed if every $F[x]$ has a zero in $F$

> Theorem.
> A field F is algebraically closed if and only if evert nonconstant polynomial over F can be expressed as a product of linear polynomials.

> Corollary
> - An algebraically closed field D has no proper algebraic extensions.

> Theorem. Every field F has an algebraic closure $\bar{F}$, that is the algebraic extension $\bar{F}$ of F that is algebraically closed.











### Comments

