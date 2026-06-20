---
tags:
alias:
creation-date: Thursday 6th April 2023
---

Developed by Perry Kaufman, **Kaufman's Adaptive Moving Average (KAMA) is a ==moving average designed to account for market noise or volatility==**. KAMA will closely follow prices when the price swings are relatively small and the noise is low. KAMA will adjust when the price swings widen and follow prices from a greater distance. **This trend-following indicator can be ==used to identify the overall trend, time turning points and filter price movements==.**^[[Kaufman's Adaptive Moving Average (KAMA) [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average)]



# Interpreting KAMA 
![](https://school.stockcharts.com/lib/exe/fetch.php?media=technical_indicators:kaufman_s_adaptive_moving_average:kama-2-hogexam.png)

**First, a ==cross above or below KAMA indicates directional changes in prices==.** 

![](https://school.stockcharts.com/lib/exe/fetch.php?media=technical_indicators:kaufman_s_adaptive_moving_average:kama-2-hogexam.png)

**Second, chartists can use the direction of KAMA to define the overall trend for a security.** This may require a parameter adjustment to smooth the indicator further. **Chartists can change the middle parameter, which is the fastest EMA constant, to smooth KAMA and look for directional changes.** The trend is down as long as KAMA is falling and forging lower lows. The trend is up as long as KAMA is rising and forging higher highs. T**he Kroger example above shows KAMA(10,5,30) with a steep uptrend from December to March and a less-steep uptrend from May to August.**

![](https://school.stockcharts.com/lib/exe/fetch.php?media=technical_indicators:kaufman_s_adaptive_moving_average:kama-4-mmmfilter.png)

 **Chartists can ==use a longer-term KAMA to define the bigger trend== and a ==shorter-term KAMA for trading signals==.** For example, KAMA (10,5,30) could be used as a trend filter and be deemed bullish when rising. Once bullish, chartists could then look for bullish crosses when price moves above KAMA (10,2,30). The example above shows MMM with a rising long-term KAMA and bullish crosses in December, January, and February. Long-term KAMA turned down in April and there were bearish crosses in May, June, and July.


# Formula
There are several steps required to calculate Kaufman's Adaptive Moving Average. Let's first start with the settings recommended by Perry Kaufman: KAMA(10,2,30).

-   10 is the number of periods for the Efficiency Ratio (ER).
-   2 is the number of periods for the fastest EMA constant.
-   30 is the number of periods for the slowest EMA constant.
    

**Before calculating KAMA, we need to calculate the Efficiency Ratio (ER) and the Smoothing Constant (SC).** Breaking down the formula into bite-size nuggets makes it easier to understand the methodology behind the indicator.












---
See also: [[Technical Analysis Indicators based solely on close prices]]