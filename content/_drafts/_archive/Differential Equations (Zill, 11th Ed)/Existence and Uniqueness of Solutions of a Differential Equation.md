Given an initial-value problem:

$$y' = f(x,y), \quad y(x_0)=y_0$$

we have the ff question:
1. Does a solution *exist*?
2. Is that solution *unique*?


Theorem
If $f$ and $\frac{\partial f}{\partial y}$ are continuous near $(x_0, y_0)$, then there is a unique solution on an interval $\alpha < x_0 < \beta$ to the initial-value problem: $$y' = f(x,y), \quad y(x_0)=y_0$$

Remarks
- The above theorem is both existence and uniqueness theorem
- The existence of a solution to a DE is quaranteed by the first condition - that is if $f$ is a continuous function near $(x_0, y_0)$


--- 
Solutions to a differential equation is always considered at a point - from an initial-value problem.

3 CASES FOR A SOLUTION OF A DIFFERENTIAL EQUATION AT A POINT
 
 If we're considering solutions to a DE at a point, there are three possibilities:
 
 1. *No solution at the particular point.* 

	- This doesn't mean that the DE has no solution. There might be a family of solution for that DE but no solution at a particular point.

2. *Infinitely many solutions at a point.*

	- Usually happens to equilibrium points.

3. *There is one unique solution to the DE in the neighborhood of that point.* 

	-	If $f(x,y)$ is continuous around $(a,b)$ - open interval atound $x=a$, then there exists at least one solution.
	-	If $\frac{\partial f}{\partial y}$ is also continuous around $(a,b)$, then the solution to the differential equation at $(a,b)$ is unique on the open interval around $x=a$


---
**Exercise**
Check for existence and uniqueness of solutions for the following initial-value problems: *(For first time answering, write your solutions below each item)*

1. $\frac{dy}{dx} = 2x^2y^2, \quad y(1)= -1$
2. $\frac{dy}{dx} = x ln(y), \quad y(1)= 1$
3. $\frac{dy}{dx} = \sqrt[3]{y}, \quad y(0)= 1$
4. $\frac{dy}{dx} = \sqrt[3]{y}, \quad y(0)= 0$
5. $\frac{dy}{dx} = \sqrt{x-y}, \quad y(2)= 2$
6. $\frac{dy}{dx} = \sqrt{x-y}, \quad y(2)= 1$


Note:
- Check solutions at [Existence and Uniqueness of Solutions (Differential Equations 11) - YouTube](https://www.youtube.com/watch?v=BVKyaEu1FWk&list=PLDesaqWTN6ESPaHy2QUKVaXNZuQNxkYQ_&index=15)