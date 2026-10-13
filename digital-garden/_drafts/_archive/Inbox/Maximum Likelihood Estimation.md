---
tags: molecule
alias: MLE
creation-date: Monday 1st August 2022
last-modified-date: Monday 1st August 2022 06:43:31
---

# Maximum Likelihood Estimation
**Maximum Likelihood Estimation** is a process of estimating a parameter from a sample, given that you have an idea about its population distribution. 

**Statement of the Problem**
Suppose we have a random sample $X_1,X_2,...,X_n$ whose assumed probability distribution depends on some unknown parameter $\theta$. The goal is to find a point estimator for the parameters $\theta$.

**Example**
Suppose we have a random sample $X_{1,}X_2,...,X_n$ for which $X_i$ is assumed to be normally distributed with mean $\mu$ and variance $\sigma^2$, then our goal will be to find a good estimate of $\mu$, using the data $x_1,x_2,...,x_n$ obtained from the random sample. 

**The main idea**
It is reasonable that a good estimate of the unknown parameter would be the value that **maximizes** the probability (or the likelihood) of having the data that we observed. This is why it is called "maximum likelihood" method. 

Suppose we have a random sample $X_1,X_2,...,X_n$ for which the probability function of each $X_i$ is $f(x|\theta)$. Then the joint probability function of the random sample $X_1,X_2,...,X_n$, which we'll call $L(\theta)$ is: $$\begin{align*}
L(\theta)&= P(X_1=x_1,X_2=x_2,...,X_n=x_n)\\
&= f(x_{1}|\theta)\cdot f(x_{2}|\theta)\cdot \cdot \cdot f(x_{n}|\theta) 
\end{align*}$$
The second line of the equation comes from the fact that we have a random sample which implies that the $X_{i}$ are independent. 

Now, we wish to find the parameters $\theta$ that maximizes the likelihood function $L(\theta)$. Usually, it ismore practical to find the maximum of the log-likelihood function since it is easier to differentiate. 

---
Check this great resource: [1.2 - Maximum Likelihood Estimation | STAT 415 (psu.edu)](https://online.stat.psu.edu/stat415/lesson/1/1.2) 