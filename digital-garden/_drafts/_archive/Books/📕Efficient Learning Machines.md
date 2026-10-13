---
tags: type/book 
alias:
creation-date: Thursday 9th March 2023
---

# Chapter 3. Support Vector Machines for Classification 
## Advantages of SVM

### SVM is a sparse technique
- Trained on all available data. However, once the model parameters is identified, SVM depends only on a subset of the training instances for future prediction.
- *"The complexity of the classification task with SVM depends on the number of support vectors rather than the dimensionality of the input space. The number of support vectors that are ultimately retained from the original dataset is data dependent and varies, based on the data complexity, which is captured by the data dimensionality and class separability."*


### SVM is a kernel technique
	- *SVM uses the kernel trick to map the data into a higher-dimensional space before solving the machine learning task as a convex optimization problem in which optima are found analytically rather than heuristically, as with other machine learning techniques.*
- SVM is a maximum margin separator

# Chapter 4. Support Vector Regression
- *As in classification, support vector regression (SVR) is characterized by the use of kernels, sparse solution, and VC control of the margin and the number of support vectors.*
- *One of the main advantages of SVR is that its computational complexity does not depend on the dimensionality of the input space. Additionally, it has excellent generalization capability, with high prediction accuracy.*