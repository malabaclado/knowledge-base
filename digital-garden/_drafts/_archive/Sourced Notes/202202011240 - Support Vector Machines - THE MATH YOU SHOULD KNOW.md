*Tags:* #thesis #topic/machine-learning #topic/machine-learning

# Source
[Support Vector Machines - THE MATH YOU SHOULD KNOW - YouTube](https://www.youtube.com/watch?v=05VABNfa1ds)

# Summary
Consider a dataset with each point $x \in \mathbb{R}^{D}$ 

Using a nonlinear feature space $\phi(x):\mathbb{R}^{D} \to \mathbb{R}^{M}$, we get the transformed feature space $\phi(x) \in \mathbb{R}^{M}$ 

**Decision Boundary**

![[Pasted image 20220201124859.png | 250]]

*(1.1)* In order to classify, we need to identify the *decision boundary* which is a line with the equation: $$y(x) = \text{w}^{T} \phi(x) +b = 0$$
In a D-dimensional space, the *hyperplane* is a (D-1)-dimensional separator.  ^b2e480


**The Distance Measure**

![[Pasted image 20220201124929.png | 250]]

The distance of a line with equation $ax+by+c=0$ to the point $(x_{0}, y_{0})$ is given by $$\frac{|ax_{0} + by_{0}+c|}{\sqrt{a^{2} + b^{2}}}$$
In the same way, we get the distance of the hyperplane with the equation [[#^b2e480|(1.1)]] to a point vector $$d(\phi(x_{0}))= \frac{|\text{w}^{T} \phi(x_{0}) +b|}{||w||^2}$$
We call this distance the *margin*. 

**Our goal is to find the hyperplane with the maximum margin from the closest point**. 

We'll consider two cases: one where the dataset is linearly separable, the other when the dataset is not linearly separable.

**Case 1: The data is linearly separable.**

Consider the 2-class classification problem.

![[Pasted image 20220201155337.png |250]]

**If a point belongs to Group 1**, substituting its value to the hyperplane equation gives a value greater than zero. $$\text{w}^{T} \phi(x_{0}) +b >0$$
**If a point belongs to Group 2**, substituting its value to the hyperplane equation gives a value less than zero. $$\text{w}^{T} \phi(x_{0}) +b <0$$
The product of the predicted label and the actual label would be positive if it is correctly labeled, and negative if it is incorrectly classified.

![[Pasted image 20220201132637.png | 250]]

Since the dataset is linearly separable, the hyperplane separates the dataset perfectly. To find this hyperplane with the maximum margin, we solve this optimization problem $$w^{*}= \arg \max_{\text{w}} [\min_{n} y(x)]$$

which can be expressed in the form
$$\arg \max_{w} \frac{1}{||\text{w}||} [\min_{n} y_{n}[\text{w}^{T} \phi(x_{n}) +b]] $$

The expression $y_{n}[\text{w}^{T} \phi(x_{n}) +b]$ refers to the distance of the hyperplane to the closest point in the dataset.

To simplify the problem, we rescale the distance of the  closet point to be equal to 1. That is, let $$\min_{n} y_{n}[\text{w}^{T} \phi(x_{n}) +b] =1$$

Doing so will arrive at the now simplified the optimization problem: $$\arg \max_{w} \frac{1}{||\text{w}||}$$subject to constraint: $\min_{n} y_{n}[\text{w}^{T} \phi(x_{n}) +b] =1$.

We can convert it to a minimization problem and introduce the factor $\frac{1}{2}$ for notation convenience.

Now we have the *primal form* optimization problem for SVM $$\min_{\text{w}} \frac{1}{2} ||\text{w}||$$
subject to the following constraint: $$y_{n}[\text{w}^{T} \phi(x_{n}) +b] \geq 1, \quad \forall n$$



**Case 2: The data is not linearly separable**

The previous problem considered the case where the dataset is linearly separable - which meas that the hyperplane always classifies correctly. In mathematics terms, that is $$y_{n}[\text{w}^{T} \phi(x_{n}) +b] >0, \quad \forall n$$
But in the real world, this rarely happen. For data that cannot be perfectly separated, the above results risk overfitting, unless we allow it to make some mistake, that is, we allow some points to only follow the above condition. $$y_{n}[\text{w}^{T} \phi(x_{n}) +b] \leq 0, \quad \exists n$$

We can do this by introducing for each data point, a slack variable $\xi$ which acts as penalty for misclassification. So that a datapoint classified correctly will have $\xi =0$ and a point classified incorrectly will have $\xi >1$.

![[Pasted image 20220201134057.png | 250]]
 
This gives the *new primal form for SVM* $$\min_{\text{w}, b, \{\xi_{n}\}} \frac{1}{2} ||\text{w}|| + C \sum_{n}\xi_{n}$$


# Thoughts  & Comments

