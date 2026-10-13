#### Gradient Descent

- What is gradient descent?
	- Gradient descent is an optimization algorithm used to find the values of parameters (coefficients) of a function (f) that minimizes a cost function (cost).
	- Gradient descent is best used when the parameters cannot be calculated analytically (e.g. using linear algebra) and must be searched for by an optimization algorithm.
- How can gradient descent be used in algorithms like linear regression?
- How can gradient descent scale to very large datasets?
- What are some tips for getting the most from gradient descent?

##### Gradient Descent Procedure
1. Set initial values v0 for the coefficients of the function (easiest = 0). 
2. Calculate the cost function at initial values v0.
3. Calculate the derivative of the cost function $\Delta$ at v0. This derivative is the rate of descent towards local optimum.
4. Set a learning rate parameter $\alpha$ and calculate new coefficients $v_0$ : $$v_1 = v_0 - (\alpha * \Delta)$$
5.  Repeat steps 1-4 until you get cost function = 0 (or something good enough)

A/N: Gradient descent is nothing but finding the local optimum.

##### Stochastic Gradient Descent

- Gradient descent can be slow to run on very large datasets.
	- Because one iteration of the gradient descent algorithm requires a prediction for each instance in the training dataset, it can take a long time when you have many millions of instances.
	- In situations when you have large amounts of data, you can use a variation of gradient descent called **stochastic gradient descent**.
- The first step of the procedure requires that **the order of the training dataset is randomized**. This is to mix up the order that updates are made to the coefficients. Because the coefficients are updated after every training instance, the updates will be noisy jumping all over the place, and so will the corresponding cost function. By mixing up the order for the updates to the coefficients, **it harnesses this random walk** and avoids it getting distracted or stuck.
- The learning can be much faster with stochastic gradient descent for very large training datasets and often you only need a small number of passes through the dataset to reach a good or good enough set of coefficients, e.g. 1-to-10 passes through the dataset.

##### Tips for Gradient Descent

This section lists some tips and tricks for getting the most out of the gradient descent algorithm for machine learning.

- **Plot Cost versus Time**: Collect and plot the cost values calculated by the algorithm each iteration. The expectation for a well performing gradient descent run is a decrease in cost each iteration. If it does not decrease, try reducing your learning rate.
- **Learning Rate**: The learning rate value is a small real value such as 0.1, 0.001 or 0.0001. Try different values for your problem and see which works best.
- **Rescale Inputs**: The algorithm will reach the minimum cost faster if the shape of the cost function is not skewed and distorted. You can achieved this by rescaling all of the input variables (X) to the same range, such as [0, 1] or [-1, 1].
- **Few Passes**: Stochastic gradient descent often does not need more than 1-to-10 passes through the training dataset to converge on good or good enough coefficients.
- **Plot Mean Cost**: The updates for each training dataset instance can result in a noisy plot of cost over time when using stochastic gradient descent. Taking the average over 10, 100, or 1000 updates can give you a better idea of the learning trend for the algorithm.