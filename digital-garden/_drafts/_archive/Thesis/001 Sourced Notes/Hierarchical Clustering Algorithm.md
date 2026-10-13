
Hierarchical clustering, as the name suggests is an algorithm that *builds hierarchy of clusters*. This algorithm starts with all the data points assigned to a cluster of their own. Then two nearest clusters are merged into the same cluster. In the end, this algorithm terminates when there is only a single cluster left.
![[Pasted image 20211216165717.png]]

At the bottom, we start with 25 data points, each assigned to separate clusters. Two closest clusters are then merged till we have just one cluster at the top. The height in the dendrogram at which two clusters are merged represents the distance between two clusters in the data space.

The decision of the no. of clusters that can best depict different groups can be chosen by observing the dendrogram. The best choice of the no. of clusters is the no. of vertical lines in the dendrogram cut by a horizontal line that can transverse the maximum distance vertically without intersecting a cluster.

![[Pasted image 20211216165816.png]]

The decision of merging two clusters is taken on the basis of closeness of these clusters.

Common Metrics:
- Euclidean Distance $$||a-b|| = \sqrt{\sum\limits(a_{i}- b_{i})^2}$$
- Squared Euclidean Distance $$||a-b||^2 = \sum\limits(a_{i}- b_{i})$$
- Manhattan Distance $$||a-b|| = \sum\limits |a_{i}- b_{i}|$$
- Maximum Distance $$||a-b|| = max (a_{i}- b_{i})$$
- Mahalanobis Distance

# Two Types of Hierarchical Clustering
**Agglomerative Clustering**
It is also known as *AGNES (AGglomerative NESting)*, it works in a *bottom-up* manner. That is, each observation is initially considered as a single-element cluster (leaf). At each step of the algorithm, the two clusters that are the most similar are combined into a new bigger cluster (nodes). This procedure is iterated until all points are a member of just one single big cluster (root). The result is a tree that can be displayed using a dendrogram.
<!--ID: 1645617152235-->


**Divisive Hierarchical Clustering**
It is also known as DIANA (DIvisive ANAlysis), it works in a top-down manner. DIANA is like the reverse of AGNES. It begins with the root, in which all observations are included in a single cluster. At each step of the algorithm, the current cluster is split into two clusters that are considered most heterogeneous. The process is iterated until all observations are in their own cluster.

# Measures of Dissimilarity
These are the common methods of measuring dissimilarity between two clusters.
<!--ID: 1645617152244-->


1. Complete Linkage Clustering 
	- Computes all pairwise dissimilarities between the elements in cluster 1 and the elements in cluster 2, and considers the *largest value* of these dissimilarities as the distance between the two clusters.
	- It tends to *produce more compact clusters*.
2. Single Linkage Clustering
	-  Computes all pairwise dissimilarities between the elements in cluster 1 and the elements in cluster 2, and considers the *smallest* of these dissimilarities as a linkage criterion. 
	-  It *tends to produce long, “loose” clusters*.
3. Mean Linkage Clustering
	- Computes all pairwise dissimilarities between the elements in cluster 1 and the elements in cluster 2, and considers the *average* of these dissimilarities as the distance between the two clusters. 
	- Can vary in the compactness of the clusters it creates.
4. Centroid Linkage Clustering
	- Computes the dissimilarity between the centroid for cluster 1 (a mean vector of length p, one element for each variable) and the centroid for cluster 2

5. Ward's Method
	- *Minimizes the total within-cluster variance*. At each step, the pair of clusters with the smallest between cluster distance are merged. *Tends to produce more compact clusters.*