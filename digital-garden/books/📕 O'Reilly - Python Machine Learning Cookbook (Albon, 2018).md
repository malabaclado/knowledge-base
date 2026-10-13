---
title: O'Reilly - Python Machine Learning Cookbook (Albon, 2018)
tags: type/book
creation-date: Thursday 7th July 2022
last-modified-date: Thursday 7th July 2022 13:56:34
---

## 9. Dimensionality Reduction Using Feature Extraction
- The goal of feature extraction for dimensionality reduction is to transform the set of features (the attributes of the data) such that we end up with a new set while still keeping the underlying information. 
- ### Reducing features Using Principal Components
	- Use [[Principal Component Analysis (PCA)]]  
- ### Reducing Features When Data Is Linearly Inseparable 
	- Use [[Kernel Principal Component Analysis]] 
		- [[Kernel Principal Component Analysis|Kernel PCA]] uses kernel functions to be able to project to lower dimensions where the data is linearly separable.
		- We use kernels to project the original data into a higher dimension where it is linearly separable. Then, we use PCA to reduce the dimension of the projected space.
		- One downside of [[Kernel Principal Component Analysis|Kernel PCA]] is that there are a number of parameters that needs to be specified: like `n_components`. Further, kernels come with their own hyperparameters that will have to be set. 
- ### Reducing Features by Maximizing Class Separability 
	- Use [[Linear Discriminant Analysis]]
		- [[Linear Discriminant Analysis|LDA]] works similarly to [[Principal Component Analysis|PCA]] in that it projects the feature space to a lower dimensional space. However, we were only interested in the component axes that maximizes the variance in the data, while in [[Linear Discriminant Analysis|LDA]] we have the additional goal of maximizing the differences between the classes. 
		- [Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#sphx-glr-auto-examples-decomposition-plot-pca-vs-lda-py)
		-  Here's a good reference for LDA: [Linear Discriminant Analysis (sebastianraschka.com)](https://sebastianraschka.com/Articles/2014_python_lda.html)
		- Wikipedia: [Linear discriminant analysis - Wikipedia](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- ### Reducing Features Using Matrix Factorization 
	- Use [[Non-negative Matrix Factorization (NMF)]]
		- You have a feature matrix of nonnegative values and want to reduce the dimensionality.
- ### Reducing Features on Sparse Dataset 
	-  Use [[Truncated Singular Value Decomposition (TSVD)]]



## 10. Dimensionality Reduction Using Feature Selection 
- There are three types of feture selection methods: filter, wrapper and embedded.
	- Filter methods selects the best features by examining their statistical properties.
	- Wrapper methods use trial and error to find the subset of features that produce models with the highest quality predictions. 
	- Embedded methods selects the best feature subset as part (or as an exteension) of a learning algorithm's learning process.


### Thresholding Numerical Feature Variance 
- **Problem:** You have a set of numerical features and you want to remove those with low variance.
- [[Variance Thresholding (VT)]] is motivated by the idea that features with low variance are less likely interesting (and useful) than features with high variance. 
- The process involves setting a variance threshold, calculating the variance of the feature space and eliminating features below the threshold.
- Two things to keep in mind when employing VT: 
	1. The variance is not centered, meaning, VT will not work when feature sets contain different units of measurement.
	2. The variance threshold (how much variance you allow to keep) is selected manually, so we have to use our best judgment for a good value to select. 
- Note that if the features are standardized (to mean zero and unit variance), then variance thresholding will not work. 
- ### Thresholding binary feature variance
	- **Problem**: You have a set of binary categorical features and you want to remove those with low-variance.
	- **Solution:** This is like the Variance Thresholding with numerical features, but for binary categorical features, we use the Bernoulli random variable variance.
	- **Code guide**: See [[📕 O'Reilly - Python Machine Learning Cookbook (Albon, 2018)]]
- ### Removing Irrelevant Features for Classification:
	- **Problem:** You have a categorical target vector and you want to remove uninformative features. 
	- **Solution:**
		- If the features are categorical,  calculate a chi-square statistic between each feature and the target vector. 
		- If the features are quantitative, compute the ANOVA F-value between each feature and the target vector.
- ### Recursively Eliminating Features 
	- **Use-case:** You want to recursively run your model and see which features make the model worse when dropped. If a model maintains or gains more accuracy when a feature is dropped, then that means we don't need that feature. 


