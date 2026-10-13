# Plotting accuracy score over different k neighbors in [[KNearest Neighbor Algorithm|KNN]] classifier

Our goal here is to see which k-value would give us the most accurate model.


### The Steps
1. Set-up your training and test sets.
2. Create a loop over different k-values
	- Set-up a KNN-classifier for each k-value
	- Fit the classifier
	- Compute the accuracy. (See [[How to measure model accuracy in sklearn]])


### Sample Code
```python 

# Setup arrays to store train and test accuracies

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):

 # Setup a k-NN Classifier with k neighbors: knn
 knn = KNeighborsClassifier(n_neighbors=k)

 # Fit the classifier to the training data
 knn.fit(X_train, y_train)

 #Compute accuracy on the training set
 train_accuracy[i] = knn.score(X_train, y_train)

 #Compute accuracy on the testing set
 test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
```