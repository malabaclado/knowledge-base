
# Objectives 
1. Define the notion of compactness in arbitrary topological spaces.
2. Characterize compact spaces
3. Learn familiar examples of compact spaces.


---
In real analysis, we learned that the subsets of $\mathbb{R}$ which are compact are those that are **closed** and **bounded**.

**Compactness** is a very important condition in optimization.

We already have a notion of *'closedness'* in our study of topological spaces. However, we do not have a notion of *'boundedness'* in this context. 

So how are we going to define compactness in arbitrary topological spaces? -> We start with the concept of *open covering*.

# Open Covering

**Definition.** Let $X$ be a set.
1. A collection $\mathcal{U}$ of subsets of $X$ is a *covering of $X$* if and only if $$\bigcup_{U \in \mathcal{U}} U =X$$
2. If $X$ is a topological space and each $U \in \mathcal{U}$ is an open set in $X$, then the collection $\mathcal{U}$ is called an *open covering of $X$*.
3. If a subset of an open covering of $X$ is also an open cover of $X$ then we call this subset the *open subcover of $X$*.


---
**Definition.** Let $X$ be a topological space. 
1. A collection $\mathscr{A}$ of subsets of $X$ is said to *cover* $X$ if and only if $$X \subset \bigcup_{A\in \mathscr{A}} A$$
2. The collection $\mathscr{A}$ is called an *open covering* (also *open cover*) of $X$ if all its elements are open subsets of $X$.
3. A space $X$ is *compact* if every open covering of $X$ contains a finite subcover of $X$.
	- *Finite subcover* refers to a subset of the open covering that contains countably many elements and which also covers $X$.
4. If $Y$ is a subspace of $X$, a collection $\mathscr{A}$ of subsets of $X$ is said to cover $Y$ if and only if $$Y \subset \bigcup_{U \in \mathscr{A}} U$$

> - The above definition for compactness *depends on all open coverings having a finite subcover*.
> - Hence, if a *set is not compact*, then *there exists* an open covering that *does not have a finite subcover*. Conversely, *if we found an open covering that doesn't have any finite subcover*, then we can conclude that the *set is not compact*.
> 	- In this case, we can think of this 'lack of a finite subcover' as a *'witness' to the 'uncompactness'* of the set.
	
---
**Lemma.** Let $Y$ be a subspace of a topological space $X$. 
The space *$Y$ is compact* $\Longleftrightarrow$ *every covering of $Y$ by sets open in $X$ contains a finite subcollection covering $Y$.*

> This lemma is just an extension of the definition of compactness onto subspaces.

---
# Characterization of Compact Spaces
**Proposition.** Every *closed subspace of a compact space* is *compact*.


---
**Proposition.** The *image of a compact set under a continuous function* is *compact*.

---
**Theorem.** *Every closed interval in $\mathbb{R}$* is *compact*. The compact subspaces of $\mathbb{R}^n$ are exactly those that are closed and bounded.

**Corollary.** Let $f: X \to  \mathbb{R}$ be a continuous function and $X$ a compact space, then $f$ assumes its maximum and minimum value.

---
# Finite Intersection Property

**Definition.** A topological space $X$ is said to have the *Finite Intersection Property* if for *every collection $\mathscr{F}$ of closed sets* in $X$, and for every finite subset $\mathscr{F}' \subset \mathscr{F}'$, $$\bigcap_{F\in \mathscr{F}'}F \neq \emptyset \text{ implies } \bigcap_{F \in \mathscr{F}} F \neq \emptyset$$


**Proposition.** Let $X$ be a topological space.
*$X$ is compact* $\Longleftrightarrow$ *$X$ satisfies the finite intersection property*.


**Proposition.** Let $X$ be a topological space.
If *$X$ is compact*, then *every infinite subset of $X$ has a limit point*.