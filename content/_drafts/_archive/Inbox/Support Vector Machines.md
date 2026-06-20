---
tags: type/concept
alias: SVM
creation-date: Sunday 10th July 2022
last-modified-date: Sunday 10th July 2022 14:48:30
---

# Support Vector Machines
The objective of the support vector machine [[Algorithm]] is to find a hyperplane in an  N-dimensional space (N is the no. of features) that classifies (or separates) the data points.

![[Pasted image 20220710145550.png|400]]

Not only we need to find a hyperplane (since there are many hyperplanes that can be considered), **we aim to find the hyperplane with the maximum margin**. 

**Why?** Because a large margin distance provides some reinforcement so that future data points can be classified with more confidence. 

In SVM, the [[Loss Function|loss function]] that helps maximize the margin is called the [[Hinge Loss Function]].

The application of support vector machines in predicting continuous variables is called [[Support Vector Regression (ChatGPT)]].

> [!NOTE]
> The SVM is a decision machine and so does not provide posterior probabilities.

---
### How it works
To demonstrate how SVM works, let's consider a simple **2-class classification problem using linear models**. This has the form: 
$$y(\text{x}) = \text{w}^{T}\phi(\text{x}) +b \tag{1}$$
where $\phi(\text{x})$ denotes a fixed feature-space transformation and $b$ denotes the *bias parameter*.  ^01e522

Consider the training data set comprised of $N$ vectors $\text{x}_{1},...,\text{x}_{N}$ with corresponding target values $t_{1},...,t_{N}$ where $t_{n} \in \{-1,1\}$. New data points are classified according to the sign of $y(\text{x})$.

###### Linearly Separable Case
Suppose the training data set is linearly separable. That is, we are sure that there exists parameters $\text{w}$ and $b$ that can classify the points. 

By classification, we mean that the function [[#^01e522|(1)]] satisfies the condition:
$$
y(\text{x}_{n})>0 \text{ for } t_{n}=1;\quad y(\text{x}_{n})>0 \text{ for } t_{n}=1;
$$
so that $$t_{n}y(\text{x}_{n})>0, \text{ for all } \text{x}_i$$
Here, our decision hyperplane is given by the equation: $y(\text{x})=0$ 

###### Distance from the hyperplane
Recall that the perpendicular distance of the point $\text{x}$ from the hyperplane defined by $y(\text{x})=0$ 
where $y(\text{x})$ takes the form of [[#^01e522|(1)]] is given by $$\frac{|y(\text{x})|}{||\text{w}||} \tag{2}$$
Following ***(2)***, the distance from the point $\text{x}_{n}$ to to the decision surface $y(\text{x})=0$: 
$$
\frac{t_{n}y(\text{x}_{n})}{||\text{w}||}= \frac{t_{n}(\text{w}^{T} \phi(\text{x}_{n}) + b )}{||\text{w}||} \tag{3}
$$

###### Maximum Margin
The idea is to find the maximum margin that separates the classes. To do this, we optimize the parameters $\text{w}$ and $b$ so that ***(3)*** is maximized. 

We have this optimization problem: $$\arg \max_{w,b} \left \{
\frac{1}{||\text{w}||} 
\min_{n} [t_{n} (\text{w}^T \phi(\text{x}_{n})+b)]
\right \}$$

> [!NOTE]- Remarks
> - The expression $\{\min_{n} [t_{n} (\text{w}^T \phi(\text{x}_{n})+b)]\}$  refers to finding the closest point $\text{x}$ to the decision hyperplane.
> - The expression above refers to finding the optimal parameters such that the distance between the closest point to the decision hyperplane is maximum.


Now, the above optimization problem is very complicated to solve. The idea for solving this is to rescale the parameters so that the closest point to the hyperplane would have a distance equal to 1. 

Rescale:  
- $\text{w} \to \kappa \text{w}$ 
- $b \to \kappa b$

Note that this rescaling does not change the distance from any point $\text{x}$ to the decision hyperplane, but it will help make our equations simpler. 

We'll set the distance of the closest point to the decision hyperplane equal to 1:  $$t_{n}(\text{w}^{T} \phi(\text{x}_{n}) + b) = 1$$
Therefore, all data points will satisfy this constraint: $$t_{n}(\text{w}^{T} \phi(\text{x}_{n}) + b) \geq 1, \quad \text{for } n=1,...,N$$
###### Simpler optimization problem





![[Pasted image 20220811173343.png]]