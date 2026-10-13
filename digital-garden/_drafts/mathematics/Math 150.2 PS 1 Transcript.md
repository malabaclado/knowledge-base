- #### Questions
1. Let $Y_1 < Y_2 < ,...,< Y_n$ be the order statistics of a random sample from a distribution with pdf $$f(x)=e^{-x}\mathbb{1}_{(0,\infty)}(x)$$ Determine the limiting distribution of $Z_n=Y_n-\ln(n)$.

2. Let $X_1,X_2,...,X_n$ be a random sample from a distribution with pdf 
$$f(x;\theta) = \frac{1}{\theta^2}xe^{-\frac{x}{\theta}}, x>0, \space \theta >0$$

A. Obtain an mle of $\theta$.
B. Obtain the method of moments estimator of $\theta$.
C. Calculate both estimates when 
$$x_1 = 0.25, x_2 = 0.75, x_3 = 1.5, x_4 = 2.5,x_5 = 2.0$$


3.  Let $Y_1,Y_2,...,Y_n$ be a random sample following Bernoulli ($p$), $0<p<1$. Show that $Y = \frac{1}{n} \sum_{i=1}^n Y_i$ is the MVUE of $p$.

4. Let $X_1$ be a single observation from the density $f(x;\theta)=\theta x^{\theta-1} \mathbb{1}_{(0,1)}(x)$, where $\theta >0$.

A.  Show that $Y = -\theta \ln X$ is a pivot. Specify its distribution.
B. Find the confidence coefficient of the confidence interval $(-\frac{1}{2 \ln X_1}, -\frac{1}{\ln X_1})$ for $\theta$.

5. Let $X \sim$ Bernoulli(p). Suppose $X_1,X_2,...,X_n$ is a random sample from the distribution of $X$ and let $\hat{p}$ be the sample proportion of successes.

A. Find an approximate $(1-\alpha)\%$ confidence interval for the parameter $p$.
B. Suppose that a car insurance company randomly surveyed a population of 400 drivers and found that 320 claimed that they always wear their seatbelts when driving. Construct a 95\% confidence interval for the population proportion who claim they always buckle up.

---
#### Solutions
1 


Let X be a random variable with pdf $f_X(x)=e^{-x}$	, $o \leq x \leq \infty$. The distribution function:

$$\begin{align}
F_X(x) &= \int_0^{x} f_X(x)dx\\
	   &= \int_0^x e^{-x}dx\\
	   &= 1-e^{-x}
\end{align}$$

Let $Z_n=Y_n-ln(n)$.
$$\begin{align}
P[Z_n\leq t] &= P[Y_n-ln(n)\leq t]\\
			 &= P[Y_n \leq ln(n)+t]\\
			 &= P[\cap_{i=1}^n \{X_i \leq \ln(n) + t\}]\\
			 &= \prod_{i=1}^n F_X(ln(n)+t)\\
			 &= \prod_{i=1}^n (1-e^{-(\ln(n)+t)})\\
			 &= (1-\frac{e^{-t}}{n})^n\\
			 &\xrightarrow{n \to \infty} e^{e^{-t}}
\end{align}$$



---
2A. Take the log likelihood function:
$$\begin{align}
l(\theta) &= \ln (L(\theta))\\
		  &= \ln (\prod_{i=1}^n f(x;\theta))\\
		  &= \ln (\theta^{-2n}\prod_{i=1}^n x_i e^{-(n/\theta)\sum_{i=1}^n x_i})\\
		  &= \ln (\theta^{-2n}\prod_{i=1}^n x_i )+ \ln(e^{-(n/\theta)\sum_{i=1}^n x_i})\\
		  &= \ln (\theta^{-2n}\prod_{i=1}^n x_i ) - (n/\theta)\sum_{i=1}^n x_i
\end{align}$$

Differentiating $l(\theta)$,
$$\begin{align}
l'(\theta) &= \frac{1}{\theta^{-2n}\prod_{i=1}^n x_i}(-2n\theta^{-2n-1}\prod_{i=1}^n x_i)-n\sum_{i=1}^n x_i(-\theta^{-2})\\
		   &= \frac{-2n}{\theta}+ \frac{n\sum_{i=1}^n x_i}{\theta^2}
\end{align}$$

Now, let $l(\theta)=0$, 

$$\begin{align}
\frac{-2n}{\theta}+ \frac{n\sum_{i=1}^n x_i}{\theta^2} &= 0\\
\frac{-2\theta n + n\sum_{i=1}^n x_i}{\theta^2} &= 0\\
-2\theta n + n\sum_{i=1}^n x_i&= 0\\
n\sum_{i=1}^n x_i&=2\theta n\\
\sum_{i=1}^n x_i&=2\theta\\
\theta = \frac{\sum_{i=1}^n x_i}{2}
\end{align}$$

