---
tags: [topic/machine-learning type/guide topic/machine-learning]
---

This is a guide to performing [[KNearest Neighbor Algorithm|KNN]] algorithm in python using scikit-learn.

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(training_data, target_data)
prediction = knn.predict(test_variable)
```

Some note:
- `n_neighbors` ➡ is a hyperparameter; number of nearest neighbors

![[Measuring Model Accuracy#^7c3bb8]]

