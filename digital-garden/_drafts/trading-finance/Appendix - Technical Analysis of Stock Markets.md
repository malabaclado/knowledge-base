  This section undertakes a thorough examination of the technical analysis indicators utilized in this study. Our focus will be on exploring their concise historical background, their overarching purpose, the formulas used to represent them, and the significance of their interpretations.

# **Exponential Moving Average** ✅

A moving average is the average price of a security at a given time. It is calculated over a set period of time. An $n$-day moving average is calculated over a period of $n$ days. A Simple Moving Average (SMA) is the sum of the security's prices divided by the period $n$.^[Technical Analysis from A to Z]

An Exponential Moving Average (EMA) is a type of moving average that places a greater weight and significance on the most recent data points. It tends to respond more quickly to price changes than SMA which assigns equal weights to all values. 

The formula for EMA is given by:
$$EMA_{t}=\alpha \mathrm{x}_{t} + (1-\alpha)EMA_{t-1}$$
where $EMA_{t}$ is the exponential moving average value at time $t$, $EMA_{t-1}$ is the previous EMA value, and $\alpha$ is the smoothing factor. The smoothing factor determines the weight given to the current input value versus the previous EMA value. It is calculated using the formula: $$\alpha=\frac{2}{n+1}$$ where $n$ is the period.

