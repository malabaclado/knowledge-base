---
tags: type/lecture-note, course/math-148, 
alias:
creation-date: Sunday 15th May 2022
last-modified-date: Sunday 15th May 2022 10:38:06
---
⬅️ 

---

# Lecture 39-43
Consider $\Pi(\mathbb{Z}_{3})$

Quadrangle ABDE 
Diagonal points:
- M diag of AD, BE 
- K diag of AB, DE 
- I diag of BD, AE 

Note that M, K, I are not collinear. 

Quadrangle HIML 
Diagonal points: E, K, C
- HM, IL meet at E 
- HI , ML meet at K 
- HI, LK meet at C 

Note that E,K,C are not collinear. 

Every quadrangle in $\Pi(\mathbb{Z}_{3})$ has diagonal points non-collinear. 

![[Pasted image 20220515104823.png]]

> [!NOTE]- Proof of theorem
> 
> Proof 
> - Consider an arbitrary complete quadrangle with vertices P1, P2, P3 and P4 with diagonal points D1, D2 and D3. 
> ![[Pasted image 20220515105100.png|200]]
> - Since P1, P2, P3, P4 are chosen st no three of them are collinear, then $P_{1} + P_{2}+P_{3}+P_{4}=0$ 
> - Then $P_{1} +P_{4}=-P_{2} - P_{3}$. The left side gives a point on the line containing P1 and P4, which is also (by the right side of the eq) the point on the line containing P2 and P3. 
> - From the illustration, $P_{1} +P_{4}=-P_{2} - P_{3} = D_{2}$
> - Also, 
> 	- $P_{1}+ P_{2}= -P_{3} - P_{4} = D_{1}$
> 	- $P_{2}+ P_{4} = - P_{1} - P_{3} = D_{3}$
> - Goal: Show that D1, D2,D3 are not collinear. ($D_{1}+D_{2}+ D_{3}=0$)
> - Suppose $a_{1}D_{1} +a_{2}D_{2}+a_{3}D_{3}=0$. (Show that D1,D2,D3 are linearly independent = a1,a2,a3 are all zero)
> ![[Pasted image 20220515110137.png]]
> ![[Pasted image 20220515110206.png]]
> ![[Pasted image 20220515110327.png]]
> 
> If the char F is 2, then any a2 would make it zero. But if char F is not 2, then 2a2=0 iff a2=0. 
> 
> Since char F is not 2, then a1=a2=3=0 therefore d1=d2=d3=0.
> 
> Indeed, the diagonal points are not collinear. 


---


==Lec 40== **Matrix Representations of Perspectivities**

Perspectivities maps a point from a line l1 to another line l2. So, for a point (x,y,z) in a line l1, our goal is to look for a matrix that would map (x,y,z) to a point in line l2.

Review:: 🗒️ Linear Transformations (Translations, Relfections, Rotations)


---
==Lec 42== Example of finding the matrix representation of a projectivity 

---
 ==Lec 43== More examples 






