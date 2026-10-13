---
tags:
alias:
creation-date: Tuesday 15th November 2022
last-modified-date: Tuesday 15th November 2022 21:16:00
---

# Introduction (Draft)

> [!NOTE]-
> Introduction should be about:
> - What is Stock Price Prediction?
> - What is Machine Learning?
> - Why is it important to predict stock prices?
> - What is support vector regression?
> - What are related works on SVR stock price prediction? (in the Philippines?)
> - What are recent advancements in stock price prediction using machine learning? 
> - * Future predictions 
> - * Generally accepted facts
> - The problem statement 
> - Current solutions to the problem 
> - What this study can offer 




## Why stock market prediction is an interesting research topic...
- ==Stock market prediction is an interesting research interest due to its potential gain.==
	- Stock market prediction has been an important issue in the field of finance, engineering and mathematics due to its potential financial gain. As a vast amount of capital is traded through the stock market, the stock market is seen as a peak investment outlet. ([[@yooMachineLearningTechniques2005|yoo2005]])
	- An intelligent trader would predict the stock price and buy a stock before the price rises, or sell it before its value declines. Though it is very hard to replace the expertise that an experienced trader has gained, an accurate prediction algorithm can directly result into high profits for investment firms, indicating a direct relationship between the accuracy of the prediction algorithm and the profit made from using the algorithm.  ([[@shahMachineLearningTechniques2007|shah2007]])
- ==Stock market prediction is a challenging task.== 
	- Asset prices forecasting for stock market is a very difficult and complicated task [1] since several micro and macroeconomic attributes and characteristics influence the price formation, such as political events, news, company balance sheets, among others [2]. These factors contribute to the nonlinear and non-stationary characteristics presented by the market, favoring the proposed task complexity [3], [4]. ([[@liStockMarketForecasting2020|li2020]])
	- Stock market forecasting is one of the biggest challenges in the financial market since its time series has a complex, noisy, chaotic, dynamic, volatile, and non-parametric nature. However, due to computing development, an intelligent model can help investors and professional analysts reduce the risk of their investments. ([[@liStockMarketForecasting2020|li2020]])
	- Stock Prices are considered to be very dynamic and susceptible to quick changes because of the underlying nature of the financial domain and in part because of the mix of known parameters (Previous Days Closing Price, P/E Ratio etc.) and unknown factors (like Election Results, Rumors etc.) ([[@shahMachineLearningTechniques2007|shah2007]])
	- A considerable number of studies have inferred that predicting stock market returns is a difficult task (Teixeira & Oliveira, 2010; Zielonka, 2004). The nonlinear and nonstationary features of the stock market make it a complicated system (Bisoi & Dash, 2014, p. 41). ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- There is also the fact that, as observed by Ticknor (2013, p. 5501), the complexity of the stock market is associated with a considerable number of factors such as political events, market news, quarterly earnings reports, international influence and conflicting trading behaviour. ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- The prediction of financial asset returns is a subject that encompasses many knowledge areas such as financial econometrics, investment analysis, corporate finance, and, most recently, behavioural finance (Chavarnakul & Enke, 2009, p. 3517; Parisi & Vasquez, 2000, p. 152–153; Roberts, 1959, p. 1). ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- Predicting stock price movement is a very difficult task. However, a non-linear approach such as an intelligent system can manage the uncertainty and imprecision in the stock market (Chavarnakul & Enke, 2009, p. 3519). Therefore, the trading system can be a different way of combining different tools, indicators and techniques to predict future market movements and to test the effectiveness of technical rules. ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])

