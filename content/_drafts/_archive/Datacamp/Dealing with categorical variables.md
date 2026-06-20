#topic/python #topic/machine-learning #type/guide 

Note that scikit-learn does not accept categorical variables. So to be able to use categorical data, we introduce a "dummy variable" with values 0 and 1.


Value = 0 👉 Not in that category
Value =1 👉 Belongs to that category

![[Pasted image 20220208004643.png]]

---
There are two ways we can do this in Python:
1. scikit-learn: `OneHotEncoder()`
2. pandas: `get_dummies()`

---
`get_dummies()` sample:
![[Pasted image 20220208004842.png]]