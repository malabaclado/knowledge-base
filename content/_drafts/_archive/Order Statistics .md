
[[Math 150.2 MOC]]

---

**Order statistics** refers to ranking of a random sample. Ranked data may be used for characterizing the cumulative distribution as well as identifying the median and quartiles, or identifying the minimum or maximum of the data.

> ==Definition.== Order Statistics
> Let $X_1,X_2,...,X_n$ be a random sample of size n. If we arrange this sample according to its size and arrive at the arrangement: $Y_1<Y_2<...<Y_n$. We call $Y_1,Y_2,...,Y_n$ the order statistics. 

- $Y_1$ is the smallest observation
- $Y_n$ is the largest observation
- $Y_k$ is called the **kth order statistic**
- Note that the definition assumes a continuous distribution. This assures that there is zero probability that any two observations are equal.


> Theorem. Let $X_1,X_2,...,X_n$ be a random sample from a continuous distribution with probability density function $f(x)$ that has support $S=(a,b)$. The joint probability density function of $Y_1,Y_2,...,Y_n$ is given by $$g(y_1,y_2,...,y_n)=n!\prod_{i=1}^n f(y_i)$$ for $a<y_1<y_2<...<y_n<b$ and zero elsewhere.