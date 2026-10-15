---
title: Machine Learning Mastery (Jason Brownlee)
description:
date: 2026-10-14
lastmod: 2026-10-14
draft: false
tags:
  - machine-learning
  - data-science
aliases:
---

This note serves a summary and a quick reference of code snippets/recipes outlined in the book.

# Top-level Framework for an End-to-End Machine Learning Project

1. **Defining the problem.** Investigate and characterize the problem in order to better understand the goals of the project.
2. **Analyze the data.** Use descriptive statistics and visualization to better understand the data.
3. **Prepare the data.** Use data transformations in order to expose the structure of the prediction problem to modeling algorithms.
4. **Evaluate algorithms.** Design a test harness to evaluate a number of standard algorithms on the data and select the top few to investigate further.
5. **Improve results.** Use algorithm tuning and ensemble methods to get the most out of well-performing algorithms on your data
6. **Present results.** Finalize the model, make predictions and present results.

The chapters of the book are arranged according to the above framework:

- Understand your data with descriptive statistics (Analyze data)
- Understand your data with visualizations (Analyze data)
- Pre-process your data (Prepare the data)
- Feature selection (Prepare the data)
- Resampling Methods. (Evaluate Algorithms)
- Algorithm Evaluation Metrics. (Evaluate Algorithms)
- Spot-Check Classification Algorithms. (Evaluate Algorithms)
- Spot-Check Regression Algorithms. (Evaluate Algorithms)
- Model Selection. (Evaluate Algorithms)
- Pipelines. (Evaluate Algorithms)
- Ensemble Methods. (Improve Results)
- Algorithm Parameter Tuning. (Improve Results)
- Model Finalization. (Present Results)

# Understand your data with descriptive statistics
You must understand your data in order to get the best results. Here's how you can use descriptive statistics to understand your data.

1. Understand the structure of your raw data - `df.head()`
2. Review the dimensions of your dataset - `df.shape`
3. Review the data types of attributes in your data - `df.dtypes`
4. Summarize the distribution of instances across classes in your dataset. 
	1. Count
	2. Mean and Standard Deviation
	3. Min/Max
	4. 25th, 50th, 75th Percentiles
5. Summarize your data using descriptive statistics. 
6. Understand the relationships in your data using correlations - `df.skew()`
7. Review the skew of the distributions of each attribute.

## Tips to Remember

- **Review the numbers.** Generating the summary statistics is not enough. Take a moment to pause, read and really think about the numbers you are seeing
- **Ask why**. Review your numbers and ask a lot of questions. How and why are you seeing specific numbers. Think about how the numbers relate to the problem domain in general and specific entities that observations relate to
- W**rite down ideas.** Write down your observations and ideas. Keep a small text file or note pad and jot down all of the ideas for how variables may relate, for what numbers mean, and ideas for techniques to try later. The things you write down now while the data is fresh will be very valuable later when you are trying to think up new things to try

# Understand your data with visualizations

Common plots to use:
- Histograms - gives idea on distribution shape
- Density Plots - gives idea on distribution shape
- Box and Whisker Plots - summarize skewness
- Correlation Matrix Plot - summarize correlation between two variables
- Scatter Plot - shows the relationship between two variables as dots in two dimensions

Here's a great Python code reference for various chart types: [Python Graph Gallery](https://python-graph-gallery.com/)

# Pre-processing your data

Many machine learning algorithms make assumptions about your data. It is often a very good idea to prepare your data in such way to best expose the structure of the problem to the machine learning algorithms that you intend to use.

Outlined below are common pre-processing techniques:
- **Rescaling** - Rescaling means putting data from varying scales and attributes to the same scale (often in a range from 0 to 1).
	- This is useful for optimization algorithms used in the core of machine learning algorithms like gradient descent. It is also useful for algorithms that weight inputs like regression and neural networks and algorithms that use distance measures like k-Nearest Neighbors.
- **Standardizing** - Transforms data with Gaussian distribution with possibly different means and standard deviation to a distribution with a mean of 0 and standard deviation of 1.
	- It is most suitable for techniques that assume a Gaussian distribution in the input variables and work better with rescaled data, such as linear regression, logistic regression and linear discriminate analysis.
- **Normalization** - rescaling each observation (row) to have a length of 1 (called a unit norm or a vector with the length of 1 in linear algebra). 
	- This pre-processing method can be useful for sparse datasets (lots of zeros) with attributes of varying scales when using algorithms that weight input values such as neural networks and algorithms that use distance measures such as k-Nearest Neighbors.
