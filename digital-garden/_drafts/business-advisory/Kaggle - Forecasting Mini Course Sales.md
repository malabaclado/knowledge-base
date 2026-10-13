For this challenge, you will be predicting a full year worth of sales for various fictitious learning modules from different fictitious Kaggle-branded stores in different (real!) countries. This dataset is completely synthetic, but contains many effects you see in real-world data, e.g., weekend and holiday effect, seasonality, etc. You are given the task of predicting sales during for year 2022.

## Files
- **train.csv** - the training set, which includes the sales data for each date-country-store-item combination.
- **test.csv** - the test set; your task is to predict the corresponding item sales for each date-country-store-item combination. Note the Public leaderboard is scored on the first quarter of the test year, and the Private on the remaining.
- **sample_submission.csv** - a sample submission file in the correct format

# Evaluation
Submissions are evaluated on [SMAPE](https://en.wikipedia.org/wiki/Symmetric_mean_absolute_percentage_error) between forecasts and actual values. We define SMAPE = 0 when the actual and predicted values are both 0.

## Submission File
For each `id` in the test set, you must predict the corresponding `num_sold`. The file should contain a header and have the following format:

```
id,num_sold
136950,100
136950,100
136950,100
etc.
```