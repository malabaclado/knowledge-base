---
tags:
alias:
creation-date: Friday 19th May 2023
---

Title: Technical Analysis Prediction of Philippine Stock Prices using Support Vector Regression

- Technical Analysis Prediction of Philippine Stock Prices using Support Vector Regressions with Bayesian Optimization.
- We used technical analysis indicators to make a prediction model
- We trained a support vector regression model to predict stock prices of PSEI
- We used grid search with k-fold cross validation to test out hyperparameters.
- Proposed a method to predict future close prices based on SVR model. We tested its performance on different prediction periods: 10-day, 20-day, 60-day and 240-day.

- Idea: Therefore, while SVR can be a useful tool for forecasting future stock prices, it should be used as one of many tools to inform investment decisions, and not relied on as the sole factor in making investment decisions. Additionally, it's important to regularly review and update the model with new data, as market conditions can change rapidly.

Thoughts on this:
- Pwede pa baguhin yung intro. (Give a stronger, and more positive intro)

# Abstract

Predicting the stock market is a highly rewarding yet a very challenging task due to the volatility and nonstationary features of financial time series data. The rise of efficient learning machines led to the development of expert systems that aid in decision making, which is a growing area in research in financial forecasting. Support Vector Regression (SVR) is a supervised machine learning algorithm that is known for its robustness, sparsity, and global optimum solutions. Using technical analysis indicators as predictors, the main goal of this paper to create a regression model for predicting the daily stock prices of the Philippine Stock Exchange Index (PSEI) using SVR. Seven years of historical stock price data was used to train and evaluate the model, the hyperparameters were obtained using grid search method with time series cross validation technique. The optimal SVR model demonstrate a mean absolute percentage error (MAPE) of 0.0083\%.A recursive multi-step forecasting strategy was implemented to evaluate the model's capability to predict future prices. The results show that the model can reliably forecast up to two trading weeks with MAPE of 0.0034\%. The findings of this study shows that SVR is an invaluable tool for predicting stock prices. This is the first study to investigate support vector regression using technical analysis in the context of Philippine markets.
