---
tags: type/research-note 
alias: [Stock Market Forecasting Using Deep Learning and Technical Analysis: A Systematic Review]
---
# Stock Market Forecasting Using Deep Learning and Technical Analysis: A Systematic Review

> [!info]
> - **Cite Key:** [[@liStockMarketForecasting2020]]
> - **Abstract:** Stock market forecasting is one of the biggest challenges in the financial market since its time series has a complex, noisy, chaotic, dynamic, volatile, and non-parametric nature. However, due to computing development, an intelligent model can help investors and professional analysts reduce the risk of their investments. As Deep Learning models have been extensively studied in recent years, several studies have explored these techniques to predict stock prices using historical data and technical indicators. However, as the objective is to generate forecasts for the financial market, it is essential to validate the model through profitability metrics and model performance. Therefore, this systematic review focuses on Deep Learning models implemented for stock market forecasting using technical analysis. Discussions were made based on four main points of view: predictor techniques, trading strategies, profitability metrics, and risk management. This study showed that the LSTM technique is widely applied in this scenario (73.5%). This work significant contribution is to highlight some limitations found in the literature, such as only 35.3% of the studies analysed profitability, and only two articles implemented risk management. Therefore, despite the widely explored theme, there are still interesting open areas for research and development.
> - **Bibliography:** Li, A. W., & Bastos, G. S. (2020). Stock Market Forecasting Using Deep Learning and Technical Analysis: A Systematic Review. _IEEE Access_, _8_, 185232–185242. [https://doi.org/10.1109/ACCESS.2020.3030226](https://doi.org/10.1109/ACCESS.2020.3030226)
> - **Tags:** #Predictive-models, #Time-series-analysis, #Forecasting, #Stock-markets, #Deep-learning, #Measurement, #profitability-metrics, #risk-management, #stock-market-forecasting, #systematic-review, #Systematics, #technical-analysis, #technical-indicators, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- ABSTRACT

- Stock market forecasting is one of the biggest challenges in the financial market since its time series has a complex, noisy, chaotic, dynamic, volatile, and non-parametric nature. However, due to computing development, an intelligent model can help investors and professional analysts reduce the risk of their investments. As Deep Learning models have been extensively studied in recent years, several studies have explored these techniques to predict stock prices using historical data and technical indicators. However, as the objective is to generate forecasts for the financial market, it is essential to validate the model through profitability metrics and model performance. Therefore, this systematic review focuses on Deep Learning models implemented for stock market forecasting using technical analysis. Discussions were made based on four main points of view: predictor techniques, trading strategies, profitability metrics, and risk management. This study showed that the LSTM technique is widely applied in this scenario (73.5%). This work significant contribution is to highlight some limitations found in the literature, such as only 35.3% of the studies analysed profitability, and only two articles implemented risk management. Therefore, despite the widely explored theme, there are still interesting open areas for research and development.

- I. INTRODUCTION

- Asset prices forecasting for stock market is a very difficult and complicated task [1] since several micro and macroeconomic attributes and characteristics influence the price formation, such as political events, news, company balance sheets, among others [2]. These factors contribute to the nonlinear and non-stationary characteristics presented by the market, favoring the proposed task complexity [3], [4].

- Therefore, the studies of these influences are made through market analysis, and their main objective is to predict future directions to assist decision making based on market behavior [5]. The literature presents two main approaches: Fundamental Analysis (FA) and Technical Analysis (TA). Both have the same primary objective, and the difference is the information set used for forecasting and decision making. The first focuses on studying company data and seeks to determine whether it has growth potential in the medium to long term [6].

- In contrast, TA does not consider the company data, since investors who use this approach believe that information capable of moving the market is absorbed and reflected in the share price [7]. In other words, company balance sheets, accounting scandals, financial crises, or any relevant information capable of generating volatility in an asset is reflected in their price. Therefore, it is possible to avoid the FA data, which are often subjective, to identify patterns present in the asset graph through this strategy type.

- Technical analysts make extensive use of Technical Indicators (TI) and candlestick pattern analysis to assist in price movement forecast. Several scientific articles used price information (Open, High, Low, Close prices – OHLC), trading volume, and indicators set as model input based on these techniques. However, when modeling these analyses, two different approaches are used; the works that used TIs generally adopted regression techniques [8]–[10] and those that analysed candlestick patterns adopted image processing techniques [11]–[13].

- Regarding works based on statistical methods, several authors stated that they did not perform efficiently and generated inferior results to models based on artificial intelligence (AI) [15]–[18], as statistical techniques treat financial time series as linear systems.

- Additionally, the survey of Cavalcante et al. [5] stated that some financial time series characteristics are responsible for the difficult task of forecasting compared to other time series. Thus, traditional statistical methods are not effectively applied to the economic context.

- White [19] was the pioneer in implementing an artificial neural network (ANN) for financial market forecasting. The author used the daily prices of IBM company as a database. As it was just an initial study, it did not achieve the expected results. It highlighted the difficulties encountered, such as the overfitting problem and low complexity of the neural network, since only a few entries and one hidden layer were used. It was also mentioned possible future works, such as adding a higher number of features in the ANN, working with different forecasting horizons, and evaluating model profitability.

- Besides, Cavalcante et al. [5] selected publications on computational intelligence from 2009 to 2015 and noted that ANNs were widely used and highlighted Deep Learning (DL) as future work. Then, the survey of Kumar et al. [14] presented works that addressed computational intelligence and explored publications from 2016 to 2019, that is, a continuation of the previous work. They highlighted several hybrid implementations and some based on ANN, fuzzy, and DL.

- Additionally, Gandhmal and Kumar [20] and Nti et al. [21] noted that ANNs were widely used and performed better than fuzzy, support vector machine (SVM) and decision trees since ANNs had more significant potential for generalization. Besides that, Fawaz et al. [22] concluded that DL techniques were able to achieve performance similar to the state-of-theart for time series classification.

- TA is often used for investments with a shorter horizon, trend forecasts, and reversal points identification [5]. Therefore, the timeframe used for model training must be taken into account. The vast majority of previous works used daily candles for a one-day forecast horizon or more. In the review by Nti et al. [21], the 81 publications using TA only 5 worked with intraday candles, showing a differential potential for future works.

- The justification for the lack of research that explores smaller timeframes can be either positive (a study yet to be explored) or negative (not showing exciting results). However, it is possible to justify, in principle, the advantage of using a smaller graphic period through the work of Kumar et al. [14], which presented the instances number of each reviewed articles and the one with the highest number was 4818, between the years 1986 and 2005, that is, 267 instances per year on average.

- Sezer et al. [23] conducted a DL techniques survey for forecasting financial time series and concluded that recurrent neural networks (RNN) are the most explored by researchers. However, in their review, the authors did not limit the entry attributes set and used FA data, news, price history, market behavior, and TIs. The work focus was to present and analyse the techniques used, including the performance criteria and platforms adopted.

- platforms adopted. Nowadays, with the development of natural language processing (NLP) and the large volume of news available, sentiment analysis has been applied with relative success in the financial market [24]. Several works use news information together with historical prices for forecasts and have shown results superior to models that use only OHLCV [25]–[27].

- Cavalcante et al. [5] identified the works generally did not use trading strategies. Also, they did not evaluate the profitability, reinforcing the conclusion of White [19] and the affirmation of Vanstone and Finnie [6], which say there is much research that does not validate the profitability, resulting in several inconsistent models in the long term. Thus, these issues have generated the greatest contribution of Cavalcante et al. [5] work, which added two final phases for the financial forecasting standard methodology: trading strategy and profitability evaluation.

- To reinforce the need for this new methodology is possible to cite the Nazário et al. [28] work, which analysed 85 articles and only 31 used some trading strategy. Also, Wang et al. [10] identified that the metrics used for Machine Learning (ML) models have a low correlation with financial metrics, reinforcing the great importance of a completely autonomous system for correct financial validation.

- Finally, this systematic review aims to gather and analyse existing articles in the literature, focusing on DL techniques for forecasting prices in the stock market, highlighting the accuracy and profitability metrics used to validate the model and trading strategies adopted.

- II. RESEARCH METHODOLOGY

- III. DISCUSSIONS

- (RQ1 - Which DL techniques are mostly used to forecast prices in the stock market?). Most studies used the LSTM network, since it is an ideal algorithm for time series forecasting, as it can store memory and solve the gradient vanishing problem.

- Regarding the works that mention which tools were used to develop the predictor based on historical price data, they all did programming in Python3 and Tensorflow.4 Other tools also widely used were NumPy,5 Pandas,6 Scikit-Learn,7 Keras,8 TA-Lib,9 and TA4J10; the last two being libraries to generate TIs.

- Answering the second question (RQ2 - Which markets and timeframes are most used for price prediction?), there is a wide variety of assets from the North American, Indian, Chinese, Brazilian, Korean, European, Taiwanese, German, Belgian, Moroccan, and cryptocurrency markets. This probably occurs due to prior knowledge of each author local market; also, for implementation in a real environment and trading assets from another country, it is usually necessary to open an account in that country, making the process bureaucratic and costly

- Table 6 shows a variety of datasets used to collect historical stock prices. However, most authors choose Yahoo Finance due to the ease of acquiring data using a library developed in Python, yahoo-finance.11

- In addition, publications that used news data for hybrid algorithms with sentiment analysis collected information from Reuters, Bloomberg, FiNet,12 Google News, Sina

- Answering the fourth question (RQ4 - The works using automated trading systems, which the methods employed?), the strategies used for trading are mostly quite simple and can be: • The trading system does long operation based on the forecasting and holds until forecasting change to short; • System buys and maintains the operation for a specific time; • In addition to the long strategy, the system can operate short and make a purchase later to effectuate the profit or loss.

- Finally, answering the fifth question (RQ5 - What are the metrics used for profitability evaluation?), the most used profitability metric is accumulated profit, which can be presented as gross or net value, after deducting costs. Only 12 articles (35.3%) presented this result showing that the concern of [5], [6], [19] is still valid since the articles analysed comprise from 2017 to 2020 and most do not address this vital metric.

- IV. CONCLUSION

- This article aimed to review the academic literature on financial time series forecasting using DL and technical analysis. Using a research methodology was possible to select 34 articles for this study. Thus, analysis and discussions were made based on four main points of view: predictor techniques, trading strategies, profitability metrics, and risk management.

- It was noted the extensive use of the recurrent neural network LSTM due to memory storage capacity and the ability to solve the vanishing gradient problem. Some hybrid models used LSTM to treat technical indicators and other techniques to deal with news, presenting more robust results, and potential future research.

- This study significant contribution was to show that a small portion of articles (35.3%) assessed the profitability and only two addressed risk management. Despite that, several authors cited the importance of these steps for model validation. Also, some analysed publications have obtained losses even with the model performance above 50%

- Therefore, some literature gaps allow research in future works, such as hybrid models with qualitative and quantitative input data, an intelligent and adaptive trading strategy, metrics with a positive correlation between performance and profitability, implementation of risk management, and others.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:44.220+08:00 %%
