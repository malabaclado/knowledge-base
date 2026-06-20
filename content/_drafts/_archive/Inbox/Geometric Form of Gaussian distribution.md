The functional dependence of the Gaussian on $\text{x}$ is through the quadratic form: $$\Delta^{2}= (\text{x}- \mu)^{T} \Sigma^{-1}(\text{x} - \mu)$$
The quantity $\Delta$ is called the Mahalanobis distance from $\mu$ to $\text{x}$ which reduces to the Euclidian distance when $\Sigma$ is the identity matrix. 

Note that the [[covariance matrix]] $\Sigma$ can be taken to be symmetric (without loss of generality).

# The eigenvectors of the [[covariance matrix]]

Consider the *eigenvector equation of the [[covariance matrix]]*: $$\Sigma\text{u}_{i} = \lambda_{i}\text{u}_{i} \tag{1}$$where $i=1,2,...,D$. 


Because the covariance matrix $\Sigma$ is a real-valued, symmetric matrix, its eigenvalues will be real, and its eigen vectors can be chosen to form an orthonormal set. So that $$\text{u}_{i}^{T} \text{u}_{j} = \text{I}_{ij}$$ where $\text{I}_{ij}$ is the identity matrix. 

##### Reforming the quadratic form of Gaussian

From (1), we can express the covariance matrix as an expansion in terms of its eigenvectors in the form: $$\Sigma = \sum_{i=1}^{D} \lambda_{i}\text{u}_{i} \text{u}_{i}^{T}$$
Similarly, the inverse covariance matrix $\Sigma^{-1}$ can be expressed as: $$\Sigma^{-1}= \sum _{i=1}^{D} \frac{1}{\lambda _{i}} \text{u}_{i} \text{u}_{i}^{T} \tag{2}$$
Substituting (2), the quadratic form now becomes $$\Delta^{2}= \sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}}$$ where $$y_{i}= \text{u}_{i}^{T}(\text{x} - \mu)$$

# The form of [[Gaussian Distribution]] on the euclidian plane

We can interpret $\{ y_{i}\}$ as a **new coordinate system defined by orthonormal vectors** $\text{u}_{i}$ , that are shifted and rotated with respect to the original $x_{i}$ coordinates. Forming the vector $\text{y} = (y_{1},...,y_{D})^{T}$, we have $$\text{y} = \text{U}(\text{x}- \mu) \tag{3}$$ where $\text{U}$ is a matrix whose rows are given by $\text{u}_{i}^{T}$.  


![[Pasted image 20220815114315.png]]


> [!NOTE] Remarks
> - The Gaussian density will be constant on surfaces for which eq. (3) is constant.
> - If all the eigenvalues $\lambda_{i}$ are positive, then these surfaces represent ellipsoids with centers at $\mu$ and their axes given by $\lambda_{i}^{\frac{1}{2}}$ as shown in the figure above.
> - For the [[Gaussian Distribution]] to be well-defined, it is necessary for all the eigenvalues of the covariance matrix to be strictly positive. Otehrwise, the distribution cannot be properly normalized. 
> - A matrix whose eigenvalues are all positive are said to be [[Positive definite matrix]].

