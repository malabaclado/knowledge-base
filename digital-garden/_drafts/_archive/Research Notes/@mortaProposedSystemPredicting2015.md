---
tags: type/research-note 
alias: [Proposed system for predicting Buy, Hold and Sell recommendations for a publicly listed Philippine company using computational intelligence]
---
# Proposed system for predicting Buy, Hold and Sell recommendations for a publicly listed Philippine company using computational intelligence

> [!info]
> - **Cite Key:** [[@mortaProposedSystemPredicting2015]]
> - **Abstract:** Stock Price movement is a non-linear Financial Time Series. Short-term stock price prediction is best done through Technical Analysis using Artificial Intelligence to detect patterns and trigger buy and sell signals. This paper aims to develop an expert system using Technical Analysis and Support Vector Machines that emulates the reasoning and decision-making process of a technical analyst as applied to the Buy, Hold and Sell recommendations of Stock Price of two publicly listed companies in the Philippines.
> - **Bibliography:** Morta, R., & Dadios, E. (2015). Proposed system for predicting Buy, Hold and Sell recommendations for a publicly listed Philippine company using computational intelligence. _TENCON 2015 - 2015 IEEE Region 10 Conference_, 1–8. [https://doi.org/10.1109/TENCON.2015.7372952](https://doi.org/10.1109/TENCON.2015.7372952)
> - **Tags:** #Support-vector-machines, #Time-series-analysis, #Stock-markets, #Market-research, #Artificial-Intelligence, #Expert-systems, #Indexes, #Stock-Price-Prediction, #Support-Vector-Machines, #Technical-Analysis, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Abstract

- Stock Price movement is a non-linear Financial Time Series. Short-term stock price prediction is best done through Technical Analysis using Artificial Intelligence to detect patterns and trigger buy and sell signals. This paper aims to develop an expert system using Technical Analysis and Support Vector Machines that emulates the reasoning and decisionmaking process of a technical analyst as applied to the Buy, Hold and Sell recommendations of Stock Price of two publicly listed companies in the Philippines.

- I. INTRODUCTION

- Most traders classify themselves as either technicians (technical analysts) or fundamentalists (fundamental analysts). The fundamentalist studies the cause of market movement, while the technician studies the effect

- Technical Analysis is the study of market action, primarily through the use of charts, for the purpose of forecasting future price trends [1], [12]. The term “market action” includes the three principal sources of information available to the technician – price, volume and open interest. Open interest is used only in futures and options

- There are three premises on which the technical approach is based. The first is that Market Action discounts everything [1], [12]. This means that the technician believes that anything that can possibly affect the price – fundamentally, politically, psychologically, or otherwise – is actually reflected in the price of that market. It follows, therefore, that a study of price action is all that is required [1], [12]. Price action should reflect shifts in supply and demand [1], [12]. As a result, the technical analysts do not concern themselves with the reasons why prices rise or fall. The second premise is that Prices move in trends [1], [12], [22]. The concept of trend is absolutely essential to the technical approach. The third premise is that History repeats itself [1], [12], [22]. Chart patterns, for example, which have been identified and categorized over the past one hundred years, reflect certain pictures that appear on price charts. These pictures reveal the bullish or bearish psychology of the market. [1], [12], [22].

- The effectiveness of technical analysis has been researched extensively. The research results are mixed. A number of research that attest to the ability of technical analysis’ ability to forecast security returns include Brock, Lakonsihok and LeBaron [2], and Gencay [3], and those that oppose include Allen and Karjalainen [4], Lo, Mamaysky and Wang [5].

- Trend is defined as the direction of the market [1], [22]. Market moves are characterized by a series of zigzag patterns that resembles a series of waves with obvious peaks and troughs. It is the direction of these peaks and troughs that tell us the market trend [1], [7].

- These market trends have generally three directions; Uptrend, Downtrend, and Sideways trend as shown in Figure 1. The Uptrend is characterized by having higher highs and lows. On the other hand, a downtrend is characterized by having lower highs and lows [1], [7]. Sideways trend are characterized by highs and lows with a tight trading range. [1],[6].

- There are two major categories of price patterns – reversal and continuation [1]. Reversal patterns suggest a change in the direction of the trend, i.e. from an uptrend to a downtrend, and vice versa [1], [7]. Please note that the existence of a prior major trend is an important prerequisite for any reversal pattern [1], [7]. On the other hand, a continuation pattern suggests that a trend is taking a pause or a correction, before moving in its original direction [1].

- The five major reversal patterns are: 1) Head and Shoulders, 2) Triple Tops and Bottoms, 3) Double tops and bottoms, 4) Spike (or V) tops and bottoms, and 5) Rounding or saucer pattern [1], [25].

- Continuation patterns indicate that the sideways price action from a previous direction is but a pause and the next move will be a continuation in the same direction as the previous trend [1], [7], [25]. Reversal patterns normally take longer to build and signal major trend changes. Continuation patterns are shorter term in duration. Continuation patterns tend to be the most accurate the duration is between one to three months [1], [25].

- This paper aims to propose a system for predicting buy, hold and sell recommendations for a publicly listed Philippine Company using Computational Intelligence. Section 1 starts with a discussion of how technical analysis can be used to analyze the historical chart patterns for a particular stock’s closing price and volume, and its relationship with other parameters such as the 50-day moving average. Section 2 provides a review of the most appropriate Artificial Intelligence techniques that can be used for short-term stock market prediction and it gives an explanation about Sector Vector Machines. Section 3 is where the System Implementation which includes data gathering, training and the prediction system are discussed. A flowchart of the steps taken to validate the trained SVM is also presented. Finally, sections 4 and 5 discusses the conclusion and future recommendation, respectively.

