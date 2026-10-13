#topic/machine-learning #topic/python #type/guide 

### Confusion matrix
Importing
```python
from sklearn.metrics import confusion_matrix
```


Usage
```python
confusion_matrix(y_test, y_pred)
```

This code outputs a $2\times 2$ matrix as in this image
![[Pasted image 20220207185036.png]]


### Classification report
Importing
```python
from sklearn.metrics import classification_report
```


Usage
```python
classification_report(y_test, y_pred)
```
