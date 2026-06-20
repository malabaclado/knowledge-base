

==**Recall.**== (Ways to show open sets in a metric space)
In a metric space $(S,\rho)$, the following are equivalent.
- A subset $U \subset S$ is open.

- For all $s \in U$, there exists $\epsilon > 0$ (possibly depending on $s$) such that $B(s,\epsilon) \subset U$.
- For all $s \in U$, there exists $\epsilon > 0$ (possibly depending on $s$) such that for all $y \in S, |y-s| < \epsilon$ implies $y \in U$.


==**Recall:**== **Proposition.** (Open subsets in a Metric Space)
Let $(S,\rho)$ be a metric space.
- The empty set and $S$ are open.

- The union of an aribtrary collection of open sets in the metric space, is also open.
> If $\{U_w\}_{w \in W}$ is an arbitrary collection of open sets in $(S,\rho)$, then $\bigcup_{w \in W}U_w$ is also open.

- The intersection of a finite number of sets in the metric space, is also open.
	> If $U_1, U_2,...,U_n$ are open sets, then $\bigcap_{i=1}^n U_i$ is also open.

These three properties of open sets in a metric space is the inspiration for the development of topological spaces.

---
### Topological spaces
==**Definition.**== (Topological space)
A topogical space is a set $X$ together with a collection of $\mathscr{T}$ subsets of $X$ such that:
1. The empty set $\emptyset$ and $X$ are in $\mathscr{T}$
2. If $\mathscr{U} \subset \mathscr{T}$, then $\bigcup_{U \in \mathscr{U}} U \in \mathscr{T}$.
3. If $U_1, U_2,..., U_n$ are elements of $\mathscr{T}$, then $\bigcap_{U \in \mathscr{U}} U \in \mathscr{T}$


Note: The elements of $\mathscr{T}$ are called the open sets in $X$. The collection $\mathscr{T}$ is called a topology on $X$.

---
Examples
- For any set $X$, there are two trivial topologies:
	- (==Discrete Topology==) The collection $\mathscr{T} =\ \mathcal{P}(X)$ equal to the power set of $X$ is a topology on $X$.
	
	- (==Indiscrete topology==) The collection $\mathscr{T} = \{\emptyset, X\}$ is a topology on $X$. 
#exercise  Show that these two are topologies on X

- The collection of all open sets in a metric space $S$ is a topology on $S$. This topology is called the metric topology induced by the given metric.


- Let $X$ be a set. The set $$\mathscr{T}_f:= \{U \in X : X\backslash U \text{ is finite or } U = \emptyset\}$$ is a topology on $X$, called the ==finite complement topology==. #exercise  (show proof)

---
### Closed subsets of topological spaces

==**Definition.**== A subset $V \subset X$ of a topological space $(X, \mathscr{T})$ is closed if and only if $X \backslash V$ is open.


Examples.
- In discrete topology $(X, \mathcal{P}(X))$, every set is both open and closed.

- In the indiscrete topology $(X, \{\emptyset, X\})$, the only open sets are $\emptyset$ and $X$. Hence, $\emptyset$ and $X$ are also the only closed sets.
- Suppose $X$ is a finite nonempty set. If $X$ is given the topology $\mathscr{T}_f$, then every set in $X$ is both open and closed.
- Suppose $X$ is an infinite topology and $X$ is a finite subset of $X$. If $X$ is given the topology $\mathscr{T}_f$, then $X\backslash V$ is finite. This means $X\backslash V$ is open. Thus, the empty set, $X$ and finite subsets are the closed subsets in $(X, X\backslash V_f)$. 
> However, it must be noted that an infinite set may or may not be open.

---
==**Proposition.**== (Closed subsets in a topological space)
Let $(X, \mathscr{T})$ be a topological space. Then
1. The empty set $\emptyset$ and $X$ are closed.
2. artbitraty intersections of closed sets are closed.
3. finite unions of closed sets are closed.

#exercise show proof

> **Remark.** A topology on a set $X$ can also be defined by identifying the closed sets in $X$.


---
### Subspace Topologies
==**Proposition.**== Let $(X, \mathscr{T})$ be a topological space. If $Y \subset X$, the collection $$\mathcal{T}_Y:= \{Y \cap U : U \in \mathscr{T}\}$$
is a topology on $Y$


==**Definition.**== The topology $\mathcal{T}_Y$, as defined above, is called the subspace topology on $Y$ induced by the topology $\mathscr{T}$ on $X$ (or inherited from the space $X$).

> Proof. 

> **Remark.** When dealing with a topological space $X$ and a subspace $Y$, one has to exercise caution with the term open sets because it is possible for a set $U$ to be open in $Y$ but not in $X$.


---
==**Proposition.**==
Let $X$ be a topological space and $Y\subset X$. If $Y$ is open in $X$ and $U$ is open in $Y$, then $U$ is open on $X$.

[[Proof. Open subsets of an open set is open]]


---
==**Proposition. **==
 Let $Y \subset X$ and $(X, \mathscr{T})$ be a topological space.
 - $V$ is closed in $Y$ if and only if $V = V' \cap Y$ for some closed set $V'$ in $X$.
 
 - $Y$ is closed in $X$ and $V$ is closed in $Y$ imply that $V$ is closed in $X$.


---

![[Pasted image 20211016123611.png]]