**[[Clustering]]** is a method of unpervised [[Machine Learning]].

**Cluster analysis** is the *grouping of objects based on their characteristics* such that there is high intra-cluster similarity and low inter-cluster similarity.

# What is clustering?
- Cluster analysis is the *grouping of objects* such that objects in the same cluster are more similar to each other than they are to objects in another cluster.
-  The classification into clusters is done using criteria such as *smallest distances*, *density of data points*, *graphs*, or *various statistical distributions*.
- Cluster analysis is used in unsupervised [[Machine Learning]], data mining, statistics, graph analytics, image processing, and numerous physical and social science applications.


# Why do we need cluster analysis?
- Data scientists and others use clustering *to gain important insights* from data by observing what groups (or clusters) the data points fall into when they apply a clustering algorithm to the data.
- Clustering *can also be used for anomaly detection* to find data points that are not part of any cluster, or outliers.
- Clustering is used to identify groups of similar objects in datasets with two or more variable quantities. In practice, this data may be collected from *marketing*, *biomedical*, or *geospatial databases*, among many other places.


# How is Cluster Analysis done?
- It’s important to note that *analysis of clusters is not the job of a single algorithm*. Rather, *various algorithms usually undertake the broader task of analysis*, each often being significantly different from others.
- A *clustering algorithm* creates clusters where intra-cluster similarity is very high, meaning the data inside the cluster is very similar to one another.
- The *clustering algorithm* should create clusters where the inter-cluster similarity is much less, meaning each cluster contains information that’s as dissimilar to other clusters as possible.


# Hard and Soft Clustering
*Hard clustering* ->  each object either belongs to a cluster or not.
*Soft clustering* -> each object belongs to each cluster to some degree.


# Examples of Clustering Analysis Methods
- *K-Means* finds clusters by minimizing the mean distance between geometric points.


- *DBSCAN* uses density-based spatial clustering.

- *Spectral clustering* is a similarity graph-based algorithm that models the nearest-neighbor relationships between data points as an undirected graph.

- *HIerarchical Clustering* groups data into a multilevel hierarchy tree of related graphs starting from a finest level (original) and proceeding to a coarsest level.

# Examples of Cluster Analysis Applications
- *Network traffic classification* Organizations seek various ways of understanding the different types of traffic entering their websites, particularly what is spam and what traffic is coming from bots.


- *Marketing and Sales* Clustering algorithms group together people with similar traits, perhaps based on their likelihood to purchase.

- *Document Analysis* Clustering algorithms examine text in documents, then group them into clusters of different themes. That way they can be speedily organized according to actual content.

---
# Sources
[What is Clustering? | Data Science | NVIDIA Glossary](https://www.nvidia.com/en-us/glossary/data-science/clustering/)
[Introduction to Clustering - YouTube](https://www.youtube.com/watch?v=4cxVDUybHrI)
