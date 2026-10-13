**Density-Based Spatial Clustering of Applications with Noise (DBSCAN)** is the most widely used density-based algorithm. DBSCAN estimates the density *by counting the number of points in a fixed-radius neighborhood* i.e ɛ and claim that *two points are connected only if they lie within each other’s neighborhood*.

**Characterization of points** 

-   A point is a *core point* if it has more than a specified number of points (MinPts) within ɛ These points belong in a dense region and are at the interior of a cluster. 
-   A *border point* has fewer than MinPts within ɛ but is in the neighborhood of a core point.
-   A *noise point* is any point that is not a core point or a border point.

A point “p” is said to be *density reachable* from a point “q” if point “p” is within ε distance from point “q” and “q” has the sufficient number of points in its neighbors which are within distance ε.

# The Algorithm
**Input**: N objects to be clusters and global parameters ɛ and MinPts.

**Output:** Clusters of objects

1.  Arbitrarily select a point p.
2.  Retrieve all point density reachable from p wrt ɛ and MinPts.
3.  If P is a core point a cluster is formed.
4.  If P is a border point, then there is no point that is density reachable, and DBSCAN moves to the next point.
6.  This process is continued until all the points are processed.

# Pros and Cons

**PROS**
1.  Does not require a prior specification of the number of clusters.
2.  Able to identify noise data while clustering.
3.  DBSCAN algorithm is able to find arbitrarily-sized and arbitrarily-shaped clusters.

**CONS**

1.  DBSCAN algorithm fails in the case of varying density clusters.
2.  Fails in case of neck type of dataset.
3.  Does not work well in the case of high-dimensional data.

---
# Applications
