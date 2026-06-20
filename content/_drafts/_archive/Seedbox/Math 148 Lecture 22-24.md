---
tags:
alias:
creation-date: Friday 1st April 2022
last-modified-date: Friday 1st April 2022 15:47:59
---
⬅️ [[Math 148 MOC]]

---

# Math 148 Lecture 22-24
==Lecture 22==

Fundamental Theorem of Projective Geometry

![[Pasted image 20220326012507.png]]

Proof:
- Existence is proved by cases 1a,1b and 2. 
- Suppose there are two projectivities: $T: ABC \to A'B'C'$ , $S: ABC \to A'B'C'$
	- $ST^{-1} = I \Rightarrow S = ST^{-1}T = IT = T$  
	- Therefore, $S=T$, the projectivity is unique.

---

*The property of being a harmonic sequence is invariant (preserved) under a projectivity.*
![[Pasted image 20220326012836.png]]

Proof:
$H(AB, CD) \Rightarrow H(ab,cd) \Rightarrow H(A'B', C'D')$
![[Pasted image 20220401160043.png|200]]

---
 Simplify finding an image under a projectivity

![[Pasted image 20220401160737.png]]
![[Pasted image 20220401160951.png|200]]

![[Pasted image 20220401161054.png]]

*Axis of homology* - is the line formed by intersection of cross joints of all pairs of corresponding points.

![[Pasted image 20220401161242.png|400]]

The purple line is the axis of homology

---
A projectivity between two lines always defines an axis of homology. The axis of homology is also called the *axis of projectivity*. 

Dual of theorem: There exists a *center of projectivity*

Given a pencil of lines, the intersection of pairs of corresponding lines define a line - a *join* (in contrast to cross-joins). These lines are concurrent at a point known as the *center of perspevtivity*.

---
![[Pasted image 20220402070911.png]]

Pappus' Theorem allows us to easily find the image of a point along a projectivity as long as we know the axis of homology.

---
Proof of Pappus' Theorem

![[Pasted image 20220402071626.png|200]]

P = AB' \cap BA'
Q = AC' \cap CA'
R= BC' \cap CB'

Let E=PQ. Show that E passes through R. 
Let E = PQ\cap l. 
Let $F = AB' \cap CA'$ and $G=A'B \cap AC'$ 
Let $D = PQ \cap BC'$. Show that D=R.
 APFB' *proj* AGQC' via A'
 AGQC' *proj* EPQD  via B (Q is sent to itself)
 APFB *proj* EPQD 👉 If a projectivity  fixes one point (case of point P), then the projectivity is a perspectivity 👉 there is a center of perspectivity (which is the intersection of the corresponding points) 👉 The perspectivity is centered at C.
This implies that B', D and C are collinear
