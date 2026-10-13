---
tags: combinatorics, course/math-158, 
alias:
creation-date: Wednesday 16th March 2022
last-modified-date: Wednesday 16th March 2022 14:30:20
---
⬅️ [[Math 158 Lecture 5]]

---

# Arrangements with repetition
The number of r-permutations of the set $A=\{a_{1},a_{2},..., a_{n}\}$ with repetitions allowed is $n^{r}$.

Theorem. Given $n$ objects with $r_{1}$ of type 1, $r_{2}$ of type 2, ..., $r_{m}$ of type m, such that $r_{1}+r_{2}+,...,r_{m}= n$, the number of different permutations of these objects is $$P(n;r_{1},r_{2},...,r_{m}) = \frac{n!}{r_{1}!r_{2}!...r_{m}!}$$
Remark. If $m=2$ in the previous theorem, then $$(n;r_{1},r_{2}) = \frac{n!}{r_{1}!r_{2}!} = \frac{n!}{r_{1}!(n-r_{1})!} = C(n,r_{1})$$