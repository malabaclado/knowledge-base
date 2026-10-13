---
tags: type/concept   course/math-148 
alias:
creation-date: Wednesday 23rd February 2022
last-modified-date: Wednesday 23rd February 2022 20:49:34
---

## Definition
**4 Basic Axioms of Projective Geometry**
![[Pasted image 20220223183211.png]]


> [!NOTE] Remarks
> - P1: There cannot be two lines passing through the same pair of points
> - P2: Common points may not be unique (but will be later proved that IT IS unique)



## Consequences of the first 4 postulates
![[Pasted image 20220223183716.png |400]]

Remarks:
- T1 follows from P4
- Proof of T2
	- Assume $l_1$ and $l_2$ be distinct lines
	- By Axiom $P_2$, there is a point p common to both l_1 and l_2
	- (By contradiction) Let q be another point of intersection for l_1 and l_2. By P1, we form the line PQ. Then l_1 = PQ and l_2=PQ. Which is a contradiction because we assume l_1 and l_2 are distinct. ⭐
- Proof of T3
	- By P4, there exists three noncollinear points P, Q and R. WLOG, we show that P lies in at least three lines. By P1, we can form lines PQ and PR. We are sure that $PQ \neq PR$ since Q and R are distinct points. By P1 again, we form the line QR. By P3, we have a point S in QR distinct from Q and R. Again by P1, we form the line PS, which is distinct from PQ and PR.
		- If PQ = PS, then Q=S. This is a contradiction since we let S to be distinct from Q and R.
	- ![[Pasted image 20220223184822.png | 100]]
- Proof of T4
	- By P4, there exists three non-collinear points P, Q and R
	- ![[Pasted image 20220223191940.png | 100]]
	- By P1, we can form lines PQ, QR and PR. 
	- These lines are not concurrent.
		- If PQ, QR and PR are concurrent, say ay point E, then $PQ \cap QR \cap PR = E$. 
		- Then $PQ \cap QR = E = Q$ and $QR \cap PR = E = R$ which implies $Q = R$ which is a contradiction because P, Q and R are distinct points.
