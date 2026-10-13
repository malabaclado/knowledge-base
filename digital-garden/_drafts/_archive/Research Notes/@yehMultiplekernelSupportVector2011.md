---
tags: type/research-note 
alias: [A multiple-kernel support vector regression approach for stock market price forecasting]
---
# A multiple-kernel support vector regression approach for stock market price forecasting

> [!info]
> - **Cite Key:** [[@yehMultiplekernelSupportVector2011]]
> - **Abstract:** Support vector regression has been applied to stock market forecasting problems. However, it is usually needed to tune manually the hyperparameters of the kernel functions. Multiple-kernel learning was developed to deal with this problem, by which the kernel matrix weights and Lagrange multipliers can be simultaneously derived through semidefinite programming. However, the amount of time and space required is very demanding. We develop a two-stage multiple-kernel learning algorithm by incorporating sequential minimal optimization and the gradient projection method. By this algorithm, advantages from different hyperparameter settings can be combined and overall system performance can be improved. Besides, the user need not specify the hyperparameter settings in advance, and trial-and-error for determining appropriate hyperparameter settings can then be avoided. Experimental results, obtained by running on datasets taken from Taiwan Capitalization Weighted Stock Index, show that our method performs better than other methods.
> - **Bibliography:** Yeh, C.-Y., Huang, C.-W., & Lee, S.-J. (2011). A multiple-kernel support vector regression approach for stock market price forecasting. _Expert Systems with Applications_, _38_(3), 2177–2186. [https://doi.org/10.1016/j.eswa.2010.08.004](https://doi.org/10.1016/j.eswa.2010.08.004)
> - **Tags:** #Support-vector-regression, #done-reading, #Gradient-projection, #Multiple-kernel-learning, #SMO, #Stock-market-forecasting, #done



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- 1. Introduction

- Accurate forecasting of stock prices is an appealing yet difficult activity in the modern business world. Many factors influence the behavior of the stock market, including both economic and noneconomic. Therefore, stock market forecasting is regarded as one of the most challenging topics in business.

- In the past, methods based on statistics were proposed for tackling this problem, such as the autoregressive (AR) model (Champernowne, 1948), the autoregressive moving average (ARMA) model (Box & Jenkins, 1994), and the autoregressive integrated moving average (ARIMA) model (Box & Jenkins, 1994). These are linear models which are, more than often, inadequate for stock market forecasting, since stock time series are inherently noisy and non-stationary.

- Recently, nonlinear approaches have been proposed, such as autoregressive conditional heteroskedasticity (ARCH) (Engle, 1982), generalized autoregressive conditional heteroskedasticity (GARCH) (Bollerslev, 1986), artificial neural networks (ANN) (Hansen & Nelson, 1997; Kim & Han, 2008; Kwon & Moon, 2007; Qi & Zhang, 2008; Zhang & Zhou, 2004), fuzzy neural networks (FNN) (Chang & Liu, 2008; Oh, Pedrycz, & Park, 2006; Zarandi, Rezaee, Turksen, & Neshat, 2009), and support vector regression

- ANN has been widely used for modeling stock market time series due to its universal approximation property (Kecman, 2001). Previous researchers indicated that ANN, which implements the empirical risk minimization principle, outperforms traditional statistical models (Hansen & Nelson, 1997). However, ANN suffers from local minimum traps and difficulty in determining the hidden layer size and learning rate.

- On the contrary, SVR, proposed by Vapnik and his co-workers, has a global optimum and exhibits better prediction accuracy due to its implementation of the structural risk minimization principle which considers both the training error and the capacity of the regression model (Cristianini & Shawe-Taylor, 2000; Vapnik, 1995). However, the practitioner has to determine in advance the type of kernel function and the associated kernel hyperparameters for SVR. Unsuitably chosen kernel functions or hyperparameter settings may lead to significantly poor performance (Chapelle, Vapnik, Bousquet, & Mukherjee, 2002; Duan, Keerthi, & Poo, 2003; Kwok, 2000).

- Most researchers use trial-and-error to choose proper values for the hyperparameters, which obviously takes a lot of efforts. In addition, using a single kernel may not be sufficient to solve a complex problem satisfactorily, especially for stock market forecasting problems. Several researchers have adopted multiple-kernels to deal with these problems

- We propose a regression model, which integrates multiple-kernel learning and SVR, to deal with the stock price forecasting problem. A two-stage multiple-kernel learning algorithm is developed to optimally combine multiple-kernel matrices for SVR. This learning algorithm applies SMO (Platt, 1999) and the gradient projection method (Bertsekas, 1999) iteratively to obtain Lagrange multipliers and optimal kernel weights. By this algorithm, advantages from different hyperparameter settings can be combined and overall system performance can be improved. Besides, the user need not specify the hyperparameter settings in advance, and trial-and-error for determining appropriate hyperparameter settings can then be avoided. Experimental results, obtained by running on datasets taken from Taiwan Capitalization Weighted Stock Index (TAIEX), which is a stock market index for companies traded on the Taiwan Stock Exchange, show that our method performs better than other methods.

- 3. Proposed method

- 3.1. Multiple-kernel support vector regression

- The SVR method presented earlier uses a single mapping function /, and hence a single kernel function K. If a dataset has a locally varying distribution, using a single kernel may not catch up the varying distribution very well. Kernel fusion can help to deal with this problem. Instead of using one single mapping function, several mapping functions are combined to do aggregate mapping

- 3.2. Two-stage multi-kernel learning

- We develop a two-stage optimization algorithm for solving Eq. (9). The algorithm consists of two-stages in which SMO and gradient projection are applied, respectively.

- 4. Experimental results

- To test the forecasting performance of our proposed method, we have conducted three experiments on the datasets taken from Taiwan Capitalization Weighted Stock Index (TAIEX). We also compare the performance of our proposed method with that of other methods, i.e., single kernel support vector regression (SKSVR) (Tay & Cao, 2001), autoregressive integrated moving average (ARIMA) model (Box & Jenkins, 1994), and TSK type fuzzy neural network (FNN) (Chang & Liu, 2008). For convenience, we abbreviate our multiple-kernel support vector regression method as MKSVR.

- First of all, we compare the performance of MKSVR with that of SKSVR. In this experiment, the daily stock closing prices of TAIEX for the period of October 2002 to December 2005 are used, and a one-season moving-window testing approach is used for generating the training/validating/testing data.

- Four datasets, DS-I to DSIV, are formed, following the way done in Tay and Cao (2001). For instance, DS-I contains the daily stock closing prices from October 2002 to September 2004 selected as training dataset, the daily stock closing prices from October 2004 to December 2004 selected as validating dataset, and the daily stock closing prices from January 2005 to March 2005 selected as testing dataset. The corresponding time periods for DS-I to DS-IV are listed in Table 1.

- 5. Conclusion

- We have proposed a multiple-kernel support vector regression approach for stock market price forecasting. A two-stage multiple-kernel learning algorithm is developed to optimally combine multiple-kernel matrices for support vector regression. The learning algorithm applies sequential minimal optimization and gradient projection iteratively to obtain Lagrange multipliers and optimal kernel weights. By this algorithm, advantages from different hyperparameter settings can be combined and overall system performance can be improved. Besides, the user need not specify the hyperparameter settings in advance, and trial-and-error for determining appropriate hyperparameter settings can then be avoided. Experimental results, obtained by running on datasets taken from Taiwan Capitalization Weighted Stock Index, have shown that our method performs better than other methods.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:47.107+08:00 %%
