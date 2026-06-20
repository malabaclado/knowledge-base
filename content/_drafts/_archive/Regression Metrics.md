---
tags:
alias:
creation-date: Sunday 23rd October 2022
last-modified-date: Sunday 23rd October 2022 14:41:30
---

# Regression Metrics
## R2 Score
The `r2_score` function computes the coefficient of determination.

Represents the proportion of variance (of y) that has been explained by the independent variables in the model. It provides an indication of goodness of fit and therefore a measure of how well unseen samples are likely to be predicted by the model, through the proportion of explained variance. 

A model that always predicts the expected value of the target variable, regardless of input has an R2 score of 0.

Note that when prediction residulas have zero mean, the R2 score and the [[explained variance score]] are identical.

**Formula**
![[SmartSelect_20221023_150150_Obsidian.jpg]]
## Mean Absolute Percentage Error
The idea of this metric is to be sensitive to relative errors. It is for example not changed by a global scaling of the target variable.

![[SmartSelect_20221023_150624_Obsidian.jpg]]

## Root Mean Squared Error
The Root Mean Square Error (RMSE) is a frequently used measure of the differences between values (sample or population values) predicted by a model or an estimator and the values observed. 

RMSE represents the square root of the second sample moment of the differences between predicted values and observed values (or the quadratic mean of these differences). 

RMSE is a measure of accuracy.

RMSE is always non-negative, and a value of 0 would indicate a perfect fit to the data.


**Root Mean Squared Error** is the standard deviation of the residuals (prediction errors). Residuals are a measure of how far from the regression line the data points are. In effect, RMSE is a measure of how spread out the residuals are. In other words, it tells you how concentrated the data is around the line of best fit. 