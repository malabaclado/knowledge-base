
Lecture 02 | [[Math 150.2 MOC]]
Date: March 4, 2021

[[math150.2_notes2018.pdf | Math 150.2 Course Notes]] ^c3cf56


---


==Statistical Inference== refers to the process of drawing conclusions about a population based on the data obtained from a sample chosen from it.



> ==Definition== (Random Sample)
> A **random sample of size n** is a set of n random variables $X_1,X_2,...,X_n$ that are ==independent and identically distributed==.

> ==Definition== (Statistic and Realization)
> Let $X_1,X_2,...,X_n$ be a random sample. A function $T(X_1,X_2,...,X_n)$ of this random sample is called a **statistic**. Moreover, once a function is drawn, the value $t=T(x_1,x_2,...,x_n)$ is called the **realization** of T.

Note that uppercase $X_i$ denote the random variable while lowercase $x_i$ denotes the realized value of that variable.

> ==Definition== (Sampling Distribution)
> A** sampling distribution **is a probability distribution of a statistic T obtained through a large number of samples drawn from a specific population.

The sampling distribution may be characterized through the mean and variance. This was summarized by Theorem 4 and Theorem 5 in [[Sampling Distributions#^c3cf56 | Course Notes]].

> ==Definition== (Unbiased Estimator)
> Let $X$ be a random variable with distribution $f(x;\theta)$. Let $X_1,X_2,...,X_n$ be a random sample and $T$ be a statistic. 
> 
> We say $T$ is an **unbiased estimator** if $$E[T]=\theta$$ for all $\theta \in \Omega$. Otherwise, it is called to be biased.

Sample Mean $$\bar{X}=\frac{1}{n}\sum_{i=1}^n  X_i$$

Sample Variance $$S^2=\frac{1}{n-1} \sum_{i=1}^n(X_i-\bar{X})$$

---
## Common Distributions from Normal Distribution
- Chi-Square Distribution
- Student's t-Distribution
- F Distribution



---
## Order Statistics

---



## Limit Theorems
