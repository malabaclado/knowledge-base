---
tags: 
alias:
creation-date: Friday 20th January 2023
last-modified-date: Friday 20th January 2023 11:10:11
---

**Parameters** in a machine learning model refer to the variables that an algorithm itself produces (such as a coefficient) to produce a prediction. These parameters are not set or hard-coded and depend on the training data that is passed into your model. Because of this, they’re likely to change when your data changes.

On the other hand, **hyper-parameters** are variables that you specify while building a machine-learning model. This means that it’s the user that defines the hyper-parameters while building the model. For example, in a k-nearest neighbour algorithm, the hyper-parameters can refer the value for `k` or the type of distance measurement used.

In short, **hyper-parameters** **control the learning process, while parameters are learned.**

K-Fold Cross Validation:
![[Pasted image 20230120111256.png]]

---- 


In machine learning, there are two types of parameters: those that are produced by the learning algorithm, such as the weights in SVR, and the parameters of a learning algorithm that must be set prior to training, such as the $\varepsilon$ parameter in SVR. Because the latter one is concerned with how the model behaves, it is called a hyperparameter. A common way of choosing the best hyperparameters for a machine learning model is through Grid Search. The Grid Search method for hyperparameter optimization is a brute-force exhaustive search over a discrete space of parameters. In this method, we define a set of values for each hyperparameter - we call this a 'grid'. Then the model is fitted at each points on this grid - that is, among every combination of the values of the hyperparameters. 

![](https://i.imgur.com/UV7qbC3.png)

---
See also: [[Thesis Scratchpad]]