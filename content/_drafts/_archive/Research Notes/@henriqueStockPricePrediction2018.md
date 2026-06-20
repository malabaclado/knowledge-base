---
tags: type/research-note 
alias: [Stock price prediction using support vector regression on daily and up to the minute prices]
---
# Stock price prediction using support vector regression on daily and up to the minute prices

> [!info]
> - **Cite Key:** [[@henriqueStockPricePrediction2018]]
> - **Abstract:** The purpose of predictive stock price systems is to provide abnormal returns for financial market operators and serve as a basis for risk management tools. Although the Efficient Market Hypothesis (EMH) states that it is not possible to anticipate market movements consistently, the use of computationally intensive systems that employ machine learning algorithms is increasingly common in the development of stock trading mechanisms. Several studies, using daily stock prices, have presented predictive system applications trained on fixed periods without considering new model updates. In this context, this study uses a machine learning technique called Support Vector Regression (SVR) to predict stock prices for large and small capitalisations and in three different markets, employing prices with both daily and up-to-the-minute frequencies. Prediction errors are measured, and the model is compared to the random walk model proposed by the EMH. The results suggest that the SVR has predictive power, especially when using a strategy of updating the model periodically. There are also indicative results of increased predictions precision during lower volatility periods.
> - **Bibliography:** Henrique, B. M., Sobreiro, V. A., & Kimura, H. (2018). Stock price prediction using support vector regression on daily and up to the minute prices. _The Journal of Finance and Data Science_, _4_(3), 183–201. [https://doi.org/10.1016/j.jfds.2018.04.003](https://doi.org/10.1016/j.jfds.2018.04.003)
> - **Tags:** #Machine-learning, #Prediction, #Support-vector-regression, #High-frequency-trading, #Stock-market, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- 1. Introduction

- Stock price prediction mechanisms are fundamental to the formation of investment strategies and the development of risk management models6; p. 43). The Efficient Market Hypothesis (EMH), however, states that it is not possible to consistently obtain risk-adjusted returns above the profitability of the market as a whole.20 Computational advances have led to several machine learning algorithms used to anticipate market movements consistently and thus estimate future asset values such as company stock prices7; pp. 193e194). Models based on the Support Vector Machine (SVM) are among the most widely used techniques.

- Information is a valuable resource when building predictive models in the pursuit of profitable financial market transaction systems. Given the peculiarities of financial time series, various challenges must be faced when developing price forecasting systems1; p. 4081).

- From a theoretical point of view, under the EMH, relevant information would be widely available to all market participants and immediately reflected in price, according to Malkiel and Fama (1970, p. 383)20's EMH claims that it is impossible, consistently and over the long term, to achieve above-market returns adjusted to the level of risk assumed.

- As summarised by Malkiel (2003)19; the EMH has been questioned since its introduction, especially with the development of Malkiel (2003)19; the EMH has been questioned since its introduction, especially with the development of predictive systems, as shown in studies based on SVM and other algorithms (for example, Ballings et al. (2015); Nayak et al. (2015)2,22; and Qu and Zhang (2016))25 that can generate profit in the long term. Malkiel and Fama (1970, pp. 386e387), however, argue that the market follows a random walk and that attempts to predict its movements in a consistent manner will be vain.

- Computational advances have led to the introduction of machine learning techniques for predictive systems in financial markets. In a review of articles on predictive systems, Hsu et al. (2016, p. 215) observed that it is common to use financial series to measure the efficiency of predictive algorithms and classifiers in machine learning. Classifiers are systems that can learn, through training, to recognise patterns and thus assign a class to new data.

- As an example, machine learning algorithms can be used to predict insolvency, as observed by Zhou et al. (2012)33 and Li et al. (2012).16 In such cases, the aim is to classify companies with the highest probability of insolvency, according to an automatic classifier algorithm. Other examples are credit risk measurement, as in Li et al. (2006)17; and asset price forecasting, as proposed by Kao et al. (2013)11 and Xiao et al. (2013).30

