#topic/machine-learning #topic/python #type/guide
Many models use some form of distance to inform them. Because of this, features on larger scales unduly influence the model. Usually, we want features to be on a similar scale. 

Scaling/Centering 👉 Normalizing the data

# Ways to normalize data
Standardization: Subtract the mean and divide by the variance
➡ All features are centered around zero and have variance one.



## Scaling in scikit-learn

![[Pasted image 20220208030837.png]]



## Scaling in a pipeline

![[Pasted image 20220208030927.png]]


## Cross-validation and scaling in a pipeline

![[Pasted image 20220208031117.png]]
![[Pasted image 20220208031137.png]]
