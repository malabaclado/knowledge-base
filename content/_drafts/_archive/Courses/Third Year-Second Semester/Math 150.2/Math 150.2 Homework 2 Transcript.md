1. A machine shop manufactures toggle levers. A lever is flawed if a standard nut cannot be screwed onto the threads. Let p be the proportion of flawed toggle levers that they manufacture. If there were 24 flawed levers out of a sample of 642 that were randomly selected from the production line, find an approximate 95% confidence interval for p.

	Solution: Let $n=642$ be the sample size and $\hat{p}=\frac{24}{642}=0.0373$ be the sample proportion.

	The $(100-\alpha)\%$ confidence interval for sample proportion is given by $$\Bigg(\hat{p}-z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\leq p \leq \hat{p}+z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\Bigg)$$

	Now, let $\alpha=0.05$, so that $z_{0.025}=2.81$.

	$$\hat{p}-z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = 0.0373 - 2.81 \sqrt{\frac{0.0373(0.9627)}{642}} = 0.0163$$ 


	$$\hat{p}+z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = 0.0373 + 2.81 \sqrt{\frac{0.0373(0.9627)}{642}} = 0.0583$$

	So we have the 95% confidence interval for proportion p:
	$$(0.0163 \leq p \leq 0.0583)$$

---
2. Let $X_1, . . ., X_n$ be a random sample from the Bernoulli distribution with parameter $\theta=\mathbb{P}[X=1]=1-\mathbb{P}[X=0]$. If $\alpha = 0.0547$, find the most powerful size-$\alpha$ test of 

	$$H_0:\theta=\frac{1}{2}\text{ vs }H_a:\theta=\frac{1}{4}$$
	
	
	The pdf of a bernoulli distributed random variable with parameter $\theta$ is given by: $$f(x;\theta)=\theta^x(1-\theta)^{1-x}$$

	Taking the likelihood functions:

	$$L\Big(\theta=\frac{1}{2}\Big)= \Big(\frac{1}{2}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{1}{2}\Big)^{n-\sum^n_{i=1} x_i}$$

	$$L\Big(\theta=\frac{1}{4}\Big)= \Big(\frac{1}{4}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{3}{4}\Big)^{n-\sum^n_{i=1} x_i}$$

	So we have 

	$$\begin{align}
	\lambda &= \frac{L\Big(\theta=\frac{1}{2}\Big)}{L\Big(\theta=\frac{1}{4}\Big)} \\
	&=\frac{\Big(\frac{1}{2}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{1}{2}\Big)^{n-\sum^n_{i=1} x_i}}{\Big(\frac{1}{4}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{3}{4}\Big)^{n-\sum^n_{i=1} x_i}} \\
	&= \frac{\Big(\frac{1}{2}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{1}{2}\Big)^{n}\Big(\frac{1}{2}\Big)^{-\sum^n_{i=1} x_i}}{\Big(\frac{1}{4}\Big)^{\sum^n_{i=1} x_i}\Big(\frac{3}{4}\Big)^{n}3^{-\sum^n_{i=1} x_i}\Big(\frac{1}{4}\Big)^{-\sum^n_{i=1} x_i}}\\
	&= \frac{\Big(\frac{1}{2}\Big)^n 3^{\sum^n_{i=1} x_i}}{\Big(\frac{3}{4}\Big)^{n}}\\
	&= \Big(\frac{2}{3}\Big)^{n}3^{\sum^n_{i=1} x_i}
	\end{align}$$

	By Neyman-Pearson Lemma, the most powerful test of size $\alpha$ will have the form:

	Reject $H_0:\theta=\frac{1}{2}$ if $\lambda \leq k$ for some constant $k$.

	That is, 

	$$\begin{align}
	\lambda=\Big(\frac{2}{3}\Big)^{n}3^{\sum^n_{i=1} x_i}&\leq k\\
	3^{\sum^n_{i=1} x_i}&\leq \Big(\frac{3}{2}\Big)^{n}k\\
	\sum^n_{i=1} x_i \ln(3) &\leq \ln\Bigg(\Big(\frac{3}{2}\Big)^{n}k\Bigg)\\
	\sum^n_{i=1} x_i &\leq \frac{\ln\Bigg(\Big(\frac{3}{2}\Big)^{n}k\Bigg)}{\ln(3)}=k^*
	\end{align}$$

	Now, 
	$$\begin{align}
	\alpha &= \mathbb{P}_{\theta=\frac{1}{2}}[\text{reject } H_0]\\
	&=\mathbb{P}_{\theta=\frac{1}{2}}[\sum X_i\leq k^*]
	\end{align}$$

	Note that since $X \sim Be(\theta)$, then $\sum X_i \sim Bi(n,\theta)$.

	Therefore, the most powerful test of size $\alpha=0.0547$ of $H_0:\theta=\frac{1}{2}$ against $H_a:\theta=\frac{1}{4}$ is:

	Reject $H_0$ if $\sum X_i\leq k^*$ where $k^*$ is the $\alpha$th percentile of $Bi(n,\theta)$



