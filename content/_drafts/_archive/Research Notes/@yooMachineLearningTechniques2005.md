---
tags: type/research-note 
alias: [Machine learning techniques and use of event information for stock market prediction: A survey and evaluation]
---
# [[Machine Learning]] techniques and use of event information for [[Stock Market Prediction]]: A survey and evaluation

> [!info]
> - **Cite Key:** [[@yooMachineLearningTechniques2005]]
> - **Abstract:** This paper surveys [[Machine Learning]] techniques for [[Stock Market Prediction]]. The prediction of stock markets is regarded as a challenging task of financial time series prediction. In this paper, we present recent developments in stock market prediction models, and discuss their advantages and disadvantages. In addition, we investigate various global events and their issues on predicting stock markets. From this survey, we found that incorporating event information with prediction model plays very important roles for more accurate prediction. Hence, an accurate event weighting method and a stable automated event extraction system are required to provide better performance in financial time series prediction.
> - **Bibliography:** Yoo, P. D., Kim, M. H., & Jan, T. (2005). Machine learning techniques and use of event information for stock market prediction: A survey and evaluation. _International Conference on Computational Intelligence for Modelling, Control and Automation and International Conference on Intelligent Agents, Web Technologies and Internet Commerce (CIMCA-IAWTIC’06)_, _2_, 835–841.
> - **Tags:** #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Abstract Abstract

- This paper surveys machine learning techniques for stock market prediction. The prediction of stock markets is regarded as a challenging task of financial time series prediction. In this paper, we present recent developments in stock market prediction models, and discuss their advantages and disadvantages. In addition, we investigate various global events and their issues on predicting stock markets. From this survey, we found that incorporating event information with prediction model plays very important roles for more accurate prediction. Hence, an accurate event weighting method and a stable automated event extraction system are required to provide better performance in financial time series prediction.

- 1. Introduction

- Stock market prediction has been an important issue in the field of finance, engineering and mathematics due to its potential financial gain. As a vast amount of capital is traded through the stock market, the stock market is seen as a peak investment outlet.

- In addition, stock market prediction brings with it the challenge of proving whether the financial market is predictable or not. Since there has been no consensus on the validity of Efficient Market Hypothesis (EMH) which states the market is efficient and there is no space for prediction, researchers have strived for proving the predictability of the financial market [23].

- To predict the stock market accurately, various prediction algorithms and models have been proposed by many researchers in both academics and industry.

- In this paper, recent development in prediction algorithms and models will be introduced and their performance will be compared. In addition, for accurate stock market prediction, we investigate various global events and their issues on predicting stock markets.

- 1.1. Background

- Since the stock market was firstly introduced, many have attempted to predict the stock markets using various computational tools such as [[linear regression]] (LR), Neural Networks (NNs), [[Genetic algorithms]] (GAs), [[Support Vector Machines]] (SVMs), Case-based Reasoning (CR) and others. Over the last decade, NNs have been most widely used and shown better performance over other approaches in many cases.

- The earliest stock market prediction model based on NNs was implemented by White [45]. He used Feed Forward Neural Networks (FFNNs) to decode previously undetected regularities in the asset price movements such as fluctuations of common stock prices and showed how to search for such regularities using FFNNs. Since the initiative attempt by White, a number of researchers have participated in developing an accurate stock market prediction model.

- Phua et al. [31] used NNs with GA to predict the Singapore Stock Exchange Index and achieved accuracy rate of 81%. Kim and Han [18] also combined NNs with GA and predicted Korea Composite Stock Price Index 200. He achieved 82% of accuracy in predicting both weekly rising and declining stock market tendencies.

- Many researchers have compared the NNs to the statistical approaches for pattern recognition [8] [35]

- Yoon et al. [47] pointed out the superiority of NNs over classical discriminant analysis. Garliauskas [8] also investigated stock market prediction using NNs in corporation with [[kernel function]] approach and the recursive prediction error method. He concluded that in predicting financial time series, NNs have better performance than classical statistical methods.

