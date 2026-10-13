---
tags: type/research-note 
alias: [Practical Bayesian support vector regression for financial time series prediction and market condition change detection]
---
# Practical Bayesian support vector regression for financial time series prediction and market condition change detection

> [!info]
> - **Cite Key:** [[@lawPracticalBayesianSupport2017]]
> - **Abstract:** Support vector regression (SVR) has long been proven to be a successful tool to predict financial time series. The core idea of this study is to outline an automated framework for achieving a faster and easier parameter selection process, and at the same time, generating useful prediction uncertainty estimates in order to effectively tackle flexible real-world financial time series prediction problems. A Bayesian approach to SVR is discussed, and implemented. It is found that the direct implementation of the probabilistic framework of Gao et al. returns unsatisfactory results in our experiments. A novel enhancement is proposed by adding a new kernel scaling parameter to overcome the difficulties encountered. In addition, the multi-armed bandit Bayesian optimization technique is applied to automate the parameter selection process. Our framework is then tested on financial time series of various asset classes (i.e. equity index, credit default swaps spread, bond yields, and commodity futures) to ensure its flexibility. It is shown that the generalization performance of this parameter selection process can reach or sometimes surpass the computationally expensive cross-validation procedure. An adaptive calibration process is also described to allow practical use of the prediction uncertainty estimates to assess the quality of predictions. It is shown that the machine-learning approach discussed in this study can be developed as a very useful pricing tool, and potentially a market condition change detector. A further extension is possible by taking the prediction uncertainties into consideration when building a financial portfolio.
> - **Bibliography:** Law, T., & Shawe-Taylor, J. (2017). Practical Bayesian support vector regression for financial time series prediction and market condition change detection. _Quantitative Finance_, _17_(9), 1403–1416. [https://doi.org/10.1080/14697688.2016.1267868](https://doi.org/10.1080/14697688.2016.1267868)
> - **Tags:** #Machine-learning, #Bayesian-inference, #C44, #C45, #C61, #Gaussian-process, #Kernel-scaling, #Multi-armed-bandit-Bayesian-optimization, #Support-vector-machines-regression, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- 1. Introduction

- Support vector regression (SVR) has been one of the most popular Machine-learning algorithms for over a decade. Its ability to predict financial time series has been demonstrated in various studies (Müller et al. 1997, Tay and Cao 2001, Cao and Tay 2003, Kim 2003, Lu et al. 2009, Gündüz and UhrigHomburg 2011) with satisfactory empirical results.

- Although the base assumption of most machine-learning models requires i.i.d. data, there is literature (Mohri and Rostamizadeh 2008, Ralaivola et al. 2010) suggesting non-i.i.d. data can be used to train the statistical learning system by increasing sample sizes.

- This supports SVR as a relevant tool for time series prediction. Comparing to other linear time series models, which require careful designing of inputs, SVR allows flexible mapping of high dimensional features to capture non-linear relationships and at the same time with a regularization technique to reduce

- However, on the other hand, financial experts in the industry may step back from using this algorithm for two reasons: (1) it is not easy, and sometimes computationally expensive to determine the parameters for the algorithm, (2) it does not provide an estimate of prediction uncertainties.

- We propose to investigate extensions to the approach that make up for these two disadvantages by generalizing it within a Bayesian approach. This allows a more efficient parameter selection procedure as well as the derivation of a prediction uncertainty estimate.

- A Bayesian approach to SVR (Gao et al. 2002) is discussed, and implemented. It is found in our experiments that direct implementation of the probabilistic framework proposed by Gao et al. (2002) gives unsatisfactory results. A novel enhancement is proposed by adding a new kernel scaling parameter μ to overcome the difficulties encountered.

- Multi-arm bandit Bayesian optimization has been gaining popularity in recent years (Shahriari et al. 2016), mainly for its capability to actively and efficiently search for the global optimum for a complex or even unknown function. We make use of this technique to fully automate the parameter selection process.

- 2. Support Vector Regression

- The concepts of support vector machine (SVM) can naturally be applied to handle regression problems. Instead of classifying testing examples into one of the two outcomes (class 1 or class 2), it is used to address target variables with real values.

- The ε-Support Vector Regression (ε-SVR) can be considered similar to the approach of applying a linear regression in the feature space. In contrast to the squared loss function used in the least squares regression, the error function for ε-SVR is the ε-insensitive loss function. This dictates that the errors smaller than ε are ignored. Figure 1 demonstrates this intuition. This method leads to sparsity similar to SVMs meaning that the form of the regression depends only on the support vectors.

- 3. Probabilistic Framework for SVR

- The selection of parameters has always been one of the most important tasks when training supervised learning algorithms, and SVR is no exception. In order to achieve good generalization performance, a process is required to fine tune the parameters in order to balance the trade-off between variance and bias. Traditionally, the multi-fold cross-validation process is employed. This process is generally very effective, but usually computationally heavy.

- We propose a new parameter μ in addition to the SVR probabilistic framework of Gao et al. (2002). This parameter μ scales the kernel, and is defined to be the a priori estimate of the output variance. We show that adding such a parameter does not affect the SVR quadratic programming problem, but may act as a scaling parameter to allow the evidence function to be more flexible when handling data with different ranges.

- 3.1. Bayesian Evidence Framework

- SVR can be interpreted as a maximum a posteriori (MAP) solution to inference problems with Gaussian priors and an appropriate likelihood function based on a probabilistic interpretation.

- 3.3. New scaling parameter μ

- The effort of deriving this evidence framework by Gao et al. (2002) is highly appreciated. Not only does it give a very good methodology to choose the ‘best’ parameters, but also it provides an error bar estimate of the SVR prediction. This is implemented in our study, but the results were rather unsatisfying, which lead to our idea of introducing a new scaling parameter μ to the evidence framework.

- 4. Bayesian optimization for parameters selection

- Recently, the popularity of Bayesian optimization has grown significantly in the artificial intelligence and machine learning community (Srinivas et al. 2010, Shahriari et al. 2016). Its capability to actively and efficiently search for the global optimum for a complex or even unknown function greatly enhance the automatic tuning process for many powerful machine learning algorithms (Snoek et al. 2012).

- In this study, we borrow such technique to optimize the log evidence function in order to obtain the ‘best’ parameters. Bayesian optimization is explained in this section, and are used in our experiments.

- 4.1. Multi-armed Bandit

- Multi-armed bandit (MAB) problem is a problem in which a gambler faces k slot machines, a.k.a. ‘one-armed bandits’. Each machine has unknown probability of winnings. The gambler is allowed to play one machine each round, and eventually has to define strategy to maximize the total winnings. The key here is to trade-off between exploration (try a new machine), and exploitation (continue to play with an already observed winning machine). This problem has been widely studied in various areas such as machine learning, operational research and control etc.

- To efficiently perform the trade-off between exploration and exploitation, the dependencies across arms are assumed and modelled (Dorard et al. 2009). Such dependencies allow exploration to be faster. When an arm is explored, knowledge is gained on that arm as well as similar arms. The rewards of arms are assumed to be correlated, which means that the resulting rewards are similar if the arms pulled are similar. The correlations are modelled by assuming that f is a function drawn from a Gaussian Process (GP).

- 4.2. Gaussian process

- GP is a widely used method in machine learning.

- 4.3. Acquisition method

- The acquisition function, which is also the expected utility in decision theory, is the key to define the order of sequence in selecting input points. It is designed to trade off exploration of the search space and exploitation of the currently known area. The inputs that correspond to the optimum of the acquisition function are usually the location of the next input.

- 5. Experiments

- SVR has long been proven to have good prediction performance. The focus of this study is to outline a Bayesian probabilistic framework for the algorithm mainly for two purposes.

- (1) Multi-fold cross validation process is well known to be an effective method to select parameters for machine learning algorithms, but is usually computationally expensive. Borrowing the MAP approach from Bayesian statistics, it may be possible to achieve similar performance as the original SVR with less computation to select the ‘best’ parameters.

- (2) Introducing the probabilistic framework allows assessment of prediction uncertainties. This is extremely important especially in the financial context, where decisions are better based on predictions with some level of confidence.

- 5.1. Data

- 5.2. Implementation

- The original Bayesian probabilistic framework by Gao et al. (2002) is implemented. However, for the theoretical reasons explained in section 3.3, the results are poor.

- As mentioned previously, the gradient method to optimize the log evidence is impractical, and seeking for another optimization method was necessary. The easiest optimization method is grid search. Although grid search is still quite computationally expensive, and its performance is highly dependent on the design of the grid, it is very easy to implement and the results are easy to assess.

- 5.3. Results

- In the first set of experiments, the original RBF kernel SVR algorithm is first trained and tested with parameters selected through five-fold cross validation. The results are then used as the benchmark performance when comparing to the ones from the Bayesian SVR where parameters are selected through the evidence maximization approach using grid search or Bayesian optimization.

- MAPEs (equation (29)) are computed to assess the predictive performance of each model for each times series. Algorithms are trained with 2.5 years of data (630 quotes), and test on the following 0.5 year (125 quotes), assuming 252 trading days in a year. Predictions are performed and assessed in a rolling window manner to cover the entire time series.

- It is interesting to observe that with S&P500 (SPX), the original SVR with five-fold cross validation shows inconsistent prediction performance. It may be a sign suggesting, in this case, cross-validation is incapable to generalize the training data distribution to the testing data. It may be fixed by fine tunes such as changing the size of training or testing window, using different number of folds in the cross-validation process etc.

- Other than SPX, the models generated from the three different parameters selection methods give comparable performance in most of the cases. This is encouraging as it suggests that it may be worthwhile to generalize SVR to Bayesian SVR to gain the additional features such as a faster and easier parameter selection process, as well as an estimate of prediction uncertainty, without sacrificing much predictive performance.

- Results from the last experiment provide initiatives to spend more effort in examining further the performance and use of Bayesian SVR. It is shown that Bayesian optimization accelerates the log evidence optimization process while retaining similar performance as using grid search. Hence, in the second set of experiments, only Bayesian SVR with Bayesian optimization selected parameters is applied. S&P500 Equity Index is used as an example to demonstrate the practical use of this Bayesian SVR framework. Since the computational cost for the parameters selection process has been significantly reduced, we are able to increase the number of iterations by training the algorithm with three months of data (63 quotes), and testing daily. This greatly enhances the sensitivity of predictions and their uncertainty measures in better adapting to the rapid-changing nature of financial time series.

- It is quite obvious that the Bayesian SVR predictions are less reliable during the high volatility regimes. This matches expectation as the data distribution may not be well represented in the training data during high volatility circumstances. Therefore, it is important to take into account prediction uncertainties to assess the quality of predictions.

- 5.4. Calibration

- 6. Conclusions and future extensions

- A Bayesian approach to SVR (Gao et al. 2002) is discussed, and implemented. It is found that direct implementation of the probabilistic framework proposed by Gao et al. (2002) returns poor results in our experiments. A novel enhancement is proposed by adding a new kernel scaling parameter μ to overcome the difficulties encountered. In addition, the multi-armed bandit Bayesian optimization technique is applied to automate the parameter selection process.

- The framework is then tested on financial time series of various asset classes to ensure its flexibility. In the experiments, it is shown that the generalization performance of the model selected through our framework can reach or sometimes surpass the ones from the model selected through the computationally more expensive cross-validation process. While taking advantage of the reduction in computational cost, iterations are increased to generate daily predictions. It is shown with the S&P500 Equity Index that the prediction error has decreased, while generating a sensible prediction uncertainty estimate.

- An adaptive calibration process is then presented to demonstrate the practical use of the prediction uncertainty estimates to identify ‘unreliable’ predictions, which greatly enhances the prediction performance.

- The machine learning approach discussed in this study can be developed as a pricing tool, and possibly as a market condition change detector.

- While the framework is quite effective as it is, there are a few directions that may justify further investigations. The multi-armed bandit optimization technique employed at the moment is sequential. Although it is quite efficient, it can be further improved by parallelizing the algorithm. This has been discussed in a few studies (Ginsbourger and Riche 2011 Snoek et al. 2012 Desautels et al. 2014).

- Also, as mentioned, the calibration process introduced is efficient and simple to implement. However, it may be interesting to find out if other clustering algorithms give better results, or possibly lead to a regime clustering algorithm. Furthermore, it may be interesting to relax the Gaussian prior distribution assumption of the probabilistic framework proposed by Gao et al. (2002) .Agood example is to extend the SVR model to a Multi-Kernel Learning formulation which assumes a non-Gaussian prior distribution. However, this may lead to significant complexity in the reconstruction of the Bayesian evidence approximation. From the financial point of view, the prediction uncertainty estimates may be extended as inputs to build financial portfolios.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:44.007+08:00 %%
