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