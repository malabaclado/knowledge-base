---
tags:
alias:
creation-date: Tuesday 21st March 2023
---

==Developed by Peter Martin and Byron McCann in 1987, the Ulcer Index is a volatility indicator that measures downside risk.== It was first introduced in their 1989 book, _The Investor's Guide to Fidelity Funds_.

As its name implies, the Ulcer Index measures the drawdown investors can expect to stomach on any given security. ==Many consider the Ulcer Index superior to the standard deviation and other measures of risk.==

# Calculation
**Based on closing prices, the Ulcer Index measures volatility based on price depreciation from its high over a specific look-back period.** The index is zero if prices close higher each period. This means there is no downside risk because prices are steadily rising. Prices, of course, do not steadily rise, so there will be declines along the way. Using a default setting of 14 periods, the Ulcer Index reflects the expected percentage drawdown over this period.


```
Percent-Drawdown = ((Close - 14-period Max Close)/14-period Max Close) x 100

Squared Average = (14-period Sum of Percent-Drawdown Squared)/14 

Ulcer Index = Square Root of Squared Average
```

# Interpretation
The following comes from Peter G. Martin himself:

> “Ulcer Index measures the depth and duration of percentage drawdowns in price from earlier highs. The greater a drawdown in value, and the longer it takes to recover to earlier highs, the higher the UI. Technically, it is the square root of the mean of the squared percentage drawdowns in value. The squaring effect penalizes large drawdowns proportionately more than small drawdowns.”

> [!NOTE]
> Martin notes that the Ulcer Index works well with weekly data.