- In addition to developing transactional strategies, progress in computational information systems has enabled rapid electronic transactions to take place in financial markets. Based on high-frequency trading algorithms, the submission and execution of purchase, sale or cancellation orders can be performed in seconds and microseconds, as Goldstein et al. (2014, pp. 182e183) note. The intensive use of rapid computational systems by some market participants may increase profitability, but the effects on normal market functioning are questionable, as not all participants have access to this type of technology8; pp. 182e183).

- To analyse the EMH, as Hsu et al. (2016)9 have sought to do, this study tests stock predictability in Brazil, the United States and China, based on prediction error analysis. The study does not seek to identify trading strategies that can lead to extraordinary gains but rather to evaluate prediction errors by comparing a machine learning model with a base model that follows a random walk. The choice of countries is due to the desire to evaluate results of machine learning techniques in both developed and developing markets.

- In regard to stock price frequency, daily data are traditional in prediction studies, such as those of Kumar et al. (2016), Zbikowski (2015)13,32 and Patel et al. (2015b).24 However, other studies, such as those of Qu and Zhang (2016)25 and Manahov et al. (2014)21; use up-to-the-minute data. Our study shows results for both daily and up-to-the-minute prices.

- Blue chip and small cap stocks are selected, as higher and lower capitalisations in each country, respectively. One hypothesis tested involves the argument that a more accurate prediction can be obtained using a frequency greater than daily. Moreover, aiming to capture changing market conditions more quickly, results are evaluated by comparing periodic updating of models with an absence of updating in terms of prediction performance in each case.

- The selected prediction method is a regression method based on SVM, as used by Qu and Zhang (2016), Patel et al. (2015b)24,25 and Choudhury et al. (2014)5; called Support Vector Regression (SVR). Finally, it should be noted that three kernel functions are tested for SVR to identify the most suitable kernel function for this type of stock price prediction. A random walk model is used as a reference to evaluate predictions of returns

- In addition to minimising risks to stock market investors, strategies based on price prediction may provide evidence against the EMH. Predictive studies such as that presented here contribute to the building of profitable strategies, especially risk-adjusted ones, as greater predictability can affect an investment portfolio's exposure level. Thus, greater accuracy in price forecasting may imply potential risk-adjusted profits for investors.

- Our study contrasts different frequencies, using the same model. Specifically, predictions are made using both daily prices and up-to-the-minute prices. Another important contribution of this study is that it contrasts the results of a training model based on a fixed period with those with dynamically updated training periods, thus comparing the predictive performances of these two strategies.

- 2. Brief literature review

- Describing the EMH, Malkiel and Fama (1970) state that, on balance, prices reflect all relevant information available when pricing an asset. This hypothesis arises from empirical observations of changes in price time series that are very similar to a random walk process. According to these authors, even a system in which a number of buy and sell orders are generated in the short term is not profitable, due to transaction costs and commissions

- Despite the evidence obtained for market efficiency, Malkiel and Fama (1970, pp. 413e416) further encourage a search for more data confirming or disproving their hypothesis. Since then, academic papers have sought to show that stock market prices are, to some extent, predictable. Malkiel (2003, p. 80) concludes that not all market participants are rational and that there are irregular price formations, leading to exploitable return patterns over short time periods.27; p. 20) consider the possibility that a profitable predictive system may exist but only up to the point of its discovery. In this case, the performance of that system would deteriorate when more market participants begin to use it.

- The development of consistently profitable systems may constitute evidence against the EMH, as suggested by Hsu et al. (2016, pp. 217e218). Such systems may benefit from computationally intensive techniques, such as those that exploit machine learning algorithms. Hsu et al. (2016, p. 229) show that machine learning algorithms commonly use financial time series to evaluate their predictive capabilities.

- Zbikowski (2015)32; for example, utilised SVM and a predictive variable selection method within Technical Analysis (TA) indicators. In an attempt to develop an optimal market transactions strategy,5 used k-means to predict market volatility and SVR to predict prices in the Indian stock market. The authors analysed daily data to estimate prices for two days.2 studied the direction of the stock market and, in so doing, evaluated classifiers.

