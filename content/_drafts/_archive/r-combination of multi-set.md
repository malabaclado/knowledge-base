---
tags: type/concept , course/math-158, 
alias:
creation-date: Wednesday 16th March 2022
last-modified-date: Wednesday 16th March 2022 14:28:28
---
⬅️ [[Math 158 Lecture 5]]

---

# r-combination of multi-set

*Definition.* Let $M$ be a multi-set. An **r-combination of M** is an unordered selection of r objects of $M$. 

![[Pasted image 20220316141151.png]]

*Theorem.* The number of r-combinations of the multi-set $M=\{\infty \cdot a_{1},\infty \cdot a_{2},...,\infty \cdot a_{n},\}$ is equal to $$H(n,r) = \binom{r+n-1}{n-1} = \binom{r+n-1}{r}$$

---
Proof. The number of r-combination is equal to the number of non-negative integer solutions of the equation $$x_{1}+x_{2}+,...,x_{n} = r$$
One can show that there exists a bijection from M to the set of non-negative integer solutions of the above equation.

---
![[Pasted image 20220316133817.png]]

Any r-subset (r-combination) of M corresponds to a nondecreasing sequence.  Hence, we have $H(n,r)$. 

---
![[Pasted image 20220316134458.png]]

The 10-combination of the multiset corresponds to the non-negative integer solutions of the equation $$x_{1}+x_{2}+x_{3}+x_{4}= 10$$
where $x_{i}\geq 1$. Hence, we get $\binom{10-1}{4-1}$.