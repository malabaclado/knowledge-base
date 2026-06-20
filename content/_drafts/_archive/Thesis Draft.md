---
tags:
alias:
creation-date: Thursday 8th September 2022
last-modified-date: Thursday 8th September 2022 08:34:41
---

# Thesis Draft
This is the draft of my thesis. 

## Tentative Title
- Short-term stock price prediction using [[Support Vector Regression (ChatGPT)]] with fine-tuning
- Machine-learning based stock price prediction model for Philippine Stock Exchange Index 
- Predicting PSEI stock prices using [[Support Vector Regression (ChatGPT)]] with fine-tuning
- Predicting Philippine stock prices using Support Vector Regression
- Philippine stock price prediction using Support Vector Regression with Bayesian optimization
- Predicting Philippine stock prices using Support Vector Regression with Bayesian Optimization
- Predicting Philippine Stock Prices using Support Vector Regression with Bayesian Optimization
- Technical Analysis Prediction of Philippine Stock Prices using Support Vector Regression

# Settings
- Train-Test Split Ratio: 7:3
- CV: TimeSeriesSplit(n=5)
- Metric: RMSE
- Date: 2010-2018
- Forecast: 30-days

# Objectives 
- How does optimizing the parameters affect predictive performance?
	- How does Bayesian optimization help in predicting performance?
	- How different hyperparameters affect predictive performance?
		- How kernel choice affects the predictive performance?
- How does the use of technical indicators give better performance? 
- OHLV vs TA indicators



# Model Validation
- Analysis of Residuals
- Goodness of Fit
- Cross Validation Results


# Results 
- Table: Kernel - RMSE - No. of support vectors
- Table: RMSE, MAPE, R2 results for each kernel (on test set) 
- Figure: Train-Test Graph of the three kernels
- Table: Forecasting - 5-day, 20-day, 60-day, 240-day
	- Columns: MAPE, RMSE, 
- Figure: Actual VS Predicted Values
- 

Additional results if implementing Bayesian Optimization:
- Table: GridSearch Results vs Bayesian Optimization 
	- Results
	- No. of function evaluations 
	- Runtime
- Figure: Bayesian-optimization 


# New Outline
- Introduction 
- Support Vector Regression 
- Bayesian Optimization 
- Methodology 
- Results and Discussion 
- Conclusion 
- Appendices

---

## Recap 
- Support Vector Regression
	- Efficient Learning Machines (book)
	- Pattern Recognition and machine learning
	- dashFinetunedSupportVector2021
	- [[Support Vector Machines]]
	- [[Support Vector Regression (ChatGPT)]]
	- 

Sources for topic: Support Vector Regression
- sklearn docs
- Efficient Learning Machines (book)
- Pattern Recognition and Machine Learning

---

[[Thesis direction]]

[[Abstract (New)]]
[[Abstract (Old)]]

[[1Introduction]]
[[2Literature]]
[[Review of Support Vector Regression]]
[[3Methodology]]
[[Thesis Scratchpad]] 
[[Thesis - Conclusion]]
[[Appendix - Lagrange Multipliers]]

[[Mercer's Theorem]]

---
[[Introduction (Draft)]]
[[Related Literature (Draft)]]
[[Conclusion(Draft)]]


---
![[Readings for Thesis]]