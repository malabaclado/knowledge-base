# Numerical Methods for Interpolation
tags:
[[Math 171 MOC]]


---
[[Interpolation]] is the process of fitting a curve to a set of discrete points for the purpose of estimating values within the range of those values. [[Extrapolation]] refers to a somewhat similar process used to predict values outside the given range. This is possible when you have a somewhat accurate interpolating curve.

---

**Problem:** Given a set of data points
1. give a value at some intermediate point
2. find a function that describes the data

**Recall:** [[Weirstrass Approximation Theorem]]
> ==**Theorem**==  (Weirstrass Approximation Theorem)
> Let f be a continuously differentiable function. For each $\epsilon>0$, there exists a polynomial P(x) such that $$|f(x)-P(x)|<\epsilon$$ for all $x\in[a,b]$

**Idea:** Polynomials can be used to interpolate the data points.
**Question:** Can we use [[Taylor Polynomials]]? -> NO. We are just limited to a certain range when using Taylor Polynomials.

*What makes a good interpolating polynomial?*  -> It should be *relatively accurate at all data points*.


## Polynomial Interpolation
Given a set of data points $x_1,x_2,x_3,\ldots , x_n$,


Find a polynomial P of degree at most $n$ such that $$P(X_k)=y_k$$ for $k=0,1,2,\ldots ,n$

In this case, P is called an **interpolating polynomial** and the $x_k$ are called **interpolation points/ nodes**

---

[[Condition Number]]

==**Definition.**== Condition number for a computational task measures how sensitive the answer is to changes in the input data and roundoff errors in the solution process.

- A problem with low condition number is said to be **well-conditioned**
- A problem with high condition number is **ill-conditioned**


---
**Condition number for determining the inverse of a matrix** 

---




### 1. Monomial Basis
This is also known as the vandermonde matrix


Consider the monomial basis $$m_k(x)=x^a \qquad k=0,1,...,n$$
Then the interpolating polynomial is of the form: $$P(x)=a_0+a_1x+a_2x^2+...+a_nx^n$$

The linear system associated to the problem is: 
![[Pasted image 20210403184700.png]]

Related: [[Vandermonde Matrix]]



---


### 2. Lagrange Basis
Consider the basis: $$l_k(x)=\prod \frac{x-x_1}{x_k - x_i}, \qquad k=0,1,...,n$$


The linear system associated with this interpoloation is:
![[Pasted image 20210404121649.png]]

The interpolating polynomial is of the form: $$P(x)=\sum y_k l_k(x), \qquad k=0,1,...,n$$


[[Lagrange elementary polynomials]]
[[Lagrange Interpolation Theorem]]

---
### 3. Newton Basis
Consider the basis: $$n_k(x)=\prod_{i=0}^{k-1} (x-x_i), \qquad k=0,1,...,n$$


The linear system associated with this interpolation is: 
![[Pasted image 20210404123522.png]]

Note that $n_k(x)=0$ for all $i<j$. This results in a lower triangular matrix and is solvable using forward direct substitution.

---

## Piecewise Interpolation
Also known as ==spline interpolation==.


The problem with polynomial interpolation is that the larger the data set, the higher the degree of the interpolating polynomial hence, the more oscillations in the graph ==*and we don't want that because oscillations are like indecisiveness -> inaccurate*==.

We remedy this by using piecewise function. Basically, we find an interpolating curve on each interval $[x_i,x_{i+1}]$. Then we form a piecewise function from these inteval-specific curves. We can use straight lines - this techniques is called ==linear spline interpolation==. We can also use derivatives to smoothen out our curve. We may opt to use ==quadratic spline interpolation== but the most common to use is the ==cubic spline interpolation== - which utilizes up to the second derivative.


### Cubic Spline Interpolation

Let $(x_1,y_1),...,(x_n,y_n)$ be a set of n-data points.


A ==cubic spline S(x)== is a set of $(n-1)$ cubic polynomials of the form $$S_i(x)=a_i +b_i(x-x_i) +c_i(x-x_i)^2 +d_i(x-x_i)^3$$ with the following properties:
![[Pasted image 20210404183516.png]]

Remarks:
- Property 1 guarantees that the spline S(x) interpolates the data points. Property 2 forces the slopes of neighboring parts of the spline to agree where they meet, and Property 3 does the same for the curvature, represented by the second derivative.

---

### Boundary Conditions

1. Natural Spline
$S_1''(x_1)=0$ and $S_{n-1}''(x_n)=0$$


3. Curvature-adjusted Cubic Spline


5. Clamped Cubic Spline
6. Parabolically terminated Cubic Spline
7. Not-a-know Cubic Spline