We have $\hat{\theta}_1=\frac{\sum_{i=1}^n x_i}{2}$ a maximum likelihood estimator of $\theta$.

2B. Based on the pdf $f(x;\theta)$, notice that $X \sim \Gamma(2,\theta)$.  Then we have the first raw moment $\mu'_1=2\theta$. The first sample moment is given by $M'_1= \frac{1}{n} \sum_{i=1}^n X_i$.

Now let 
$$\begin{align}
\mu'_1 &= M'_1\\
2\theta &= \frac{1}{n} \sum_{i=1}^n X_i\\
\theta &= \frac{\sum_{i=1}^n X_i}{2n}
\end{align}$$

Then we have $\hat{\theta}_2 =\frac{\sum_{i=1}^n X_i}{2n}$ an estimator of $\theta$ obtained by method of moments.

2C. Using the maximum likelihood estimator:
$$\begin{align}
\hat{\theta}_1 &= \frac{\sum_{i=1}^n x_i}{2}\\
&= \frac{0.25+0.75+ 1.5+2.5+2}{2} = \frac{7}{2} =0.35\\

\end{align}$$

Using the estimator obtained by method of moments:

$$\begin{align}
\hat{\theta}_2 &= \frac{\sum_{i=1}^n X_i}{2n}\\
&= \frac{0.25+0.75+ 1.5+2.5+2}{2(5)}=\frac{7}{10}= 0.7\\
\end{align}$$
---
3 Unbiasedness:

$$\begin{align}
\mathbb{E}[Y] &= \mathbb{E}(\frac{1}{n}\sum_{i=1}^n Y_i)\\
&= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[Y_i]\\
&= \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i]\\
&= \frac{1}{n} \sum_{i=1}^n p\\
&= \frac{1}{n} (np)\\
&=p
\end{align}$$

This shows that Y is an unbiased estimator of p.