- **Binarize** - transform your data into binary using a binary threshold. All values above the threshold are marked 1 and all equal to or below are marked as 0.
	- It can be useful when you have probabilities that you want to make crisp values. It is also useful when feature engineering and you want to add new features that indicate something meaningful.

# Feature Selection

**What is feature selection?**

Feature selection is a process where you automatically select those features in your data that contribute most to the prediction variable or output in which you are interested. Having irrelevant features in your data can decrease the accuracy of many models, especially linear algorithms like linear and logistic regression.

**Why perform feature selection?**

- Reduces Overfitting: Less redundant data means less opportunity to make decisions based on noise.
- Improves Accuracy: Less misleading data means modeling accuracy improves.
- Reduces Training Time: Less data means that algorithms train faster.

**Common techniques for feature selection**

- **Univariate Selection** - **uses statistical tests** (eg. chi-squared test) to select those features that have the strongest relationship with the output variable
	- The scikit-learn library provides the `SelectKBest` class that can be used with a suite of different statistical tests to select a specific number of features.
- **Recursive Feature Elimination** - **recursively removes attributes** and builds a model on those attributes that remain
	- It **uses the model accuracy** to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute.
- **Principal Component Analysis** - uses linear algebra to transform the dataset into a compressed form. 
	- Generally this is called a **data reduction technique**. 
	- A property of PCA is that you can choose the number of dimensions or principal components in the transformed result.
- **Feature Importance** - uses bagged decision trees (eg. Random Forest and Extra Trees) to estimate the importance of features.

# Evaluate the performance of ML algorithms with Resampling

You need to know how well your algorithms perform on unseen data. The best way to evaluate the performance of an algorithm would be to make predictions for new data to which you already know the answers.

The *second best way* is to use clever techniques from statistics called **resampling methods** that allow you to make accurate estimates for how well your algorithm will perform on new data.

**Common resampling methods for machine learning**

- Train and Test Set Splits
	- Split the original data set into training and testing data sets (usually at 2:1 ratio).
	- It is ideal for large datasets (millions of records) where there is strong evidence that both splits of the data are representative of the underlying problem. **Because of the speed, it is useful to use this approach when the algorithm you are investigating is slow to train.**
	- **A downside of this technique is that it can have a high variance.** This means that differences in the training and test dataset can result in meaningful differences in the estimate of accuracy.
- k-fold Cross Validation
	- Use to estimate the performance of a machine learning algorithm with less variance than a single train-test set split.
	- It works by splitting the dataset into k-parts (e.g. k = 5 or k = 10). Each split of the data is called a fold. The algorithm is trained on k − 1 folds with one held back and tested on the held back fold. This is repeated so that each fold of the dataset is given a chance to be the held back test set. After running cross validation you end up with k different performance scores that you can summarize using a mean and a standard deviation.
- Leave One Out Cross Validation
	- You can configure cross validation so that the size of the fold is 1 (k is set to the number of observations in your dataset). This variation of cross validation is called leave-one-out cross validation.
- Repeated Random Test-Train Splits
	- Another variation on k-fold cross validation is to create a random split of the data like the train/test split described above, but repeat the process of splitting and evaluation of the algorithm multiple times, like cross validation. 
	- This has the speed of using a train/test split and the reduction in variance in the estimated performance of k-fold cross validation. 
	- You can also repeat the process many more times as needed to improve the accuracy. A down side is that repetitions may include much of the same data in the train or the test split from run to run, introducing redundancy into the evaluation.

**What technique to use when?**

- Generally, k-fold cross validation is the *gold standard* for evaluating the performance of a machine learning algorithm on unseen data with *k* set to 3, 5 or 10.
- Using a train/test split is good for speed when using a slow algorithm and produces performance estimates with lower bias when using large datasets.
- Techniques like leave-one-out cross validation and repeated random splits can be useful intermediates when trying to balance variance in the estimated performance, model training speed and size.

The best advice is to experiment and find a technique for your problem that is fast and produces reasonable estimates of performance that you can use to make decisions. 

*If in doubt, use 10-fold cross validation.* 

# Algorithm Evaluation Metrics

## Common Classification Metrics

