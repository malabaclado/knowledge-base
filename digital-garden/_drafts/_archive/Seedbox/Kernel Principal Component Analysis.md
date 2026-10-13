
---
tags: topic/python topic/machine-learning chapter, type/concept 
alias: Kernel PCA
creation-date: Tuesday 22nd February 2022
last-modified-date: Tuesday 22nd February 2022 00:09:12
---

> Many machine learning algorithms make assumptions about the linear separability of the input data. However, if we are dealing with nonlinear problems, which we may encounter rather frequently in real-world applications, linear transformation techniques for dimensionality reduction, such as PCA and LDA, may not be the best choice.^[[[📕 Python Machine Learning (Raschka, Mirjalili)]], p. 166]


Using kernel PCA, we will learn how to transform data that is not linearly separable onto a new, lower-dimensional subspace that is suitable for linear classifiers.

# General idea of KPCA
1. Project the $d$-dimensional dataset to a higher $k$-dimensional subspace using a nonlinear mapping function.
2. Use standard PCA in this higher-dimensional space to project back to a lower-dimensional space (where samples can be separated by a linear classifier)


# Main steps of KPCA
1. Compute the kernel matrix $\text{K}$.
![[Pasted image 20220222003701.png|400]]
2. Center the kernel matrix. To do this, we use the equation:
![[Pasted image 20220222003748.png | 200]]
3. Collect the top $k$ eigenvectors of the centered kernel matrix based on their corresponding eigenvalues. In contrast to standard PCA, these eigenvectors are not principal component axes but are already the samples projected onto these axes.



---
Source:
- [[📕 O'Reilly - Python Machine Learning Cookbook (Albon, 2018)]] 
- [[📕 Python Machine Learning (Raschka, Mirjalili)]] 