---
title: Machine Learning Mastery (Jason Brownlee)
---
# Top-level Framework for an End-to-End Machine Learning Project

1. **Defining the problem.** Investigate and characterize the problem in order to better understand the goals of the project.
2. **Analyze the data.** Use descriptive statistics and visualization to better understand the data.
3. **Prepare the data.** Use data transformations in order to expose the structure of the prediction problem to modeling algorithms.
4. **Evaluate algorithms.** Design a test harness to evaluate a number of standard algorithms on the data and select the top few to investigate further.
5. **Improve results.** Use algorithm tuning and ensemble methods to get the most out of well-performing algorithms on your data
6. **Present results.** Finalize the model, make predictions and present results.

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

Outlined below aCommon pre-processing techniques:

## Rescaling
## Standardizing
## Normalizing
## Binarize


# Code Snippets

# Pearwise Pearson Correlation

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

# Calculate Skew

```python
# Skew for each attribute
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = [’preg’, ’plas’, ’pres’, ’skin’, ’test’, ’mass’, ’pedi’, ’age’, ’class’]
data = read_csv(filename, names=names)
skew = data.skew()
print(skew)
```