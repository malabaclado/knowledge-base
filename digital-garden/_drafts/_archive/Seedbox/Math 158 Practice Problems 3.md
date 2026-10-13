---
tags:
alias:
creation-date: Thursday 10th March 2022
last-modified-date: Thursday 10th March 2022 12:18:32
---


## Examples: Combination

![[Pasted image 20220310130503.png | 400]]

```ad-solution
collapse: closed
1. Any two points define a line. Just pick any two points. *Answer:* $C(20,2)$
2. This is just the combination of any three points since no three points are collinear. *Answer:* $C(20,3)$
3. *Answer: NO*. Because non-convex quadrilaterals might be on the same set of points but might have different orientations.

```

---
![[Pasted image 20220310131026.png|500]]

```ad-solution
collapse: closed
1. *Answer:* $C(52,5)$
   
2. Take 5 cards from exactly one suit (one suit has 13 cards), this counts $C(13,5)$. There are 4 suits. By multiplication principle, we have  $4\cdot C(13,5)$.
   *Answer:* $4\cdot C(13,5)$
   
3. Pick 3 cards from 4 kings, we count $C(4,3)$. Pick 2 cards from the non-king cards, we count $C(48, 2)$. We do not include the other king on picking the last two because the problem says it should be exactly.
   *Answer:* $C(4,3) \cdot C(48,2)$

```

---
![[Pasted image 20220310131928.png|500]]

```ad-solution
collapse: closed

We have 11 people (7 seniors and 4 juniors). 

1. Pick any 6 committee member from 11 candidates. *Answer:* $C(11,6)$
2. *Answer:* $C(7,3) \cdot C(4,2)$
3. One of the committee posts was occupied by Juan Reyes. Therefore, we now pick 3 committee members from the remaining 10 people. *Answer:* $C(10,3)$

```


![[Pasted image 20220310132425.png|500]]


```ad-solution
collapse: closed
1. *Case 1 (there are 2 seniors)*: $C(7,2)\cdot C(4,2)$
    *Case 2 (there are 3 seniors):* $C(7,3) \cdot C(4,1)$ 
    *Case 3 (there are 4 seniors):* $C(7,4) \cdot C(4,0)$
   By addition principle, we have $$[C(7,2)\cdot C(4,2)] + [C(7,3) \cdot C(4,1)] + [C(7,4) \cdot C(4,0)]$$
2. The committee has *2n* members where *n* is a number from 1 to 4.
   Case *i*: *2i* members  = $C(7,i) \cdot C(4,i)$
   By Addition Principle, we have $\sum^{4}_{i=1} C(7,i)\cdot C(4,i)$

3. Use complementation principle.$$\text{Total number of committees } - \text{ Number of committees where Juan and Maria are both included}$$
   *Answer:* $[C(7,2) \cdot C(4,2)] - [C(6,1) \cdot C(3,1)]$

```
---


![[Pasted image 20220301124123.png|500]]

```ad-solution
collapse: closed

1. By MP, $[C(2,1)]^{8}$
2. Count the number of positions where you'll place 1. Note that $C(8,6) = C(8,2)$. *Answer: C(8,6) or C(8,2)*
3. ![[Pasted image 20220310134814.png|400]]
```



![[Pasted image 20220303113523.png|400]]


