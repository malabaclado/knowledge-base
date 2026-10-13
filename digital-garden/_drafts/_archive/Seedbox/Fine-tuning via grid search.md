---
tags:
alias:
creation-date: Tuesday 18th October 2022
last-modified-date: Tuesday 18th October 2022 10:57:08
---

# Fine-tuning via grid search
There are **two types of parameters**: learned and tuning parameters. 

**Learned parameters** are parameters learned from training data. *Example: the weights in logistic regression.* 

**Tuning parameters** are the innate parameter of a model, such as the regularization parameter in logistic regression. *These are also called hyperparameters.* 

The grid search method specify a list of values for different hyperparameters and the computer evaluates the model performance for each combination of those to obtain the optimal combination of values. 



## How to tune hyperparameters using GridSearchCV in sklearn

1. Import `GridSearchCV`
```python
# Importing GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC 

# Pipelining
pipe_svc=make_pipeline(StandardScaler(),SVC(random_state=1))
```

2. Setup parameter range - these are the values that you'd want to test.

```python
# Setting up parameter range
param_range=[0.0001,0.001,0.01, 0.1,1.0, 10.0, 100.0, 1000.0]
```

3. Setup parameter grid which includes the parameter/s to be tuned and the kernel in a dictionary.
```python
param_grid=[
			{'svc_C':param_range, 'svc_kernel':['linear']}, 
			{'svc_C':param_range, 'svc_gamma': param_range, 'svc_kernel':['rbf']}]
```

4. Fit GridSearchCV
```python
# Initializeing GridSearchCV
gs = GridSearchCV(
				  estimator = pipe_svc,  
				  param_grid=param_grid ,
				  scoring='accuracy'
				  cv=10,
				  n_jobs=-1)

# Fitting GSCV
gs = gs.fit(X_train, t_train)

# Best score and parameters
print(gs.best_score_)
>>> 0.984615384615

print(gs.best_params_)
>>> {'svc__C': 100.0, 'svc__gamma': 0.001, 'svc__kernel': 'rbf'}
```





```