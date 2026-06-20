---
tags: #math150p2 #MathStat 
---

Point estimation refers to estimating a set of k parameters from a random sample $X_1,X_2,..,X_n$ with probability density function $f(x;\theta)$.
We currently know two methods: the method of moments and the maximum likelihood methods.

## Method of Moments
Let $f(x;\theta_1,\theta_2,..,\theta_k)$ be the probability density function of the random variable X with k parameters. Let $\mu'_x$ denote the rth raw moment. Let $X_1, X_2,...,X_n$ be a random sample derived from the distribution and $M'_j$ be the jth sample moment.
<!--ID: 1619312064447-->



==Process==
- Form the system of k equations: $$M'_j=\mu'_j(\theta_1,\theta_2,...,\theta_k)$$
- Solve the system and the resulting solution $(\hat{\theta}_1,\hat{\theta}_2,..,\hat{\theta}_k)$  is the estimator obtained by the method of moments.

---
## Maximum Likelihood Methods
> ==Definition== (Likelihood Function)
> Define the likellihood function as: $$L(\theta)=\prod^n_{i=1}f(x;\theta)$$
> in logarithmic form: $$l(\theta)=ln L(\theta) = \sum^n_{i=1}lnf(x;\theta)$$
<!--ID: 1619312064502-->


> ==Definition== (Maximum Likelihood Estimator)
> We say that the estimator $\hat{\theta}$ is a maximum likelihood estimator (mle) of $\theta$ if the value of the likelihood function $L(\theta)$ is maximum at $\theta$. This is denoted by: $$\hat{\theta}=Argmax \space L(\theta,X)$$

### Process of Point Estimation using Maximum Likelihood Method
- Find the likelihood function using the pdf of $X$.
- In some cases, it is easier to take the logarithmic form of the likelihood function.
- Take the derivative of the likelihood function(or its log form) then evaluate at zero. 
- Solve for the missing parameter $\theta$.
- This $\theta$ is the estimator obtained using the maximum likelihood method
<!--ID: 1645617153481-->



---
If a parameter $η=g(\theta)$ is a function of another parameter $\theta$, then the mle of that parameter is a function of the mle of the other.


> ==Theorem==
> Let $X_1,X_2,..., X_n$ be a random sample with probability density function $f(x;\theta)$. For a specified function g, let $η=g(\theta)$ be a parameter of interest. Suppose $\hat{\theta}$ is the maximum likelihood  estimator of $\theta$. Then $g(\hat{\theta})$ is the maximum likelihood estimator of $η$.

### Regularity Conditions
Let $\theta_0$ be the true value  of $\theta$. Assume the regularity conditions.
<!--ID: 1619312064544-->


- (R0) The probability density functions are distinct.
- (R1) The probability density function have common support for all $\theta$.
- (R2) The point $\theta_0$ is an interior point in $\Omega$.


**Two theorems about MLE**
- First theorem says that we need to maximize the likelihood function to get an estimator.
> ==Theorem.== Let $\theta_0$ be the true parameter and $X=(X_1,X_2,...,X_n)$ be the random sample. Under conditions R0 and R1, for all $\theta \neq \theta_0$, 
> 
> $$\lim_{n\to \infty} \mathbb{P}[L(\theta_0,X)>L(\theta,X)] = 1$$

- Second theorem says that the MLE, under the regularity conditions, are consistent estimators.
> ==Theorem== Assume $X_1,X_2,...,X_n$ satisfies the regularity conditions R0-R2, where $\theta_0$ is the true parameter, and $f(x;\theta)$ is differentiable with respect to $\theta\in \Omega$. Then the likelihood equation $$\frac{\partial}{\partial \theta}L(\theta, X)=0$$ has a solution $\hat{\theta}_n$ such that $\hat{\theta}_n \xrightarrow{P} \theta_0$.


## Minimum Variance Unbiased Estimator

> Suppose there are two unbiased estimators. How do we determine which is a “better” estimator?
<!--ID: 1645617153490-->


> ==Definition.== Minimum Variance Unbiased Estiimator (MVUE)
> A point estimator Y is a *minimum variance unbiased estimator* of a parameter $\theta$ if it satisfies  the following criteria:
> - Y is unbiased ($E[Y]=0$)
> - The variance of Y is less than or equal to variance of any other *unbiased estimator*.

### Sufficient Statistic

> ==Definition.== Sufficient Statistic
> A statistic $Y_1=u(x_1,x_2,...,x_n)$ is a sufficient statistic for $\theta$ if and only if 
> $$\frac{\prod f(x_i;\theta)}{f_{Y_1}(x_1,x_2,...,x_n;\theta)}=H(x_1,x_2,...,x_n)$$ where $H$ is a function not dependent on $\theta$.
<!--ID: 1645617153500-->


The following theorem gives an easier way to characterize a sufficient statistic:

> ==Theorem.== Fisher- Neyman Factorization Theorem
> $Y_1=u(x_1,x_2,...,x_n)$ is a sufficient statistic for $\theta$ if and only if there exists **two non-negative** functions g and h such that $$\prod_{i=1}^n f(x_i;\theta)=g(u(x_1,x_2,...,x_n);\theta)h(x_1,x_2,...,x_n)$$ where **h does not depend on $\theta$**.

The [[Rao-Blackwell Theorem]] allows us to find an unbiased estimator that is a sufficient statistic with a lower variance.

> ==Theorem.== Rao-Blackwell Theorem
> Let $Y_1$ be a sufficient statistic of  $\theta$, $Y_2$ (that is a *NOT function* of $Y_1$) be an unbiased estimator of $\theta$ . Then $\mathbb{E}[Y_2|Y_1]=\phi(y_1)$ is a sufficient statistic for $\theta$, is also an unbiased estimator and $Var(\phi(y_1))\leq Var(Y_2)$.

The next theorem shows the connection between a sufficient statistic and a unique MLE.

> Theorem. (Sufficient statistic and Unique MLE)
> If $Y_1=u(x_1,x_2,...,x_n)$ a sufficient statistic for $\theta$ exists and a unique MLE $\hat{\theta}$ of $\theta$ exists, then $\hat{\theta}$ is a function of $Y_1$.

> ==Definition.== Complete Family of Statistic
> Let Z be a random variable with pdf/pmf that is a member of a parametric family $\{h(z;\theta):\theta\in \Omega\}$. The family $\{h(z;\theta):\theta\in \Omega\}$ is a complete family of pdf/pmf for Z if $$\mathbb{E}[u(Z)]=0,\space \forall \theta \Longrightarrow u(Z)=0$$ except possible at a set of points that have probability zero.

> ==Theorem.== Lehmann-Scheffe Theorem
> - Let $Y_1=u(x_1,x_2,...,x_n)$ be a sufficient statistic for $\theta$.
> - Let  $\{f_Y(y;\theta):\theta\in \Omega\}$ be a complete family.
> 
> If there exists a functon $Y$ that is an unbiased estimator of $\theta$, then this function is  the unique MVUE of $\theta$ (except possibly at certain points).








