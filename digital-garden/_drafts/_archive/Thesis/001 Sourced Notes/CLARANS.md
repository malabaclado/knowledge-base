CLARANS stands for *Clustering Large Applications based on RANdomized Search*. CLARANS at times is thought of as an *enhanced version of primitive CLARA* (which is an algorithm used in reducing the computational efforts that one comes across using the k-medoid algorithm) and thus termed as Randomized “CLARA”.

It does not have restrictions on search terms as with CLARA for any subset of objects. 

The basic CLARANS method starts with selecting a few pairs, say (i, h), instead of working on the whole dataset. It starts with randomly selected medoids and then checks for *minimal dissimilarity measure* i.e. it looks for medoid which is extremely near, termed as “*Max-Neighbour*” pair for swapping. If the cost is negative, it just updates the medoid set and the process continues. The process ends after reaching the optimal medoid set (termed as “*Num-Local*”) is achieved.

**Advantages**:

1. It is thought to be better than most medoid-based algorithms like k-medoids and CLARA.

2. It is more flexible, efficient, and scalable.

3. It covers major aspects of outliers.

4. It is robust to noisy data.

**Disadvantages**:

1. It assumes that every object of the entire data set fits into the main memory and hence is very sensitive to input order.

2. The trimming aspect of “Max-Neighbour”-driven searching degrades the efficiency of finding a true local minimum, or “Loc-Min”.