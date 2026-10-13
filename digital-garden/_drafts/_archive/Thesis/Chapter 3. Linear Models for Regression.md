
The goal of regression is to predict the value  
of one or more continuous target variables t given the value of a D-dimensional vec-  
tor x of input variables.

# Outline

- **3.1 Linear Basis Function Models**
	- Linear regression
	- Basis functions
	- **3.1.1 Maximum Likelihood and Least Squares**
		- Normal equations
		- Moore-Penrose pseudo-inverse
	- **3.1.2 Geometry of Least Squares**
		- Singular Value Decomposition (SVD)
	- **3.1.3 Sequential Learning**
		- Stochastic Gradient Descent
		- Least Mean Squares algorithm
	- **3.1.4 Regularized Least Squares**
		- Weight decay
		- Parameter shrinkage
	- **3.1.5 Multiple Outputs**
- **3.2 The Bias-Variance Decomposition**
- **3.3 Bayesian Linear Regression**
	- **3.3.1 Parameter distribution**
	- **3.3.2 Predictive distribution**
	- **3.3.3 Equivalent Kernel**
- **3.4 Bayesian Model Comparison**
- **3.5 Evidence Approximation**
	- **3.5.1 Evaluation of the evidence function**
	- **3.5.2 Maximizing the evidence function**
	- **3.5.3 Effective number of parameters**
- **3.6 Limitations of Fixed Basis Functions**

---
**Goal of regression:** To *predict* the value of one (or more) continuous *target variable $t$* given the value of a $D$-dimensional vector $\text{x}$ of *input variables*. 

The simplest form of linear regression models are also linear functions of the input variables.

Construct a function $y(\text{x})$ such that for new input $\text{x}$, $y(\text{x}) = t$ -> Model the predictive distribution $p(t|\text{x})$ -> Predict $t$ such that the expectation $\mathbb{E}[(\text{loss function})]$ is minimal.

---
# Linear Basis Function Models
