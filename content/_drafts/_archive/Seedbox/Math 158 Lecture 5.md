---
tags:
alias:
creation-date: Tuesday 15th March 2022
last-modified-date: Tuesday 15th March 2022 23:18:22
---
⬅️ [[Math 158 MOC]]

---

# Math 158 Lecture 5 - Arrangement and Selections with Repetition
Topic Outline
- [[Arrangements with repetition]]
- [[Multi-set]]
	- [[r-permutation of multi-set]]
	- [[r-combination of multi-set]]
---

## Active Recall
1. The number of r-permutations of the set $A=\{a_{1},a_{2},..., a_{n}\}$ with repetitions allowed is equal to?
	- $n^{r}$

2. Given $n$ objects with $r_{1}$ of type 1, $r_{2}$ of type 2, ..., $r_{m}$ of type m, such that $r_{1}+r_{2}+,...,r_{m}= n$, the number of different permutations of these objects is?
	- $$P(n;r_{1},r_{2},...,r_{m}) = \frac{n!}{r_{1}!r_{2}!...r_{m}!}$$

3. Define a multiset. Give an example.

4. The number of r-permutations of the multi-set $\{\infty \cdot a_{1},\infty \cdot a_{2},...,\infty \cdot a_{n}\}$ is?
	- $n^{r}$

5. The number of r-permutations of the multi-set $\{r_{1}\cdot a_{1},r_{2}\cdot a_{2},...,r_{m}\cdot a_{m} \}$ is equal to?
	- $$P(n;r_{1},r_{2},...,r_{m}) = \frac{n!}{r_{1}!r_{2}!...r_{m}!}$$

1. The number of r-combinations of the multi-set $M=\{\infty \cdot a_{1},\infty \cdot a_{2},...,\infty \cdot a_{n},\}$ is equal to?
	- $$H(n,r) = \binom{r+n-1}{n-1} = \binom{r+n-1}{r}$$
