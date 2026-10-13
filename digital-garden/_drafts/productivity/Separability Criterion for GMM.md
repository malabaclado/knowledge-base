---
tags:
alias:
creation-date: Wednesday 24th August 2022
last-modified-date: Wednesday 24th August 2022 13:56:04
---

# Separability Criterion for GMM
SCGMM classifier uses the separability criterion and an agglomerative hierarchical clustering algorithm to find $K_{opt}$ for each class.

The separability criterion attempts to find the clustering that maximises the average distance between the mean of a class and the means of clusters in this class, which is defined as follows: $$K_{i}^{*}=\arg \max_{k} (AED_{k}^{i})$$
where:
- $K_{i}^{*}$ is the optimal number of clusters in class $i$. We also take this as the optimal number of gaussian components for each class $i$.
- $AED_{k}^{i}$ is the **average Euclidian distance** between the mean of class $i$ and the means of its $k$ clusters. 

The average Euclidian distance is defined as:
$$AED_{k}^{i} = \frac{1}{k}\sum_{j=1}^{k}||\mu_{ij} - \mu_{i}||_{2}$$
where:
- $\mu_{ij}$ is the mean of the jth cluster in class $i$;
- $\mu_{i}$ is the mean of class $i$


> [!NOTE] Remark
> The larger the AED, the more separated the clusters are from each other.



