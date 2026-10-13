---
tags:
alias:
creation-date: Friday 11th November 2022
last-modified-date: Friday 11th November 2022 16:13:43
---

# Bringing features onto the same scale

**Feature scaling** is a crucial step in our preprocessing pipeline that can easily be  forgotten. 

Decision trees and random forests are two of the very few machine 
learning algorithms where we don't need to worry about feature scaling. These algorithms are what we call **scale invariant**

Now, there are **two common approaches** to bring different features onto the same scale: **normalization** and **standardization**. 

**Normalization** refers to rescaling of the features to a range of $[0,1]$. This is a special-case of min-max scaling. 
```python
from  sklearn.preprocessing import MinMaxScaler
mms=MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
```


In **Standardization**, we center the feature columns at mean 0 with standard deviation of 1 so that the feature columns take the form of a normal distribution, which makes it easier to learn the weights. 

An **advantage of standardization** is that it maintains useful information about outliers and makes the algorithm more sensitive to them (in contrast to min-max scaling, which scales the data to a limited range of values).

![[Pasted image 20221111162239.png]]


```python
from sklearn.preprocessing import StandardScaler
stdsc=StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)
```