- II. ARTIFICIAL INTELLIGENCE TECHNIQUES USED FOR STOCK MARKET PREDICTION

- A. Artificial Intelligence

- Artificial Intelligence deals with problems of classification, prediction and optimization incorporating processes that can be called intelligent in decision making [8].

- AI systems are designed to adapt and learn. Alan Turing, the British pioneer who was highly influential in the development of computer science, formalized “algorithm” and “computation” with the Turing machine - which can be considered a model of a general purpose computer [8], [26].

- The first definition of AI is based on the Turing test which is as follows: a human judge engages in a natural language conversation with one human and one machine, each of which tries to appear human. The aim of the judge is to distinguish human from machine, only on the basis of conversation (without visual or other help). When the judge cannot distinguish between human and machine, then the machine may be considered as intelligent [8].

- B. Expert Systems based on Technical Analysis

- An expert system is a computer-based system that emulates the reasoning and decision-making process of a human expert within a specific domain of knowledge. Expert systems are based on explicitly formulated special knowledge obtained from experts to achieve decision on the expert level [10].

- Most technicians chose the closing price to average because it is considered by most to be the most important price of the trading day. Price patterns are a kind of geometric forms or shapes whose practical use is to forecast the direction of the stock price.

- To identify the unique patterns, vector data (or information set) must be collected over a given period and there must be a way to clearly determine whether the vector is to be assigned to one or the other pattern. There is no need to find the causal relationship between the occurrence of the pattern and the continuation of the price behavior symptomatic linking would be good enough [11].

- Chart analysis is largely subjective and difficult to test, thus, making it difficult to program in a computer. As an example, two technicians can argue that a certain price pattern is either a wedge or a triangle. On the other hand, the Moving average is one of the most versatile and widely used of all technical indicators because it can be so easily quantified and tested.

- Incidentally, stock traders heavily rely on a 50 day or 10 week moving average, and for longer range stock market analysis, popular weekly moving averages are 200 days or 40 weeks

- The moving average is a trend following device. Its objective is to identify the start of a new trend or the end of an old trend. It can also be used to identify if trends have reversed direction. However, it does not predict market action because moving average is a follower, not a leader. The moving average follows a market and tells us that a trend has begun, but only after the fact [1].

- Mechanical trend following systems such as Welles Wilder’s Directional Movement and Parabolic Systems, only work well in certain types of market environments

- A comparison was made between a mechanical trading system using the Directional Movement Indicator (DMI) with a common-sense buy and hold strategy using data from the 1998 Standard & Poor’s 500 Index. The result was that the traders that chose the DMI did not yield higher returns than the buyand-hold strategy. However, the DMI did provide a better sell signal during the third quarter of 1998 when the market price dropped drastically [12].

- C. Machine Learning Approaches

- Moreover, traditional time-series models (such as movingaverage, auto-aggressive, integrated, and regression) attempt to forecast future values of a time series as a linear combination of historic data. However, financial time series exhibit high non-linearity [13]. Machine learning methods are used to identify linear and non-linear patterns through the design and development of algorithms and techniques that allow the computer to “learn”.

- The most popular machine learning approaches are Artificial Neural Network (ANN), Random Forest Method (RFM), and Support Vector Machines. Existing literature with sufficient empirical evidence shows ANN outperforming traditional models [14]. There is also evidence of SVM outperforming ANN for stock market returns [15].

- A study focused on using Support Vector Machines (SVM) to predict the directional movement of the Madrid IBEX-35 stock index using two Technical Analysis Indicators; the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD)

- SVM was also used to predict the movement of the S&P 500 Daily Index in the Chicago Mercantile that revealed the degree of accuracy of this study measured in terms of estimates’ deviation from the observed value [17].

- SVMs were used in the daily Korean composite stock index and were benchmarked against back-propagation neural networks and Case Base Reasoning resulting in SVM outperforming the other methods and that they should be considered as a promising methodology for financial time series forecasting [18].

- A Support Vector Machines Classifier was used to predict the directional movement of the Nikkei225 index with very promising results [19]. Least Squares Support Vector Machines time series model was implemented to predict the stock price movement of German stocks [20]

- According to Das and Padhy [21], the advantages of SVM over other machine learning methods for supervised learning are: a) training a support vector machine involves optimization of a convex function with linear constraint. This problem has a unique global minimum which in turn overcome strucking to local minima observed in neural network, and b) the constructed model has an explicit dependence only on the support vectors, which reduces the computational cost.

- D. Support Vector Machines

- The SVMs are a supervised learning technique used for data analysis and pattern recognition by classifying the data set. A standard SVM is a non-probabilistic binary linear classifier which mathematically classifies input in two possible classes [22].

- III. SYSTEM IMPLEMENTATION

- V. CONCLUSION

- using Sector Vector Machines, it is conclusive that the resulting Buy, Sell and Hold recommendations for the test data have very low discrepancies with the target recommendations

- Taking away the volume parameter results in accurate predictions of Buy, Sell and Hold recommendations. Thus, one can use Closing Price and the 50-day Moving Average as data points for prediction. However, taking away the relationship between the Closing Price and the 50-day Moving Average and retaining the Closing Price, 50-day Moving average and volume results in less accurate buy, sell and hold recommendations

- VI. FUTURE RECOMMENDATIONS

- For further studies, one can access live data feeds to populate the training data file. This will allow the system to be able to support intraday transactions so that the current intraday price is used, and the system can make daily recommendations to produce daily profitable transactions. This will result in compounded gains as long as the profit covers the transaction costs.

- Another further study can be in the area of calculating profitability returns for the given test period and develop further conditions to optimize profitability. One can also expand the methodology outlined in this paper to other stocks.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:44.491+08:00 %%
