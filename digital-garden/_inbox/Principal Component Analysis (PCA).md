---
tags: type/concept
alias: PCA
creation-date: Wednesday 6th July 2022
last-modified-date: Wednesday 6th July 2022 20:08:21
---

Principal Component Analysis (PCA) is an unsupervised linear transformation technique used in [[Feature Extraction]] and [[Dimensionality Reduction]].  [[Principal Component Analysis (PCA)|PCA]] reduces the feature dimension with the goal of keeping the variance of the dataset.

PCA helps us to **identify patterns in data based on the correlation between features.** In a nutshell, PCA aims to find the directions of maximum variance in high-dimensional data and projects it onto a new subspace with equal or fewer dimensions than the original one. The orthogonal axes (principal components) of the new subspace can be interpreted as the directions of maximum variance given the constraint that the new feature axes are orthogonal to each other.

![](https://i.imgur.com/07L0yKA.png)

We use PCA in dimensionality reduction by projecting each data point onto only the first few principal components to obtain lower-dimensional data while preserving as much of the data's variation as possible. 

**PCA is most commonly used** when many of the variables are highly correlated with each other and it is desirable to reduce their number to an independent set.

Note that the PCA directions are **highly sensitive to data scaling**, and **we need to standardize the features prior to PCA** if the features were measured on different scales and we want to assign equal importance to all features.

---
- Wikipedia: [Principal component analysis - Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)
- [[Principal Component Analysis (Algorithm)]] 