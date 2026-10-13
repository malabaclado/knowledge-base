
**Goal:** Assign the input vector $\text{x}$ to a class $C_k$ where $k=1,...,K$

Linear Model -> because the decision boundaries (also decision surfaces) are *linear functions of the input vector $\text{x}$*. 
- The decision boundaries are the $(D-1)$ hyperplanes within the $D$-dimentional input space.


---
Outline
- 4.1 Discriminant Functions
	- 4.1.1 For Two classes
	- 4.1.2 For Multiple classes
	- 4.1.3 Least Squares
	- 4.1.4 Fisher's linear discriminant
	- 4.1.5 Relation to least squares (of Fisher's discriminant)
	- 4.1.6 Fisher's discriminant for multiple classes
	- 4.1.7 The perceptron algorithm
- 4.2 Probabilistic Generative Models 
	- 4.2.1 Continuous Inputs (Assume that the class-conditional densities are Gaussian and then explore the resulting form for the posterior probabilities)
	- 4.2.2 Maximum likelihood solution (Once we have specified a parametric functional form for the class-conditional densities p(x|Ck), we can then determine the values of the parameters, together with the prior class probabilities p(Ck), using maximum likelihood)
	- 4.2.3 Discrete Features
	- 4.2.4 Exponential Family
- 4.3 Probabilistic Discriminative Models
	- 4.3.1 Fixed basis functions
	- 4.3.2 Logistic Regression
	- 4.3.3 Iterative Reweighted Least Squares
	- 4.3.4 Multiclass Logistic Regression
	- 4.3.5 Probit Regression
	- 4.3.6 Canonical Link Functions
- 4.4 Laplace Approximation
	- 4.4.1 Model Comparison and BIC
- 4.5 Bayesian Logistic Regression
	- 4.5.1 Laplace approximation
	- 4.5.2 Predictive distribution