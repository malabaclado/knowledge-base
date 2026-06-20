---
tags: type/concept, topic/machine-learning 
alias: LDA
creation-date: Friday 18th February 2022
last-modified-date: Saturday 19th February 2022 00:35:43
---
> The general concept behind LDA is very similar to PCA. Whereas PCA attempts to find the orthogonal component axes of maximum variance in a dataset, the goal in LDA is to find the feature subspace that optimizes class separability.^[[[📕 Python Machine Learning (Raschka, Mirjalili)]], p. 155]


[[Linear Discriminant Analysis]] is a supervised dimensionality reduction method. 

![[Pasted image 20220221234557.png]]



## Assumptions for [[Linear Discriminant Analysis]]:
1. The data is normally distributed.
2. The classes have identical covariance matrices.
3. The features are statistically independent of each other.


>   However, even if one or more of those assumptions are (slightly) violated, LDA for dimensionality reduction can still work reasonably well.^[Pattern Classification 2nd Edition , R. O. Duda, P. E. Hart,  
and D. G. Stork, New York, 2001]

## Main steps of [[Linear Discriminant Analysis|LDA]]
1. Standardize the $d$-dimensional dataset.
2. For each class, compute the $d$-dimensional mean vector.
3. Construct the between-class scatter matrix $S_{B}$ and the within-class scatter matrix $S_{W}$.
4. Compute the eigenvectors and the corresponding eigenvalues of the matrix $S^{-1}_{W} S_{B}$.
5. Sort the eigenvalues by decreasing order to rank the corresponding eigenvectors.
6. Construct the $k$ eigenvectors that corresponds to the $k$ kargest eigenvalues to construct a $d\times k$-dimensional transformation matrix $\text{W}$. The eigenvectors are the columns of this matrix.
7. Project the samples onto the new feature subspace using the transformation matrix.




---
- [[📕 O'Reilly - Python Machine Learning Cookbook (Albon, 2018)]]
- [[📕 Python Machine Learning (Raschka, Mirjalili)]]
- 

