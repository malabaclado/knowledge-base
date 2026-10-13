---
tags:
alias:
creation-date: Friday 11th November 2022
last-modified-date: Friday 11th November 2022 17:02:40
---

In this section, we will take a look at two very simple yet powerful diagnostic 
tools that can help us improve the performance of a learning algorithm: learning curves and validation curves. 


## Learning Curves

Learning curves helps us diagnose whether a learning algorithm has a problem with overfitting (high variance) or underfitting(high bias).

> [!NOTE]
> If a model is too complex for a given training dataset, the model tends to *overfit*  and does not generalize well to unseen data.

 By plotting the model training and validation accuracies as functions of the training set size, we can easily detect whether the model suffers from high variance or high bias, and whether the collection of more data could help address this problem.

![[Pasted image 20221111170708.png]]

- The graph on the upper -left has high bias (underfitting). The training and validation accuracies converge but it is below the desired accuracy.

To address the issue of underfitting, we can: 
1. Increase the numebr of parameters of the model 
2. decrease the degree of regularization

- High variance (overfitting) is indicated by a large gap between the training and validation accuracy.

To address the problem of overfitting, we can:
1. collect more training data
2. reduce the complexity of the model 
3. increase the regularization parameter
4. decrease the number of features via feature selection 

Here's how to plot the learning curve using the learning curve function from sklearn:

```python
import matplotlib.pyploy as plt
from sklearn.model_selection import learning_curve

pipe_lr = make_pipeline (StandardScaler(), 
						LogisticRegression(penalty='12', 
											random_state=1))

train_sizes, train_scores, test_scores = \
		learning_curve(estimator=pipe_lr, 
						X=X_train,
						y=y_train,
						train_sizes=np.linspace(
							0.1, 1.0, 10),
						cv=10,
						n_jobs=1 )


train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores,axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores,axis=1)

plt.plot(train_sizes, train_mean, color='blue', marker='o',
		markersize=5, label='training accuracy')

plt.fill_between(train_sizes,
				train_mean + train_std,
				train_mean- train_std,
				alpha=0.15, color='blue')

plt.plot(train_sizes, test_mean, 
		color='green', linestyle='--',
		marker='s', markersize=5,
		label='validation accuracy')

plt.fill_between(train_sizes, 
				test_mean + test_std,
				test_mean - test_std,
				alpha=0.15, color='green')

plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower_right')
plt.ylim([0.8, 1.0])
plt.show()
```

![[Pasted image 20221111172551.png]]
As we can see in the plot above, the model performs quite well if it had seen more than 250 samples.

We can also see that the training accuracy (blue line) is higher for training sets with less than 250 samples but the gap between the training accuracy and the validation accuracy (green line) widens - an indicator of an increasing degree of overfitting. 

## Validation Curves
Validation curves are a useful tool for improving the performance of a model by addressing issues such as overfitting or underfitting. Validation curves are related to learning curves, but instead of plotting the training and test accuracies as functions of the sample size, we vary the values of the model parameters. 

```python
from sklearn.model_selection import validation_curve
param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
train_scores, test_scores = validation_curve(
                estimator=pipe_lr,
                X=X_train,
                y=y_train,
                param_name='logisticregression__C',
                param_range=param_range,
                cv=10)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
plt.plot(param_range, train_mean,
          color='blue', marker='o',
         markersize=5, label='training accuracy')
plt.fill_between(param_range, train_mean + train_std,
                 train_mean - train_std, alpha=0.15,
                 color='blue')
plt.plot(param_range, test_mean,
         color='green', linestyle='--',
         marker='s', markersize=5,
         label='validation accuracy')
plt.fill_between(param_range,
                 test_mean + test_std,
                 test_mean - test_std,
                 alpha=0.15, color='green')
plt.grid()
plt.legend(loc='lower right')
plt.xlabel('Parameter C')
plt.ylabel('Accuracy')
plt.ylim([0.8, 1.03])
plt.show()
```

![[Pasted image 20221111173451.png]]

