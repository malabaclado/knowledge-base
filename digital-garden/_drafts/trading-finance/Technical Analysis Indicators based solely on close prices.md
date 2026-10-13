---
tags:
alias:
creation-date: Thursday 22nd December 2022
last-modified-date: Thursday 22nd December 2022 02:24:06
---


# Technical Analysis Indicators based solely on close prices


# Momentum Indicators

[[Kaufman's Adaptive Moving Average (KAMA)]]

## True Strength Index 
- True Strength Index (TSI) is a momentum oscillator based on a double smoothing of price changes.
- By smoothing price changes, TSI captures the ebbs and flows of price action with a steadier line that filters out the noise.
- s with most momentum oscillators, chartists can derive signals from overbought/oversold readings, centerline crossovers, bullish/bearish divergences and signal line crossovers.
### Calculation (TSI)
First, calculate the price change from one period to the next. Second, calculate a 25-period EMA of this price change. Third, calculate a 13-period EMA of this 25-period EMA to create a double smoothing. The same double smoothing technique is used for the absolute price change. After these initial calculations, divide the double smoothed price change by the absolute double smoothed price change and multiply by 100 to move the decimal two places.

```
Double Smoothed PC
------------------
PC = Current Price minus Prior Price
First Smoothing = 25-period EMA of PC
Second Smoothing = 13-period EMA of 25-period EMA of PC

Double Smoothed Absolute PC
---------------------------
Absolute Price Change |PC| = Absolute Value of Current Price minus Prior Price
First Smoothing = 25-period EMA of |PC|
Second Smoothing = 13-period EMA of 25-period EMA of |PC|

TSI = 100 x (Double Smoothed PC / Double Smoothed Absolute PC)
```

### Interpretation (TSI)
- The True Strength Index (TSI) is an oscillator that fluctuates between positive and negative territory. As with many momentum oscillators, the centerline defines the overall bias. The bulls have the momentum edge when TSI is positive and the bears have the edge when it's negative.
- The last parameter in the TSI setting is the signal line, which is simply an exponential moving average of TSI. Signal line crossovers are by far the most common signals, meaning there will be good, bad and ugly signals. In an effort to reduce signals and noise, chartists should consider increasing the settings for TSI or the price chart settings. The example below shows TSI(40,20,10) using a weekly chart. This means the signal line is a 10-period EMA of TSI.

[True Strength Index (TSI) [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:true_strength_index)

---
[[Stochastic RSI]]

---
## Rate of Change (ROC)
- is a pure momentum oscillator that measures the percent change in price from one period to the next.
- The ROC calculation compares the current price with the price “n” periods ago. The plot forms an oscillator that fluctuates above and below the zero line as the Rate-of-Change moves from positive to negative.

### Calculation (ROC) 
```
ROC = [(Close - Close n periods ago) / (Close n periods ago)] * 100
```

### Interpretation (ROC) 
- As noted above, the Rate-of-Change indicator is momentum in its purest form. It measures the percentage increase or decrease in price over a given period of time. Think of it as the rise (price change) over the run (time). 
- In general, prices are rising as long as the Rate-of-Change remains positive. Conversely, prices are falling when the Rate-of-Change is negative.

[Rate of Change (ROC) [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:rate_of_change_roc_and_momentum)

---
## # Percentage Price Oscillator (PPO) 
-  The Percentage Price Oscillator (PPO) is a momentum oscillator that measures the difference between two moving averages as a percentage of the larger moving average.
- While MACD measures the absolute difference between two moving averages, PPO makes this a relative value by dividing the difference by the slower moving average (26-day EMA).

### Calculation (PPO) 
```
Percentage Price Oscillator (PPO): {(12-day EMA - 26-day EMA)/26-day EMA} x 100

Signal Line: 9-day EMA of PPO

PPO Histogram: PPO - Signal Line
```

- MACD levels are affected by the price of a security. A high-priced security will have higher or lower MACD values than a low-priced security, even if volatility is basically equal. This is because MACD is based on the absolute difference in the two moving averages.

---

# Volatility 

## [[Ulcer Index ]]

- Ulcer Index is a volatility indicator that measures downside risk
- Originally, the index was designed with mutual funds in mind, which is why it is only focused on downside risk. Mutual funds are designed to make money by increasing in value; the only risk, therefore, is the drawdown or downside. As its name implies, the Ulcer Index measures the drawdown investors can expect to stomach on any given security.

### Calculation (UI) 
- Based on closing prices, the Ulcer Index measures volatility based on price depreciation from its high over a specific look-back period. The index is zero if prices close higher each period. This means there is no downside risk because prices are steadily rising. Prices, of course, do not steadily rise, so there will be declines along the way. 
- Using a default setting of 14 periods, the Ulcer Index reflects the expected percentage drawdown over this period. The table shows a sample calculation for 14-periods.

```
Percent-Drawdown = ((Close - 14-period Max Close)/14-period Max Close) x 100

Squared Average = (14-period Sum of Percent-Drawdown Squared)/14 

Ulcer Index = Square Root of Squared Average
```

“Ulcer Index measures the depth and duration of percentage drawdowns in price from earlier highs. The greater a drawdown in value, and the longer it takes to recover to earlier highs, the higher the UI. Technically, it is the square root of the mean of the squared percentage drawdowns in value. The squaring effect penalizes large drawdowns proportionately more than small drawdowns.”

Keep in mind that the Ulcer Index is not an indicator per se. It is just a measure of downside risk that can be used to compute risk-adjusted returns.

[Ulcer Index [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:ulcer_index)


---
# Trend 
## TRIX 
- TRIX is a momentum oscillator that displays the percent rate of change of a triple exponentially smoothed moving average.
- With its triple smoothing, TRIX is designed to filter out insignificant price movements.
- Chartists can use TRIX to generate signals similar to MACD.
- A signal line can be applied to look for signal line crossovers. A directional bias can be determined with the absolute level. Bullish and bearish divergences can be used to anticipate reversals.

### Calculation (TRIX)
TRIX is the 1-period percentage rate-of-change for a triple smoothed exponential moving average (EMA), which is an EMA of an EMA of an EMA. Here is a breakdown of the steps involved for a 15 period TRIX.

1. Single-Smoothed EMA = 15-period EMA of the closing price
2. Double-Smoothed EMA = 15-period EMA of Single-Smoothed EMA
3. Triple-Smoothed EMA = 15-period EMA of Double-Smoothed EMA
4. TRIX = 1-period percent change in Triple-Smoothed EMA

- TRIX is an indicator that combines trend with momentum.
- The triple smoothed moving average covers the trend, while the 1-period percentage change measures momentum. In this regard, TRIX is similar to MACD and PPO.
- The standard setting for TRIX is 15 for the triple smoothed EMA and 9 for the signal line.
- Chartists looking for more sensitivity should try a shorter timeframe (5 versus 15). This will make the indicator more volatile and better suited for centerline crossovers.

[TRIX [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:trix)

---
## # Schaff Trend

- The Schaff Trend Cycle (STC) is a charting indicator that is commonly used to identify market trends and provide buy and sell signals to traders.
- Compared to the popular MACD indicator, STC will react faster to changing market conditions.
- While the STC indicator seems to boast higher reliability than MACD, it has some inherent flaws. Namely, it can linger in overbought and oversold territory for extended periods of time.

## MACD 
- The MACD turns two trend-following indicators, moving averages, into a momentum oscillator by subtracting the longer moving average from the shorter one. As a result, the MACD offers the best of both worlds: trend following and momentum. 
-  The MACD fluctuates above and below the zero line as the moving averages converge, cross and diverge. Traders can look for signal line crossovers, centerline crossovers and divergences to generate signals. Because the MACD is unbounded, it is not particularly useful for identifying overbought and oversold levels.

### Calculation (MACD) 
```
MACD Line: (12-day EMA - 26-day EMA)

Signal Line: 9-day EMA of MACD Line

MACD Histogram: MACD Line - Signal Line
```

- The MACD line is the 12-day [Exponential Moving Average](https://school.stockcharts.com/doku.php?id=technical_indicators:moving_averages "technical_indicators:moving_averages") (EMA) less the 26-day EMA. Closing prices are used for these moving averages. A 9-day EMA of the MACD line is plotted with the indicator to act as a signal line and identify turns.

## Interpretation 
-  Positive MACD = short EMA above longer EMA = upside momentum is increasing. 
- Negative MACD = short EMA below longer EMA = downside momentum is increasing
- As its name implies, the MACD is all about the convergence and divergence of the two moving averages. Convergence occurs when the moving averages move towards each other. Divergence occurs when the moving averages move away from each other. 
- The shorter moving average (12-day) is faster and responsible for most MACD movements. The longer moving average (26-day) is slower and less reactive to price changes in the underlying security.


[MACD (Moving Average Convergence/Divergence Oscillator) [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:moving_average_convergence_divergence_macd)


---

##  Know Sure Thing (KST)
- Developed by Martin Pring, Know Sure Thing (KST) is a momentum oscillator based on the smoothed rate-of-change for four different timeframes.
- In short, KST measures price momentum for four different price cycles, combining them into a single momentum oscillator. Like any other unbound momentum oscillator, chartists can use KST to look for divergences, signal line crossovers, and centerline crossovers.

### Calculation (KST)
```
RCMA1 = 10-Period SMA of 10-Period Rate-of-Change 
RCMA2 = 10-Period SMA of 15-Period Rate-of-Change 
RCMA3 = 10-Period SMA of 20-Period Rate-of-Change 
RCMA4 = 15-Period SMA of 30-Period Rate-of-Change 

KST = (RCMA1 x 1) + (RCMA2 x 2) + (RCMA3 x 3) + (RCMA4 x 4)  

Signal Line = 9-period SMA of KST
```

---
##  Detrended Price Oscillator (DPO)
- The Detrended Price Oscillator (DPO) is an indicator designed to remove trend from price and make it easier to identify cycles. 
- DPO does not extend to the last date because it is based on a displaced moving average. However, alignment with the most recent date is not an issue because DPO is not a momentum oscillator. Instead, DPO is used to identify cycle highs/lows and estimate cycle length

### Calculation (DPO)
```
Price {X/2 + 1} periods ago less the X-period simple moving average.
```

---
See also: [[Technical Analysis Indicators based solely on close prices]]