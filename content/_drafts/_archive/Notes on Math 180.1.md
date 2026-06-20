**Operations Research**
- also known as management science or decision science
- is a scientific approach to making the best decisions

>' All models are wrong, but some are useful.' 
>- George Box

**Optimization model** - is a model that seeks to find values of the decision variables that optimize one or more objective functions among a set of values that satisfy the given constraints.

**Decision variables** - are controllable variables that influences the system.

**Objective function** - functions that we wish to optimize

**Constraints** - are set of restrictions for the decision variables

**Linear programming**
- where the objective function is a linear function
- every constant must be a linear equality/inequality

---

**Linear Programming Model**
Let: 
$z$ - the value of overall measure of performance
$x_{j}$ - the level of activity $j$, where $j \in \{1,2,3,\dots\}$
$c_{j}$ -the increase in $z$ for each $x_{j}$
$b_{i}$ - the amount of resource available for allocation
$a_{ij}$ - the amount of resource $i$ consumed by each unit of activity $j$

**Standard Form of a Linear Programming Model**
Maximize:
$$z=c_{1}x_{1} + c_{2}x_{2}+\dots+c_{n}x_{n}$$

subject to the following restrictions:
$$a_{11}x_{1}+a_{12}x_{2}+\dots+a_{1n}x_{n} \leq b_{1}$$
$$a_{21}x_{1}+a_{22}x_{2}+\dots+a_{2n}x_{n} \leq b_{2}$$
$$\vdots$$
$$a_{m1}x_{1}+a_{m2}x_{2}+\dots+a_{mn}x_{n} \leq b_{m}$$

and
$$x_{1}, x_{2},\dots,x_{n}\geq 0$$

**Other variations of the Linear Programming Model**
- Minimizing the objective function
- Constraints with $\geq$/$=$ relations
- Decision variables are unrestricted in sign

**The solution to a Linear Programming Problem** - specific values for the decision variables $\{x_{1}, x_{2},\dots,x_{n}\}$.

A **feasible solution** is a solution where all constraints are satisfied while an **infeasible solution** is a solution where at least one of the constraints are violated.

**Assumptions of Linear Programming**
1. Proportionality
2. Additivity
3. Divisibility
4. Certainty

---
**THE ESSENSE OF THE SIMPLEX METHOD**
For any Linear Programming problem with $n$ decision variables, two corner-point feasible (CPF) solutions are *adjacent* to each other if they share $(n-1)$ constraint boundaries. Meaning, they are on the same line. Such line segment formed is called an *edge* of the feasible region.


**Optimality test**
Consider a linear programming problem with at least one optimal solution. If a CPF solution has no adjacent CPF solution that has better measure (relative to $z$), then it must be the **optimal solution**.

---

**6 Key Solution Concepts behind Simplex Method**
1. The Simplex method focuses solely on CPF solutions.
2. It is an iterative algorithm.
3. Whenever possible, the initialization of the simplex method chooses the origin as the initial CPF solution.
4. Each time an iteration is performed, it always chooses an adjacent CPF solition.
5. Instead of solving, the simplex method simply identify the rate of change along the edge.
6. Among the two adjacent CPF solutions, the simplex method chooses the one that gives a better measure of $z$.

---

**Slack variables** = a newly-defined variable from a constraint

For example:
Constraint: $x_1 \leq 4$, which can be transformed to $4-x_1 \geq 0$
Define slack variable $x_2$ such that the constraint becomes: $$x_2 = 4-x_1 \text{ , where } x_2 \geq 0$$

Remark: Using slack variables, the original form of the model takes an *augmented form*.

Further example:
**Original form:**
maximize $Z = 3x_1 + 5x_2$
subject to:
$x_1 \leq 4$, 
$2x_2 \leq 12$,
$3x_1 + 2x_2 \leq 18$, 
and $x_1, x_2 \geq 0$

**Augmented form:**
maximize $Z = 3x_1 + 5x_2$
subject to:
$x_1 + x_3 = 4$
$2x_2 + x_4 = 12$
$3x_1 + 2x_2 + x_5 = 18$
and $x_1, x_2, x_3, x_4, x_5 \geq 0$

---
**Interpretation of Slack Variables**
If the slack variable in the solution is:
- 0, then the solution is on the boundary region.
- >0, then the solution is in the feasible region.
- <0, then the solution is in the infeasible region.
---
Definition:
- An **augmented solution** is a solution for the original variables that has been augmented by corresponding values of the slack variables.
- A **basic solution** is an augmented corner-point solution.
- A **basic feasible (BF) solution** is an augmented corner-point solution.

**Properties of a Basic Solution**
1. A variable is either basic or non-basic.
2. The number of basic variables equals the number of functional constraints.
3. Non-basic variables are set equal to zero.
4. The values of basic variables are the solution to the system of equations (of functional constraints in augmented form)
5. If the basic variables satisfy the non-negativity constraints, then the basic solution is a **BF solution**.

**Adjacent BF solutions**
Two BF solutions are *adjacent* if all but one of their non-basic variables are the same.

For example:
Original solution
(0,0)
(0,6)

Augmented solution
(0,0,4,12,18)
(0,6,4,0,6)

---