- In Ballings et al. (2015)2's study, annual data from more than 5000 European companies were used in classifiers such as logistic regression, neural networks, KNN and SVM. Classifiers are used to determine the direction of the respective company stocks in the following year. The authors compared the results of those classifiers to ensemble approaches, such as Random Forests (RF), AdaBoost and kernel factory. The so-called ensemble techniques involve multiple classifiers, usually of the same type or algorithm, resulting in independent classifications but with some decision method for determining a single final classification. Applying these techniques,2 calculated their predictive variables, considering companies' balance sheets and financial statements. Based on the prediction of the direction that a particular stock would take during the year, the authors showed how a profitable strategy could be built.

- The predictive variables used by Barak and Modarres (2015)3 were constructed from financial statements published by companies. Zbikowski (2015)32 used TA indicator values as predictive variables in his short-term trends prediction model. Zbikowski (2015)32 proposed a modified SVM, with variable selection determined by Fisher scores, a method used to rank definitions into classes according to certain predictor variables. The TA variables used by Zbikowski (2015)32 included On Balance Volume (OBV), the Relative Strength Index (RSI) and the Williams oscillator. The results obtained through the SVM approach exceeded those based on a buy-and-hold strategy in Zbikowski (2015)32's study. In turn, Yeh et al. (2011)31 and Lu et al. (2009)18 applied SVR-based systems to predict the TAIEX and Nikkei 225 indices, both using daily data.

- Gerlein et al. (2016)7 proposed using computationally simpler classifiers for intraday strategies in the Foreign Exchange (FOREX) market. Decision tree algorithms and lazy models were applied to TA variables for strategies on USDJPY, GBPUSD and EURUSD prices. Patel et al. (2015a)23 also used TA variables as inputs in their model but in a different manner from other authors. Instead of using the indicator values directly, as Gerlein et al. (2016)7 and Zbikowski (2015)32 did, Patel et al. (2015a)23 used the trend indication given by the indicators. A TA indicator can identify the market trend as bullish or bearish. Thus, Patel et al. (2015a)23's model uses this information as a predictive variable in algorithms such as SVM, random trees and neural networks to predict trend rather than price.

- Some authors have used hybrid machine learning algorithms to increase predictive performance. Xiao et al. (2013)30; for example, proposed integrating various neural networks with SVM to predict the daily values of stock indices. Using TA indicators as input variables, Nayak et al. (2015)22 proposed a hybrid SVM and KNN system for predicting index values. The results were better than those of traditional neural networks. In turn, Patel et al. (2015b)24 evaluated the efficiency of the daily closing price predictions performed by SVM, RF and neural network hybrids, comparing the results with the isolated use of these same algorithms. The authors concluded that hybrid uses of these algorithms offered better results. Finally, Dash and Dash (2016) investigated an approach to neural networks with TA compared to traditional machine learning algorithms in stock transaction decisions.

- Brownlees and Gallo (2006)4 suggest ways of treating high frequency data with regard to outliers and temporal irregularities. Once treated, high frequency data can be used to develop very fast market transaction strategies, known as High Frequency Trading (HFT). This type of transaction has become common in today's financial markets, and its effects have been studied by authors such as Lee (2013)14 and Goldstein et al. (2014).8

- 3. Method

- The prediction of closing stock prices in this study is performed by SVR. The results are compared to returns obtained by the random walk model, assuming zero average returns on stocks and a given variance.

- The Root Mean Squared Error (RMSE) and Mean Absolute Percentage Error (MAPE) are used to evaluate the adequacy of the models' price predictions. These measures have also been used by Nayak et al. (2015), Patel et al. (2015b), Arau ́jo et al. (2015), Manahov et al. (2014)1,21,22,24 and Choudhury et al. (2014).

- 3.1. Technical analysis indicators

- The predictor variables commonly used in the literature for SVR and SVM models are TA indicators.

- According to Nayak et al. (2015, p. 672), a TA indicator is composed of data derived from the application of a certain formula to the past prices of a stock. This paper considers the values of these indicators, detailed below, as predictive variables in the SVR model.

- 3.2. Support vector regression

- A classification method based on SVM maps the independent variables of N samples available into a space of more dimensions and is typically used to classify observations between groups. This method, developed by Vapnik (1995)28; uses fðxk; ykÞgN k¼1 training observations to build a linear model using non-linear classification thresholds, mapping variables on a greater number of dimensions. Separation between classes is achieved using an optimal hyperplane, calculated based on N observations, where x is the independent variable vector, and y is classification yk2 f1; 1g for each sample.

