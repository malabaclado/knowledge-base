[[Math 171 MOC]]

Class date: 
Tags: #course/math-171 #topic/math/numerical-analysis 

---

# Solution of Nonlinear Equations
This chapter introduces iterative methods for locating the solution $x$ of the equation $f(x)=0$. We'll examine when a solution exists, the conditions for convergence of each method, the rate of convergence and accuracy of each method.



---
==**Remark:**== $f\in C^2$ means that the function f is continuous up to its second derivative.


## Some definitions on convergence
Give the definition of the following terminologies:


[[Rate of Convergence]]
[[Order of Convergence]] 
[[Linear Convergence]]
[[Locally Convergent]]

---


## Bisection Method
---

##### How does the bisection method work?
1.  Start with an interval [a,b]
3.  Denote the midpoint of $[a,b]$ as $c$
4.  Identify whether the solution is in $[a,c]$ or $[c,b]$
5.  Iterate until you break the stopping criteria.
6.  The approximate root is the midpoint of the final interval.


Bisection Method Pseudocode: 
![[Pasted image 20210330155853.png]]


---
##### What guarantees the existence of a root in a specific interval?
Recall: [[Intermediate Value Theorem]]
We use the following corollary to [[Intermediate Value Theorem]]:


==**Corollary.**== The polynomial $f(x)=0$ has a root in the interval $[a,b]$ if $f(a)f(b)<0$.

==Intuition:== If the y-values of the two endpoints are in the opposing sides of the x-axis, then the graph of a  continuous in that interval would surely cross the x-axis, thus having a zero in that interval.

---

##### What are the conditions for the Bisection Method to converge?
1. f must have a root on the interval [a,b] *(meaning f(a)f(b)<0)*
2. f must be differentiable on the interval [a,b]


*These conditions are stated in this theorem:*

==**Theorem.**== (Bisection Theorem)
Suppose $f\in C[a,b]$ and $f(a)f(b)<0$. The Bisection method generates a sequence $\{c_n\}$ approximating a zero $x*$ of f with $$|c_n-x*|\leq \frac{b-a}{2^{n-1}}$$

The theorem implies that as long as the above conditions are satisfied, the Bisection Theorem *always converge* albeit *slow*.

The Bisection method is linearly convergent with rate of convergence $O(\frac{1}{2^{n+1}})$. 

---




##### How many iterations would it take the bisection method to obtain an accuracy $\epsilon$ (tolerance), given interval $[a_0,b_0]$?

The number of iterations N needed in a bisection method to achieve an accuracy of $\epsilon$ is $$N\geq \frac{ln(b_0 -a_0)-ln \epsilon}{2}$$


For the Bisection Method, the question of how many steps to run is a simpleone—just choose the desired precision and find the number of necessary steps.

---

##### How accurate is the Bisection Method?
Solution error in using the Bisection Error is given by $|x_c-r|$ where $$|x_c-r|\leq \frac{b-a}{2^{n-1}}$$


A good way to assess the efficiency of the Bisection Method is to ask how much accuracy can be bought per function evaluation. Each step, or each function evaluation, *cuts the uncertainty in the root by a factor of two*.

The above formula can be used to determnine the number of iterations of a bisection process until the desired solution error is achieved.

---
==**Definition.**==  A solution is correct within p decimal places if the error is less than $0.5\times 10^{-p}$

---



---


## Fixed-Point Iteration Method
Recall:
[[Continuous Limits Theorem]]
[[Mean Value Theorem]]


---

Definition: [[Fixed Point]]

---
Fixed-Point Iteration solves the fixed-point problem $g(x)=x$, but we are primarily interested in solving  the roots of an equation. Hence it is a necessary step to express $f(x)=0$ to $g(x)=x$ before using the Fixed Point Iteration Method.
 
Once the equation is written as $g(x)=x$, Fixed-Point Iteration proceeds by starting with an initial guess $x_0$ and iterating the function $g$.

Pseudocode for the Fixed Point Iteration Method:
![[Pasted image 20210330165747.png]]


---
##### The Geometry of the Fixed Point Iteration

![[Pasted image 20210331125431.png]]


---
##### What conditions are necessary for the Fixed-Point Iteration to converge?

1. g(x)=x -> has a fixed-point/ intersects with the identity function
2.  $g(x) \in C[a,b]$ -> g(x) is continuously differentiable on interval (a,b) 
3.  $|g'(x)|<1$ -> the absolute value of the derivative of g(x) is  less than 1 (this is actually the rate of convergence of the FPI)


