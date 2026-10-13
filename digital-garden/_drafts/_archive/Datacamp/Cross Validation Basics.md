#type/guide #topic/python #topic/machine-learning 

**Motivation:** The model's performance is dependent on the way the data is split - it does not represent the model's ability to generalize.


This method avoid the problem of your metric of choice being dependent on train-test-split.

## Guide to 5-fold Cross Validation

How does 5-fold CV work?
1. Split the dataset info 5 folds
2. Take fold 1 as test set
	- Fit the model into the other 4 folds
	- Predict on test set
	- Compute the metric of interest
3. Repeat step 2 for the other four folds as test set


![[Pasted image 20220207011233.png]]


## How to perform cross validation in sklearn



```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
cv_results = cross_val_score(reg, X,y,cv=5)
```


1. Import packages
2. Initialize regression model
3. Cross-validate

## How to compute how much time a CV takes
```python
%timeit cross_val_score(reg, X, y, cv = ____)
```