- In general, numerous studies have shown that NNs have the ability to predict stock markets more accurately than other methods

- Although the former studies were confined to quantitative analysis, several recent studies have been performed based on the qualitative analysis. Many believed the integration of event-knowledge and NNs hold great promise for improved prediction in stock markets

- Kohara [20] investigated ways of improving multivariate predictive models in stock price prediction using priorknowledge and NNs. He used information from the newspaper headlines to improve the prediction ability.

- Their experimental results showed that the use of event-knowledge based on the prior-knowledge with NNs significantly reduced the prediction error rate on the 5% level of significance with profit by 40%.

- In addition, Hong and Han [12] compared NNs with the event information to Random Walk (RW) model and NNs without event information. NNs with the event information have a figure of 0.527% in average error, which is a smaller error in comparison to other models. They proved that the NNs based forecaster is greatly superior to RW and that the effect of event information does exist.

- Furthermore, in predicting stock market, many researchers have recognized that qualitative factors such as political effects and international events played a very important role. Thus, they proposed that a stock market prediction system incorporate both quantitative and qualitative factors.

- 1.2. Key issues in financial prediction

- A number of researchers have shown their official viewpoint of EMH in academia [24] [45].

- that the current market price reflects the assimilation of all the information available [10]. The information relevant to a market is contained in the prices and each time that new information arises, the market corrects itself and absorbs it, thus, the market is efficient and there is no space for prediction [5]. There has been a long ongoing debate about the validity of EMH, but no consensus has been made. In recent years, many researchers have claimed that EMH surely must be false [6]. Several studies have been performed on the data of stock markets in order to prove that the market is predictable. If any computational based systems have the capability to show reasonable prediction accuracy based on the market historical data, the validity of EMH can be questioned.

- Tsibouris and Zeidenberg [42] used NNs to predict stock market only based on past stock prices as inputs. Their empirical results showed some level of predictive ability and rejected the weak form of EMH. In addition, Eyden [3] developed a system which models the performance of the Johannesburg Stock Exchange and their system provided significant evidence by showing its capability to predict stock market directions, thus, it again dissented from EMH.

- On the other hand, various studies were based on EMH. Fung et al. [7] investigated the immediate impact of news articles on the time series based on EMH. They presented an EMH based system to predict the future behavior of the stock market using nonquantifiable information (news articles) and the predictions were made only according to the contents of the news article. Finally, their empirical result indicated that the approach built based on EMH is profitable than simple trading strategy based on Buyand-Hold.

- As it has been discussed, many of different studies have concluded to accept or refute EMH. Thus, the issue of market efficiency is still not fully investigated and it leads to a need for further research.

- A number of researchers have used historical numeric [[Time Series Data]] to predict stock markets and they achieved reasonable prediction accuracy while denying EMH [3] [42]. However, there are various factors that influence stock prices such as company’s performance and robustness, trends of the market, investors’ psychology, government involvement, changes in economic activity and so forth. Thus, many researchers have agreed to the existence of significant correlation between the events which represent above factors, and stock markets

- 2. Prediction methods

- 2.1. Traditional time series prediction

- Traditional statistical models are widely used in economics for time series prediction. These models are capable of modeling linear relationships between factors that influence the market and the value of the market. In economics, there are two basic types of time series forecasting: univariate (simple regression) and multivariate (multivariate regression)

- Although Box-Jenkins shows good ability for shortterm forecasting, it requires a large amount data to yield high accuracy

- A number of studies have compared the multivariate statistical model with NNs. Although the multivariate models had been widely used for predicting stock markets, several machine learning techniques are now replacing their roles.

- In the literature, many researchers claimed that NNs substantially outperform traditional statistical methods [8] [35].

- 2.2. Neural Networks

- In the literature, it has been shown that NNs offer the ability to predict market directions more accurately than other existing techniques. The ability of NNs to discover non-linear relationships between the training input/output pairs makes them ideal for modeling nonlinear dynamic systems such as stock markets

