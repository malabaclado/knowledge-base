⬅️ [[📕 Python Machine Learning (Raschka, Mirjalili)]]

# Chapter 5. Compressing data via Dimensionality Reduction
---
In this chapter, we'll learn about: ^1a2e78
- [[Concepts/Principal Component Analysis]]
- [[Linear Discriminant Analysis]]
- [[Kernel Principal Component Analysis]]



---
# Summary
In this chapter,  we learned about three different dimensionality reduction techniques: the [[Concepts/Principal Component Analysis]], [[Linear Discriminant Analysis]] and the [[Kernel Principal Component Analysis]].

Using [[Concepts/Principal Component Analysis|PCA]], we can project data to a lower-dimensional subspace to maximize the variance along the orthogonal feature axes. This method ignores class labels, hence it is an unsupervised method.

In contrast, [[Linear Discriminant Analysis|LDA]] is a supervised [[Dimensionality Reduction]] technique  which means it considers class information in the training dataset to attempt to maximize the class separability in a linear feature space.

Lastly, we learned about [[Kernel Principal Component Analysis|KPCA]] which works well for non-linear data.  Using the  kernel trick and a temporary projection into a higher-dimensional feature space, you were ultimately able to compress datasets consisting of nonlinear features onto a lower-dimensional subspace where the classes became linearly separable.


