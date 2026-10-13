---
tags: type/concept  topic/machine-learning 
alias: PCA algorithm
creation-date: Saturday 19th February 2022
last-modified-date: Saturday 19th February 2022 08:49:47
---


Summary of the [[Principal Component Analysis (Algorithm)|PCA algorithm]] in a few steps:
1. Standardize the $d$-dimensional dataset
2. Construct the covariance matrix
3. Decompose the covariance matrix into its eigenvectors and eigenvalues
4. Sort the eigenvalues by decreasing order to rank the corresponding eigenvectors
5. Select $k$ eigenvectors which correspond to the $k$ largest eigenvalues, where $k$ is the dimensionality of the new feature subspace.
6. Construct a projection matrix $\text{W}$ from the "top" $k$  eigenvectors.
7. Transform the d-dimensional input dataset $\text{X}$ using the projection matrix $\text{W}$ to obtain the new k-dimensional feature subspace.


---
Eigenvectors 👉 the principal components (the direction of maximum variance)
Eigenvalues 👉 magnitude 




---
# Related
[[Covariance]]
[[Eigenvalues]] and [[Eigenvectors]]