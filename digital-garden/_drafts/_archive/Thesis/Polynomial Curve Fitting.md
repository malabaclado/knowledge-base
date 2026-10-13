
---
tags:
alias:
creation-date: Tuesday 7th December 2021
last-modified-date: Wednesday 23rd February 2022 19:52:41
---

# Polynomial Curve Fitting

Here we return to the curve fitting example and **view it from a probabilistic perspective**, thereby **gaining some insights into error functions and regularization**, as well as taking us towards a full Bayesian treatment.


The **goal in the curve fitting problem** is to be able to make predictions for the target variable $t$ given some new value of the input variable $x$ on the basis of a set of training data comprising $N$ input values $x = (x_1,x_2,...,x_N)^T$ and their corresponding target values $t=(t_1,t_2,...,t_N)^T$

Let's assume that given the value of $x$, the corresponding value of $t$ has a Gaussian distribution with a mean equal to the value $y(x,w)$ of the polynomial curve.
$$p(t|x,w,\beta) = \mathscr{N}(t|y(x,w),\beta)$$

We now use the training data $\{\textbf{x},\textbf{t}\}$ to determine the values of the unknown parameters $\textbf{w}$ and $\beta$ by *maximum likelihood*.

---
**The Maximum Likelihood Method**
- Get the likelihood function.
- Maximize the likelihood function (It is more *usually more convenient* to maximize the log likelihood function)
	- Sometimes, instead of maximizing the log likelihood function, you may choose to minimize the negative log likelihood function

---
If the data are drawn independently from the distribution, we have the *likelihood function*: ![[Pasted image 20211207121526.png]]


Which gives the *log likelihood function*: ![[Pasted image 20211207121543.png]]

Maximizing (1.62) with respect to $\textbf{w}$ gives us the maximum likelihood solution $\textbf{w}_{ML}$. 

> Maximizing likelihood is equivalent (as far as determining $\textbf{w}$ is concerned) to minimizing the sum-of-squares error.	

Maximizing (1.62) with respect to the precision parameter $\beta$ gives ![[Pasted image 20211207124715.png]]

Once $\textbf{w}$ and $\beta$ are determined, we can now make preditions for the new values of $\textbf{x}$ - which are expressed in terms of a predictive distribution that gives the probability distribution over $t$ rather than a point estimate. This is obtained by substituting the maximum likelihood parameters to ![[Pasted image 20211207125234.png]] which yields
![[Pasted image 20211207125253.png]]

---
### Maximum Posterior
Now, let's take a more Bayesian approach.


Introduce a prior distribution over the polynomial coefficients $\textbf{w}$: ![[Pasted image 20211207125435.png]]
where:
- $\alpha$ -> precision of distribution
- $(M+1)$ -> total number of elements in the vector $\textbf{w}$ for an $M^{th}$ order polynomial.

> The variables such as $\alpha$ - control the distribution of the model parameters, are called **hyperparameters**.

Using Bayes' theorem:![[Pasted image 20211207125712.png]]

We can now determine $\textbf{w}$ by finding the mist probable value of $\textbf{w}$ given the data = maximizing the posterior distribution. This technique is called *maximum posterior*.

> Maximizing the posterior distribution is equivalent to minimizing  
the regularized sum-of-squares error function