### Classification Accuracy
- Accuracy = Correct # of Predictions / Total # Predictions Made
- This is the most common evaluation metric for classification problems, it is also the most misused. **It is really only suitable when there are an equal number of observations in each class (which is rarely the case) and that all predictions and prediction errors are equally important**, which is often not the case.
### Logarithmic Loss
- Logarithmic loss (or logloss) is a performance metric for evaluating the predictions of probabilities of membership to a given class. 
- The scalar probability between 0 and 1 can be seen as a measure of confidence for a prediction by an algorithm. Predictions that are correct or incorrect are rewarded or punished proportionally to the confidence of the prediction.
### Area under ROC Curve
- Area under ROC Curve (or AUC for short) is a performance metric for binary classification problems. 
- The AUC represents a model’s ability to discriminate between positive and negative classes. An area of 1.0 represents a model that made all predictions perfectly. An area of 0.5 represents a model that is as good as random. 
- ROC can be broken down into sensitivity and specificity. A binary classification problem is really a trade-off between sensitivity and specificity.
	- Sensitivity is the true positive rate also called the recall. It is the number of instances from the positive (first) class that actually predicted correctly.
	- Specificity is also called the true negative rate. Is the number of instances from the negative (second) class that were actually predicted correctly.
### Confusion Matrix
### Classification Report







# Code Snippets

## Pearwise Pearson Correlation

#code-snippets Pearson Correlation

``` python
# Pairwise Pearson correlations
from pandas import read_csv
from pandas import set_option
filename = "pima-indians-diabetes.data.csv"
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
data = read_csv(filename, names=names)
set_option(’display.width’, 100)
set_option(’precision’, 3)
correlations = data.corr(method=’pearson’)
print(correlations)
```

## Calculate Skew

```python
# Skew for each attribute
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
data = read_csv(filename, names=names)
skew = data.skew()
print(skew)
```

## Rescaling `MinMaxScaler`

```
# Rescale data (between 0 and 1)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
set_printoptions(precision=3)
```

## Standardizing data with StandardScaler

``` python
# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])
```

## Normalizing data with `Normalizer`

```python
# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(normalizedX[0:5,:])
```


## Feature Selection with `SelectKBest`
```python
# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
# summarize selected features
print(features[0:5,:])
```

## Feature Extraction with RFE
```python
# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# load data
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("Num Features: %d") % fit.n_features_
print("Selected Features: %s") % fit.support_
print("Feature Ranking: %s") % fit.ranking_
```

## Dimension reduction with PCA
```python
# Feature Extraction with PCA
from pandas import read_csv
from sklearn.decomposition import PCA
# load data
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
print("Explained Variance: %s") % fit.explained_variance_ratio_
print(fit.components_)
```

## Feature Importance with Extra Trees Classifier

```python
# Feature Importance with Extra Trees Classifier
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# load data
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
model = ExtraTreesClassifier()
model.fit(X, Y)
print(model.feature_importances_)
```

## Evaluate using train-test set

```python
# Evaluate using a train and a test set
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size,
random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("Accuracy: %.3f%%") % (result*100.0)
```

Remarks:
- Note that in addition to specifying the size of the split, we also specify the random seed. Because the split of the data is random, we want to ensure that the results are reproducible. 
- By specifying the random seed we ensure that we get the same random numbers each time we run the code and in turn the same split of data. 
- This is important if we want to compare this result to the estimated accuracy of another machine learning algorithm or the same algorithm with a different configuration. 
- To ensure the comparison was apples-for-apples, we must ensure that they are trained and tested on exactly the same data.

## Evaluate using Cross Validation

```python
# Evaluate using Cross Validation
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, random_state=seed)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)
```

## Evaluate using Leave One Out Cross Validation

```python
# Evaluate using Leave One Out Cross Validation
from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_folds = 10
loocv = LeaveOneOut()
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)
```

## Evaluate using Shuffle Split Cross Validation

```python
# Evaluate using Shuffle Split Cross Validation
from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=seed)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)") % (results.mean()*100.0, results.std()*100.0)
```

## Cross Validation Classification Accuracy

```python
# Cross Validation Classification Accuracy
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()
scoring = ’accuracy’
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Accuracy: %.3f (%.3f)") % (results.mean(), results.std())
```

## Cross Validation Classification LogLoss

```python
# Cross Validation Classification LogLoss
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()
scoring = ’neg_log_loss’
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Logloss: %.3f (%.3f)") % (results.mean(), results.std())
```

## Cross Validation Classification ROC AUC

```python
# Cross Validation Classification ROC AUC
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = ’pima-indians-diabetes.data.csv’
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()
scoring = ’roc_auc’
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("AUC: %.3f (%.3f)") % (results.mean(), results.std())
```