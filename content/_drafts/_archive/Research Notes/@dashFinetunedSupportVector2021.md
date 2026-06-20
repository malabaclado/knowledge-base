---
tags: type/research-note 
alias: [Fine-tuned support vector regression model for stock predictions]
---
# Fine-tuned support vector regression model for stock predictions

> [!info]
> - **Cite Key:** [[@dashFinetunedSupportVector2021]]
> - **Abstract:** In this paper, a new machine learning (ML) technique is proposed that uses the fine-tuned version of support vector regression for stock forecasting of time series data. Grid search technique is applied over training dataset to select the best kernel function and to optimize its parameters. The optimized parameters are validated through validation dataset. Thus, the tuning of this parameters to their optimized value not only increases model’s overall accuracy but also requires less time and memory. Further, this also minimizes the model from being data overfitted. The proposed method is used to analysis different performance parameters of stock market like up-to-daily and up-to-monthly return, cumulative monthly return, its volatility nature and the risk associated with it. Eight different large-sized datasets are chosen from different domain, and stock is predicted for each case by using the proposed method. A comparison is carried out among the proposed method and some similar methods of same interest in terms of computed root mean square error and the mean absolute percentage error. The comparison reveals the proposed method to be more accurate in predicting the stocks for the chosen datasets. Further, the proposed method requires much less time than its counterpart methods.
> - **Bibliography:** Dash, R. K., Nguyen, T. N., Cengiz, K., & Sharma, A. (2021). Fine-tuned support vector regression model for stock predictions. _Neural Computing and Applications_. [https://doi.org/10.1007/s00521-021-05842-w](https://doi.org/10.1007/s00521-021-05842-w)
> - **Tags:** #Machine-learning, #Support-vector-regression, #Grid-search, #Mean-absolute-percentage-error, #Root-mean-square-error, #Volatility, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Abstract

- 1 Introduction

- Stock market prediction is a forecasting method that relies on technical aspects of the stock price to predict its future value. The success of such a predictive system mainly depends on the availability of a huge amount of historical data so that it can be used in the pursuit of the lucrative financial markets. The data confined for this type of study are financial time series data which puts stringent constraints on the performance of these models.

- Furthermore, the risk associated with such models cannot be overlooked since risks are implicit due to irregular market trends, instability, noise, etc. [1]. Thus, the predictive models inherently obey the efficient market hypothesis (EMH) which states that the risk-adjusted return cannot consistently be obtained above the profitability of the whole [1, 2].

- EMH assumes that the current stock price can be determined as a function of stock price history and rational expectations. Any deviation to this assumption may leave the stock price to be unpredictable.

- The prominent algorithms that have been used by the researchers to predict stock price include an artificial neural network (ANN) and its variants, genetic algorithm, support vector machine (SVM), support vector regression (SVR), etc.

- The most common challenges to such predictive models are to deal with a risk while predicting the stock price with greater accuracy which in turn minimizes risks for stock market investors and results in a profitable strategy. The accuracy of these models attracts more researchers and makes them motivated to propose new predictive techniques with greater accuracy.

- The proposed study in this paper is an attempt towards improve the precision of the predictive model in an time efficient manner by utilizing SVR as an predictive method.

- 2 Related work

- The study carried out in [12] presents a combined method of autoregressive integrated moving average (ARIMA) and artificial neural network (ANN) models for stock prediction.

- Hamzaebi et al. [13] propose two artificial neural network-based methods for multi-periodic forecasting. The first one is an iterative method that uses past observations to predict subsequent period information. This predicted value is used for the prediction of subsequent periods. These operations are repeated until stopping criterion is met. The second one is an forecast approach in which subsequent periods can be estimated all at once. The main result of this study shows that the direct scheme superiors the iterative model.

- The authors of paper [14] elaborate how artificial neural network (ANN)-based methods can be used as an efficient model in stock-market predictions by analyzing the following models: multi-layer perceptron (MLP), dynamic artificial NN (DAN2) and the hybrid NNs (HNN) using the generalized autoregressive conditional heteroscedasticity (GARCH). Then, they build an efficient stock index prediction scheme for the Shanghai composite index. The model uses a genetic method to train the backpropagation neural network (BPNN). The study concludes that the designed method is better in terms of function approximating capacity yielding ideal results for stock forecasting.

- The work carried out in [15] a new method based on wavelet de-noising-based backpropagation (WDBP) neural network is proposed for stock prediction.

- A new model [16] that uses evolving partially connected neural networks (EPCNNs) for stock prediction. Their model architecture is different from traditional artificial neural networks because they have random connections among neurons, more than one hidden layer, and use evolutionary algorithms to train the artificial neural network.

- Jo et al. [17] propose a method that has a filter and a modified genetic algorithm (MGA). MGA is used to set initial parameters for morphological-rank-linear (MRL) filters and to fine tune these parameters. The least mean squares (LMS) algorithm is used to further develop these parameters.

- The work carried out in [18] uses the least square SVM (LS-SVM) with an integration of particle swarm optimization (PSO) to predict the daily stock prices. The hyperparameters of LS-SVM are optimized by using the PSO algorithm. The authors claim that the optimized hyperparameters avoid data over-fitting and local minima issues, and thus, they improve the predictions of the precision.

- Stock forecasting involves time series data containing highly unpredictable errors. This is the main reason that artificial neural network and its variants are dominantly become the best choice of the researchers. However, irrespective of the type of learning algorithms used, the time to converge to optimal solution by using artificial neural networks or its variants is a major concerned.

- However, support vector regression is observed to be a prominent technique for stock forecasting with a good measure of accuracy. The lack of fine tuning its parameters may lead to a time consuming method which distracts the researchers to use this technique further.

- The above-mentioned problems motivates us to propose a new method based on SVR for stock forecasting. In this work, a method that efficiently manages the risk in terms of errors is presented. Grid search technique is used to optimize the parameters of support vector regression for entire dataset

- 3 Support vector regression (SVR)

- 4 FTSVR: Fine-tuned support vector regression model for stock predictions

- 4.1 Selection of dataset and its pre-processing

- 4.2 Creation of training and validation dataset

- Normally, the profit or loss is usually determined by the value of the closing price of a stock for a particular day; hence, closing price is treated as the target variable

- Out of dataset, 70% records i.e. 4163 are used for training while the rest number of records i.e. 1784 are for the purpose of testing.

- 4.3 Selection of kernel function and parameters tuning

- The performance of machine learning algorithms largely depends on their parameters. So, it is almost essential to fine tune the parameters to design a predictive model that predicts future outcome with greater accuracy. Further, the tuning of parameters avoids the model to suffer from data overfitting which is a serious issue in machine learning. The selection of kernel function and its optimized parameters of a support vector regression is a great challenge since these are very much data oriented.

- Grid search optimizes different SVR parameters to select a combination of parameters; thus, the method can predict unknown data exactly.

- 5 Performance of the proposed model for stock analysis

- 5.1 Up-to-daily and Up-to-monthly return prediction

- Cumulative up-to-monthly return is a measure that aggregates gain/loss amount for a certain period of time. The cumulative up-to-monthly return (or up-to-daily return) can be calculated from up-to-monthly return(or upto-daily return) for a certain period of time. The cumulative up-to-monthly return is depicted in Fig. 12. Cumulative up-to-monthly return of SBIN presents the growth of Rs.1 over the entire period which indicates a return of Rs. 30 after 16 years of investment.

- 5.2 Prediction of volatility nature of stock

- Volatility is a measure that disperses around the mean or average return of a stock. Higher degree of volatility of a stock indicates a higher probability of a declining market, while its lower value indicates to a higher probability of a rising market.

- 6 Results and discussion

- The comparison is made among the existing method, SVR method [2] and hybrid NN [32] based on generated values of RMSE and MAPE for the whole dataset (see Table 7). Although SVR method [2] uses support vector regression, it is missing with optimization technique. Further, this work does not have any dedicated method to deal with missing data (SBIN has 128 number of missing closing values which is around 2% of SBIN dataset). Hybrid neural network [32] is a combined method containing the artificial neural network and particle swarm optimization.

- The proposed method in this study aims to use a new finetuned support vector regression model for predicting the stock price. A suitable dataset is taken to explain each step of this method. Missing attributes are well handled by using appropriate techniques. Grid search is performed on the entire training dataset to choose the kernel function and its optimized parameters. The training of the proposed method is performed over 4163 records while validation is performed by using 1800 records. RMSE and MAPE are computed for training and validation, respectively. The proposed method is compared against some existing methods of similar interest in terms of computed RMSE, MAPE and time

- Eight different datasets from four different sectors are considered for their stock prediction. The results show the prediction values are closely fitted with the actual values. The proposed method can further be used to predict the stock of any industry with greater accuracy.




%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:42.670+08:00 %%
