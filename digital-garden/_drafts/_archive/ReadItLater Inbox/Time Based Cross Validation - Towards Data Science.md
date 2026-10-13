---
tags:
creation-date: 2023-03-27
---

[[ReadItLater]] [[article]]

# [Time Based Cross Validation - Towards Data Science](https://towardsdatascience.com/time-based-cross-validation-d259b13d42b8)

Photo by [Curtis MacNewton](https://unsplash.com/@curtismacnewton?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/time-based-validation?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## **What happens when our data is not a time-series, but still have a time dimension which is very important? This is a** Python solution for time-based cross-validation with all required inputs and an output matches scikit-learn methods.

Training and evaluating machine learning models usually require a training set and a test set. In most cases, train and test splitting is done randomly by taking 20% of the data as test data, unseen by the model and using the rest for training.

When dealing with time-related and dynamically changing environments, where the characteristics of the environment change throughout time, it is best to use time-based splitting to provide statistically robust model evaluation and best simulate real-life scenarios. For this we should use time-based cross validation, a method taken from the time-series field, which forms a type of “sliding window” training approach.

Time based cross validation approach

This approach is well known in the time-series domain, where we have a signal which is a sequence taken at successive equally spaced points in time.

But what happens when our data is not a time-series, but still have a time dimension which is very important?

## **Example of a problem requires time-based cross-validation**

We would like to predict delivery time of an order. Each record is an order, represented by set of features to create data table. We know **when** each order happened, and **several** orders could be placed on the same date. Detailed explanation of such problem could be found in my previous [blog](https://towardsdatascience.com/delivery-date-estimation-5aff1a0ff8dc). In this case, our intention was to train a new model based on last month orders, then apply it to predict the delivery time of next week’s orders.  
In order to best mimic real world, we should train our models using data taken from a time period of a month, then test them on new data captured from the following week. To create robust and general models, we should use several splitting-points in time and apply time-based cross validation. Our final test results would be the weighted average over all test windows.

*We need to pay attention to 3 important aspects:*

1\. **Time-based train\\test split**\- in each split, test indices must be higher than before.

2\. We would like to choose our **train\\test set sizes** in order to mimic real world scenarios in which we will train a model over some period and then apply it on the upcoming period. For example- train the model over last month data and apply it to predict on the upcoming week data.

3\. **Dates matter**. For our intention, the number of records in each set does not matter. What matters is the size of the windows in terms of days. We would like to split the data so that each window will consist data from X days.

## Other partial solutions

Scikit-learn has [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) method, but it has several drawbacks. Assuming our data is sorted by time, this method splits it into train\\test sets in a “sliding window” approach, but it doesn’t allow us to choose the sets sizes, we can only choose how many splits we would like to have. Scikit-learn TimeSeriesSplit also assumes that there is one observation per date, and therefore does not address 2 and 3 above.

Another solution is the one suggested by Germayne and presented in his [blog](https://medium.com/eatpredlove/time-series-cross-validation-a-walk-forward-approach-in-python-8534dd1db51a). He explains very well the entire approach and the differences from Scikit-learn method. One of the inputs for this solution is the train set size (called initial) and test set size (called horizon), but it creates sets containing a fixed number of **records**. For our purpose, we should create sets contain fixed number of **days**. This solution does not address point 3.

## Suggested solution

Therefore, I have written my own solution for time-based train and test splitting, that not only allow us to choose relevant set sizes, but also address the significant aspect of considering the window size in terms of days (and not in terms of records).

*The returned CV splits works like any other scikit-learn cross validator and could be used with any of their methods.*

Note that your data frame must have one column that contains the date for each record, as this solution leverages the dates of the data.

## Parameters:

-   train\_period: int, default=30  
    Number of time units to include in each train set.
-   test\_period: int, default=7  
    Number of time units to include in each test set.
-   freq: string, default=’days’  
    Frequency of input parameters. possible values are: days, months, years, weeks, hours, minutes, seconds.

## Methods:

**get\_n\_splits**(self)  
Returns the number of splitting iterations in the cross-validator

**split**(self, data, validation\_split\_date=None, date\_column=’record\_date’, gap=0)  
Returns list of tuples (train\_index, test\_index) similar to sklearn cross-validators.

-   data: pandas DataFrame  
    Your data, contain one column that indicates the record’s date
-   validation\_split\_date: datetime.date  
    First date to perform the splitting on. This is the date when the first test set starts.
-   date\_column: string  
    Date of each record
-   gap: int  
    For cases the test set does not come right after the train set, \*gap\* days are left between train and test sets

## Examples- how to use

## Closing

The suggested solution worked very well on various problems I have encountered in the past. Please let me know how it worked out for you, and if you think more adjustments could be made to improve this class.

Special thanks to Noga Gershon who shared with me her experience with related challenges.  
Thanks to Noga and Idan Richman-Goshen for their awesome technical feedback and for proofreading and reviewing this article.