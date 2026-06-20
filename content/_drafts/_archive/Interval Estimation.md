
Let $X_1,X_2,...,X_n$ denote a random sample of size n from a distribution (either continuous or discrete) that has pdf/pmf $f(x;\theta)$, $\theta \in\Omega$. Let $\alpha\in [0,1]$. Let $T_1=t_1(X_1,X_2,...,X_n)$ and $T_2=t_2(X_1,X_2,...,X_n)$ be two (ordered) statistics. 

Definition. 
- We say that the interval $(T_1,T_2)$ is a $(1-\alpha)100\%$ confidence interval if   $$P[T_1<\theta<T_2]=1-\alpha$$
- The expression $\gamma=(1-\alpha)$ is called the **confidence coefficient**.
- In the interval $(T_1,T_2)$, $T_1$ is called the **lower confidence limit** while $T_2$  is called the **upper confidence limit**.

#### Efficiency of Confidence Intervals

Suppose $(T_1,T_2)$ and $(T_1^*,T_2^*)$ are two confidence intervalswith same confidence coefficient, then we say $(T_1,T_2)$ is more efficient than $(T_1^*,T_2^*)$ if $$\mathbb{E}[T_2-T_1]\leq \mathbb{E}[T_2^*-T_1^*], \text{ for all } \theta \in \Omega$$


### Pivot-Quantity Method

Let $X$ be a random sample from a distribution with pdf $f(x;\theta)$, $\theta \in \Omega$.


> ==Definition.== Pivot Quantity
> Let $Q=q(X_1,X_2,...,X_n;\theta)$. If $Q$ has a distribution that does not depend on $\theta$, then $Q$ is a **pivotal quantity** (or simply a pivot.)

If $Q=q(X_1,X_2,...,X_n;\theta)$ is a pivot, then for any fixed $\alpha \in (0,1)$, there exists $q_1$ and $q_2$ such that $$\mathbb{P}[q_1<Q<q_2]=1-\alpha$$ Now, for each possible sample value $(x_1,x_2,...,x_n)$, $$q_1<q(x_1,x_2,...,x_n)<q_2$$ if and only if: $$t_1(x_1,x_2,...,x_n)<\tau(\theta)<t_2(x_1,x_2,...,x_n)$$ for functions  $t_1$ and $t_2$ not depending on $\theta$.

Then $(T_1,T_2)$ is a $(1-\alpha)100\%$ confidence interval for $\tau(\theta)$,where $T_i=t_i(X_1,X_2,...,X_n)$ for $i=1,2$.


Remarks: 
- $q_1$ and $q_2$ are independent of $\theta$.
- A statistic can be a pivot but a pivot is need not be a statistic.


#### Confidence Intervals for the Mean

##### Population is normal with variance is known


> Theorem. 
> Suppose $X_1,X_2,...,X_n$ are random sample from a normal distribution $N(\mu,\sigma^2)$ and that $\sigma^2$ is known. The $(1-\alpha)100\%$ confidence interval for the population mean $\mu$ is the interval: 
> 
> $$\Big(\bar{X}-z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\bar{X}+z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\Big)$$


Note that $z_{\alpha/2}$ is the Z-value (obtained from a standard normal table) such that the area to the right of it under the standard normal curve is $\frac{\alpha}{2}$. That is $$P(Z\geq z_{\alpha/2})=\frac{\alpha}{2}$$

Here's the illustration of the following interval:
![[Pasted image 20210427160154.png|300]]

---
##### Population is normal with variance unknown

When the variance is unknown, the reasonable thing to dois to estimate it with the sample variance. 


Theorem. 
Suppose $X_1,X_2,...,X_n$ is a random sample from a normal distribution $N(\mu,\sigma^2)$ where $\sigma^2$ is unknown. The $(1-\alpha)100\%$ confidence interval for the population mean $\mu$ is the interval: 

$$\Big(\bar{X}-t_{\alpha/2}(n-1)\frac{S}{\sqrt{n}},\bar{X}+t_{\alpha/2}(n-1)\frac{S}{\sqrt{n}}\Big)$$

##### Population is not necessarily normal

Suppose $X_1,X_2,...,X_n$ is a random sample from a distribution (not normal) with finite mean $\mu$ and variance $\sigma^2$. By the [[Central Limit Theorem]], the distribution of the pivot $$Q=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$$ is approximately standard normal for large sample size n. 


The $(1-\alpha)100\%$ confidence interval for the population mean $\mu$ is the interval: 
> 
> $$\Big(\bar{X}-z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\bar{X}+z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\Big)$$

###### How large must the sample size be?

It is previously mentioned that the sample size must be  large enough to invoke the [[Central Limit Theorem]]. 


#### Confidence Interval for Difference in Means



##### When $\sigma^2_X=\sigma^2_Y$ but unknown.

#### Confidence interval for Difference in Proportions



---
[Introduction to Mathematical Statistics STAT 415](https://online.stat.psu.edu/stat415/lesson/introduction-stat-415)
