---
tags:
alias:
creation-date: Thursday 8th September 2022
last-modified-date: Thursday 8th September 2022 08:39:47
---

In this chapter, we discuss the methods used in developing the prediction model. More specifically, we cover the steps used in the collection and preparation of data, the training phase of the SVR model, selection of hyperparameters and the evaluation of its performance. 


# Conceptual Framework

# Collection and Preparation of data
The Philippine Stock Exhange Index is the congregation of the top 30 publicly-listed companies in the country. The Philippine Stock Exchange Index (PSEI) daily stock prices dataset was downloaded from **Yahoo!Finance**. This dataset will be used as the primary data under study. 

The dataset was downloaded in *.csv* format. It was read and cleaned using python's *pandas* library. The data was read using the pandas *pd.read_csv()* command with the date column as its index in *datetime* format. This allows the use of specific commands that are available only to time series data. The dataset is composed on 5 columns: Open, High, Low, Close, Adj_Close and Volume. For the purpose of this study, we will only be using the Adj Close column. The adjusted close prices are the close prices of a particular stock after the dividends have been accounted for. 

In this study, only a portion of the dataset was used. The sample taken from the original data contains stock prices from June 2010 to June 2017. For the forecasting, we use the date from July 2017 to July 2018. 

To ensure the integrity of the data, a 2-step data cleaning operation was employed: (1) all zero values are replaced by \verb|NaN| and then (2) all rows with \verb|NaN| values are removed from the dataset.

A total number of 59 rows out of 2288 original rows were removed through this data cleaning process which amounts to 2.58% of the original data.

The sample research data under study was chosen to be eight-years long. Seven-year data from June 2010 to June 2017 was used for training and testing the predictive model. One-year data from July 2017 to July 2018 was used to test the forecasting performance of the best model. This time period was deliberately chosen to strike a compromise between maximizing the amount of available data and minimizing the effects of external factors such as 2008's Great Recession and 2019's COVID-19 pandemic. 

The technical analysis indicators were generated using the existing ta library in Python. Three types of TA indicators were used: momentum, volatility and trend. The chosen TA indicators were all dependent on the Close price only. The TA indicators used were Exponential Moving Average (EMA), Relative Strength Index (RSI) and Ulcer Index (UI). A 10-day, 20-day and  60-day variants of each of these indicators were used to represent the short-term and long-term effects respectively. In addition, we also included Kaufman Adaptive Moving Average (KAMA) and Moving Average Convergence/Divergence (MACD). A total of 11 technical indicators were used.

The 11 technical indicators will form the feature set. The Close price column will be the target set. The data were split into 70% training set and 30% test set. The training set for was composed of 1163 samples while the test set was composed of 499 samples.

# Model Training
The feature selection, feature scaling, model selection, and evaluation of the SVR model is aided uwith Python's scikit-learn library. The hyperparameter optimization using Bayesian optimization was done using Python's scikit-optimize library.


----
[[Proposed Method]]
[[Model Evaluation]]
