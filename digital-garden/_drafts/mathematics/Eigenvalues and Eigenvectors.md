---
tags: type/concept  topic/math/linear-algebra 
alias:
creation-date: Tuesday 2nd August 2022
last-modified-date: Tuesday 2nd August 2022 11:50:54
---

# Eigenvalues and Eigenvectors
In linear algebra, an **eigenvector**  (or **characteristic vector**) of a linear transformation i**s a nonzero vector** that changes at most by a scalar factor when that linear transformation is applied to it. The corresponding eigenvalue, often denoted by $\lambda$ , is the factor by which the eigenvector is scaled.

> [!NOTE] Definition
> Let $T:V\to V$ be a linear operator. If there exists a scalar $\lambda$ and a vector $v$ such that $$T(v) = \lambda v$$
Then we call $\lambda$ the eigenvalue of $T$ associated with eigenvector $v$

Note: 
- The eigenvector must not be a zero vector (otherwise, we have $T(0) = \lambda \cdot 0$ which means every scalar is an eigenvalue of $T$)  
- If $v$ is the eigenvector associated with eigenvalue $\lambda$, then all nonzero multliples of $v$ are also eigenvectors associated with $\lambda$. 
- The set $W = \{a\text{v} | a\ \in \mathbb{F}\}$ is an *invariant subspace of V under T*.

