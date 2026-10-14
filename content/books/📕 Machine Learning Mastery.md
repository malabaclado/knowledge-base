---
title: Machine Learning Mastery (Jason Brownlee)
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

Common techniques for feature selection
- **Univariate Selection** - **uses statistical tests** (eg. chi-squared test) to select those features that have the strongest relationship with the output variable
	- The scikit-learn library provides the `SelectKBest` class that can be used with a suite of different statistical tests to select a specific number of features.
- **Recursive Feature Elimination** - **recursively removes attributes** and builds a model on those attributes that remain
	- It uses the model accuracy to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute.
- Principal Component Analysis - Principal Component Analysis (or PCA) uses linear algebra to transform the dataset into a
compressed form. Generally this is called a data reduction technique. A property of PCA is that
you can choose the number of dimensions or principal components in the transformed result.
- Feature Importance

# Code Snippets

## Pearwise Pearson Correlation

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