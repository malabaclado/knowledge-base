K-Means [[Clustering]] [[Algorithm]] is an *iterative* clustering [[Algorithm]] that aims to find *local maxima* in each iteration. 

K-Means is a good choice for high dimensional data with balanced cluster size and features having equal variance.

# The Mathematics of K-Means Algorithm
Suppose we have a vector $\mu_{k}$ where $k=1,...,K$. Let $x_n$ be the individual data points.  


Define the variable $r_{nk} \in \{0,1\}$ as follows:
- $r_{nk}=1$ if $x_n$ is in cluster $k$
- $r_{nk}=0$ otherwise 
  
  Then we'll have the relative measure of each point to the cluster center via the distortion function $$J = \sum\limits_{n=1}^{N} \sum\limits_{k=1}^{K} r_{nk}||x_{n} - \mu_{k}|| $$
  
  Our goal is to find $r_{nk}$ and $\mu_{k}$ such that the distortion function $J$ is a minimum.
  
  We do this using the following steps:
  1. Initialize $\mu_{k}$
  
  2. Repeat the following steps until convergence is achieved:
  	1. Minimize $J$ with respect to $r_{nk}$ (keeping $\mu_k$ fixed)
	- To do this, we need to find $r_{nk}$ such that:
		- $r_{nk}=1$ if $k=argmin_{j}||x_{n}- \mu_{j}||^{2}$
		  	2. Minimize $J$ with respect to $\mu_k$ (keeping $r_{nk}$ fixed)
	- To do this, we set the derivative of $J$ to zero. Upon algebraic manipulation, we arrive at the minimum: $$\mu_{k}= \frac{\sum\limits_{n} r_{nk}(x_n)}{\sum\limits_{n}r_{nk}}$$
	  
	  This section sums up how to mathematically implement the K-Means algorithm.
	  
	  ---
# The Algorithm
This algorithm works in these 5 steps :


1. Specify the desired number of clusters $K$.
2. Randomly assign each data point to a cluster.
3. Compute cluster centroids.
4. Re-assign each point to the closest centroid
5. Re-compute cluster centroids
6. Repeat steps 4-5 until no improvements are no longer possible.
- # Pros and Cons
  
  **PROS**
  1. It is the *fastest* centroid-based algorithm.
  <!--ID: 1645617152208-->
  
  
  2. It can *work for large data sets*.
	- K-Means grows linearly, in contrast to HCA that grows quadratically.
	  
	  3. It *helps in reducing the intra-cluster variance measure*. 
	  4. Produces *tighter clusters* than hierarchical clustering
	  5. It is effective initializing other clustering algorithms (e.g. Gausian-Mixture Models)
	  
	  **CONS**
	  1. *Performance* is affected when there is more noise in the data.
	  
	  2. *Outliers* can never be studied.
	  
	  3. Even though it reduces intra-cluster variance, it can’t affect or deal with the *global minimum variance of measure*.
	  
	  4. It is *very sensitive* at [[Clustering]] data sets of *non-convex shaped clusters*.
	  
	  5. It is bad for datasets with different size and density.
	  6. It favors larger clusters. This means that smaller, scattered clusters might be too far away.
	  7. It does not tell you how good the clustering is.
	  
	  
	  ---
# Applications
- Document classification
	- We can classify documents based on text, topics and contents of the document.
	- Represent each document as a vector and use term frequency to  classify each document.
	- Then the document vectors are clustered to identify similarities between documents.
	  <!--ID: 1645617152215-->
- Delivery Store Optimization
	- Find the optimal number of launch locations to solve the truck route as a travelling salesman problem.
- Locating crime localities
	- Categorize crime, area and association between those two.
- Fantasy Leagues Debt Analysis
	- Task of finding similar players for fantasy drafts.
	- Analysing player stats
- Insurance Fraud Detection
	- By studying previous patterns of fraudulent claims, we can use K-Means to see how close new claims are to these clusters of fraudulent claims.
- Color Quantization
	- The process of reducing the number of distinct colors used in an image.
	- Useful for rendering images in low-memory devices.
	  
	  
	  ---