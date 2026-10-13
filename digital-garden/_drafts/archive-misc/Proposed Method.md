---
tags:
alias:
creation-date: Friday 28th October 2022
last-modified-date: Friday 28th October 2022 10:28:54
---

# Proposed Method
**Objectives and Significance**
The primary objective of this study is to test the efficiency of support vector regression in predicting Philippine stock market prices. More specifically, the author hope to accomplish the following:
 - To obtain the best possible model for predicting the Philippine Stock Exchange index prices from June 2015 to June 2019, using appropriate feature selection methods and hyperparameter tuning. 
 - To compare the performance of the obtained model before the COVID-19 pandemic (from June 2015 to June 2019) against during and after the COVID-19 pandemic (June 2019 to June 2022).
 - To apply and evaluate the performance of SVR in predicting the stock prices of three other Philippine companies.
 -  To predict future 10-day close prices of the Philippine Stock Exchange index with reasonable accuracy.


###### Data Collection
Four stock prices datasets was downloaded directly from Yahoo! Finance. One of these downloaded data contains price information from the Philippine Stock Exchange index, the primary data under study, which is the congregation of the top 30 publicly-listed companies in the country. The other three datasets are from Banco De Oro (stock code: BDOUY), San Miguel Corporation (SMGBY) and PLDT Inc. (PHI). These companies are chosen because they are one of the biggest business in the Philippines and are representative of their different industries which are finance/banking, food & beverages, and services respectively.

The datasets were downloaded in *.csv* format. The data is read using the `pd.read_csv` command with the date column as its index in `datetime` format. This is to allow the use of specific commands only available to time series data. Each dataset is composed of 6 columns which are Open, High, Low,  Close, Adj Close and Volume. Only the Open and Adj Close prices will be used for the purpose of this study. The Adj Close column contains the stock's adjusted close prices after giving out dividends to their shareholders. This will be the target variable in this study. Note that by predicting close prices, we are referring to predicting the values from the Adj Close column. 

###### Data Preparation  (*Cleaning, Feature Engineering, Feature Scaling*)

The integrity of data is ensured via a 2-step method: (1) all zero values are replaced by `Nan` and then (2) all rows with `NaN` values are removed from the dataset. A total number of 373 columns out of 2975 columns are removed from the dataset via this process which amounts to 12.54% of the original dataset.

A 3-year time frame is selected to be the period under study starting from June 2019 to June 2022. The total number of samples within this period is 729. 

The technical analysis indicators are computed using the `ta` python library. Five technical analysis indicators are added as new columns to the data set. These are:
- SMA - Simple Moving Average
- WMA - Weighted Moving Average
- RSI - Relative Strength Index
- ADI - Accumulation/Distribution Index
- ATR - Average True Range

A 14-day window period is applied to the above listed indicators. We note that some indicators do not output values during their window period. Thus, we remove the first 15 days from our sample set. We use the use the following columns: Open, high, Low, Volume, SMA, WMA, RSI, ADI, and ATR to form the feature set while the Adj Close column would be designated as out target vector. 

*(Find references why 14-days is the most common)* 

###### Exploratory Analysis

###### Model Selection
The data is normalized using the `--` function. The data is split into training and validation sets. The training set comprised of -- days. The validation set comprised of -- days. An SVR predictor is fitted to the training set and is tested on the validation set. Result is shown in figure 1. 


**Model Evaluation**
![[Review of Evaluation Metrics]]