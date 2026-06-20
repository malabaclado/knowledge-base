---
tags: #python #machine-learning 
alias:
creation-date: Tuesday 22nd February 2022
last-modified-date: Tuesday 22nd February 2022 01:22:35
---
⬅️ 

# Dealing with missing data
## Identifying missing values in tabular data
To find missing values: use `isnull()` method
![[Pasted image 20220222012821.png|300]]
<!--ID: 1645617152672-->



## Eliminating samples or features with missing values
- Drop rows (individual data points): `df.dropna(axis=0)`
- Drop columns (features): `df.dropna(axis=1)`
- Drop rows where all columns are `NaN`: `df.dropa(how='all')`
- Drop rows that have less than 4 real values: `df.dropna(thresh=4)`
- Only drop rwos where `NaN` appear in specific columns (ex. `C`): `df.dropna(subset=['C']`
<!--ID: 1645617152681-->


## Imputing missing values
Often, the removal of samples or dropping of entire feature columns is simply not feasible, because we might lose too much valuable data. In this case, we can use different interpolation techniques to estimate the missing values from the other training samples in our dataset.
<!--ID: 1645617152688-->


One of the most common interpolation techniques is mean imputation. Other strategies include `median` or `most_frequency`

### Mean Imputation
![[Pasted image 20220222013849.png]]
<!--ID: 1645617152697-->


## Understanding the scikit-learn estimator API

