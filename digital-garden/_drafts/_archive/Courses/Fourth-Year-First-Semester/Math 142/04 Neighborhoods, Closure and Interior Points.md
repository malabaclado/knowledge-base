
### Neighborhood of x
==**Definition.**== (Neighborhood)
Let $(X, \mathscr{T})$ be a topological space and $x \in X$. The subset $V \subset X$ is a neighborhood of $x$ if and only if there exists an open set $U \subset V$ such that $x \in U$.



==**Proposition.**==
Let $(X, \mathscr{T})$ be a topological space and $p \in X$.
1. A subset $N \subset X$ is a neighborhood of all its points if and only if $N$ is open.

2. If $N$ is a neighborhood of $p$ and $N \subset N' \subset X$, then $N'$ is also a neighborhood of $p$.
3. If $N_1, N_2,...,N_r$ are neighborhoods of $p$, then the intersection $\bigcap^n_{i=1}N_i$ is also a neighborhood of $p$.
4. If $N$ is a neighborhood of $p$, then $p \in N$

#exercise Show proof.

---

### Interior, Exterior and Boundary
Note. Let $X$ be a topological space $x\in X$ and $A \subset X$. Exactly one of the following holds.
1. There exists an open set $U$ such that $x \in U \subset A$.
2. There exists an open set $U$ such that $x \in U \subset (X\backslash A)$
3. Every open set $U$ containing $x$ satisfies $U \cap A \neq \emptyset$ and $U \cap (X\backslash A) \neq \emptyset$.


> (3) means that all open sets containing $x$ intersects with both $A$ and its complement $X/A$



==**Definition.**==
Let $X$ be a topological space and $A \subset X$.
1. A point $x \in X$ is an ==interior point== of A: if there exists an open set $U$ such that $x \in U \subset A$. 
	- The set of all interior points of A, denoted $\text{int } A$ or $A^0$, is called the ==interior of A==.

2. A point $x \in X$ is an ==exterior point== of A if there exists and open set $U$ such that $x \in U \subset (X\backslash A)$.
	- The set of all exterior points of A, denoted $\text{ext }A$ or $(X\backslash A)^0$ , is called the exterior of $A$.
3. A point $x \in X$ is called a boundary point of $A$ if for  every open set $U$ that contains $x$, $U \cap A \neq \emptyset$ and $U \cap (X\backslash A) \neq \emptyset$. 
	- The collection of all boundary points of $A$, denoted $\partial A$, is called the boundary of $A$.
4. The closure of $A$, denoted $\overline{A}$, is deined to be $\overline{A} = A^0 \sqcup \partial A$.

---
**Remark.** Note that for any topological space $X$ and any subset $A \subset X$, we have $$X = A^0 \sqcup \partial A \sqcup (X\backslash A)$$
where $\sqcup$ denote disjoint unions. 

> That is, the set X is partitioned into three subsets: $A^0$, $\partial A$ and $(X \backslash A)^0$


---
Let $X$ be a topological space and $A \subset X$. The following statements follow immediately from the definitions.
1. $A^0 \subset A \subset \overline{A}$ 

> *The interior of A is a subset of the closure of A.*

2. $X\backslash \overline{A} = (X\backslash A)^0$

> *The complement of the closure is the interior of the complement*

3. The set of interior points $A^0$ is open

4. The closure $\overline{A}$ is closed

5. The set $A$ is open if and only if $A = A^0$

6. The set $A$ is closed if and only if $A = \overline{A}$
7. If $U$ is an open set and $U \subset A$, then $U \subset A^0$. ^f2695f

> The interior $A^0$ is the largest open set in $A$.

8. If $V$ is a closed set and $A \subset V$, then $\overline{A} \subset V$. ^626037

> The closure $\overline{A}$ is the smallest closed set containing $A$.

---
==**Proposition.**==
Let $X$ be a topological space and $A \subset B \subset X$, then
1. $A^0 \subset  B^0$

> The interior of A is a subset of the interior of B.

2. $\overline{A} \subset \overline{B}$

> The closure of A is a subset of the closure of B

Proof. 
1. Observe that $A^0 \subset A \subset B$ and $A^0$ is open. By [[04 Neighborhoods, Closure and Interior Points#^f2695f | Proposition 7 ]], $A^0 \subset B^0$.

2. Likewise, $\overline{B}$ is a closed set and $A \subset B \subset \overline{B}$. By [[04 Neighborhoods, Closure and Interior Points#^626037 | Proposition 8]], $\overline{A} \subset \overline{B}$.


---
==**Proposition.**==
Let $X$ be a topological space and $A,B$ be subsets of $X$.
1. $\emptyset^0 = \overline{\emptyset} = \emptyset$ and $X^0 = \overline{X} = X$ and $\partial \emptyset = \partial X = \emptyset$.

2. $(A^0)^0 = A^0$ and $\overline{\overline{A}} = \overline{A}$

3. $(A^0 \cup B^0) \subset (A\cup B)^0$, $\partial (A\cup B) \subset (\partial A \cup \partial B)$ and $\overline{A \cap B} = \overline{A} \cap \overline{B}$
4. $(A^0 \cap B^0) = (A \cap B)^0$ and $\overline{A \cup B} = \overline{A} \cup \overline{B}$

#exercise show proof for item 3 and 4

---
==**Proposition.**==
Let $Y$ be a subspace of $X$ and $A \subset Y$. Let $\overline{A}$ be the closure of $A$ in $X$. Then the closure of $A$ in $Y$ is $\overline{A} \cap Y$.



---
==**Proposition.**==
Let $A$ be a subset of a topological space $X$.
1. A point $x \in A$ if and only if every open set $U$ containing $x$ intersect $A$.

2. If $\mathscr{B}$ is a basis for $X$, $x \in \overline{A}$ if and only if every basis element $B \in \mathscr{B}$ containing $X$ intersects $A$.

#exercise Show proof.

---
### Limit Points
==**Definition.**==
Let $X$ be a topological space and $A \subset X$. A point $x \in X$ is a ==limit point== of $A$ if and only if for all open set $U$ containing $X$ satisfies $(U\backslash \{x\})\cap A \neq \emptyset$.


> Intuitively, a point is a limit point if for all open sets near it, not necessarily containing it, intersects with $A$.

---
###### Examples
Consider the following subset of $\mathbb{R}$ under the usual topology:
- Let $A= (0, 1] \subset \mathbb{R}$. The real number $0$ is a limit point of $A$. The set of limit points of $A$ is $[0,1]$
 - The set $\mathbb{Z}$ has no limit point.
- Every $r \in \mathbb{R}$ is a limit point for $\mathbb{Q}$.

---
==**Proposition 4.14.**== Let $X$ be a topological space and $A \subset X$. If we let $A'$ be the set of all limit points of $A$, then $$\overline{A} = A \cup A'$$

#todo missing proof

---
==**Proposition 4.15**==
A subset of a topological space $X$ is closed if and only if it contains all its limit points.


---
==**Definition 4.16.**==
Let $X$ be a topological space.
1. A subset $A \subset X$ is said to be dense if and only if $\overline{A} = X$.

2. A subset $A \subset X$ is said to be nowhere dense if $(\overline{A})^0 = \emptyset$

---
==**Proposition 4.17**==
The following statements are equivalent:
- $A$ is dense in $X$
- The exterior of $A$ is empty
- Every nonempty open set of $X$ intersects $A$.

Example:
- The set $\mathbb{Q}$ is dense in $\mathbb{R}$
- The cantor set is nowhere dense.