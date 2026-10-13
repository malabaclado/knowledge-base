---
tags:
alias:
creation-date: Tuesday 22nd March 2022
last-modified-date: Tuesday 22nd March 2022 18:18:50
---
⬅️ 

---

# Math 148 Lecture 9
![[Pasted image 20220322183414.png]]

![[Pasted image 20220322183627.png|300]]
==Lecture 10==

Smallest non-desarguesian plane ➡ Projective plane with 91 points $\Pi(\mathbb{F}_{3^2})$

![[Pasted image 20220322184202.png]]

Proof of (T5)

![[Pasted image 20220322184547.png|400]]

Show: AA', BB' and CC' are concurrent.

---
==Lecture 11==

Quadrangles 
- Dual: Quadrilateral
Harmonic Sets
- Harmonic Sets of Points
- Harmonic Sets of Lines

Quadrangle (4 vertices; 6 sides; no three points are collinear)
![[Pasted image 20220322223332.png]]


Dual: Quadrilateral (4 sides, 6 vertices; no three lines are concurrent)
![[Pasted image 20220322223507.png|250]]

Therefore, **a quadrangle is not a quadrilateral**. (It is not self-dual)

Given a quadrangle, the **opposite sides** are the  sides with no common vertex.

The three points resulting from the intersection of every pair of opposite sides are the **vertices of the diagonal triangle.**

==Lecture 12==
Given a quadrilateral, two vertices are opposite vertices if they are not lying on the same line.

There are three pairs of opposite vertices.  

The three lines determined by each pair of opposite vertices are the **sides of the diagonal trilateral**.

Def. Harmonic Set of Points
![[Pasted image 20220322225025.png]]

Note
- A and B must be diagonal points

Example:
![[Pasted image 20220322225513.png]]


![[Pasted image 20220322225756.png]]


==Lecture 13==

Finding the harmonic conjugate of C with respect to A and B
![[Pasted image 20220322233922.png|250]]

TO be shown later on: Harmonic conjugate is unique

Note: In H(AB, CD), the point D is called the harmonic conjugate of C with resect to A and B.

==Lecture 14==
Theorem: Harmonic Conjugate is unique
![[Pasted image 20220323000255.png|200]]

Proof:
(Consider two pairs of perspective triangles from the line AD)

![[Pasted image 20220323000708.png|200]]

Let $D' = S'Q' \cap AB$  (Show: $D' =D$)
It easy easy to verify that $\Delta PRS$ and $\Delta P'R'S'$ are perspective from the line $AB$. In the same way, $\Delta PRQ$  and $\Delta P'R'Q'$ are also perspective from $AB$.

By **T5**,  the triangles $\Delta PRS$ and $\Delta P'R'S'$; and  $\Delta PRQ$  and $\Delta P'R'Q'$  are perspective from a point.

$PP' \cap RR' \cap SS'$
$PP' \cap RR' \cap QQ'$

$PP' \cap RR' \cap SS' = PP' \cap RR' \cap QQ'$

Since $PP' \cap RR' \cap SS' = PP' \cap RR' \cap QQ'$, then $SS', RR', QQ'$ are concurrent and their intersection is the point of perspectivity of the two pairs of perspective triangles.


==Lecture 15==
Show: $H(AB, CD) \Rightarrow H(CD, AB)$

![[Pasted image 20220323013617.png|250]]
Form the line  $PD$ and $CQ$.
Let $T = PD \cap CQ$ and  $U = QS \cap PC$ .
Consider the quadrangle $PTQU$. 
![[Pasted image 20220323013816.png|250]]

- Side PU is opposite to side TQ and they meet at point C. Therefore C is a diagonal point.

- Side PT is opposite to side UQ and they meet at point D. This shows D is another diagonal point.

- Side PQ pass through B. 

It remains to show that TU passes through A. (Hint: Use Desargues' Thm)

Consider the triangles PQT and SRU. 
![[Pasted image 20220323014231.png|250]]

- $PQ \cap SR =B$
-  $QT \cap RU = C$
- $PT \cap SU = D$

This implies that the triangles PQT and SRU are perspective with respect to the line AB. (Show that it is perspective to point A)

By **T5**, the same triangles PQT and SRU are perspective from a point with center of perspectivity: $PS \cap QR \cap TU$. 

Note that $PS \cap RQ = A$. (Show TU contains A)


Exercise:
![[Pasted image 20220323014834.png]]