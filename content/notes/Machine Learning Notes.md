---
title: machine learning
---


Readings from: https://machinelearningmastery.com/

The goal of all supervised machine learning algorithms is to best estimate a target function (f) that maps input data (X) onto output variables (Y).


## Machine Learning Algorithms

### Linear Algorithms

#### Gradient Descent

- What is gradient descent?
	- Gradient descent is an optimization algorithm used to find the values of parameters (coefficients) of a function (f) that minimizes a cost function (cost).
	- Gradient descent is best used when the parameters cannot be calculated analytically (e.g. using linear algebra) and must be searched for by an optimization algorithm.
- How can gradient descent be used in algorithms like linear regression?
- How can gradient descent scale to very large datasets?
- What are some tips for getting the most from gradient descent?

##### Gradient Descent Procedure
1. Set initial values v0 for the coefficients of the function (easiest = 0). 
2. Calculate the cost function at initial values v0.
3. Calculate the derivative of the cost function $\Delta$ at v0. This derivative is the rate of descent towards local optimum.
4. Set a learning rate parameter $\alpha$ and calculate new coefficients $v_0$ : $$v_1 = v_0 - (\alpha * \Delta)$$
5.  Repeat steps 1-4 until you get cost function = 0 (or something good enough)

A/N: Gradient descent is nothing but finding the local optimum.

##### Stochastic Gradient Descent

- Gradient descent can be slow to run on very large datasets.
	- Because one iteration of the gradient descent algorithm requires a prediction for each instance in the training dataset, it can take a long time when you have many millions of instances.
	- In situations when you have large amounts of data, you can use a variation of gradient descent called **stochastic gradient descent**.
- The first step of the procedure requires that **the order of the training dataset is randomized**. This is to mix up the order that updates are made to the coefficients. Because the coefficients are updated after every training instance, the updates will be noisy jumping all over the place, and so will the corresponding cost function. By mixing up the order for the updates to the coefficients, **it harnesses this random walk** and avoids it getting distracted or stuck.
- The learning can be much faster with stochastic gradient descent for very large training datasets and often you only need a small number of passes through the dataset to reach a good or good enough set of coefficients, e.g. 1-to-10 passes through the dataset.

##### Tips for Gradient Descent

This section lists some tips and tricks for getting the most out of the gradient descent algorithm for machine learning.

- **Plot Cost versus Time**: Collect and plot the cost values calculated by the algorithm each iteration. The expectation for a well performing gradient descent run is a decrease in cost each iteration. If it does not decrease, try reducing your learning rate.
- **Learning Rate**: The learning rate value is a small real value such as 0.1, 0.001 or 0.0001. Try different values for your problem and see which works best.
- **Rescale Inputs**: The algorithm will reach the minimum cost faster if the shape of the cost function is not skewed and distorted. You can achieved this by rescaling all of the input variables (X) to the same range, such as [0, 1] or [-1, 1].
- **Few Passes**: Stochastic gradient descent often does not need more than 1-to-10 passes through the training dataset to converge on good or good enough coefficients.
- **Plot Mean Cost**: The updates for each training dataset instance can result in a noisy plot of cost over time when using stochastic gradient descent. Taking the average over 10, 100, or 1000 updates can give you a better idea of the learning trend for the algorithm.


#### Linear Regression

Mathematical form of a linear regression model: $$f(x) = B_0 + B_1 * x$$
##### Sample Python Code
```py
import numpy as np

# Function to calculate m and b
def linear_regression(X, y):
    x_mean = np.mean(X)
    y_mean = np.mean(y)
    numerator = np.sum((X - x_mean) * (y - y_mean))
    denominator = np.sum((X - x_mean) ** 2)
    m = numerator / denominator
    b = y_mean - (m * x_mean)
    return m, b

# Function to calculate prediction
def predict(X, m, b):
    return m * X + b

# Function to calculate RMSE
def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))</prev>

<ol start="3">
<li>We will train our model by providing the sample data. 
<li>Make a prediction.
<li>By using the predicted values, calculate the RMSE metric. 
</ol>

<pre class="lang:default decode:true">X = np.array([7, 8, 10, 12, 15, 18])
Y = np.array([9, 10, 12, 13, 16, 20])

# Training the model
m, b = linear_regression(X, Y)

# Making predictions
predictions = predict(X, m, b)

# Calculating RMSE
error = rmse(Y, predictions)

print("Slope (m):", m)
print("Intercept (b):", b)
print("Predictions:", predictions)
print("RMSE:", error)
```


##### Assumptions of Linear Regression Model
- Linear regression assumes that the relationship between your input and output is linear.
- Linear regression assumes that your input and output variables are not noisy. (No external factors)
- Linear regression assumues non-collinearity between variables, ie., your input variables must not be highly correlated to each other.

##### Best practices for linear regression
A linear regression model would give more reliable results if the following are followed:
- Input variables are normally distributed.
- Input values are standardized/normalized.

#### Logistic Regression

Contrary to its name, a logistic regression model is a classification model, not a regression model.

Logistic regression is named for the function used at the core of the method, the logistic function.
### Nonlinear Algorithms

### Ensemble Algorithms