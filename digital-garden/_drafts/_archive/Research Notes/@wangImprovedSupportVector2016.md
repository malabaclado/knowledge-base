---
tags: type/research-note 
alias: [Improved v -Support vector regression model based on variable selection and brain storm optimization for stock price forecasting]
---
# Improved v -Support vector regression model based on variable selection and brain storm optimization for stock price forecasting

> [!info]
> - **Cite Key:** [[@wangImprovedSupportVector2016]]
> - **Abstract:** Big data mining, analysis and forecasting always play a vital role in modern economic and industrial fields, and selecting an optimization model to improve time series’ forecasting accuracy is challenging. A support vector regression (SVR) model is widely used forecasting and data processing, but the individual SVR cannot always satisfy the requirements of time series forecasting. In this paper, a hybrid v-SVR model is developed and combined with principal component analysis (PCA) and brain storm optimization (BSO) for stock price index forecasting. Correlation analysis and PCA are conducted initially to select the input variables of the v-SVR from 20 technical indicators, while the advanced BSO algorithm is used to search for optimal parameters of v-SVR. Case studies of the China Securities Index 300 (CSI300) and the Shenzhen Stock Exchange Component Index (SZSE Component Index) are examined as illustrative examples to evaluate the effectiveness and efficiency of the developed hybrid forecast strategy. Numerical results indicate that the developed hybrid model is not only simple but also able to satisfactorily approximate the actual CSI300stock price index, and it can be an effective tool in stock market mining and analysis.
> - **Bibliography:** Wang, J., Hou, R., Wang, C., & Shen, L. (2016). Improved v -Support vector regression model based on variable selection and brain storm optimization for stock price forecasting. _Applied Soft Computing_, _49_, 164–178. [https://doi.org/10.1016/j.asoc.2016.07.024](https://doi.org/10.1016/j.asoc.2016.07.024)
> - **Tags:** #-Support-vector-regression, #Brain-storm-optimization, #Data-pre-analysis, #Forecasting-validity, #Stock-price-index, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- 1. Introduction

- Regarded as one of the most challenging tasks of the financial arena, stock price forecasting attracts the interest of many researchers.

- Various algorithms and models have been devoted to this hot issue, such as fuzzy time series [1][2], Bayesian network[3], and wavelet de-noising-based back propagation neural network[4].

- Egrioglu [5] proposed the high order time invariant fuzzy time series method integrated with artificial intelligence techniques, applied it to stock index time series and demonstrated that the proposed method performed better than other methods in the literature.

- A new hybrid fuzzy time-series approach[6] with fuzzy c-means clustering procedure and feed-forward neural networks was employed to conduct empirical analysis on the Istanbul stock market and exhibited the best forecasting accuracy performance, according to some error criteria

- In the literature, it has been verified that conventional modeling techniques, such as the Box-Jenkins autoregressive integrated moving average (ARIMA), are not adequate for stock market price forecasting[7].

- Thus, in this paper, we construct a novel hybrid model based on -support vector regression ( -SVR), principal component analysis (PCA) and brain storm optimization (BSO) algorithm for stock price forecasting.

- As the literature supports the implementation of structural risk minimization[7]in an effort to attain high forecast accuracy, integrated support vector regression (SVR) models draw great attention from researchers of stock price forecasting.

- For example, Kao et al.[10]constructed a hybrid model integrating wavelet transform, multivariate adaptive regression splines and SVR, and the empirical study showed that the proposed model not only addressed the problem of wavelet sub-series selection but also improved the forecasting accuracy. The authors [10]believed that the first step of a model construction for stock price forecasting is usually feature extraction, or variable selection, and many studies validated this point because of the non-stationary and chaotic properties of the stock index data. For example, nonlinear independent component analysis has been integrated with support vector regression because feature extraction can discover valuable information hidden in the original data[11].

- Artificial neural network models[12][13][14] have been used in the field of stock price forecasting for the absence of restrictive assumptions such as linearity and normal distribution. However, they suffer from local minimum traps and over-fitting problems because of the empirical risk minimization principle, difficulty in determining the network structure, hidden layer size and learning rate[15].

- On the contrary, SVR has a global optimum and exhibits better prediction accuracy for its structural risk minimization principle. It considers both the training error and the capacity of the regression model to avoid under-fitting and over-fitting problems in the training process.

- However, in the literature, the original form of SVR, namely -SVR , has been widely used, while the updated version -SVR still deserves further investigation. Thus, this work mainly focuses on the feasible improvements of conventional -SVR and its application.

- The research of Xiong et al.[16]also indicated that the selection of optimal parameters is crucial to obtain satisfactory forecast performance because the generalization ability of the support vector regression models depends on adequately tuning parameters, such as the penalty coefficient C and kernel parameters.

- Up to now, many evolutionary algorithms, such as differential evolution[17], firefly algorithm[16], genetic algorithm[18], and particle swarm optimization[19], have been employed to efficiently tune and optimize the parameters of SVR in order to improve the forecast accuracy.

- Taking into account the discussion above, this paper focuses on two issues: selecting appropriate input variables and searching for optimized parameters for -SVR.

- For the first issue, several statistical techniques, including standardization, Pearson’s correlation coefficient and principal component analysis, are employed to preprocess the original stock index related data and determine the input variables of -SVR.

- Specifically, principal component analysis (PCA) is a multivariate statistical technique implemented to reduce dimensionality and to extract characteristic features from the original dataset. Recent works in different fields such as chemistry, renewable energy, material and medical science have already indicated the effectiveness of this data preprocessing method. For example, PCA algorithm was implemented by Segreto et al.[20]to extract characteristic features from acquired sensor signals in experimental cutting tests on C45 carbon steel turning for pattern recognition. Skittides and Früh[21] regarded principal component analysis as a statistical tool for wind speed forecasting using an ensemble of dynamically similar past events. Moreover, Gu et al. applied the Taguchi method and principal component analysis to improve the mechanical properties of recycled polypropylene blends in an injection molding procedure. Kobayashi et al.[23]analyzed the sampled joint kinematics data using principal component analysis to identify the key joint kinematic characteristics of human gait related to the risk of falling.

- As for the second issue in this paper, brain storm optimization (BSO) is initially utilized for parameter optimization in the training process of -SVR.

- Proposed by Shi in 2011[24], BSO is a novel swarm intelligence algorithm inspired by the social and swarm behaviors of more intelligent organisms, e.g., the human being[25]. The superiority of the BSO against other evolutionary computation algorithms is that BSO emulates the brainstorming process of the most intelligent animal in the world (human being) instead of the swarm behaviors and biological evolution of other simple creatures, such as ants in ant colony optimization (ACO), birds in particle swarm optimization (PSO), bees in honey bee optimization (HBO), and bacteria in bacterial forging optimization (BFO). In practice, the usefulness and effectiveness of BSO in solving optimization problems have been validated by the simulation results of typical benchmark functions[26].

- However, to the best of our knowledge, the BSO algorithm has not yet been integrated with -SVR model in the field of stock price forecasting. The existing studies motivate us to use the BSO for selecting parameters for the -SVR model. Therefore, in this paper, a hybrid improved -SVR model coupled with PCA and BSO is proposed for stock price forecasting.

- This paper contributes to the existing support vector machine and CSI300 stock price forecasting literature in the following three aspects. First, although stock price forecasting has always attracted much research interest, the combined research on statistical learning theory and artificial intelligence still deserves further exploration.

- This is the first study to propose a modified -SVR model based on data pre-analysis and the advanced parameter optimization technique, namely BSO. Secondly, the hyper parameters in the original -SVR model are determined by the empirical trail-and-error process or expert experience, which consumes time and limits the generalization ability of SVR. However, simulation results of this paper suggest that the BSO technique can efficiently solve this problem, provide optimal parameters for -SVR and further improve the forecasting accuracy of stock price data. Third, two typical performance benchmarks of the Chinese stock market, namely, the China Securities Index 300 (CSI300) and the Shenzhen Stock Exchange Component Index (SZSE Component Index), are investigated in this research, and as many as 20 related technical indicators are involved in the model construction process. This paper highlights the input variable selection process and extracts the most representative information from an original high-dimensional dataset. Lastly, from the aspects of both forecasting accuracy and calculative efficiency, the proposed hybrid forecast strategy is compared with other existing -SVR related approaches in the literature, such as -SVR with default parameters and grid search algorithm-based -SVR as well as -SVR integrated with particle swarm optimization algorithm. To test the model’s performance, two case studies concerning the Chinese stock market are conducted, and the simulation results clearly indicate the superiority of the hybrid forecasting model developed in this research.

- 2. Related methodology

- 2.1 Data pre-analysis

- 2.2  -support vector regression

- v-SVR[32] is a new class of promising non-linear kernel-based regression method that aims to find the best regression hyper plane with the smallest structural risk in a high dimensional feature space[7][33].

- 2.3 Brain storm optimization

- First proposed by Shi in 2011[24], the BSO algorithm is inspired by the human brainstorming process that has been successfully applied to generate ideas to solve difficult and challenging problems. As human beings are the most intelligent animals in the world, the BSO algorithm based on the idea generation process of human beings should outperform the optimization algorithms inspired by the collective behaviors of other animals such as ants and birds[25-26].

- For the kernel function of the -SVR, the linear kernel function, polynomial kernel function, radial basis kernel function and sigmoid function are the most commonly used.

- The width of the radial basis function is the same in all kernel functions, and can reflect the corresponding width of the inner product kernel for input. If is too small, it will lead to over fitting or memory of the training group. If is too large, -SVR’s discriminant function will be too gentle.

- he width of kernel function and the penalty coefficient C affect the shape of prediction curve of the support vector machine from different angles. In practical applications, too large or too small penalty coefficient C and kernel function will worsen the generalization performance of the support vector machine.

- 3. Case Study Results

- 3.1 Case study of CSI300 forecasting

- The China Securities Index 300 (CSI300) consists of 300 stocks with the largest market capitalization and liquidity from the listed A share companies in China

- In this paper, 160 groups ofCSI300related indicators, sampled from April 20, 2011 to December 9, 2011, constituted the original data set, and the opening price of CSI300was forecasted one day ahead. Twenty indicators of technical analysis are initially selected for the forecasting task and illustrated in Table 1.

- First, all collected data are standardized as mentioned in Section 2.1, and the correlation coefficients between the 20 indicators of the current day and the opening CSI300 price of the next day are calculated to remove indicators with low correlation. The coefficients are listed in Table 2.

- As demonstrated in Table 2, a total of seven indicators of the current day, including change amount, change ratio, MACD, KDJ.K, KDJ.D, RSI6 and BIAS6, exhibit weak relationships with the opening price of the next day, as the calculated correlation coefficients are no more than 0.3428. Thus, these technical indicators are excluded from further forecasting model construction.

- For the remaining 13 indicators, PCA is performed to reduce the numbers of variables and extract characteristic information. Table 3 and Table 4 present total variance explained and component matrix obtained from the procedure of PCA, respectively.

- According to the results of PCA shown in Table 3 and Table 4, four principal components are generated that can explain 97.12% of total variance.

- From Table 5, we can conclude that the calculation time of -SVR-BSO is much less than those of -SVR-GS and -SVR-PSO, which indicates that the BSO algorithm is much more efficient than GS and PSO when combined with -SVR. Especially, -SVR-BSO costs roughly one-tenth the time of -SVR-GS or one-third the time of -SVR-PSO, which is a remarkable advantage in practice. Next, the four types of -SVR-related models are trained, and the training results are shown in Table 6.

- From Table 8, we can see that compared with the original -SVR model, the other three models incorporating parameter optimization algorithms achieve much lower forecasting errors. Thus, it is necessary to enhance the forecasting performance of the original -SVR model using parameter optimization process, for it is capable of significantly decreasing forecasting errors.

- In conclusion, when both calculation time and forecasting accuracy are comprehensively considered, we confirm that the -SVR-BSO model is superior to -SVR-GS, as it greatly reduces computational complexity, which is a meaningful improvement in a world of big data.

- 3.2 Case study of SZSE Component Index forecasting

- To enhance the robustness of our conclusion, another case study regarding Shenzhen Stock Exchange Component Index (SZSE Component Index) is further conducted. The constituents of SZSE Component Index are 40 selected stocks traded at the Shenzhen Stock Exchange, China.

- 3.3 Forecasting validity assessment and analysis

- The validity index of the forecasting method, introduced in [39-40], defines the normal forecasting validity degree based on the invalid degree element with k-order forecasting fractional error.

- 4. Conclusions

- In this paper, a hybrid -SVR model based on PCA and BSO is proposed forCSI300 stock price forecasting. This research suggests that the original -SVR model can be improved in the following two aspects. Data preprocessing techniques such as correlation analysis and PCA are employed to select appropriate variables for a primitive -SVR model. Additionally, BSO is for the first time integrated with a -SVR model for the purpose of parameter optimization. Case studies of the CSI300 Index and the SZSE Component Index of China are conducted to demonstrate the superiority and robustness of the novel hybrid model. Our findings contribute to several scientific conclusions as follows

- First, the proposed hybrid model is effective and efficient for stock index forecasting, considering both forecasting accuracy and calculation time consumed by the parameter optimization process.

- Moreover, the experimental results also suggest that, in contrast to -SVR with default parameters, hybrid -SVR models integrated with parameter optimization algorithms obtain much lower forecasting errors.

- Finally, this study indicates the feasibility of combining statistical learning theory with meta-heuristic global optimization algorithms to achieve better forecasting performance. The research ideas and improved -SVR forecasting model proposed in this paper may provide meaningful reference for other forecasting tasks.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:46.966+08:00 %%
