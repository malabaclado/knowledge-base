# How to measure model performance (accuracy)
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = 
	train_test_split(X,y, test_size=0.3, random_state=21, 
        stratify=y)
y_pred = knn.predict(X_test)
knn.score(X_text, y_test)


```

1. Import train_test_split
2. Split data set


	> There are some things you should note here:
	> - `test_size`: sets the allotted percentage for your test data. `0.3` means you split the data into 70% training and 30% test.
	> - `random_state`: makes sure your data in randomized
	> - `stratify`: makes sure that your target values are properly distributed between training and test set

	> This preparation is made before you train your machine. Once you are done with its training, you may now use it on test data to find its accuracy score.

3. Getting accuracy score