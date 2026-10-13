---
tags: type/research-note 
alias: [Financial time series forecasting using independent component analysis and support vector regression]
---
# Financial time series forecasting using independent component analysis and support vector regression

> [!info]
> - **Cite Key:** [[@luFinancialTimeSeries2009]]
> - **Abstract:** As financial time series are inherently noisy and non-stationary, it is regarded as one of the most challenging applications of time series forecasting. Due to the advantages of generalization capability in obtaining a unique solution, support vector regression (SVR) has also been successfully applied in financial time series forecasting. In the modeling of financial time series using SVR, one of the key problems is the inherent high noise. Thus, detecting and removing the noise are important but difficult tasks when building an SVR forecasting model. To alleviate the influence of noise, a two-stage modeling approach using independent component analysis (ICA) and support vector regression is proposed in financial time series forecasting. ICA is a novel statistical signal processing technique that was originally proposed to find the latent source signals from observed mixture signals without having any prior knowledge of the mixing mechanism. The proposed approach first uses ICA to the forecasting variables for generating the independent components (ICs). After identifying and removing the ICs containing the noise, the rest of the ICs are then used to reconstruct the forecasting variables which contain less noise and served as the input variables of the SVR forecasting model. In order to evaluate the performance of the proposed approach, the Nikkei 225 opening index and TAIEX closing index are used as illustrative examples. Experimental results show that the proposed model outperforms the SVR model with non-filtered forecasting variables and a random walk model.
> - **Bibliography:** Lu, C.-J., Lee, T.-S., & Chiu, C.-C. (2009). Financial time series forecasting using independent component analysis and support vector regression. _Decision Support Systems_, _47_(2), 115–125. [https://doi.org/10.1016/j.dss.2009.02.001](https://doi.org/10.1016/j.dss.2009.02.001)
> - **Tags:** #Support-vector-regression, #SVR, #Financial-time-series-forecasting, #Independent-component-analysis, #Stock-index, #stock-forecasting, #modified-SVR, #🏷️, #time-series, #independent-component-analysis, #done-reading

## Executive Summary
%% begin summary %%
- *What is it about?*
- *What is great about this paper?*


%% end summary %%



## Highlights
%% begin annotations %%


### Imported: 2023-05-02 7:43 pm
- There has been growing interest in financial time series forecasting in recent years as accurate forecasting of financial prices/indices has become an important issue in investment decision making.

- However, **financial time series are inherently noisy and non-stationary** [19,64].The noise characteristic refers to the unavailability of complete information from past behavior of financial markets to fully capture the dependency between future and past prices. The information that is not included in the forecasting model is considered as noise while the non-stationary characteristic implies that the distribution of financial time series is changing over time. Therefore, financial time series forecasting is regarded as one of the most challenging tasks of time series forecasting.

- Neural networks have been found to be useful techniques for modeling financial time series due to their ability to capture subtle functional relationships among the empirical data even though the underlying relationships are unknown or hard to describe [34,3638,52,61,65,66].

- The most popular neural network training algorithm for financial forecasting is the backpropagation neural networks (BPN) that has a simple architecture but a powerful problem-solving ability. However, the BPN also suffers from a number of shortcomings such as the need for a large number of controlling parameters, difficulty in obtaining a stable solution and the risk of model over-fitting [7,8,55,56].

- Support vector machines (SVMs) is a novel neural network algorithm based on statistical learning theory [59,60]. It can lead to great potential and superior performance in practical applications. This is largely due to the structure risk minimization principles in SVMs, which has greater generalization ability and is superior to the empirical risk minimization principle as adopted by traditional neural networks. Due to the advantages of the generalization capability in obtaining a unique solution, the SVMs have drawn the attention of researchers and have been applied in many applications such as texture classification, image recognition, data mining and bioinformatics [6,14,22,31,40,44,46,50].

- With the introduction of Vapnik's εinsensitivity loss function, the regression model of SVMs, called support vector regression (SVR), has also been receiving increasing attention to solve nonlinear estimation problems [59,60]. It has been successfully applied in different problems of time series prediction

- Since there are many successful results of utilizing SVR in time series prediction, it motivates our research work by using SVR for financial time series forecasting.

- n the modeling of financial time series using SVR, one of the key problems is the inherent noise of the financial time series. Learning observations with noise without paying attention may lead to fitting those unwanted data and may torture the approximation function. This will result in the loss of generalization capability in the testing phase. Moreover, the noise in the data could lead to over-fitting or under-fitting problems [7,19]. Therefore, detecting and removing the noise are important but difficult tasks when building an SVR forecasting model. Few studies have been proposed to deflate the influence of noisy data and enhance the robust capability of SVR.

- Chuang et al. [15] proposed a robust support vector regression network. They used the concept of tradition robust statistics to fine tune the model obtained by SVR trying to reduce the overfitting phenomenon and improve the learning performance.

- Suykens et al. [53] presented a weighted version of least squares SVM (LS-SVM) to overcome the effects of outliers. In their approach, an LS-SVM was trained on the entire dataset for yielding the support values. A small fraction of the dataset associated with support values having the smallest magnitude are discarded and the LS-SVM retrained on the remaining data. This process is repeated until a sufficiently small kernel expansion is obtained.

- As the existing methods would either involve extensive computation or use additional parameters in SVR algorithm to reduce the effects of outliers/noise contained in the data. However, the consuming time of performing SVR algorithm will be increased while the extensive computation is carried out. When the parameters are not properly chosen, the final results may be affected by its parameters. Moreover, the selection of parameters is not straightforward.

- To avoid the limitations of the existing method and reduce the influenceofnoise,atwo-stageapproach by combining independent component analysis (ICA) and support vector regression is proposed in this research for modeling financial time series.

- ICA is a novel statistical signal processing technique to find independent sources given only observed data that are mixtures of unknown sources without any prior knowledge of the mixing mechanism [25,35].

- In the basic ICA model, the observed mixture signals X can be expressed as X = AS, where A is an unknown mixing matrix and S represents the latent source signals that cannot be directly observed from the mixture signals X. The ICA model describes how the observed mixture signals are generated by a process that uses the mixing matrix A to linearly mix the latent source signals S. The source signals are assumed to be mutually statistically independent. Based on this assumption, the ICA solution is obtained in an unsupervised learning process that finds a de-mixing matrix W. The de-mixing matrix W is used to transform the observed mixture signals X to yield the independent signals Y, i.e., WX = Y. The independent signals Y are then used as the estimates of the latent source signals S. The rows of Y, called independent components (ICs), are required to be as mutually independent as possible. Even though the basic ICA model has been widely applied in signal processing, face recognition, feature extraction and quality control [3,17,28,29,32,43,42,58], there are still few applications using ICA in financial time series forecasting.

- Back and Weigend [1] used ICA to exact the features of the daily returns of the 28 largest Japanese stocks. The results showed that the dominant ICs can reveal more underlying structure and information of the stock prices than principal component analysis.

- Kiviluoto and Oja [33] employed ICA to find the fundamental factors affecting the cash flow of 40 stores in the same retail chain. They found that the cash flow of the retail stores was mainly affected by holidays, seasons and competitors' strategies.

- There are only very few articles addressing both ICA and SVR in conducting forecasting tasks. Cao and Chong [9] employed ICA as a feature extraction tool in developing a SVM forecaster. The independent components (ICs) were considered as features of the forecasting data and used to build the SVM forecasting model.

- Chen et al. [11] combined dynamic independent component analysis (DICA) with SVR to construct multi-layer support vector regression model. The DICA was used in the first layer to extract the major dynamic features from the process. The second layer is the SVR that makes the regression estimation based the extracted features.

- Hou et al. [21] applied ICA and SVR in near-infrared (NIR) spectral analysis. They used ICA to extract the independent components and corresponding mixing matrix from the NIR spectra of chemical components, then the SVR was used to build a model between mixing matrix and the real concentration matrix of chemical components for spectral analysis.

- Wang et al. [62] utilized kernel independent component analysis and SVR for the estimation of source ultraviolet spectra profiles and simultaneous determination of polycomponents in mixtures. They applied ICA to estimate the ultraviolet source spectra profiles. Then, the calibration model was build by using SVR based on the mixing matrix.

- In this study, we present a financial time series forecasting model by integrating ICA and SVR. The ICA method is used to detect and remove the noise of financial time series data and further improve the performance of SVR. The proposed approach first uses ICA to the forecasting variables to estimate the independent components and mixing matrix. Since the financial time series are inherently noisy, at least one IC can be used to represent noise information of the data. After identifying and removing the ICs containing the noise, the rest of the ICs are then used to reconstruct the forecasting variables which contain less noise. The SVR then uses the filtered (or de-noised) forecasting variables to build the forecasting model. In order to evaluate the performance of the proposed approach, the Nikkei 225 opening cash index and TAIEX (Taiwan Stock Exchange Capitalization Weighted Stock Index) closing cash index are used as the illustrative examples.

- 2. Independent component analysis

- 3. Support vector regression

- 4. Proposed forecasting model using ICA and SVR

- For the proposed two-stage forecasting method, ICA is first applied to filter out the noise contained in forecasting variables. The filtered forecasting variables are then used in SVR for constructing a forecasting model.

- 5. Empirical study

- 5.1. Datasets and performance criteria

- In forecasting Nikkei 225 opening cash index, the Nikkei 225 index futures prices are used as forecasting variables since the futures price changes lead price changes of the cash market [36,37]. Using the leading futures as forecasting variables should contribute to the success in increasing the forecasting accuracy. There are three Nikkei 255 index futures contracts traded on SGX-DT (Singapore ExchangeDerivative Trading Limited), OSE (Osaka Securities Exchange) and CME (Chicago Mercantile Exchange) markets. The previous day's cash market closing index is also an important variable for predicting the cash market opening price [36,37]. Therefore, four forecasting variables are used for predicting the Nikkei 225 opening cash index. The daily data of futures and cash prices from October 4, 1999 to September 30, 2004 of the Nikkei 225 cash index provided by Bloomberg are collected in this study. There are totally 1144 data points in the dataset and the daily Nikkei 225 opening cash prices are shown in Fig. 5. The first 794 data points (69.41% of the total sample points) are used as the training sample while the remaining 350 data points (30.59% of the total sample points) are used as the testing sample.

- For forecasting the TAIEX closing cash index, the TAIEX index futures prices and technical indicators are used as forecasting variables since technical indicators are the most widely used features in financial time series prediction [2,39]. There are two TAIEX index future contracts traded on SGX-DT and TAIFEX (Taiwan Futures Exchange) markets. The seven technical indicators, determined by the review of domain experts and literatures [39,63], are selected as forecasting variables for predicting the TAIEX closing cash index.

- Thus, 9 forecasting variables are used for TAIEX closing cash index forecasting. The daily data of futures, technical indicators, and cash prices from January 2, 2003 to February 27, 2006 of the TAIEX cash index provided by Capital Futures Corporation, Taipei, are collected as a dataset. The daily TAIEX closing cash prices in the TAIEX dataset are depicted in Fig. 6. There are totally 781 data points in the dataset. The first 546 data points (69.90% of the total sample points) are used as the training sample and the remaining 235 data points (30.10% of the total sample points) are used as testing sample.

- The prediction performance is evaluated using the following performance measures, namely, the root mean square error (RMSE), normalized mean square error (NMSE), mean absolute difference (MAD), directional Symmetry (DS), correct up trend (CP) and correct down trend (CD).

- RMSE, NMSE and MAD are measures of the deviation between actual and predicted values. The smaller values of RMSE, NMSE and MAD, the closer are the predicted time series values to that of the actual value. They can be used to evaluate the prediction error. DS provides the correctness of the predicted direction of the cash index in terms of percentage. CP and CD provide the correctness of the predicted up trend and predicted down trend of the cash index in terms of percentage. DS, CP and CD can be utilized to evaluate the prediction accuracy

- 5.2. Forecasting results of Nikkei 225 and TAIEX cash prices

- The forecasting results of the proposed ICA–SVR model are compared to the SVR model using non-filtered forecasting variables (called single SVR model) and the random work model simply uses the previous day's price to predict today's price.

- For building SVR forecasting model, the LIBSVM package proposed by Chang and Lin [10] is adapted in this study. The original datasets are first scaled into the range of [−1.0, 1.0] when using LIBSVM package. The purpose of doing so is to ensure that large value input variables do not overwhelm smaller value inputs, thus helping to reduce prediction errors.

- In the selection of parameters for modeling SVR, C =1.25 and ε= 0.0019 can be obtained by the analytic approach mentioned in Section 4. Since C=1.25 is near C=21 and ε=0.0019 is close to ε=2−9,the parameter set (C=21, ε=2−9)isusedasthestartingpointofgridsearch for searching the best parameters. The testing results of the SVR model with combinations of different parameter sets are summarized in Table 3.

- From Table 3,itcanbefoundthattheparameterset(C=21, ε=2−11) gives the best forecasting result (minimum testing MSE) and is the best parametersetforSVRmodelinforecastingNikkei225openingcashindex.

- In the modeling of the proposed ICA–SVR model, the noise of four forecasting variables should be removed first using ICA approach. As the four forecasting variables are the time series discussed and expressed in Fig. 2, the noise removing process and results have been discussed in Section 4. After using ICA to filter out the noise of the four forecasting variables, the de-noised forecasting variables are then used for building the SVR forecasting model. Using the same process when building the SVR model, the parameter set (C =21, ε =2− 9) obtained by the analytic method is used as the starting point of grid search.

- It can be observed from Table 4 that the parameter set (C =23, ε =2− 7) gives the best forecasting result and hence is the best parameter setup for the proposed ICA–SVR model in forecasting Nikkei 225 opening cash index.

- Moreover, compared to the random walk and SVR models, the ICA–SVR model has the highest DS (directional Symmetry), CP (correct up trend) and CD (correct down trend) ratios which are 87.53%, 88.77% and 86.09%, respectively. DS, CP and CD provide a good measure of the consistency in prediction of the price direction. Thus, it can be concluded that the proposed ICA–SVR model provides a better forecasting result than the random walk and SVR models in terms of prediction error and prediction accuracy.

- The actual Nikkei 225 opening cash price values and predicted values from the random walk, SVR and ICA–SVR models are illustrated in Fig. 7. Note that, to save space, the last 50 data points of the Nikkei 255 index in Fig. 5 are used as illustrative example and shown in Fig. 7. It can be observed from Fig. 7 that the predicted values obtained from the proposed ICA–SVR model are closer to the actual values than those of random walk and SVR models.

- The proposed ICA–SVR method also performs well in forecasting the TAIEX closing cash prices. Table 6 summarizes the TAIEX closing cash prices forecasting results using random walk, SVR and ICA–SVR models. It can also be observed from Table 6 that the proposed ICASVR model has the smallest RMSE, NMSE and MAD values and the highest DS, CP and CD values in comparison with random walk and SVR models. Thus, the proposed method can produce lower prediction errors and higher prediction accuracy on the direction of change in price and outperforms random walk and SVR models in forecasting of the TAIEX closing cash prices.

- 5.3. Robustness evaluation

- To evaluate the robustness of the proposed ICA–SVR method, the performance of the random walk, SVR and proposed models was tested using different ratios of training and testing sample sizes. The testing plan is based on the relative ratio of the size of the training dataset size to complete dataset size. In this section, four relative ratios, 60, 70, 80, and 90% are considered. The prediction results for the Nikkei 225 opening cash index and TAIEX closing cash index by the three methods are summarized in Table 7 in terms of two criteria, RMSE and directional Symmetry (DS).

- Based on the findings in Table 7, it can be observed that the proposed ICA–SVR method outperforms the other benchmarking tools under all four different ratios in terms of the RMSE and DS criteria. It therefore indicates that ICA–SVR based approach indeed provides better forecasting accuracy than the other two approaches. Nevertheless, under a ratio of only 60%, the proposed ICA–SVR based approach can still provide reasonably good forecasting results (DS higher than 80%). The proposed method can effectively detect and remove the noise from financial time series data and improve the forecasting performance of SVR.

- 5.4. Significance test

- In order to test whether the proposed ICA–SVR model is superior to the single SVR and random walk models in financial time series forecasting, the Wilcoxon signed-rank test is applied. The test is a distribution-free, non-parametric technique that does not require any underlying distributions in the data, and deals with the signs and ranks of the values and not with their magnitude (thus not influenced by outlier data points). It is one of the most commonly adopted tests in evaluating the predictive capabilities of two different models to see whether they are statistically significant difference between them [18,27,49,51,54,65]

- We employ the test to evaluate the predictive performance of the three built models under different ratios of the size of the training data set to complete data set. Table 8 presents the Z statistic values of the two-tailed Wilcoxon signed-rank test for RMSE values between the proposed ICA–SVR model and other two models, where the numbers in parentheses are the corresponding p-values. It can be observed from Table 8, under different ratios of training sample dataset size to the complete dataset size, that the RMSE values of the proposed ICASVR model is significantly different from the SVR and random models.

- 6. Conclusions

- This paper proposed a two-stage forecasting model by integrating ICA and SVR for financial time series. The proposed ICA–SVR method first uses ICA based on reconstruction criterion to remove the noise from forecasting variables since the financial time series data is inherently noisy. The noise in the data could lead to an over-fitting or under-fitting problem.

- The filtered forecasting variables containing less noise information are then used in SVR for building forecasting model. The experiments have evaluated two datasets including the Nikkei 225 opening cash index and the TAIEX closing cash index. This study compared the proposed method with traditional SVR and random walk models using prediction error and prediction accuracy as criteria.

- Experimental results showed that the proposed model can produce lower prediction error and higher prediction accuracy and outperformed the SVR and random walk models. According to the experiments, it can be concluded that the proposed method can effectively detect and remove the noise from financial time series data and improve the forecasting performance of SVR.

- Future researches may aim at combining ICA and other forecasting tools, like neural networks and grey system theory, in evaluating the ability of the proposed de-noise forecasting scheme. Integrating SVR and other signal processing techniques, like wavelet transform and nonnegative matrix factorization, in further improving the forecasting capabilities can also be investigated in future studies.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-05-02T19:43:11.474+08:00 %%