- One of the advantages is the ability to learn relationship through the data itself rather than assuming the functional form of the relationship.

- Another advantage is that NNs have non-linear, non-parametric adaptive learning properties and they have the most practical effect in modeling and forecasting. The non-linear nature of NNs shows great potential to solve many complex problems.

- Due to the above characteristics of stock markets, NNs can be applied to stock market prediction. Firstly, stock data is hard to model due to its complexity, thus, non-linear model is beneficial. Secondly, a large set of interacting input series is often required to explain a specific stock.

- Regarding downsides, NNs have the black box problem, which does not reveal the significance of each variable and the way they weigh independent variables

- Another major problem with NNs is the overtraining problem. When NNs fit the data too well, the system loses the ability to generalize. Since the [[Generalization]] ability of NNs is fundamental to predict future stock prices, overtraining is a serious problem.

- 2.3. Support Vector Machine

- Support Vector Machine (SVM) based on the statistical learning theory, was developed by Vapnik [44] and his colleagues in the late 1970s. It has become a hot topic of intensive study due to its successful application in classification and regression tasks, especially in time series prediction and financial related applications [46]

- SVM is a very specific type of learning algorithms characterized by the capacity control of the decision function, the use of the kernel functions and the sparsity of the solution

- Established on the unique theory of the [[Structural Risk Minimization]] principle to estimate a function by minimizing an upper bound of the generalization error, [[Support Vector Machines|SVM]] is shown to be very resistant to the overtraining problem, eventually achieving a high generalization performance

- Another key property of [[Support Vector Machines|SVM]] is that training SVM is equivalent to solving a linearly constrained quadratic programming problem. Thus, the solution of SVM is relatively unique and globally optimal, unlike NNs training which requires nonlinear optimization with the danger of getting stuck at local minima.

- As SVM implements the [[Structural Risk Minimization]] principle, SVM leads to better [[Generalization]] than traditional techniques.

- 2.4. Case Based Reasoning

- 3. Event information

- The primary reason of incorporating event knowledge in stock market prediction is based on an assumption that the future price of a stock partially depends on various political and international events as alongside the various economic indicators. Thus, many studies have used event information (qualitative factors) as well as quantitative data in predicting stock markets.

- In the literature, a number of researchers stated that stock prices are significantly correlated with the event information and many attempted to use both the event information and numeric time series data as input data.

- 4. Event information on the Web

- 5. Conclusion and future work

- In this paper, we examined recent developments in stock market prediction models. By comparing various prediction models, we found that NNs offer the ability to predict market directions more accurately than other existing techniques. The ability of NNs to learn nonlinear relationships from the training input/output pairs enables them to model non-linear dynamic systems such as stock markets more precisely [23].

- Other models such as SVM and CBR have also become popular in stock market prediction. SVM showed its successful application in classification task and regression tasks, especially on time series prediction and financial related applications [46].

- CBR is a reasoning technique that reuses past cases to find a solution to the new problem. CBR captures organization knowledge and expertise while providing explanations for the derived solutions. For this reason, CBR is popularly applied to many applications.

- n addition, by studying several important issues in stock markets, we found that that many researchers have recognized that qualitative factors such as political effects and international events can have a significant impact on stock prices.

- It has been reviewed that NNs based on both quantitative and qualitative factors are far superior to the ones based only on the quantitative factors. In addition, the web is regarded as the primary event source for stock market prediction containing the latest and latent event information. Thus, for the stock market prediction, a level of web mining technique is required in order to yield higher prediction accuracy and to make prediction in short time frame.

- For further research, firstly, prior-knowledge database should be built by analyzing historical events on stock markets. Based on the prior-knowledge, the event weighting schema will be developed and each event should be weighted accordingly. Finally, a proposed model which incorporates the weighed events into the numeric time series data should be compared empirically with other models


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:47.235+08:00 %%
