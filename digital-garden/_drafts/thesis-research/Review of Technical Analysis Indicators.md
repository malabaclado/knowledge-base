---
tags:
alias:
creation-date: Sunday 23rd October 2022
last-modified-date: Sunday 23rd October 2022 20:50:54
---

# Review of Technical Analysis Indicators

**What is Technical Analysis? (Start with the difference between technical analysis and fundamental analysis)**

Existing literature reveals that there are two approaches to stock market prediction - technical analysis and fundamental analysis. Technical analysis is concerned with predicting future stock price based solely on hypotheses derived from the stock prices. Fundamental analyses on the other hand focuses on how the company image and policies affect investor buying strategies. 

Technical analysis is usually done using different indicators, which describes different aspects of the historical stock prices to predict future price direction based on trends. 

Technical analyses literature states that when using technical analysis indicators as features for a machine learning predictor, it is best not to use indicators that describe the same thing. 

We'll discuss the technical analysis indicators that are used in this paper, namely: Simple Moving Average (SMA), Weighted Moving Average (WMA), Relative Strength Index (RSI), Accumulation/Distribution Index (ADI) and the Average True Range (ATR).


## Simple Moving Average

A moving average is an indicator that computes the average price of an asset over a specified time period. It may be used to forecast trends and provide buy and sell recommendations. The most common way to interpret a moving average is to analyze the relationship between the moving average of a security's price and the actual price of the security. A buy signal is created when the security's price rises above its moving average, and a sell signal is issued when the security's price falls below its moving average. ([[Technical Analysis from A to Z|achelisTechnicalAnalysis2000]])

The Simple Moving Average (SMA) is the arithmetic mean of $N$ past prices $Cl_{i}$ and is describe by the following equation: 
$$SMA = \frac{1}{N} \sum^N_{i=1}Cl_{i}$$


The Weighted Moving Average (WMA) is a variation of the simple moving average that gives more value to latest prices. It is computed by assigning weights to the prices and dividing by the total sum of weights. The formula for calculating WMA is given by: 
$$WMA = \frac{P Cl_{i} + (P-1) Cl_{i-1} +...+ Cl_i-P}{P + (P-1) +...+ 1}$$


## Relative Strength Index 

## Accumulation/Distribution Index

## Average True Range 





---
*References:*
- TA documentation
- Technical Analysis from A to Z (book)