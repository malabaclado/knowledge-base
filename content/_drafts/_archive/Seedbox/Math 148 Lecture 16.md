---
tags:
alias:
creation-date: Friday 25th March 2022
last-modified-date: Friday 25th March 2022 23:07:34
---
⬅️ 

---

# Math 148 Lecture 16
# Harmonic  Set of Lines

> In $\Pi (\mathbb{Z}_3)$, every set of points on line form a harmonic set of points.

**Definition.** Harmonic set of lines
Four concurrent lines *a,b,c,d* form a  harmonic set, denoted $H(ab,cd)$, if *a* and *b* are diagonal lines of a quadrilateral while *c* and *d* contain the last pair of opposire vertices of the quadrilateral.

Example:
![[Pasted image 20220325233614.png|400 ]]

Remarks:
- The *diagonal lines of a quadrilateral* are the lines passing through opposite points.
- A quadrilateral has exactly 3 pairs of opposite points. 


---

The next theorem relates the harmonic set of points to harmonic set of lines.

**Theorem.** Let four concurrent lines *a,b,c,d* meet a line *l* at the points *A,B,C,D* respectively, then $H(AB,CD) \Leftrightarrow H(ab,cd)$. 

![[Pasted image 20220325235017.png|300]]

Proof of thm.
- Consider the quadrilateral with sides AD, SD, AQ and SB (with vertices A,S,R,Q,B,D)
- Notice that:
	- AS = line a.
	- QB = line b
	- line c contains R
	- line d contains D
- Thus, $H(AB,CD) \Rightarrow H(ab,cd)$
- We can prove  $H(AB,CD) \Leftarrow H(ab,cd)$ by similar construction (or by duality)

---
# Perspectivities and Projectivities

There are two kinds of perspectivity:
1. Central Perspectivity
2. Axial Perspectivity


## Central Perspectivity
A **central perspectivity** is a *one-to-one correspondence between a set of points of line l and the set of points of line l' such that the lines formed by the corresponding points are concurrent at a point O*. 

The point of concurrency is called the *center of perspectivity*.

![[Pasted image 20220325235809.png]]

![[Pasted image 20220325235952.png]]
 
In latex: `\doublebarwedge`

## Axial Perspectivity
The points of intersection of corresponding lines are collinear at the axis of perspectivity.
![[Pasted image 20220326000811.png]]

![[Pasted image 20220326000916.png]]

> Key idea: We can treat perspectivities as functions, and so we can use them in function compositions. 


---


**Definition.** Pencil of Lines and Points
- *Pencil of lines with center P*  - set of all lines passing through P
- *Pencil of points on line l* - set of all points with axis l (in some books, it is called projective range)

![[Pasted image 20220326001410.png]]


## Alternate definition for central and axial perspectivity.

 ![[Pasted image 20220326001517.png]]
![[Pasted image 20220326001614.png]]


## Projectivities

Projectivity is a product or composition of two or more perspectivity of the same type.

![[Pasted image 20220326001916.png|400]]

Example:

![[Pasted image 20220326002257.png|400]]

==Lecture 19==

Constructing projectivities from l to l'
- Case 1: l and l' are distinct
	- Case 1a: Pair of corresponding points are equal A=A'
		- ![[Pasted image 20220326002926.png|150]]
		- Let $O=BB' \cap CC'$. Then connect A and O.
		- ![[Pasted image 20220326003022.png|200]]
	- Case 1b: No pair of corresponding points are equal.
		- ![[Pasted image 20220326003147.png|200]]
		- ==Tip: Make two or more perspectivity==
		- ![[Pasted image 20220326003647.png|400]]
- ==Lecture 20== Case 2: l=l' 
	- Walang magkapareho na corresponding points (A=A',B=B', C=C'). If that happens, the perspectivity is the identity.
	- Key idea: Make another line and create a perspectivity from the original to that line. Then project back to the original line. Then proceed t case 1b
	- ![[Pasted image 20220326004545.png|400]]
	- ![[Pasted image 20220326004909.png|400]]
	- ![[Pasted image 20220326004934.png|400]]
	- 



Remarks:
1. A projectivity between to lines which fixes a point is a perspectivity (case 1a)
2. A projectiviyt between two distinct lines is the product of at most two perspectivities. (case 1b)
3. A projectivity from a line to itself is the product of at most three perspectivities. (case 2)

6th postulate
![[Pasted image 20220326005206.png]]

---

