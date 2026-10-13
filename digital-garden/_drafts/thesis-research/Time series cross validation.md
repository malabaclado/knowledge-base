When training supervised machine learning models, it is a common practice to split the dataset into training and testing set. This is done so that the model would not be tested using the information it used to learn from. A model that is tested on the same data it used for training would just repeat the labeles of the samples it has just seen and would have a perfevt score, but would fail to predict anything on yet-to-be-seen data. Such situation is called overfitting. Now, when optimizing different parameter settings, such as the $C$  parameter in an SVR model, it is common practice to evaluate on a separate holdout set known as the *validation set* to optimize the parameters, before finally testing the model on a testing dataset. 

A k-fold cross validation technique divides the samples into k-groups of similar size, if possible. This is analogous to the 'leave one out' technique, in which the prediction model is trained using k-1 folds and tested on the left out set.

Time series cross validation is a k-fold cross validation technique that divides the dataset sequentially. In this case, the succeeding training set is a superset of the preceding training sets,  and the testing set is always near the end of the dataset. This ensures that the model learns the information in the manner in which it occured.

Time series cross validation is performed in Python using the scikit-learn library's TimeSeriesSplit() function.



![](https://i.imgur.com/zYXCyLY.png)
![](https://i.imgur.com/UzNk8dh.png)

---
See also: [[Thesis Scratchpad]]