- As already indicated, SVR uses principles similar to SVM, but the response variable is a continuous value y2ℝ. However, as shown by Huang and Tsai (2009, p. 1530) and Patel et al. (2015b, p. 2164), instead of seeking the hyperplane in Eq. (13), SVR seeks the linear regression function, given by Eq. (17). To achieve this, a threshold error ε is defined to be minimised in the expression in Equation (18). This expression is called the ε-insensitivity loss error function. The SVR regression process therefore seeks to minimise ε in Eq. (18) and jjwjj2 in the expression of R, defined in Eq. (19).

- Note that the shape of the kernel function directly influences the values obtained by the SVR regression. Similarly, the constant c in Eq. (19) and the parameters g and d in Eqs. (24) and (25) should be optimised. For this purpose, a training data set is divided into two new sets: the first is used to choose the optimal parameters, and the second is used to validate the smallest error possible, given these choices. This process, called k-fold cross validation, selects the parameters c, g and d, according to the lowest RMSE.

- This study considers Brazilian, American and Chinese stocks, with three blue chip and three small cap stocks for each country, totaling 18 assets. The stocks were chosen to obtain a distribution of companies of different sizes in different markets of both developed and developing nature. The stocks selected in this study are shown in Table 2. The time period selected for daily prices comprises 15 years.

- bull and bear periods.

- The results obtained with daily prices can be compared to the use of higher frequency, up-to-the-minute prices. It is worth mentioning that valid prices in this study include only those obtained during the respective sessions in each market considered. Thus, the data were limited in advance to the official opening and closing times of each market. It should be noted that high frequency data, for example, those expressed in milliseconds, are not within the scope of this study, due to the method employed.

- Two strategies are considered when using SVR. The first is to separate the data into training observations, for the optimisation of the SVR model, and test observations, with prediction errors calculated on the closing prices, as adopted by Gerlein et al. (2016), 296 Manahov et al. (2014), Nayak et al. (2015)7,21,22 and Patel et al. (2015b).24 For daily prices, each period in Table 2 is split in a training set, with approximately 70% contiguous days, and a test set, with the remaining 30% days. For the 1-min historical prices, Table 3 shows the divisions into training and testing periods for all studied stocks, following the same strategy of separating 70% of data for training the models and 30% for testing them.

- The second SVR optimisation strategy involves updating the model as new information becomes available in the market, as suggested by Lessmann et al. (201115; p. 2122) and Hsu et al. (2016, p. 223). It is a dynamic optimisation that uses periodically updated training data, known as a sliding or moving window. It is expected that this procedure will capture new market conditions as soon as possible.

- Regarding the up-to-the-minute prices, although three months seems a short interval, it should be noted that period comprises more than 33000 data points, making the task of obtaining and processing the prices for all 18 selected securities a challenging effort. However, a longer period of analysis is desirable, mainly because three months may not include all possible market conditions for real tests. In this context, as stated before, this article brings yet another SVR evaluation for price prediction, using 2 whole years of up-to-the-minutes prices. Brazilian stocks are selected for this simulation over the long run, with data gathered directly from BM&F Bovespa. Such a long period, in terms of 1-min prices, contains short-term bull and bear markets for this timeframe, being suitable for evaluating the models' predictions stability

- 4. Analysis and results

- Before applying SVR to the prices described in this paper, prices and the TA indicators highlighted above e namely, SMA, WMA, RSI, ADO and ATR e were calculated and normalized.

- The analysis of results are organised into two sections, one dedicated to the use of a fixed training period as described before and other section dedicated to constantly updating the model in a moving training window. Both these sections consider the 15 years historical daily prices, the 3 months period for up-to-the-minutes prices and the results of predicting prices using 2 years of 1-min Brazilian stock data.

- 4.1. Fixed training

- Comparison of Tables 4 and 7 reveals that the daily test data SVR had smaller errors, compared to those RMSE errors on the optimization phase on the daily training data for the following stocks: PETR4, VALE5, DIRR3, BAC, ANGI, HL, 601318, 1970 and 2030.

