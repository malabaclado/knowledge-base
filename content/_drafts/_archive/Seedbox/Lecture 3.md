---
tags:
alias:
creation-date: Tuesday 1st March 2022
last-modified-date: Tuesday 1st March 2022 12:27:36
---
⬅️ [[Math 158 MOC]]

---

# Lecture 3
## Combination
Let A be a set of n distinct objects.  A  **r-combination**  of A is simply a subset of A containing *r*-elements.

**Permutation vs Combination**
In permutation, order matters. In combination, order DOES NOT matter.

Notation: The number of *r*-combination of a set of *n* distinct objects is denoted by $C(n,r), \space_{n}C_{r} \text{ or }{n \choose k}$ 

### Formula for Combination
The number of *r*-combinations of a set of *n* distinct objects, denoted $C(n,r)$ is given by: $$C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{r! (n-r)!}$$
```ad-note
collapse: closed
title: Proof

Note that $P(n,r) = r! \cdot C(n,r)$ . *(Why?)*

Each *r*-combination corresponds to $r!$ *r*-permutations

Thus, $$C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{r!(n-r)!}$$
*End of proof*
```

**Remarks**
- For any natural number $n \in \mathbb{N}$,  $C(n,0) = C(n,n) = 1$ 
- For any $n\in \mathbb{N}$ and $r>n$, $C(n,r)=0$
---

## Sterling number of first kind
![[Pasted image 20220303121349.png|400]]

![[Pasted image 20220310125407.png|400]]

## Sterling number examples
![[Pasted image 20220303121837.png|400]]



## Homework
![[Pasted image 20220303121804.png|400]]


---

[[Injection Principle]]


