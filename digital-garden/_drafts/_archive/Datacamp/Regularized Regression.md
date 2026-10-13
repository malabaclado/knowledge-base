
#topic/machine-learning #topic/python #type/guide #topic/machine-learning/regression 

Recall that [[linear regression]] minimizes the loss function. It chooses a coefficient for each feature variable. 


Large coefficients can lead to [[overfitting]]. [[Regularization]] is a technique used to circumnavigate this problem by penalizing large coefficients in the model.

We usually introduce a new variable $\alpha$ which controls the complexity of the model.
- Low $\alpha$  ($\alpha =0$) ➡ simple OLS; *can lead to overfitting*
- High $\alpha$ ($\alpha \to \infty$) ➡ very strict model; *can lead to underfitting*



## Ridge Regression
In ridge regression, the loss function is modified 
$$\text{Loss function} = \text{OLS loss fn} + \alpha\sum^{n}_{i=1} a_i^2 $$


### Ridge Regression in sklearn
1. Import Ridge


```python
from sklearn.linear_model import Ridge
```

2. Train-test-split and create ridge regressor

```python
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state=42)
ridge = Ridge(alpha =0.1, normalize=True)
```

3. Train and test the model

```python
ridge.fit(X_train, y_train)
ridge_pred=ridge.predict(X_test)
ridge.score(X_test, y_test)
```

## Lasso Regression
In lasso regression, the loss function is modified 
$$\text{Loss function} = \text{OLS loss fn} + \alpha\sum^{n}_{i=1} |a_i| $$


### Lasso regression for feature selections
Import Lasso
```python
from sklearn.linear_model import Lasso
```


Take features

```python
names = boston.drop('MEDV', axis=1).columns
```

Train and test the model
```python
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X,y).coef_
```