- When using daily prices, the use of radial kernel resulted in smaller errors for the test data set only in the case of BAC stock. Usage of polynomial kernels did not, for any stock, result in smaller errors in the test data than in the training data.

- The variance in daily prices was therefore estimated using the closing prices of the most recent 7 days. Similarly, the 90 most recent minutes were used to estimate the variance in the distribution of returns for up-to-the-minute prices. Based on this procedure, the RMSE and MAPE results from obtaining the random walk model's predictions of daily closing and up-to-the-minute prices are as shown in Table 10.

- 4.2. Moving training window

- Having recorded the closing price prediction errors for the SVR models with fixed training and test sets, we turn to an examination of the strategy of constantly updating the models. In this study, the frequency selected for updating the models was the extreme case of an update made whenever a new price becomes available. Thus, for daily prices, the model was updated every day, and the next day's closing price served as a test observation. The daily prices of the 7 most recent days were selected for training, leaving the closing price on the 8th day for the prediction test.

- The results obtained when periodically updating the model are recorded in Table 11 (for daily prices) and 12 (for up-to-the-minute prices in the 3-months period). The Brazilian cases selected for the 2-years 1-min price prediction study using the moving training window SVR strategy are reported in Table 13. These results were measured in RMSE and MAPE and compared with the results obtained by the random walk model. Therefore, comparing the results in Tables 10 and 11, smaller errors were observed in the SVR model predictions, using linear and radial kernels for virtually all selected stocks, regardless of country of origin or capitalisation, for daily prices. The exception was LEVE3 stock, which presented odd results, possibly due to data errors. Moreover, on average, errors measured by MAPE were reduced when the linear kernel was used.

- Tables 12 and 10 allow for a comparison of the SVR model with the random walk model for up-to-the-minute prices during the 3-months period proposed. In this case, attention is drawn to the errors obtained using the linear kernel for the US stocks, GOOGL, XOM and ANGI. In these cases, the SVR model had no predictive power for the up-to-the-minute prices selected for this study possibly due to data errors. However, for the other stocks, the linear kernel returned smaller errors than the random walk model. Use of the radial kernel returned smaller errors than the random model for all stocks, regardless of the country of origin or capitalisation, as shown in Table 2. Finally, the use of SVR with a polynomial kernel had predictive power only for the American small cap stock, PZZA.

- Comparing those results with the predictions obtained with the random walk model of Table 10, SVR updated regularly confirms its predictive power observed in the 3-months cases for almost all stocks, specially using the linear kernel.

- To illustrate SVR price prediction capabilities using both strategies, fixed trained model and moving training window, the daily returns for the American BAC stock are plotted in Fig. 2 as a continuous line. The returns for the stock are shown for roughly 5 months. The returns predicted by a fixed trained SVR model are plotted as a dashed line, whereas a dotted line represents the returns predicted by a moving training window SVR model. Both models track the real returns without the typical lag present in most technical indicators used alone. However, the moving training window SVR model tracks the real returns more closely in general, resulting in smaller RMSE for most of the curve.

- 4.3. SVR prediction models and stocks volatility

- After registering SVR prediction results and comparing them with the random walk model-generated predictions in the previous paragraphs, this section verifies possible relationships between stocks basic statistics and the predictions themselves.

- Two measures are examined for each of the 15-years historical prices per stock: average returns and volatility

- Then we tabulate the correlations between yearly volatility and RMSE values obtained by SVR prediction models. Correlations are also calculated between the RMSE values and average daily return. Results are given in Table 14.

- Although the average returns do not seem related to the SVR predictions, there are indications of a strong relationship between the prediction errors and volatility.

- However, apart from that case, SVR predictions, considering constantly updated models using linear and radial kernels, seem to be more precise during periods with lower volatility in prices.

- 5. Conclusion

- Developing predictive price models for the stock market is challenging, but it is an important task when building profitable financial market transaction strategies. Computationally intensive methods, using past prices, are developed to facilitate better management of market risk for investors and speculators. Of the machine learning techniques available, this study uses SVR and measures its performance on various Brazilian, American and Chinese stocks with different characteristics, for example, small cap or blue chip. The predictive variables are calculated using TA indicators on asset prices. The results show the magnitude of the mean squared errors for the three common kernels in the literature, using specific algorithm training strategies with different price frequencies of days and minutes. The results are contrasted with those of a random walk-based model.

