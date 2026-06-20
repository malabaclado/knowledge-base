---
tags: type/research-note 
alias: [A systematic review of fundamental and technical analysis of stock market predictions]
---
# A systematic review of fundamental and technical analysis of stock market predictions

> [!info]
> - **Cite Key:** [[@ntiSystematicReviewFundamental2020]]
> - **Abstract:** The stock market is a key pivot in every growing and thriving economy, and every investment in the market is aimed at maximising profit and minimising associated risk. As a result, numerous studies have been conducted on the stock-market prediction using technical or fundamental analysis through various soft-computing techniques and algorithms. This study attempted to undertake a systematic and critical review of about one hundred and twenty-two (122) pertinent research works reported in academic journals over 11 years (2007–2018) in the area of stock market prediction using machine learning. The various techniques identified from these reports were clustered into three categories, namely technical, fundamental, and combined analyses. The grouping was done based on the following criteria: the nature of a dataset and the number of data sources used, the data timeframe, the machine learning algorithms used, machine learning task, used accuracy and error metrics and software packages used for modelling. The results revealed that 66% of documents reviewed were based on technical analysis; whiles 23% and 11% were based on fundamental analysis and combined analyses, respectively. Concerning the number of data source, 89.34% of documents reviewed, used single sources; whiles 8.2% and 2.46% used two and three sources respectively. Support vector machine and artificial neural network were found to be the most used machine learning algorithms for stock market prediction.
> - **Bibliography:** Nti, I. K., Adekoya, A. F., & Weyori, B. A. (2020). A systematic review of fundamental and technical analysis of stock market predictions. _Artificial Intelligence Review_, _53_(4), 3007–3057. [https://doi.org/10.1007/s10462-019-09754-z](https://doi.org/10.1007/s10462-019-09754-z)
> - **Tags:** #Artificial-intelligence, #Ensemble, #Fundamental-analysis, #Machine-learning, #Stock-prediction, #Technical-analysis



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Support vector machine and artificial neural network were found to be the most used machine learning algorithms for stock market prediction.

- 1 Introduction

- The well-being of every growing economy, country or societies in this twenty first century mainly hinges on their market economies and stock-price, with the financial market being the pivot (Nassirtoussi et al. 2014; Göçken et al. 2016). Thus, it is essential and vital to study and learn about the financial market extensively.

- A stock market is a place for trading stocks (equity) and other financial instruments of public listed companies, where the price of shares is termed “share” or “stock price” (Wanjawa and Muchemi 2014). In reality, the stock price level of a firm, to a large extent reflects how it “cuts its pie” (Chan et al. 2017).

- Investments in the stock markets are often guided by some form of prediction (Wanjawa and Muchemi 2014; Ghaznavi et  al. 2016). Three main approaches for stock market prediction, namely: fundamental analysis, technical analysis (charting) and technology (Machine learning) methods (Dunne 2015). Conversely, some scholars do categorise these three into 2, thus technical analysis and fundamental analysis (Nassirtoussi et  al. 2014; Dunne 2015; Gyan 2015; Prem Sankar et al. 2015; Ahmadi et al. 2018).

- The fundamental analysts approach concerned with the company that underlies the stock itself instead of the actual stock (Anbalagan and Maheswari 2014; Ghaznavi et al. 2016; Agarwal et al. 2017). The data used by the fundamental analyst usually are unstructured, which poses a difficult challenge. However, occasionally been proven to be a good predictor of stock price movement

- On the other hand, in the technical analysis, the analyst predicts the future price of stocks by studying the trends in the past and present stock price (Anbalagan and Maheswari 2014; Agarwal et  al. 2017; Ahmadi et  al. 2018). The following studies (Akinwale Adio et al. 2009; Guresen et al. 2011; Ju-Jie et al. 2012) and present (Rather et al. 2014; Laboissiere et al. 2015; Adebayo et al. 2017; Thanh et al. 2018; Umoru and Nwokoye 2018; Zhou et  al. 2018) predicted future stock-price movement based on technical analysis.

- Globally, billions of dollars are traded on the stock market daily, to make a profit (Dunne 2015). Thus, making stock-market prediction an attractive research area for researchers, investors and financial analysts, despite its difficulty

- Hence, resulting in the application of machine learning and computational intelligence techniques in analysing the stock market trend. These include hidden Markov model, neural network, neuro-fuzzy inference system, genetic algorithm, time series analysis, regression, mining association rules, support vector machine (SVM), principal component analysis (PCA) and rough set theory among others (Chen et al. 2014; Lin 2018; Thanh et al. 2018).

- This research seeks to perform a comprehensive systematic review of previous studies on stock market predictions based on the fundamental and technical analyst point of view, leading to the clarification of the current state-of-the-art and its possible future directions.

- 2 The categorisation of stock market decision techniques

- Technical analysis

- The technical analyst tries to predict the stock market through the learning of charts that portray the historical market-prices and technical indicators

- Some of the technical indicators used in technical analysis discussed in Anbalagan and Maheswari (2014), Bisoi and Dash (2014) and Rajashree et al. (2014) are simple-moving average (SMA), exponential moving average (EMA), moving average convergence/divergence rules (MACD), relative-strength index (RSI) and on-balance-volume (OBV)

- SMA

- The SMA is ascertained by totalling the most recent closing prices of a stock and then dividing that by the number “n” of periods in the calculation average (Anbalagan and Maheswari 2014).

- EMA

- The EMA is similar to the SMA line except the given day’s EMA determination depends on the EMA calculations for all the days preceding that day.

- MACD

- The MACD indicator was a momentum indicator; it tries to predict stock market trends by a comparison between short and long-term trends.

- OBV

- The OBV indicator is also a momentum indicator that employs volume-flow to predict movements in stock price. An indication of a fall in stock price is a falling OBV line, whiles a future rising in stock price is indicated by growing OBV line.

- RSI

- This is an indicator that measures whether a stock bought is oversold or overboug.

- Conventionally most stock market prediction methods usually employ technical analysis techniques to predict future trends in stock values.

- Fundamental analysis

- The fundamental analysis uses the economic standing of the firm, employees, the board of directors, financial status, firm’s yearly report, balancesheets, income-reports, terrestrial and climatic circumstances like unnatural or natural disasters and political data to predict future stock price (Tsai and Hsiao 2010; Anbalagan and Maheswari 2014; Ghaznavi et al. 2016; Agarwal et al. 2017).

- Due to the unstructured nature of fundamental factors, automation of fundamental analysis is difficult. On the other hand, the emergence of machine learning has enabled researchers to automate stock market prediction based on unstructured data, which in some cases has reported higher prediction accuracy.

- fundamental analysis is useful for long-term stock-price movement, but not suitable for short-term stock-price change (Khan et al. 2011).

- The fundamental analyst uses the openly accessible facts about the stock to perform analysis of stock price movement in three dimensions, concerning the economy, its industry, and the firm

- Again, the fundamental analyst also considers different financial ratios of the firm.

- Return on  equity (ROE)

- This ratio offers an overview of how well the shareholder’s funds were used and the gain made out of its investment. When ROE is low, it implies that the shareholder’s funds were not used properly.

- Debt/equity ratio (D/E)

- Reveals the power of the available capital as opposed to the capital engaged. A low value of D/E means the credit accessible was not used.

- Market capitalization (MC)

- MC measures the total stocks transacted in the market. Concerning MC, stocks can be categorised into three groups, namely: small-cap, mediumcap, and large-cap.

- Price/sales ratio (P/S)

- his ratio ascertains if a share price of a stock depicts stock’s value.

- Price/book ratio (P/B)

- s a comparison of the stock’s fundamental value with the share price. P/B is an indication of underestimate or overestimate of the stock.

- Earnings per share (EPS)

- EPS provides the profitability indication of a firm, and can be determined by dividing the firm’s net income with its whole number of remaining stocks.

- Price/earnings ratio (P/E)

- This ratio a very valuable evaluation metric for estimating the relative attractiveness of a firm’s current stock price compared to the firm’s per-share earnings.

- Return on  assets (ROA)

- This ratio signifies the proportion of earnings a firm earns about the firm’s overall assets or resources. Thus, an indication of how profitable a firm is relative to the firm’s total resources or assets.

- This method of stock market analysis has become common in recent years, with the introduction of text mining techniques. Many studies have used the fundamental analysis for stock prediction, but (Talib et al. 2016) in their work titled “Text Mining-Techniques Applications and Issues”, they argue that quite several problems are associated with the text mining process which turns to affect the effectiveness and efficacy of decision making.

- Despite the increase in stock-market prediction from both technical and fundamental analysis point of view, some scholars (Fama 1965, 1970; Malkiel 1999) holds the belief that the stock market is unpredictable.

- 2.1 The unpredictability of the stock market

- In Fama (1965, 1970) and Malkiel (1999), the authors holds a view that the stock market is stochastic, and hence, it is not predictable. This lead to the two famous hypotheses, namely, The random-walk hypothesis (RWH) and the efficient market hypothesis (EMH).

- 2.1.1 The random‑walk hypothesis (RWH)

- The Random-walk hypothesis reveals the unpleasant view of the predictability of the stock market. The assumption holds the belief that the stock price is fundamentally stochastic; hence, any initiative or effort to forecast or predict the future stock price will unavoidably fail (Dunne 2015). If indeed the market is stochastic, then there is a little chance of continuing.

- 2.1.2 The efficient market hypothesis (EMH)

- The second hypothesis that the market is random, hence not predictable is the famous EMH by Fama (1965), which says the stock market is “informationally-efficient.” It hypothesised that the market is efficient at discovering the correct price for the stock market. On the other hand, the credibility of this hypothesis is challengeable since the hypothesizer Fama revised it and categorised it into three levels of efficacy as Weak-form, semi-strong, and robust (Fama 1970).

- Carefully studying these two hypotheses, there is a chance to predict the stock market when one has fundamental and technical knowledge about the stock market. That is, knowing and understanding of the historical stock data and fundamental or financial data of a firm can lead to a successful prediction of the firm’s future stock price.

- 2.2 Markets’ predictability

- Despite the stands of the EMH (Fama 1965) against stock-market forecast established on historical publicly accessible data and information, a considerable amount of research advocates that more or fewer markets, particularly markets emerging, are not entirely and thoroughly well-organized, and prediction of future stock-prices and stock-returns possibly will yield better outcomes than random selection (Zhang et al. 2014).

- Chen et al. (2014) argues that the stock market is predictable to an extent when looking from behavioural economics and socioeconomic theory of finance viewpoint.

- 2.3 Machine learning

- Machine learning is a branch of Artificial Intelligent (AI), and it is a learning process, that starts with the identification of the learning-domain and concludes with testing and employing the obtained results of learning in solving a problem (Perwej and Perwej 2012). Many machine learning algorithms have been developed and applied to stock market prediction (Dunne 2015; Paik and Kumari 2017).

- In literature, it is revealed that, for one to make an effective economic prediction, it is essential to detect which variables help or contributes to predicting other economic variables (de Oliveira et al. 2013). Generally, financial data can be characterised by quantitative data (technical analysis) and qualitative reports of companies and investors sentiments (fundamental analysis) (Li et al. 2015).

- 2.6 Model evaluation

- Every prediction model needs evaluation to ascertain the accuracy of the model. Some of the most commonly used accuracy metrics in literature include: the mean absolute percentage error (MAPE), mean square error (MSE), mean absolute error (MAE) and root mean squared error (RMSE)

- Volatility

- A comparison of volatility prediction for (1 day, 1 week, 1 month) ahead horizon in terms of root mean squared prediction error (RMSPE), mean squared prediction error (MSPE), and mean absolute prediction error (MAPE) defined in Minxia and Zhang (2014) and Nayak et al. (2015).

- Momentum

- An Assessment for energy on (1-day, 1-week, 1-month) ahead horizon in terms of MSPE, RMSPE and MAPE defined in Nayak et al. (2015)

- Accuracy

- Precision

- Recall

- F‑score

- The association that exists between right stock (rise/fall) and that given by a predictor, if there is equality between precision and recall.

- Review of artificial neural network (ANN) in stock market prediction has been carried out by Dase and Pawar (2010), Soni (2011), Neelima et  al. (2012), Chang et  al. (2013), Goel et al. (2016) and Murekachiro (2016). These works concluded that ANN dominates in stock-market predictions globally.

- A comparative summary of predictive models for financial stock-market projections was carried out by Suthar et al. (2012). An overview of the techniques employed in predicting the stock market and enhancement made on these techniques in India was presented by Agrawal et al. (2013).

- In another study, a comprehensive, systematic reveal of fundamental analysis techniques for stock market prediction was undertaken in Nassirtoussi et al. (2014).

- An analysis of the present and new (fundamental analysis, technical analysis, and machine learning) techniques in stock-market prediction were carried to verify if there is sufficient evidence to support weak-form EMH (Dunne 2015).

- A review of technical analysis on stock-markets to categorise and code published articles, to offer a summary of research works that have added up to the development in stock-market predictions was performed by Nazário et al. (2017). The authors concluded that ANNs are best effected with backpropagation (BP).

- From the above reviews, it was evident that none of the previous studies considered 1. The number of data-sources employed in stock prediction and how it influences the predictive models and methodology used. 2. A comparison of self-stated accuracy among research works of same soft-computing approach. 3. The software package for building predictive models and the approach (technical analy sis or fundamental analysis) used.

- This paper fills in the gap by reviewing past, and current state-of-the-art stock market prediction works based on the type of input data; the number of data-source and the soft-computing technique used; and a comparison of accuracy, time frame, software packages used for modelling.

- 3 Research design

- One hundred and twenty-two (122) related essays were collected using random sampling technique. These include published journal articles, conference proceedings papers, doctoral dissertations or supplementary unpublished academic working papers and reports between 2007 and 2018.

- First, the selected papers were grouped into three broad categories based on the input data used, namely textual data, historical market data, and a combination of textual and historical market data

- Table 1 shows the distribution of surveyed works based on categorisation into the fundamental analysis, technical analysis, and combined. Eighty-one (81) was based on technical analysis (historical stock prices), twenty-eight (28) based on fundamental (web news, social media sentiments and macroeconomic variable) and thirteen (13) based on the combined analysis.

- 4.2 Technical analysis (quantitative stocks‑market data)

- The results also revealed that the most utilised technical indicator was the simple moving average (SMA). Besides, it was observed that a very high percentage of studies that employed SMA are likely to use EMA, MACD, and RSI, as shown in Table 2 (Appendix).

- An interesting observation from the study is that as little as 3.28% of the 122 articles focused on the African market.

- 4.3 Fundamental analysis (qualitative data)

- The results revealed that twenty-eight (28) out of 122 reviewed papers used fundamental analysis for stock market prediction, and 98% of these works used sentiment analysis of social network sites (SSNs), as predictors of market movement as shown in Table 3 (Appendix). This result confirms (Bollen et  al. 2011) report that the analysis of daily content of twitter feeds had the ability and capacity to cause an increase of DJIA prediction accuracy up to 87.6%.

- Out of this twenty-eight (28), social media accounted for 54%, financial web-news accounted for 29%, while search engine queries and macroeconomic variables accounted for 7% each.

- Again, it is revealed that macroeconomic variables as the only data source to stock-market prediction have not seen much attention

- This gap in literature creates the need for future research into the stock market prediction based on macroeconomic variables. Furthermore, the study revealed that 89% out of the twenty-eight (28) works based on social media sentiments, were all on stock markets outside African. Thus, there is a need for studies measuring social media sentiments influence on the Africa stock markets.

- 4.4 Combined (qualitative and quantitative data) analysis

- Some researchers sought to harness the power in both data sources by formulating a joint input data of fundamental and technical indicators to improve the accuracy of stock-price predictive models. The study revealed that thirteen (13) out one hundred and twenty-two (122) of reviewed works was based on this approach, as shown in Table  4 (Appendix). The study revealed that 77% of these works used two (2) data sources, and 23% used three (3) data sources. To the best of our knowledge, none of the previous study as at the time of this paper have used four (past stock-data, social media, financial news, and macroeconomic variable) or more data source for stock-market prediction. Another opportunity for future studies based on four (4) or more data sources for stock market prediction.

- 4.5 Methods used for modelling and analysis

- A summary of all the machine-learning algorithms used in the reviewed works is presented in this section. Hence, the main objective here was to give a report of what has been used and obtain a clearer understanding of what is lacking, which could be a pointer for future research

- The results reveal that 92% of the algorithms used were classification machinelearning algorithms as tabulated in Table 5 (Appendix). This revelation implies that most of the reviewed work predicted stock price movement. Few of these works predicted the actual price of future stock. Hence, further studies can look at the difficulty in predicting the exact cost as compared to the movement.

- The study again reveals that DTs, SVM, and ANN are the most used machine learning algorithms in stock market predictions, with ANN and SVM topping the list, as shown in Table  5 (Appendix). This outcome confirms (Almeida et  al. 2010; Adebiyi et  al. 2014a) report that ANN and SVM achieve higher generalisation potential than their counterparts.

- Again, more than 50% of the works reviewed, used hybrid algorithms as a way of compensating the flaws in individual algorithms, and this is evident in the accuracy reported in some hybrid models compared to different models of the same kind, as shown in Table  5 (Appendix). Hence, investigation of such hybrid algorithms in the environment of stock-market prediction may lead to novel insights that can lead to curiosity for future researchers.

- Ballings et al. (2015) in their works concludes that ensemble techniques should be benchmarked against other technology, with market-data from different continents. Their reason is that the accuracy of ensemble methods might differ over different dataset from different continents.

- Term Frequency-Inverse Document Frequency (TF-IDF) was among the most common feature-representation technique for the textual data. However, 99% of the works reviewed implements feature selection algorithms that depend on correlation analysis. The most used metrics identified in the literature were MSE, RMSE, and MAPE. The high use of MSE and RMSE can be attributed to their effectiveness in measuring predictive model performance for short-term prediction. Furthermore, it was observed that MATLAB is the most used modelling tool for stock market prediction, as shown in Table  5 (Appendix). For prediction accuracy of stock-price movement, previous studies reported accuracy within 36.55–97.8%, as shown in Table 5 (Appendix). The outcome confirms that the stock market is highly predictable.

- 4.6 Training verse testing data volume

- Every predictive model receives training and testing datasets, and Table 5 (Appendix) gives how most research works on stock market predictions partitioning their dataset. A higher percentage of the paper reviewed divides that dataset between (70–80%) for training and (30–20%) for testing.

- 5 Summary of findings

- The extensive literature survey done in this paper was embarked on, to identify and assess all stock-market price and movement prediction related to academic articles from all possible sources of stock-market prediction research. Hence, resulted in the identification and assessment of one hundred and twenty-two (122) relevant literature on stock-market prediction between 2007 and 2018.

- However, we do not claim that this review is exhaustive, in that this paper does not give detailed practical understandings into the state of the predictive model research. There is a high bias in the use of technical indicators as input variables in the abovereviewed experiments; this leaves a gap for future research that combines behavioural and fundamental input variables.

- Again the commonest and used technical indicators for stock market prediction were found to be SMA, EMA, MACD, RSI, and rate of change (ROC) which confirms (Krollner et al. 2010a; Renu and Christie 2018).

- Also, none of the one hundred and twenty-two (122) reviewed works has incorporate variable from past stock data, financial news, macroeconomic data, and social media sentiment as the input dataset. If all these data sources serve as input to a predictive model, a better and higher prediction accuracy results might be obtained as argued by Geva and Zahavi (2014).

- More than 87% of the papers reviewed reported that their model beat their benchmark model. On the other hand, a percentage of previous studies did not cover real-world constraints like slippage and trading costs. A high percentage of stock-market prediction studies were carried out on the Asian and European stock markets, but Kumar and Thenmozhi (2006) and Ballings et al. (2015), argues that benchmarking ensemble machine learning algorithms for different continents against other techniques is of a higher necessity. In that, some learning techniques tend to perform better and of high accuracy in some parts of the globe than others

- Finally, an experimental setup with stock data from the Ghana Stock Exchange shows and affirms that artificial neural networks fit very well for stock market prediction as compared with support vector machines and decision trees, based on RMSE, MAE and MSE error metrics.

- The results revealed that ANN and SVM are usually used machine-learning algorithms for stock prediction. However, a lot of research work to improve stock prediction accuracy are ongoing using hybrid ensemble machine–learning method. It was noticed that, considering internal and more external factors could provide a more precise and accurate prediction.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:44.739+08:00 %%
