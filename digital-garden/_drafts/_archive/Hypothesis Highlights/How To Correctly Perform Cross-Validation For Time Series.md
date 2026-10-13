---
doc_type: hypothesis-highlights
url: >-
  https://towardsdatascience.com/how-to-correctly-perform-cross-validation-for-time-series-b083b869e42c
---


## Metadata
- Author: [towardsdatascience.com]()
- Title: How To Correctly Perform Cross-Validation For Time Series
- Reference: https://towardsdatascience.com/how-to-correctly-perform-cross-validation-for-time-series-b083b869e42c
- Category: #article

## Page Notes
## Highlights
- Cross-validation is a method to determine the best performing model and parameters through training and testing the model on different portions of the data. The most common and basic approach is the classic train-test split. This is where we split our data into a training set that is used to fit our model and then evaluated it on the test set.This idea can be taken one step further by carrying out the train-test split numerous times by varying the data we train and test on. This process is cross-validation as we are using every row of data for both training and evaluation to ensure we choose the most robust model over all the possible available data. — [Updated on 2023-03-27 15:10:44](https://hyp.is/fe_Y2sxuEe28n9-DY8FfaA/towardsdatascience.com/how-to-correctly-perform-cross-validation-for-time-series-b083b869e42c) — Group: #Just-Me

- For time series, we always predict into the future. However, in the above approach we will be training on data that is further in time than the evaluation test data. This is data leakage and should be avoided at all costs. — [Updated on 2023-03-27 15:11:48](https://hyp.is/o73RKsxuEe2VsPMCAn5QxA/towardsdatascience.com/how-to-correctly-perform-cross-validation-for-time-series-b083b869e42c) — Group: #Just-Me



