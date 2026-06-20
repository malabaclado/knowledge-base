---
tags:
alias:
creation-date: Monday 4th July 2022
last-modified-date: Monday 4th July 2022 19:56:09
---

# Time Series (Kaggle Course)

**What is a Time Series?**
The basic object of forecasting is the time series, which is a set of observations recorded over time. In forecasting applications, the observations are typically recorded with a regular frequency, like daily or monthly.

There are two kinds of features unique to time series: time-step features and lag features.


**Time-step features**
Time-step features are features we can derive directly from the time index. The most basic time-step feature is the **time dummy**, which counts off time steps in the series from beginning to end.

Time-step features let you model **[[time dependence]]**.


**Lag features**
To make a **lag feature** we shift the observations of the target series so that they appear to have occured later in time. Here we've created a 1-step lag feature, though shifting by multiple steps is possible too.

Lag features let us fit curves to _lag plots_ where each observation in a series is plotted against the previous observation.

More generally, lag features let you model **[[serial dependence]]**.