Sufficient Statistic:
Let $Y_1,Y_2,...,Y_n$ be a random sample from a Bernoulli distribution. Then we have $$f_{Y_i}(y;p)=p^{y}(1-p)^{1-y}$$
Consider the statistic $Y' = \sum_{i=1}^n Y_i$, it has a pmf:
$$f_{Y'}(y';p) = \binom{n}{y'}p^{y'}(1-p)^{n-y'}$$
Then,

$$\begin{align}
H(y_1,y_2,...,y_n) &= \frac{\prod_{i=1}^n f_{Y_i}(y;p)}{f_{Y'}(y');p}\\
&= \frac{(p^{y_1}(1-p)^{1-y_1})(p^{y_2}(1-p)^{1-y_2})...(p^{y_n}(1-p)^{1-y_n})}{\binom{n}{y'}p^{y'}(1-p)^{1-y'}}\\
&= \frac{p^{\sum y_i} (1-p)^{n-\sum y_i}}{\binom{n}{\sum y_i} p^{\sum y_i}(1-p)^{n-\sum y_i}}\\
&= \frac{1}{\binom{n}{\sum y_i}}
\end{align}$$

Since the function H is independent of the parameter p, then Y' is a sufficient statistic. Note that $Y = \frac{1}{n}Y'$. This condition will be used later when proving Y is an MVUE.

Completeness of Distribution
Consider the family of pmf $\{f_{Y'}(y';p);0\leq p \leq 1\}$. Suppose that the function $u(Y')$ is such that $\mathbb{E}[u(Y')]=0$. 

$$\begin{align}
0 = \mathbb{E}[u(Y')] &= \sum_{i=0}^n u(y')f_{Y'}(y')\\
&= \sum_{i=0}^n u(y') \binom{n}{y'}p^{y'}(1-p)^{n-y'}\\
&= u(y')\sum_{i=0}^n \binom{n}{y'}p^{y'}(1-p)^{n-y'}
\end{align}$$

But $\sum_{i=0}^n \binom{n}{y'}p^{y'}(1-p)^{n-y'}$ is the binomial expansion of $(p + (1-p))^n = (1)^n=1$.

Hence, $0=u(y')\sum_{i=0}^n \binom{n}{y'}p^{y'}(1-p)^{n-y'}=u(y')$. Thus, the family of pmf $\{f_{Y'}(y';p);0\leq p \leq 1\}$ is complete. 


Now, let $Y_1, Y_2,..., Y_n$ a random sample from a Bernoulli distribution. We have found a sufficient statistic $Y' = \sum_{i=1}^n Y_i$ for $p$ with complete family of pmf $\{f_{Y'}(y';p);0\leq p \leq 1\}$. The statistic $Y=\frac{1}{n} \sum_{i=1}^n Y_i=\frac{1}{n} Y'$ is a function of$Y'$ and is an unbiased estimator of $p$. By Lehmann-Scheffe Theorem, Y is the unique MVUE of $p$



---
4A. Take the cdf of $X_1$, $F_{X_1}=x^{\theta}$. 

$$\begin{align}
F_Y(y) = P[Y\leq y] &= P[-\theta \ln(X_1)\leq y]\\
					&= P[X \geq e^{-y/\theta}]\\
					&= 1 - P[X \leq e^{-y/\theta}]\\
					&= 1 - F_{X_1}(e^{-y/\theta})\\
					&= 1 - (e^{-y/\theta})^\theta\\
					&= 1-e^{-y}
\end{align}$$

The distribution of Y is not a function of $\theta$, hence Y is  a pivot. Y is exponentially distributed with $\lambda=1$


4B. $$\begin{align}
P(\frac{-1}{2\ln{x}}\leq \theta\leq \frac{-1}{\ln{x}}) &= P(1\leq -\theta \ln{x}\leq \frac{1}{2})\\
&= P(1 \leq y \leq \frac{1}{2})\\
&= 1 - P(\frac{1}{2} \leq y \leq 1)\\
&= 1 -(F_Y(1)-F_Y(1/2))\\
&= 1 - (1-\frac{1}{e}-1+\frac{1}{\sqrt{e}})\\
&= 1+\frac{1}{e}-\frac{1}{\sqrt{e}}\\
&\approx0.7613
\end{align}$$

Hence, we have the confidence coefficient $(1-\alpha)$=0.7613.




---
5A. Recall that for a Bernoulli random variable X with probability of success p, we have the mean $E[X]=p$ and variance $Var[X]=p(1-p)$.

Let $X_1,X_2,...,X_n$ be a random sample from ${X}$.  Let $\hat{p}=\bar{X}$ be the sample proportion of successes. 

For sufficiently large sample size n, the Central Limit Theorem says that X is approximately standard normal, ${X} \approx Z \sim N(0,1)$.

For $\mu\approx E[X]=p$ and $\sigma^2 \approx Var[X]=p(1-p)$, we have:
$$Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \approx \frac{\hat{p}-p}{\sqrt{\frac{p(1-p)}{n}}}$$

We can approximate the confidence interval using the probability statement:


$$P\Bigg[ -z_{\alpha/2} \leq\frac{\hat{p}-p}{\sqrt{\frac{p(1-p)}{n}}} \leq z_{\alpha/2} \Bigg] \approx 1- \alpha$$

Which gives us the inequality:

$$\begin{align}
-z_{\alpha/2} &\leq\frac{\hat{p}-p}{\sqrt{\frac{p(1-p)}{n}}} \leq z_{\alpha/2} \\
-z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}} &\leq{\hat{p}-p} \leq z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}}\\

-\hat{p}-z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}} &\leq{-p} \leq -\hat{p}+z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}}\\
\hat{p}-z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}}&\leq{p} \leq \hat{p}+z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}}
\end{align}$$

It is reasonable to use $\hat{p}(1-\hat{p})$ to approximate $p(1-p)$. 
$$\hat{p}-z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\leq{p} \leq \hat{p}+z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
Thus we have the approximate $(1-\alpha)100\%$ confidence interval:
$$\Bigg(\hat{p}-z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}},\hat{p}+z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\Bigg)$$

5B. Given: sample size $n=400$ and $\hat{p}=\frac{320}{400}=0.8$. Let $\alpha = 0.05$. Based on the above results, we have the $(1-\alpha)100\%$ confidence interval:

$$\begin{align}

\hat{p}-z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} &\leq{p} \leq \hat{p}+z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\\
&= 0.8-z_{0.025}\sqrt{\frac{(0.8)(0.2)}{400}}\leq{p} \leq 0.8+z_{0.025}\sqrt{\frac{(0.8)(0.2)}{400}}\\
&= 0.8 - 0.02z_{0.025}\leq{p} \leq 0.8 + 0.02z_{0.025}\\
&=0.8 - 0.02(1.96)\leq{p} \leq 0.8 + 0.02(1.96)\\
&=0.7608 \leq{p} \leq 0.8392
\end{align}$$

Therefore, we get 95% confidence interval for the population proportion who claim they always buckle up: $$[0.7608,0.8392]$$

