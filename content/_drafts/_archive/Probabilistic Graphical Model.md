---
tags:
alias:
creation-date: Friday 26th August 2022
last-modified-date: Friday 26th August 2022 14:34:14
---

# Probabilistic Graphical Model
A graph is comprised of nodes (also called vertices) that rae connected by links (also called edges). In a probabilistic graphical model, **each node represents a random variable** (or group of random variables), and **the links express probabilistic relationships** between these variables. The graph then **captures the way in which the joint distribution over all of the random variables can be decomposed into a product of factors** each depending only on a subset of the variables.

Graphical models can be **directed** (Bayesian networks) or **undirected** (Markov random fields). Directed graphs are useful for expressing causal relationships between random variables, whereas undirected graphs are better suited to expressing soft constraints between random variables. For the purposes of solving inference problems, it is often convenient to convert both directed and undirected graphs into a different representation called a **factor graph**.

---
Bayesian Networks 

Consider an arbitrary joint distribution $p(a,b,c)$ over three variables a,b, and c. By application of product rule of probability: $$p(a,b,c)=p(c|a,b) \cdot p(a,b)$$
Apply it again:
$$p(a,b,c)=p(c|a,b) \cdot p(b|a) \cdot p(a)$$
Note that this decomposition holds for any choice of the joint distribution. We now represent the right-hand side in terms of a simple graphical model as follows.
![[Pasted image 20220826144229.png|100%]]
First we introduce a node for each of the random variables a, b, and c and associate each node with the corresponding conditional distribution on the right-hand side. Then, for each conditional distribution we add directed links (arrows) to the graph from the nodes corresponding to the variables on which the distribution is conditioned.

If there is a link going from a node a to a node b, then we say that node a is the **parent** of node b, and we say that node b is the **child** of node a.


