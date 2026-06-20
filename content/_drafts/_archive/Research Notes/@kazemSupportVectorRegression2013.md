---
tags: type/research-note 
alias: [Support vector regression with chaos-based firefly algorithm for stock market price forecasting]
---
# Support vector regression with chaos-based firefly algorithm for stock market price forecasting

> [!info]
> - **Cite Key:** [[@kazemSupportVectorRegression2013]]
> - **Abstract:** Due to the inherent non-linearity and non-stationary characteristics of financial stock market price time series, conventional modeling techniques such as the Box–Jenkins autoregressive integrated moving average (ARIMA) are not adequate for stock market price forecasting. In this paper, a forecasting model based on chaotic mapping, firefly algorithm, and support vector regression (SVR) is proposed to predict stock market price. The forecasting model has three stages. In the first stage, a delay coordinate embedding method is used to reconstruct unseen phase space dynamics. In the second stage, a chaotic firefly algorithm is employed to optimize SVR hyperparameters. Finally in the third stage, the optimized SVR is used to forecast stock market price. The significance of the proposed algorithm is 3-fold. First, it integrates both chaos theory and the firefly algorithm to optimize SVR hyperparameters, whereas previous studies employ a genetic algorithm (GA) to optimize these parameters. Second, it uses a delay coordinate embedding method to reconstruct phase space dynamics. Third, it has high prediction accuracy due to its implementation of structural risk minimization (SRM). To show the applicability and superiority of the proposed algorithm, we selected the three most challenging stock market time series data from NASDAQ historical quotes, namely Intel, National Bank shares and Microsoft daily closed (last) stock price, and applied the proposed algorithm to these data. Compared with genetic algorithm-based SVR (SVR-GA), chaotic genetic algorithm-based SVR (SVR-CGA), firefly-based SVR (SVR-FA), artificial neural networks (ANNs) and adaptive neuro-fuzzy inference systems (ANFIS), the proposed model performs best based on two error measures, namely mean squared error (MSE) and mean absolute percent error (MAPE).
> - **Bibliography:** Kazem, A., Sharifi, E., Hussain, F. K., Saberi, M., & Hussain, O. K. (2013). Support vector regression with chaos-based firefly algorithm for stock market price forecasting. _Applied Soft Computing_, _13_(2), 947–958. [https://doi.org/10.1016/j.asoc.2012.09.024](https://doi.org/10.1016/j.asoc.2012.09.024)
> - **Tags:** #Support-vector-regression, #Chaotic-mapping, #Firefly-algorithm, #Stock-market-price-forecasting, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Stock market price prediction is regarded as one of the most 24 challenging tasks of financial time series prediction. The diffi25 culty of forecasting arises from the inherent non-linearity and 26 non-stationarity of the stock market and financial time series.

- In 27 the past, Box–Jenkins models [1], such as the autoregressive (AR) 28 model and the autoregressive integrated moving average (ARIMA) 29 model, were proposed to tackle this problem. However, these mod30 els were developed based on the assumption that the time series 31 being forecasted are linear and stationary.

- ANN has been widely used for modeling stock market time 38 series due to its universal approximation property [23]. Previ- 39 ous researchers have indicated that ANN, which implements the 40 empirical risk minimization principle in its learning process, out- 41 performs traditional statistical models [4].

- In this paper, we propose a chaotic firefly algorithm for opti57 mizing the SVR hyperparameters. Results show that our method 58 performs better than SVR-FA, SVR-GA SVR-CGA, ANFIS, ANN and 59 other previous algorithms.

- 2. Support vector regression with chaotic firefly algorithm

- 2.1. Delay-coordinate embedding

- 2.3. Support vector regressions (SVR)

- 2.4. Firefly algorithm (FA)

- The firefly algorithm is a metaheuristic optimization algorithm 172 inspired by the flashing behavior of fireflies [41]. Fireflies use 173 their natural glowing mechanism to attract other fireflies. In this 174 algorithm, each firefly represents a possible solution and its light 175 intensity is proportional to its objective function value. Fireflies 176 with lower light intensity (fitness) move toward fireflies with 177 higher light intensity

- 3. Proposed integrated algorithm

- 3.1. Data preprocessing

- 3.2. Proposed chaotic firefly algorithm

- Firefly algorithms (FAs), like other nature-inspired optimization 220 algorithms, use a random approach to generate an initial solu- 221 tion. However, this approach has two major shortcomings, namely 222 slow convergence and becoming trapped in local optima, caused 223 by reduced population diversity. In this approach, the initial pos- 224 itions of fireflies are not necessarily fully diversified in the search 225 space [32]. To improve initial solution diversity and the quality of 226 the initial population, a CMO (Eq. (1)) is used instead of a random 227 approach to generate an initial solution.

- 4. Case study

- 4.1. Data collection and performance evaluation

- Daily closing (last) stock market prices for Microsoft (from 280 9/12/2007 to 11/11/2011), Intel (from 9/12/2007 to 11/11/2010) 281 and National Bank shares (from 6/27/2008 to 8/29/2011) were 282 extracted from NASDAQ historical quotes.

- The dataset was divided 283 into two sets, a training dataset and a testing dataset; 80% of the 284 daily data (a total of 640 observations) were used for the train- 285 ing dataset and the remainder of the daily data (a total of 160 286 observations) were used for the testing dataset.

- 4.2. Parameter setting in CFA algorithm

- The parameters of the CFA algorithm in the proposed model for 293 three numerical examples are experimentally set. The number of 294 fireflies is 20, the maximum number of iterations is 200, ˇ0 is 4, 295 the constant of the annealing operator is 0.25 and the absorption 296 coefficient is 1.

- 4.3. Phase space reconstruction

- 4.4. Performance comparison

- 5. Conclusion


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:43.863+08:00 %%