*The above conditions are stated in this theorem:*

> ==Theorem== (Fixed-Point Theorem)
> Suppose $g$ is continuously differentiable, $g(r)=r$ and $S=|g'(r)|<1$. Then the Fixed Point Iteration converges linearly with rate S to the fixed point r for any initial guesses sufficiently close to r.
> 
> If $S>1$, then the FPI diverges. This means that the process moves away and away from the true solution.
> 
---


## Newton's Method

The [[Newton's Method]] is a special case of the Fixed-Point Iteration method.


This is also called as Newton-Raphson Method

Iterative Formula:
![[Pasted image 20210331130144.png]]

---
##### Geometric Intuition
![[Pasted image 20210331130421.png]]


---

##### Necessary conditions for Newton's Method to converge:
Recall: [[Taylor's Theorem of order n]]


1. $f(x) \in C^2[a,b]$ -> f(x) must be continuously differentiable up to second degree on the interval [a,b].


---
##### Convergence of Newton's Method
TL;DR There are two possible rates of convergence for Newton's Method. When $f'(r)\neq 0$, Newton's method follows quadratic convergence. When $f'(r)=0$, Newton's method follows linear convergence. 



###### Quadratic Convergence 

> ==**Theorem**== Let be twice continuously differentiable and f(r)=0. If $f'(r)\neq 0$, then Newton's method is **locally**  and **quadratically convergent** to r. The error $e_i$ at step $i$ satisfies $$\lim_{i\to \infty} \frac{e_{i+1}}{e_i^2}=M$$ where $$M=\frac{f''(r)}{2f'(r)}$$



==**Proof of Theorem**==
- **To prove local convergence**: note that Newton's Method is a particular form of the Fixed-Point Iteration with $$g(x)=x_0-\frac{f(x)}{f'(x)}$$ Taking the derivative, $$g'(x)=\frac{f(x)f''(x)}{f'(x)^2}$$
Since $g'(r)=0$, Newton's method is locally convergent by [[Fixed Point Theorem]].

- **To prove quadratic convergence**, we derive Newton’s Method a second way, this time keeping a close eye on the error at each step. By error, we mean the difference between the correct root and the current best guess.

###### Linear Convergence

Suppose the (m+1)-times continuously differentiable function f on [a,b] has a multiplicity m root at r. Then Newton's method is locally convergent to r, and the error $e_i$ satisfies $$\lim_{i\to \infty} \frac{e_i+1}{e_i}=S$$ where $S= \frac{m-1}{m}$


---



##### Modified Newton's Method

If the multiplicity of a root is known in advance, convergence of Newton’s Methodcan be improved with a small modification.


==**Theorem**== If f is (m+1)-times continuously differentiable on [a,b], which contains a root $r$ of multiplicity m>1, then $$x_{i+1}=x_i-\frac{mf(x_i)}{f'(x_i)}$$ converges locally and quadratically to r.

---
##### Stopping criteria
1. $|X_N-X_{N-1}|<\epsilon$
2. $\frac{|X_N-X_{N-1}|}{X_N}<\epsilon$



---

## Secant Method
This method is a variant of the [[Newton's Method]]. Secant method is used when you cannot compute the derivative of f(x).


In this method, we're going to use the secant line instead of the tangent line, replacing the derivative of the function by a quotient. 

![[Pasted image 20210402162214.png]]

The convergence of the Secant Method to simple roots is called superlinear, meaning that it lies between linearly andquadratically convergent methods

---
Geometry of the Secant Method
![[Pasted image 20210402162508.png]]

---

### Three Generalizations of the Secant Method
1. Method of False Position


This is also known as [[Regula Falsi]]. This is similar to BIsection Method but instead of the midpoint, the third point is obtained by using  the secant line. Given an interval [a,b], define the next point: $$c=\frac{bf(a)-af(b)}{f(a)-f(b)}$$

---

2. Muller's Method

Muller's method is a root-finding [[Algorithm]] based on the secant method. It uses three initial points $x_1,x_2,x_3$, then draws a parabola $y=p(x)$ through them and intersecting them with the x-axis. The parabola will generally intersect in 0 or 2 points. If there are two intersection points, the one nearest to the last point $x_2$ is chosen to be $x_3$. It is a simple matter of the quadratic formula to determine the two possibilities. Ifthe parabola misses the x-axis, there are complex number solutions.


3. Inverse Quadratic Interpolation

---