- Moreover, this kernel was more adequate for price predictions than the radial and polynomial kernels in the case of daily prices and fixed training models and outperformed the random model for some stocks classified as blue chips and small caps in the three studied countries.

- However, increasing the price frequency to minutes reduced the model's predictive power using a fixed training period. In particular, SVR obtained inferior predictive results relative to a random walk model for almost all stocks studied in up-to-the-minute prices, using fixed training, regardless of the adopted kernel function.

- The periodically updated models provided important evidence. In these cases, the use of linear and radial kernels resulted in smaller errors that the random walk model for almost all daily stock prices. The only exception was a stock with a high missing data rate. Constant model updating was also beneficial in the up-to-the-minute price frequency, and SVR models with linear and radial kernels achieved better results than the random walk model when this strategy was used.

- The analyses presented in this study suggest that periodically updating the SVR model reduces the mean square error compared to using a rigid model without periodic updating. This result contrasts with that of Hsu et al. (2016)9; who did not achieve better performance when using a sliding window on the training data.

- An important contribution of this study is a comparison of price prediction results of the presented SVR models with those of the random walk model, according to which markets are unpredictable in the long term. In this respect, the results presented here show that some SVR models, with periodic or fixed updates, may achieve better than random predictive performance, especially with the use of the linear kernel. Another result which prompts further investigation is the indication of a strong relationship between SVR price prediction and volatility, considering a moving training window.

- Importantly, despite the evidence of asset price predictability presented here, this article does not propose transactional strategies applicable to the stock market. The results therefore do not directly refute the EMH.

- Given that the focus of the analysis is not the identification of purchasing or sales strategies that allow for extraordinary gains, the study does not address issues such as transaction costs or portfolio risk levels.

- As the focus of the study is the analysis of asset price prediction errors, it is possible to build risk management models using SVR-based estimates. Exposure limits may be obtained by evaluating model errors. This study therefore provides a basis for the construction of systems that, while not directly evaluating the EMH, make possible the study of market efficiency and risk analysis. This study obtained results using SVR that were better than those of a null mean return random model.

- Despite comparing daily rates with the use of high frequency up-to-the-minute trading, this paper considers only a predictive algorithm based on machine learning. Furthermore, the SVR model allows for testing of many kernel functions, while this study is limited to only the three most common in the literature. It should be noted that, for a more robust simulation of high frequency stock market strategies, it would be necessary to include transaction costs, communications network delays, differentiation between the market price and actual value of a purchase or sale transaction (slippage) and transaction liquidity.

- Another limitation of these research results is the length of the periods of historical prices considered, specially the 3-months up-to-the-minutes prices data. Although the 3-months period seem short compared to the 15 years daily historical prices data, it should be noted it contains nearly 33000 data points per stock, compared to the approximately 3700 data points for the daily period selected, posing a challenging processing task. For future reference, all processing of the 15 years daily data, 3-months 1-min data and the 2-years 1-min Brazilian stock data took about 15 h per stock in a powerful machine, with 24 processors type Intel® Xeon® CPU E5-2650 v4 @ 2,20 GHz with 226GB of RAM, running Linux 3.10.0, distribution CentOS 7.3. The implementations of SVR and related functions used in this research are scripted in the R® statistical language, version 3.4.1, using functions from e1071 and caret packages. To reduce computation time, we took advantage of the parallel capabilities of the computer environment, allocating each stock simulations to an exclusive processor. Therefore, careful considerations are necessary for any real trading implementation attempts.

- Future studies may include a larger number of test stocks and markets other than those selected here. Other predictive models could also be compared, including classifiers of the directions of asset prices. Independent variables may include other TA indicators, trend predictors or past prices. In addition, fundamental analysis indicators, such as company size, liquidity, indebtedness, profitability and activity measures, could be included. The inclusion of such data could improve the machine learning mechanism. It is also recommended that other model updating periodicities be tested, especially those with higher frequency than up-to-the-minute prices.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:43.572+08:00 %%