- ==There are different approaches to stock market prediction.== 
	- In an effort to effectively address the uncertainties involved in trading stocks, futures and other assets, many traders use price-based strategies to enter and exit markets, such as stop-loss, price targets, price breakouts, planning horizons, and other strategies (Warburton & Zhang, 2006, p. 33). ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- Technical trading techniques were developed by analysts based on daily use to forecast stock prices (Dawson & Steeley, 2003, p. 263). In light of this background, it is common to note that different authors utilize their trading systems in the market, using past prices to test them ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- Econometric Models
		- Econometric models can be autoregressive (AR); autoregressive moving averages (ARMAs); autoregressive integrated moving average (ARIMAs); autoregressive conditional heteroscedasticity (ARCH); generalized autoregressive conditional heteroscedasticity (GARCH); or support vector regression (SVR), or they can take other forms. ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- Neural Network
		- This method is based on biological neurosystems, and it is able to learn from examples to make forecasts in examples that have never been observed before (Zhang, Eddy Patuwo, & Hu, 1998, p. 37) ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
		- In the technical analysis context, neural networks allow for trading rules to be remodelled because the parameters of the change generate as an output a prediction of the future situation of the series; neural networks are also better suited for small-range data (Oliveira et al., 2013, p. 7598; Ticknor, 2013, p. 5502). Consequently, neural networks are mostly used to improve on technical trading rules (Creamer, 2012, p. 531) ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])

## What is machine learning and SVR?
- ==There are many works that use machine learning to predict the stock market.== 
	- In this paper, we examined recent developments in stock market prediction models. By comparing various prediction models, we found that NNs offer the ability to predict market directions more accurately than other existing techniques. The ability of NNs to learn nonlinear relationships from the training input/output pairs enables them to model non-linear dynamic systems such as stock markets more precisely [23]. ([[@yooMachineLearningTechniques2005|yoo2005]])
	- Regarding works based on statistical methods, several authors stated that they did not perform efficiently and generated inferior results to models based on artificial intelligence (AI) [15]–[18], as statistical techniques treat financial time series as linear systems. ([[@liStockMarketForecasting2020|li2020]])
	- Additionally, the survey of Cavalcante et al. [5] stated that some financial time series characteristics are responsible for the difficult task of forecasting compared to other time series. Thus, traditional statistical methods are not effectively applied to the economic context. ([[@liStockMarketForecasting2020|li2020]])
- ==The most widely used machine learning algorithm for stock price prediction are neural networks. However, there are disadvantages of using them...==
- ==SVM is a popular machine learning tool that has good generalization ability.==
	- Other models such as SVM and CBR have also become popular in stock market prediction. SVM showed its successful application in classification task and regression tasks, especially on time series prediction and financial related applications [46].  ([[@yooMachineLearningTechniques2005|yoo2005]])
	-  Of all the Algorithms we applied, we saw that only Support Vector Machine combined with Boosting gave us satisfactory results. Linear Regression gave lower mean squared errors while predicting the EMA pattern. ([[@shahMachineLearningTechniques2007|shah2007]])
- ==SVR is a regression model that uses the same concept as SVMs== 
	- Papers that discuss SVR: ([[@shahMachineLearningTechniques2007|shah2007]])

## Related works
- ==What are existing research globally?==
	-  Analysis of different economies is a concern in the technical analysis literature because the volatility and size of the stock markets, the tax systems, people’s education levels, and levels of political instability are different, and, these may influence operational dynamics (Wang, Chiao, et al., 2012; Yu, Nartea, Gan, & Yao, 2013). ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
- ==What are existing research in the Philippines?==




## What is this paper all about?
- ==Gap: There are few studies on developing markets==
	- [x]  Keeping this in mind, it was possible to identify that even though there is a growing number of studies on emerging countries, their numbers cannot be compared with the studies on advanced countries, which can in its turn be considered a gap (G1), as shown below, in the technical analysis literature. ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])
	- [ ] G1 Why are there so few studies of technical analysis that focus on developing economies or emerging countries such as the BRICS1? Since there may be important market frictions in emerging markets and some data may have just recently become available, this technical analysis could be explored further. In addition, less mature markets may be less efficient in the weak form when compared to longer standing markets ([[@fariasnazarioLiteratureReviewTechnical2017|farias2017]])




