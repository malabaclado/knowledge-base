
### Details
Source: [Math 171 Class](https://www.youtube.com/watch?v=AOdfMwM4mek&t=560s) 

### Notes
We're going to discuss numerical methods for approximating a definite integral $$\int_a^b f(x)dx$$

In particular we'll discuss 4 methods:
1. Trapezoidal Rule
2. Simpson's Rule
3. Newton-Cotes Rule
4. Composite Rule


### Trapezoidal Rule
Using the first-order lagrange polynomial:


$$\int_1^b f(x)dx = \frac{h}{2}[f(a)+f(b)]+O(h^3)$$

**Error:**
$$err = -\frac{h^3}{12}f''(\zeta)$$


This method gives exact approximations for polynomials of at most first degree.

### Simpson's Rule
Using the trapezoidal rule with the second-order lagrange polynomial, we get the Simpson's rule.


$$\int_1^b f(x)dx = \frac{h}{3}[f(x_0)+4f(x_1)+f(x_2)] + O(h^4)$$

where $x_0=a, x_2=b$ and $x_1$ is the midpoint of $[a,b]$.

$$err = -\frac{h^5}{90}f^{(4)}(\zeta)$$

### Newton-Cotes Rule
We have two types of Newton-Cotes:
1. Closed -> the points a,b in the interval [a,b]are used as endpoints. (eg. Trapezoidal rule, Simpson's rule)
2. Open -> the endpoints are not included in the computation.


#### Midpoint Rule
This method is categorized under the Open Newton-Cotes Rules.
It basically looks for the midpoint of the interval and approximates the integral from there.


$$\int_a^b f(x)dx = 2hf(x_0) + O(h^3)$$

**Error:**
$$err=\frac{h^3}{3}f''(\zeta)$$

This method is gives exact result for linear functions.

### Composite Rule
So far, all our methods use only a single interval. The concept of  the composite rule is to subdivide the interval [a,b] into smaller intervals, integrate with respect to each subintervals and add the results.


#### Composite Trapezoidal Rule
- divide [a,b] into N subintervals
- integrate each subintervals using the Trapezoidal rule
- add each result


$$\int_a^b f(x)dx = \frac{h}{2} [f(a) + f(b) + 2\sum_{i=1}^{N-1}f(x_1)] + O(h^2)$$

**Error:**

$$O(h^2) = - \frac{(b-a)}{12}h^2f''(\zeta)$$

#### Composite Simpson's Rule
- divide [a,b] into N=2m subintervals.


$$\int_a^b f(x)dx = \frac{h}{3} [f(a) + f(b) + 2\sum_i f(x_{2i}) + 4\sum_i f(x_{2i-1})]$$

#### Composite Midpoint Rule



### Comments

