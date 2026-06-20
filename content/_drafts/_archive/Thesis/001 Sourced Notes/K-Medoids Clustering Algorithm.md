In k-medoids, each cluster is represented by the nearest object towards the center.

A *medoid* can be defined as the object of a cluster whose average dissimilarity to all the objects in the cluster is minimal.

The process deals with applying the improved combination of k-medoids and the *Partitioning Around Medoids (PAM)* algorithm on the data.

This is not sensitive to outliers.

Computational complexity: PAM $O(K(n-K)^2))$

### Steps:
- Select $K$ points as initial representative objects. (These are your initial K-medoids)
- Repeat the following:
	- Assign each point to the cluster with the closest medoid.
	- Randomly select a non-representative object $o_i$
	- Compute the total cost $S$fo swapping the medoid $m$ with $o_i$
	- If $S < 0$, then swap $m$ and $o_i$ to form the new set of medoids
- Stop when convergence criterion is satisfied.


**Advantages**:

1. It is very robust to noisy data.

2. It is not sensitive to outliers.

3. Pairwise dissimilarity measure comes into play in the case of squared Euclidean distance measures.

**Disadvantages**:

1. Different initial sets of medoids affect the shape and effectiveness of the final cluster.

2. Clustering depends on the units of measurement, the difference in nature of objects differs in the efficiency.

3. It is also sensitive at clustering non-convex shaped clusters.