EMA is an indicator of market trend. A upward EMA means that there is an uptrend in the market. A downward, on the other hand, implies a downtrend. A rising EMA is usually interpreted as a support for price activity and a falling EMA as a resistance. Investors that adhere to this interpretation look to buy when the price is near the rising EMA and sell when the price is near the falling EMA.^[[What is EMA? How to Use Exponential Moving Average With Formula (investopedia.com)](https://www.investopedia.com/terms/e/ema.asp)]


# **Relative Strength Index** ✅
The Relative Strength Index (RSI) is a widely recognized oscillator that was initially introduced by Welles Wilder in a publication appearing in Commodities Magazine (currently known as Futures Magazine) in June 1978. Further elaboration on the RSI can be found in Wilder's book titled *"New Concepts in Technical Trading Systems"*

The Relative Strength Index (RSI) serves as a price-following indicator that provides insights into the strength and potential reversal points of a security. Ranging from 0 to 100, the RSI compares the magnitude of recent losses and gains, offering indications of overbought or oversold conditions. When the RSI surpasses the threshold of 70, it suggests that the security may be overbought, implying a potential downward price correction. Conversely, an RSI value below 30 indicates potential oversold conditions, hinting at a potential upward price correction. Thus, the RSI aids traders and investors in identifying potential opportunities for buying or selling securities based on the prevailing market sentiment.^[Henrique (2018)]. 

The formula for calculating RSI is given by:
$$RSI_{t} = 100 - \left(  \frac{100}{1+RS} \right)$$
where $RSI_{t}$ is the Relative Strength Index value at time $t$, and $RS$ is the relative strength. To calculate the relative strength, calculate the average gain $gain_{ave,n}$ and the average loss $loss_{ave,n}$ over a look-back period $n$. 
$$RS_{t} = \frac{gain_{ave, n}}{loss_{ave,n}}$$

The average gain $gain_{ave,n}$ and the average loss $loss_{ave,n}$ can be computed using these equations:
$$\text{gain}_{ave} = \sum^{x}_{x-n}  r_{up} \quad \text{where } \space r_{up}=\begin{cases}
	0, \space &\text{if } x_{i} - x_{i-1} \leq 0 \space \text{\textit{(loss)}} \\
	x_{i} - x_{i-1}, \space &\text{otherwise}
\end{cases}$$

$$\text{loss}_{ave} = \sum^{x}_{x-n}  r_{dn} \quad \text{where } \space r_{dn}=\begin{cases}
	0, \space &\text{if } x_{i} - x_{i-1} \geq 0  \space \text{\textit{(gain)}}\\
	|x_{i} - x_{i-1}|, \space &\text{otherwise}
\end{cases}$$


According to the equations provided above, the average gain is calculated by adding up all the gains and assigning a value of 0 whenever a loss occurs. On the other hand, the average loss is determined by adding up all the losses that happen on a daily basis, and assigning a value of 0 whenever a gain occurs.


# **Ulcer Index** ✅
The Ulcer Index, created in 1987 by Peter Martin and Byron McCann, is a volatility indicator that assesses downside risk. It first appeared in their 1989 publication, *The Investor's Guide to Fidelity Funds*. The Ulcer Index, like its name implies, assesses the maximum loss investors may expect to stomach on a given security.^[[Ulcer Index [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:ulcer_index)]


The formula for Ulcer Index is as follows:
$$UI_{t} = \sqrt{ \left[ \frac{1}{n}  \sum_{t-n}^{t}R_{k}^{2}\right] }$$



where $R_{k}$, known as the percentage-drawdown is calculated by:
$$R_{t} = \frac{y_{t} - \hat{y}_{t,n}}{\hat{y}_{t,n}} \times 100$$

where $y_{t}$ is the price at time $t$, and $\hat{y}_{t,n}$ is the highest price over the look-back period $n$ starting from time $t$.

The Ulcer index measures the depth and duration of percentage drawdowns in price from earlier highs. The greater the drawdown value, the longer it takes to recover, hence, the higher the UI. A UI value of zero means there is a higher high each period. This means that there is no downside risk because the prices are steadily rising. The Ulcer Index is a volatility metric that only captures persistent downward fluctuations in share prices and excludes upward volatility. The greater the continuous and long drop, the higher the index, and the greater the likelihood that investing in it would result in ulcers or restless nights.^[Kumaran (Zotero)]


# **Moving Average Convergence/Divergence**

The Moving Average Convergence/Divergence (MACD) is a momentum indicator that uses moving averages to identify trends and generate trading signals. It is calculated by subtracting the 26-day Exponential Moving Average (EMA) from the 12-day EMA. The 12-day EMA emphasizes shorter-term price action, while the 26-day EMA focuses on longer-term price movements. The MACD Line represents the difference between these two EMAs and serves as an indication of the overall trend direction. 

A signal line, usually a 9-day EMA of the MACD Line is used for generating trading signals whenever it crosses above or below the MACD Line. When the MACD line (the fast line) crosses above the signal line (the slow line), it generates a bullish signal, indicating a potential upward trend. Conversely, when the MACD line crosses below the signal line, it generates a bearish signal, indicating a potential downward trend. Traders interpret these crossovers as potential entry or exit points. 

In this study, instead of the MACD line, we used the MACD histogram values. The MACD Histogram is derived by subtracting the Signal Line from the MACD Line. This provides a visual representation of the difference between the MACD Line and the Signal Line, indicating the strength and momentum of the underlying trend.

The formula for MACD value at time $t$ is:
$$MACD_{t} = EMA_{fast,t} - EMA_{slow, t}$$

The formula for MACD Histogram at time $t$ is:
$$MACD_{hist, t}  = MACD_{t} - EMA_{signal,t}$$


The MACD histogram can be interpreted based on its magnitude, and direction. The magnitude of the MACD Histogram values reflects the strength and intensity of the underlying trend. Higher values indicate a stronger momentum, whether bullish or bearish. When the MACD Histogram value goes above the zero line, it suggests that the MACD Line is above the signal line, indicating bullish momentum. Conversely, when the bars are below the zero line, it indicates that the MACD Line is below the signal line, suggesting bearish momentum.






# **Kaufmann Adaptive Moving Average** ✅
Kauman Adaptive Moving Average is an trend indicator created by Perry Kaufmann in 19995 and was first introduced in his book *Smarter Trading.*^[boskoskaALTERNATIVESOURCESFINANCING] KAMA will closely follow prices when the price swings are relatively small and the noise is low. KAMA will adjust when the price swings widen and follow prices from a greater distance. **This trend-following indicator can be ==used to identify the overall trend, time turning points and filter price movements==.**^[[Kaufman's Adaptive Moving Average (KAMA) [ChartSchool] (stockcharts.com)](https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average)]

The term "adaptive" in the context of the Kaufman's Adaptive Moving Average (KAMA) refers to its capability to dynamically adapt and modify its smoothing factor in response to the current market conditions. This adjustment process is facilitated by the utilization of Kaufman's Efficiency Ratio (ER), a metric that quantifies the efficiency of the market. This distinctive feature of KAMA sets it apart from traditional moving averages, which typically employ fixed smoothing factors that do not adjust to changing market dynamics.

The formula to compute KAMA is given by:
$$KAMA_{t} = KAMA_{t-1} + \alpha (P_{t} - KAMA_{t-1})$$
where
- $KAMA_{t}$ is the value at time $t$,
- $KAMA_{t-1}$ is the previous KAMA value,
- $P_{t}$ is the stock price at time $t$ and
- $\alpha$ is the smoothing factor.


ER is computed as:
$$ER = \frac{D_{t,n}}{V_{t,n}}$$
where mometum is computed as:
$$D_{t,n} = P_{t} - P_{t-n}$$
and volatility is computed as:
$$V_{t,n} = \sum^{n}_{i=1} | P_{t} - P_{t-i}|$$

The smoothing factor is computed as:
$$\alpha = (ER\times(\alpha_{fast} - \alpha_{slow})) + \alpha_{slow}$$


---



---
See also: [[Thesis Scratchpad]]