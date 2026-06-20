### Introduction
Gram-Schmidt Process refers to the process of constructing an orthogonal set from a linearly independent subset of an inner-product space. The technique is attributed to Jørgen Pedersen Gram, a Danish mathematician. Later on, a German mathematician named Erhard Schmidt published a paper on orthogonalization [[Algorithm]] which became widely used. Schmidt acknowledged that this is the same algorithm as that was previously used by Gram. Thus, this is how the process was named after.


The earliest linkage of the names Gram and Schmidt to describe this process appears to be in a paper by Y. K. Wong: *An application of orthogonalization process to the theory of least squares*, even though orthogonalization algorithms had been used much earlier by other mathematicians.

The main objective of this paper is to discuss the development, process and applications of  the Gram-Schmidt process. In the next section, we discuss the important concepts that are essential in the development of the algorithm. In section 3: we analyse the construction of the algorithm and provide some examples of its application.



### Background
Definition (Inner Product)
Let $V$ a vector space over $\mathbb{F}$. An innner product on $V$  is a function from $V \times V$ to $\mathbb{F}$ which sends a pair of vectors $(u,v)\in V \times V$ to a scalar $\langle u,v \rangle \in \mathbb{F}$.


Definition (Inner Product Space)

A vector space $V$ with an inner product defined on it is called an inner product space. An inner product space over $\mathbb{R}$ is called a Euclidean space.

Let us recall some common inner product spaces. 
- Let $\mathbb{F}$ be a field. Consider $\mathbb{F}^n$. Let $X=(x_1,.x_2,...,x_n)$ and $Y=(y_1,y_2,...,y_n)$ we define the standard inner product as $$\langle X,Y  \rangle=\sum_{i=1}^n x_i\bar{y_i}$$
- In $\mathbb{R}^2$. Let 

Examples:
1. ($\mathbb{R}^2$)
2. ($\mathbb{R}^n$)
3. (space of polynomials)
4. (space of functions - with complex values)



Definition (Norm of a Vector)
Let u be a vector. The norm or length of the vector u, denoted $||u||$, is defined as $$||u||=(\langle u,u\rangle)^{1/2}$$

If $u,v \in V$, the distance between u and v is given by $$d(u,v)=||u-v||$$


Definition (Orthogonality and Orthonormality)
A vector $v \in V$ is said to be of unit length if $||v||=1$. Two vectors $u$ and $v$ are said to be orthogonal if $\langle u,v \rangle =0$. If two vectors are of unit length and orthogonal, then they are said to be orthonormal to each other.


Definition. A subset $S \subseteq V$ is called an orthogonal set if every pair of distinct vectors in $S$ is orthogonal. An orthogonal set $S$ such that every vector in $S$ has unit length is called an orthonormal set. A basis for $V$ which is an orthonormal set is called an orthonormal basis for $V$.

Note that the notion of length and orthogonality is dependent on the inner product chosen. For instance, a basis for V may be orthonormal with respct to one inner product, but not orthonormal with respect to a different inner product.


---

   An orthonormal basis offers several computational advantage. For instance, if $B=\{v_1,v_2,...,v_n\}$ is an orthonormal basis for a vector space $V$, then any vector $v\in V$ is can be expressed as a linear combination of elements of $B$ whose $i$th coefficient is the inner product of $v$ with $v_i$. This result is summarized in the following theorem:
   
   Theorem. If $B=\{v_1,v_2,...,v_n\}$ is an orthonormal basis for $V$, then for any $v \in V$,  $$v=sum_{i=1}^n \langle v,v_i \rangle v_i$$
   
---
Definition (Orthogonal Complement)
If $W$ is a subspace of a real inner product space $V$, then the set of all vectors in $V$ that are orthogonal to every vector in $W$ is called the orthogonal complement of $W$ and is denoted by the symbol $W^\perp$

Theorem
If $W$ is a subspace of a real inner product space $V$, then:
- $W^\perp$ is a subspace of $V$ .
- $W \cup W^\perp = \{\emptyset\}$