---

3. Assume that IQ scores for a certain population are approximately $N(\mu, 100)$. To test $H_0 : µ = 110$ against $H_a : µ > 110$, we take a random sample of size $n = 16$ from this population. Find the most powerful test of size a. $\alpha=5\%$, b. $\alpha=10\%$.

	Solution: The pdf of a normally distributed random variable X with mean $\mu$ and variance 100 is given by 

	$$\begin{align}
	f(x) &= \frac{1}{10\sqrt{2\pi}}\exp \Big[-\frac{1}{2}\Big( \frac{x-\mu}{10}\Big)^2\Big]\\
	&= (200\pi)^{-\frac{1}{2}}\exp\Big[-\frac{1}{200}(x-\mu)^2\Big]
	\end{align}$$

	Let $\mu_\alpha$  be the possible values for composite alternative hypothesis $H_a: µ > 110$.
	Solving for the General Likelihood Ratio:

	$$\begin{align}
	\lambda_n = \frac{L(\mu=110)}{L(\mu=\mu_\alpha)} &= \frac{(200\pi)^{-\frac{16}{2}}\exp\Big[-\frac{1}{200}\sum_{i=1}^{16}(x-110)^2\Big]}{(200\pi)^{-\frac{16}{2}}\exp\Big[-\frac{1}{200}\sum_{i=1}^{16}(x-\mu_\alpha)^2\Big]} \\
	&=\exp\Big[ -\frac{1}{200}\Big(\sum_{i=1}^{16}(x-110)^2-\sum_{i=1}^{16}(x-\mu_\alpha)^2 \Big)\Big]\\
	&=\exp \Big[ -\frac{1}{200}\Big( \sum_{i=1}^{16}x_i^2 - 2(110)\sum_{i=1}^{16}x_i+16(110)^2 \\
	&-\sum_{i=1}^{16}x_i^2 +2(\mu_\alpha)\sum_{i=1}^{16}x_i +16(\mu_\alpha)^2 \Big)\Big] \\
	&=\exp \Big[ \frac{1}{200}\Big( 2\sum_{i=1}^{16}x_i(110-\mu_\alpha) -16(110^2 +\mu_\alpha^2)\Big)\Big]\\
	\end{align}$$

	Now let k be a constant such that

	$$\begin{align}
	\lambda_n &\leq k\\
	\exp \Big[ \frac{1}{200}\Big( 2\sum_{i=1}^{16}x_i(110-\mu_\alpha) -16(110^2 +\mu_\alpha^2)\Big)\Big] &\leq k\\
	 2\sum_{i=1}^{16}x_i(110-\mu_\alpha) -16(110^2 +\mu_\alpha^2) &\leq 200 \ln(k)\\
	 2\sum_{i=1}^{16}x_i(110-\mu_\alpha) &\leq 200 \ln(k) +16(110^2 +\mu_\alpha^2)\\
	 \frac{1}{16}\sum_{i=1}^{16}x_i &\leq \frac{1}{32(110-\mu_\alpha)} (200 \ln(k) +16(110^2 +\mu_\alpha^2)) =k^*\\
	 \bar{x}\leq k^*
	\end{align}$$

	By Neyman-Pearson Lemma, the (uniformly) most powerful test of size $\alpha$ of $H_0:\mu=110$ against $H_a:\mu>110$ has the form: Reject $H_0: \mu=110$ if $\bar{x}\leq k^*$.
	
	For (a):
	$$\begin{align}
	\alpha &= \mathbb{P}[\text{reject }H_0]\\
	0.05&= \mathbb{P}[\bar{X}\leq k^*]\\
	\Phi(1.645)&=\mathbb{P}[Z\leq \frac{k^*-110}{10/4}]\\
	\Phi(1.645)&=\Phi(Z\leq \frac{k^*-110}{10/4})\\
	\frac{k^*-110}{10/4}a&\geq1.645\\
	k^* \geq 114.11
	\end{align}$$
	
	Now, the (uniformly) most powerful test of size $\alpha=0.05$ is: Reject $H_0: \mu=110$ if $\bar{x}\leq k^*$, that is, if $k^*\geq114.11$.
	
	For (b):
		$$\begin{align}
	\alpha &= \mathbb{P}[\text{reject }H_0]\\
	0.10&= \mathbb{P}[\bar{X}\leq k^*]\\
	\Phi(1.285)&=\mathbb{P}[Z\leq \frac{k^*-110}{10/4}]\\
	\Phi(1.285)&=\Phi(Z\leq\frac{k^*-110}{10/4})\\
	\frac{k^*-110}{10/4}a&\geq1.285\\
	k^* \geq 113.21
	\end{align}$$
	
	Now, the (uniformly) most powerful test of size $\alpha=0.10$ is: Reject $H_0: \mu=110$ if $\bar{x}\leq k^*$, that is, if $k^*\geq114.11$.
	