---
tags:
alias:
creation-date: Friday 28th October 2022
last-modified-date: Friday 28th October 2022 10:26:21
---

# Introduction of the Topic
The prediction of stock market prices is a widely explored topic of interest in the field of finance, engineering and mathematics. ([[@yooMachineLearningTechniques2005|yoo2005]], [[@shahMachineLearningTechniques2007|shah2007]]) The term *stock market* (sometimes called *stock exchange*) refers to the collection of buyers and sellers of stocks, which are financial instruments that represent ownership of businesses. 

A substantial amount of research literature reveal that stock market price forecasting is a challenging task. Some studies show that the problem is due to the nonlinear and nonstationary feature of financial time series data. ([[@liStockMarketForecasting2020|li2020]], [[@fariasnazarioLiteratureReviewTechnical2017|farias2017]]) Others have cited that the complexity of stock market forecasting is associated with a considerable number of factors such as political events, market news and company policies. ([[@shahMachineLearningTechniques2007|shah2007]])

One of the motivations for stock price forecasting is financial gain. The monetary value of a stock is dynamically changing over time. Stock traders take opportunity of this volatility to make profits off the market. As massive amount of capital is traded through the stock market, a system that can determine which assets are doing well and which assets are not in the dynamic stock market will make it easy for investors or finance professionals make decisions. Hence, making stock price prediction a worthwhile research endeavor.


Traditional approaches for stock price prediction includes Autoregressive Integrated Moving Average (ARIMA). 

*The problem with these models*

Due to computational advancements and availability of large data, there is an increasing use of machine learning for financial forecasting problems like the prediction of stock market prices. 

Machine learning is a branch of artificial intelligence that allow computers to generalize patterns  from data, giving rise to expert systems that are efficient in classification and regression tasks. 

*Examples of machine learning algorithms*

Studies show that artificial neural networks are the most efficient machine learning approach for stock market price prediction. 

*Disadvantages with Neural Networks*

Artificial Neural Networks and its variants dominantly became the best choice for researchers when it comes to stock price prediction. However, the time to converge to optimal solution by using ANNs or its variants is a major concern. However, support vector regression is observed to be a prominent technique for stock forecasting with a good measure of accuracy. ([[@dashFinetunedSupportVector2021|dash2021]])

*Solution offered by Support Vector Machines*

Support vector machine (SVM) is a machine learning model that has good generalization ability, since it was based on Structural Risk Minimization. 

Support vector regression (SVR) is a regression model based on SVMs. Instead of findinf the largest margin from the separating hyperplane, SVR seeks to find the flattest line inside an $\epsilon$-tube. It seeks to minimize a certain loss function called the $\epsilon$-insensitivity function. 

At the time of writing, there is no study that applies support vector regression (SVR) in predicting Philippine stocks.

In a literature review conducted by [[@fariasnazarioLiteratureReviewTechnical2017|farias2017]] on studies that use technical analysis approach on stock price prediction for the last 55 years, it is found that there is a gap between the number of studies aimed at advanced markets than developing markets like the Philippines.

This study aims to make a significant contribution to fill that gap by a creating a stock prediction model for the Phlilippine Stock Exchange Index based on support vector regression. 

The challenge of choosing the best predictive SVR model lies on the kernel and regularization values. To solve this problem, we used the grid search method to find the optimal parameters over a range of values. The performance of the model is measured using the Root Mean Squared Error (RMSE) and Mean Absolute Percentage Error (MAPE). 

The rest of this paper is organized as follows: Section 2 describes the technical analysis indicators that will be used as features. Section 3 discussed the workings behind Support Vector Regression. Section 4 presents the proposed stock price forecasting method. Experimental results are discussed in section 5. Finally, a conclusion is given on Section 6.




----
### References
