### Lecture
Finer and Coarser Topology
![[Pasted image 20211020134606.png]]


On convergence in finer and coarser topologies
![[Pasted image 20211020135118.png]]

**Taniyama-Shimura Conjecture**
*All elliptic curves are modular*

If you want to prove a theorem on a set $U$, it is useful to see if it applies on the subsets of $U$.

---
Prop. 5.4.1
![[Pasted image 20211020140629.png]]

--- 
Basis := Intersections of elements of X.
Coarsest Topology := Arbitrary unions of elemetns of a basis.

![[Pasted image 20211020141650.png]]

---
How to make a topology on a set X
1. Define a collection $\mathscr{T}$: The open sets are the elements of $\mathscr{T}$
2. Define a basis: The open sets are arbitrary unions of the elements of the basis.
3. Define a subbasis: The open sets are arbitrary unions of finite intersection of elements of the subbasis.

![[Pasted image 20211020142113.png]]

---
### Summary

==**Proposition 5.1**== (Finer and Coarser Topology)
If $\{\mathscr{T}_w\}_{w \in \mathscr{W}}$ is a collection of topologies on a set $X$, then the intersection $\cap_{w \in \mathscr{W}} \mathscr{T}_w$ is also a topology on $X$.

Proof. *Direct proof by definition of topological space.*

---

==**Definition 5.2**==
Let $\mathscr{T}_1$ and $\mathscr{T}_2$ be topologies on a set $X$. We say that $\mathscr{T}_1$ is finer than $\mathscr{T}_2$ (equivalently $\mathscr{T}_2$ is coarser than $\mathscr{T}_1$) if $\mathscr{T}_2 \subset \mathscr{T}_2$.

> Remark. If $\mathscr{T}_1$ is a finer topology than $\mathscr{T}_2$, then the open sets in $\mathscr{T}_2$ are also open in $\mathscr{T}_1$. Likewise, the closed sets in $\mathscr{T}_2$ are also closed in $\mathscr{T}_1$.

---
==**Proposition 5.4**== (Construction of coarsest topology)
Let $X$ be a set and $\mathscr{S}$ be a collection of subsets of $X$ containing $\emptyset$ and $X$.
- There exists a unique topology $\mathscr{T}_{\mathscr{S}}$ which is coarser than every topology on $X$ containing $\mathscr{S}$.
- The topology $\mathscr{T}_{\mathscr{S}}$ can be obtained by following a two-step procedure:
	1. Take all finite intersections of subsets in $\mathscr{S}$.
	2. Take arbitrary unions of the resulting collection.


---
### Basis of a topology
==**Definition 5.6**== (Basis and subbasis)
Let $(X, \mathcal{T})$ be a topological space. Let $\mathcal{S}$ and $\mathcal{B}$ be subsets of $\mathcal{T}$ containing $\emptyset$ and $X$.
- The set $\mathcal{B}$ is a basis for $\mathcal{T}$ if every open subset in $(X, \mathcal{T})$ is a union of open subsets in $\mathcal{B}$.
- The set $\mathcal{S}$ is called a subbasis of $\mathcal{T}$ if and only if the collection of all finite intersections of elements of $\mathcal{S}$ forms a basis for $\mathcal{T}$



> Question to ponder: Under what conditions will a collection $\mathcal{B}$ of subsets of $X$ constitutes a basis for some topologies on $X$?

---
==**Proposition 5.9**== (Construction of a basis)
Let $X$ be a set and $\mathcal{P}(X)$ denote the power set of $X$. Let $\mathcal{B} \subset \mathcal{P}(X)$ such that
- $\emptyset \in \mathcal{B}$

- $\bigcup_{B \in \mathcal{B}}B = X$
- If $B_1$ and $B_2$ are in B, then there exists a set $\overline{\mathcal{B}} \subset \mathcal{B}$ such that $\bigcup_{B \in \overline{\mathcal{B}}}B = B_1 \cap B_2$, 

Then $$\mathcal{U}_\mathcal{B} = \{U \in \mathcal{P}(X) : U \text{ is the union of elements of } \mathcal{B}\}$$ is a topology on $X$ having $\mathcal{B}$ as a basis.


---
==**Proposition 5.12**== (Basis for a subspace topology)
Let $\mathcal{B}$ be a basis for the topology on $X$, then $\mathcal{B}_Y = \{B\cap Y : B \in \mathcal{B}\}$ is a basis for the subspace topology on $Y$ inherited from $X$.


