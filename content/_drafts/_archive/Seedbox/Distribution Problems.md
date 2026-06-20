---
tags:
alias:
creation-date: Tuesday 29th March 2022
last-modified-date: Tuesday 29th March 2022 21:50:11
---
⬅️ 

---

# Distribution Problems

III. n **Labeled** balls to k **Labeled** boxes

$\leq$ 1 ball per box (Possible iff $n\leq k$)

Let $f: [n] \to [k]$  be a map from n balls to k boxes.
First, choose the image of $1 \in [n]$ (there are k possibilities).
Then, choose the image of $2 \in [n]$ (there are $k-1$) possibilities .

Such arrangements correspond to the number of injective functions $f$. Therefore, we count: $$k \cdot (k-1) \cdot ,..., \cdot (k-n+1) = \frac{k!}{(k-n)!}= \binom{k}{n}n!$$

