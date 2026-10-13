
The essence of topology is to give structure to sets, which without topology, is just a vague collection of elements.

### The Distance Function

> **Defintion.** Let $n$ be a positive integer, we define $\mathbb{R}^n$ as the set 
> $$\mathbb{R}^n:= \{(x_1,x_2,...,x_n) : x_i \in \mathbb{R} \text{ for each } i=1,2,...,n\}$$



> **Definition.** (Distance Function)
> The distance between two points: $p=(x_1,x_2,...,x_n), q = (y_1, y_1,...,y_n) \in \mathbb{R}^n$ is given by the distance function which is given by
> $$||p-q|| := \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$
> 
---
*Proposition.*  (Properties of the distance function in $\mathbb{R}^n$)
1. $||p-q|| \geq 0$ for any $p,q \in \mathbb{R}^n$  *(Non-negativity)*

2. $||p-q|| = 0$ if and only if $p=q$.

3. $||p-q|| = ||q-p||$ *(Commutativity)*

4. $||p-q|| \leq ||p-r|| + ||r-q||$ *(Triangle Inequality)*

---

### Metric Spaces

==**Definition.**==
A metric space $S$ is a set together with a function $\rho: S \to [0, +\infty)$ that satisfies the following properties:
- $\rho(p,q) = 0$ if and only if $p=q$, for all $(p,q) \in S \times S$ 



- $\rho(p,q) = \rho(q,p)$ *Symmetry*

- $\rho(p,q) \leq \rho(p,r) + \rho(r,q)$  *Triangle Inequality*
---

> The function $\rho$ is called a 'metric'. This is an abstraction of the concept of the distance function in $\mathbb{R}^n$

---
###### Examples
- The set $\mathbb{R}^n$ is a metric space under the usual distance formula.
- The set $\mathbb{R}$ is a metric space under absolute value.
- (Discrete Metric) Let $S$ be a nonempty set. The discrete metric on $S$ is defined by 
![[Pasted image 20211014153043.png]]
- The set of integrable functions is a metric space under the metric defined by $$\rho(f(x),g(x) = \sqrt{\int_a^b (f(t) - g(t))^2dt}$$
- *More examples on the module.*

---
###### Open subsets in a Metric Space

^ae93f6



**Definition.** (Open subsets in a metric space). Let $(S,\rho)$ be a metric space.
1. The ==open ball==$B(s_0, a)$ of radius $a \geq 0$ centered at $s_0$ is defined as $$B(s_0, a):=\{ s \in S : \rho(s,s_0) < a\}$$

> The open ball contains all the points $s \in S$ at least a distance from $s_0$.

2. A subset $U \subset S$ is called an ==open set== in the metric space $(S,\rho)$ if for all points $p \in U$, there exists a radius $\epsilon_p > 0$, depending on $p$ such that the open ball $B(p,\epsilon_p) \in U$.

> A set is open if for every element in the set, you can find an open ball inside that set.

---
###### Open subsets in a metric space
**Proposition.** (Open subsets in a Metric Space)
Let $(S,\rho)$ be a metric space.
- All open balls $B(p,r)$, where $p \in S$ and $r>0$ are open.



- The empty set and $S$ are open.

- The union of an aribtrary collection of open sets in the metric space, is also open.
> If $\{U_w\}_{w \in W}$ is an arbitrary collection of open sets in $(S,\rho)$, then $\bigcup_{w \in W}U_w$ is also open.

- The intersection of a finite number of sets in the metric space, is also open.
	> If $U_1, U_2,...,U_n$ are open sets, then $\bigcap_{i=1}^n U_i$ is also open.

#exercise Proof of the above proposition.

---


###### Closed Sets in a Metric Space
==**Definition.**== (Closed sets in a metric space)
Let $(S,ρ)$ be a metric space.



1. The closed ball $\overline{B(s_0, a)}$ of radius $a \leq 0$ centered at $s_0$ is defined as $$\overline{B(s_0, a)} = \{s\in S : \rho(s,s_0) \leq a\}$$

> Note that the difference of the definition of open and closed sets lies with the *additional* equality relation.

2. A subset $V \subset S$ is a closed set in $(S, \rho)$ if and only if the complement $S/V$ is open.

> Note that the open ball is always a subset of the closed ball. That is, for any $p\in S$ and $r\geq 0$, we have $B(s_0, a) \subset \overline{B(s_0, a)}$.

---
**Proposition.** (Closed sets in a metric space) Let $(S,\rho)$ be a metric space.
- All closed balls $B(p,r)$ with $p\in S$ and $r>0$ are closed.

- The empty set an $S$ are closed.
- The intersection of arbitrary collection of closed sets in S is closed.
> If $\{U_w\}_{w \in W}$ is an arbitrary collection of closed sets in $(S,\rho)$, then $\bigcap_{w \in W}U_w$ is also closed.

- The union of finite number of closed sets in S is also closed.
> If $U_1, U_2,...,U_n$ are closed sets, then $\bigcup_{i=1}^n U_i$ is also closed.

#exercise Show proof of above proposition.

---



**Definition.** (Continuity of a Funtion) 
Let $f: (S, \rho) \to (T, \tau)$ be a function from the metric space $(S, \rho)$ to the metric space $(T, \tau)$.

- (Continuity at a point) The function $f$ is continous at $p\in S$ if for all $\epsilon > 0$, there exists $\delta$ such that $\tau(f(p) , f(q)) < \epsilon$ whenever $\rho(p,q) < \delta$

- (Continuity over a set) The function $f$ is continuous on $S$ if it is continous on every point $p \in S$.

---
**Proposition 2.31.** (Continuity of a Function over two metric spaces)
Let $f: (S, \rho) \to (T, \tau)$ be a function from the metric space $(S, \rho)$ to the metric space $(T, \tau)$.

1. The function $f$ is continuous at $p\in S$ if for every open set $\mathcal{U} \in T$, the pre-image $f^{-1}(\mathcal{U})$ contains a subset $\mathcal{O}$ such that $p \in \mathcal{O}$

2. The function $f$ is continuous iff the pre-image $f^{-1}(\mathcal{U})$ of overy open set $\mathcal{U}$ in $T$ is open in $S$.

#exercise Verify the proof of these two propositions.
[[Proof - Proposition 2.31.1]]
[[Proof - Proposition 2.31.2]]



---
#exercise Do exercises portion of module 2.