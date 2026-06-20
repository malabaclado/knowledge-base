---
tags:
alias: ['positive definite']
creation-date: Sunday 21st May 2023
---

> [!NOTE] Definition
> A $n \times n$ complex matrix $A$ is called [[Positive definite matrix|positive definite]] if $$\mathfrak{R}[\mathrm{x}^{*} A \mathrm{x}] > 0$$
> for all nonzero complex vectors $\mathrm{x} \in \mathbb{C}^{n}$, where $\mathrm{x}^{*}$ denotes the [[conjugate transpose]] of the vector $\mathrm{x}$. 
> 
> In the case of a real matrix, the matrix $A$ is called positive definite if $$\mathrm{x}^{T} A\mathrm{x} >0$$
> where $\mathrm{x}^{T}$ denotes the transpose.

From [Positive Definite Matrix -- from Wolfram MathWorld](https://mathworld.wolfram.com/PositiveDefiniteMatrix.html)

>  Positive definite matrices are of both theoretical and computational importance in a wide variety of applications. They are used, for example, in optimization algorithms and in the construction of various linear regression models (Johnson 1970).

> A linear system of equations with a positive definite matrix can be efficiently solved using the so-called [[Cholesky decomposition]]. ==A positive definite matrix has at least one matrix square root==. Furthermore, exactly one of its matrix square roots is itself positive definite.

> Confusingly, the discussion of positive definite matrices is often restricted to only Hermitian matrices, or symmetric matrices in the case of real matrices (Pease 1965, Johnson 1970, Marcus and Minc 1988, p. 182; Marcus and Minc 1992, p. 69; Golub and Van Loan 1996, p. 140).
 
> A Hermitian (or symmetric) matrix is positive definite iff all its eigenvalues are positive. Therefore, a general complex (respectively, real) matrix is positive definite iff its Hermitian (or symmetric) part has all positive eigenvalues.

> [!NOTE]
> The determinant of a positive definite matrix is always positive, so a positive definite matrix is always nonsingular.

> [!NOTE]
> The definition of positive definiteness is equivalent to the requirement that the determinants associated with all upper-left submatrices are positive.

