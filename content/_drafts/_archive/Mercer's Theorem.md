If the [[Gram matrix]] is [[Positive definite matrix|positive definite]], we can compute an eigenvector decomposition of the Gram matrix as: $$\mathrm{K}=U^{T}\Lambda U$$
where $$\Lambda =diag(\lambda_{1}, ..., \lambda_{n}) $$

> [!NOTE] 
> Note that $\lambda_{i}$ is the $i$-th eigenvalue of $\mathrm{K}$ and will be greater than 0 because the matrix is positive definite.

---
Consider an element of $\mathrm{K}$, we have a dot product between two vectors $$\mathrm{K}_{ij}=\left(\Lambda^{\frac{1}{2}}U_{;, i}\right)^{T}\left(\Lambda^{\frac{1}{2}}U_{;, j} \right)$$
Define $\phi(\mathrm{x}_{i})=\Lambda^{\frac{1}{2}} U_{ :,i}$. Then the equation above can be written as a $$\mathrm{K}_{ij}=\phi(\mathrm{ x}_{i})^{T} \phi(\mathrm{ x}_{j })$$

This means that each element of the kernel can be described as the inner product of a function $\phi(\cdot)$ applied to objects $\mathrm{x}, \mathrm{x}^{'}$.  





---
See also:
- [[Mercer's Kernel]]