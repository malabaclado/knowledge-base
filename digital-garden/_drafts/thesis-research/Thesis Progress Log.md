---
tags: progress-note
alias:
creation-date: Tuesday 11th April 2023
---

# What to do next
- # Coding Part
	- Currently working on: main_project3
	- Create the 2 forecasting methods: (Remove the open prices)
		1. Lagged moving average (Lagged 10 WMA/EMA)
		2. Recurring moving average (Recalculate indicators after every prediction)
	- [ ] ~~Recreate baseline project: Recreate results done on first experiment~~ I would no longer do this.
		- Indicators: SMA, WMA, RSI (10,20,60)
		- Use time series CV
		- No SelectKBest
		- Use three-year training data
		- [ ] Perform forecasting
		- [ ] Do baseline analysis on four other stock prices
	- [ ] Using the baseline project details, test different indicators:
		- MACD, RSI, UI
		- KAMA, RSI, UI
		- EMA, RSI, UI
		- MACD, KAMA, UI
		- SMA, WMA, RSI
	- [ ] Test the effectiveness of changing the training size: 3-year vs 10-year
	- [ ] Try removing Open price from the feature set. (All features depend on closing price only
	**Further research**
	- [ ] Use firefly algorithm instead of GSCV to predict stock prices
	- [ ] Compare firefly algorithm and GSCV results
	- [ ] Use eagle search algorithm to predict stock prices
	- [ ] Compare firefly algorithm, eagle search algorithm and GSCV
- # Writing Part
	- [ ] Complete review of SVR  
	- [ ] Illustrations/Frameworks:  
	    - [ ] Time Series Split   
	    - [ ] Grid Search Cross CV  
	- [ ] Add mention of time series split in methodology  
  
# Progress History  
- April 5  
	- [x] Wrote functions into a py file for faster setup of experiments.  
	- [x] Researched more abt the technical analysis indicators: ATR, MACD, RSI, KAMA, ADI, OBV  
	- **Question idea: What if we can use an assymetric loss function for the SVR for that it is more sensitive to losses than to gains?**
- April 11
	- [x] Tried indicators: EMA (5,10,60), KAMA, RSI, MACD
	- [x] Checked if there is improvement when using MACD vs MACD Histogram
	- [x] Made code for assessing multiple combinations of ta indicators (functions stored in a py file)

# Results
File: stock-project-indicators-testing.ipnyb
Testing different indicators.
- Training evaluation
	- ![](https://i.imgur.com/Uo00Dtm.png)
		- 3 Lowest Train RMSE: indicators 8,5,3
		- 3 Lowest Test RMSE: indicators 5,9,4
		- 3 Lowesr Test MAPE: indicators 5,9,4
- Forecast evaluation
	- ![](https://i.imgur.com/7chlHra.png)
		- 3 Lowest Forecast RMSE: indicators 6,7,9
		- 3 Lowest Forecast MAPE: indicators 7,9,5
- Observations
	- MACD vs MACD Histogram? 
		- A: When SMA(10,20,60) is used, it is better to use MACD_Histogram. When SMA(5,20,60) is used, it is better to use MACD. In forecast results, MACD_Histogram is better.
	- EMA vs SMA? 
		- A: Using SMA yielded better results in both Test and Forecasting
	- Interval (5,20,60) VS (5,10,60)
		- A: If using MACD, interval (5,10,60) is better. If using MACD_Histogram, interval (5,20,60) is better.
