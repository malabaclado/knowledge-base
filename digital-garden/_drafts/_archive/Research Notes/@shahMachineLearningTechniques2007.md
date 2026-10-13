---
tags: type/research-note 
alias: [Machine learning techniques for stock prediction]
---
# Machine learning techniques for stock prediction

> [!info]
> - **Cite Key:** [[@shahMachineLearningTechniques2007]]
> - **Bibliography:** Shah, V. H. (2007). Machine learning techniques for stock prediction. _Foundations of Machine Learning| Spring_, _1_(1), 6–12.
> - **Tags:** #to-read, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- 1. Introduction

- Stock Prices are considered to be very dynamic and susceptible to quick changes because of the underlying nature of the financial domain and in part because of the mix of known parameters (Previous Days Closing Price, P/E Ratio etc.) and unknown factors (like Election Results, Rumors etc.)

- An intelligent trader would predict the stock price and buy a stock before the price rises, or sell it before its value declines. Though it is very hard to replace the expertise that an experienced trader has gained, an accurate prediction algorithm can directly result into high profits for investment firms, indicating a direct relationship between the accuracy of the prediction algorithm and the profit made from using the algorithm.

- n this paper, we discuss the Machine Learning techniques which have been applied for stock trading to predict the rise and fall of stock prices before the actual event of an increase or decrease in the stock price occurs. In particular the paper discusses the application of Support Vector Machines, Linear Regression, Prediction using Decision Stumps, Expert Weighting and Online Learning in detail along with the benefits and pitfalls of each method. The paper introduces the parameters and variables that can be used in order to recognize the patterns in stock prices which can be helpful in the future prediction of stocks and how Boosting can be combined with other learning algorithms to improve the accuracy of such prediction systems.

- 2. Background

- In practice, there are 2 Stock Prediction Methodologies: Fundamental Analysis: Performed by the Fundamental Analysts, this method is concerned more with the company rather than the actual stock. The analysts make their decisions based on the past performance of the company, the earnings forecast etc. Technical Analysis: Performed by the Technical Analysts, this method deals with the determination of the stock price based on the past patterns of the stock (using time-series analysis.)

- When applying Machine Learning to Stock Data, we are more interested in doing a Technical Analysis to see if our algorithm can accurately learn the underlying patterns in the stock time series. This said, Machine Learning can also play a major role in evaluating and forecasting the performance of the company and other similar parameters helpful in Fundamental Analysis. In fact, the most successful automated stock prediction and recommendation systems use some sort of a hybrid analysis model involving both Fundamental and Technical Analysis.

- The Efficient Market Hypothesis (EMH) The EMH hypothesizes that the future stock price is completely unpredictable given the past trading history of the stock. There are 3 types of EMH’s: strong, semi-strong, and weak form. In the weak EMH, any information acquired from examining the stock’s history is immediately reflected in the price of the stock.

- The Random Walk Hypothesis The Random Walk Hypothesis claims that stock prices do not depend on past stock prices, so patterns cannot be exploited since trends to not exist.

- With the advent of more powerful computing infrastructure (hardware and software) trading companies now build very efficient algorithmic trading systems that can exploit the underlying pricing patterns when a huge amount of data-points are made available to them. Clearly with huge datasets available on hand, Machine Learning Techniques can seriously challenge the EMH.

- 4. Conclusion

- Of all the Algorithms we applied, we saw that only Support Vector Machine combined with Boosting gave us satisfactory results. Linear Regression gave lower mean squared errors while predicting the EMA pattern.

- Another technique which looks promising but which we did not cover the evaluation of was Expert Weighting. More recently, the linguistic analysis of Financial News Results to predict stocks has been a topic of extensive study.

- The choice of the indicator function can dramatically improve/reduce the accuracy of the prediction system. Also a particular Machine Learning Algorithm might be better suited to a particular type of stock, say Technology Stocks, whereas the same algorithm might give lower accuracies while predicting some other types of Stocks, say Energy Stocks.

- Moreover, we should also note that while applying the Machine Learning Algorithms for Technical Analysis, we assumed that the effect of the Unknown Factors (Election Results, Rumors, Political Effects etc.) was already embedded into the historical stock pattern. Commercial Trading systems might have a more sophisticated mechanism for taking the unknowns into account.

- While we studied the algorithms discretely, more often than not, a hybrid algorithm is used for stock prediction. For instance an Algorithmic Trading System might involve a 3-tier architecture with SVM’s and Boosting at the bottom, an Online Algorithm (For instance an Expert Weighting scheme that we discussed in section 3.6 as the middle layer and Textual Analysis of Stock Market News, Financial Reports as the top layer to make predictions.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:46.090+08:00 %%
