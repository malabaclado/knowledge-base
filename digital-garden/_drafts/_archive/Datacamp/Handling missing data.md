---
tags: type/concept
---


What is missing data? Missing data can be `NaN`, corrupted entries/symbols `?` or zero values for non-zero variables. 

# What do we do with missing data?[[Handling missing data]]
It is a good practice to replace all missing data with the `Nan` object.
![[Pasted image 20220208010323.png]]


From here, we can do two things: 
1. Drop missing data
2. Imputate

### Drop missing data
![[Pasted image 20220208010425.png]]



### Imputing data
"Imputing" means making an educated guess about the missing data. For example, we can replace the missing data with the mean of its available data.


![[Pasted image 20220208010451.png]]

Other strategy: `most_frequent`

### Imputing within a pipeline
Pipeline 👉 is a way to do both imputing and model-fitting.


Note that, in a pipeline, each step but the last must be a transformer and the last must be an estimator, such as, a classifier or a regressor.

![[Pasted image 20220208010735.png]]
![[Pasted image 20220208010755.png]]