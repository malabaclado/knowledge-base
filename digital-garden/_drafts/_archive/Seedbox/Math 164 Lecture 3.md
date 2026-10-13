---
tags: type/lecture-note, course/math-164, 
alias:
creation-date: Monday 14th March 2022
last-modified-date: Monday 14th March 2022 19:10:16
---
⬅️ [[Math 164 MOC]]

---

# Math 164 Lecture 3
Survival Models
- Life Tables
- Probabilities with Fractional Ages
- Select Tables

---
# Active Recall
- Notation
	- $l_{0}$
	- $l_{x}$
	- ndx
	- dx
	- $\mathcal{L_{x,t}}$ random variable
- Formulas related to lifetable
	- Expectation of $\mathcal{L_{x,t}}$
	- ![[Pasted image 20220315014839.png|200]]
- Fractional Part Random Variable
- Assumptions
	- UDD (5 Formulas)
	- Constant Force of Mortality (5 Formulas)
- Select and Ultimate Tables
	- Select age
	- Identifying select and ultimate tables


---
## Life Tables 
A basic life table shows a list of the number of individuals alive at each age and the number of deaths in each period. 

![[Pasted image 20220504013257.png]]

**Survivorship Random Variable**

The number of survivors from age $x$ to age $x+t$ can be regarded as a random variable that follows a Binomial distribution. 

![[Pasted image 20220504013454.png]]

![[Pasted image 20220504013832.png]]

---
Standard ultimate life table assumption : $i= 5\%$
Illustrative Life Table at $i=6\%$

Difference: 
- Interest rate
- ILT starts at age 0. SUL starts at age 20. 


Life table - list of the number of individuals alive at each age and number of deaths in each period of time.

*Commutation functions* - ginagamit sa pagcompute ng premiums.

---
**Probabilities with Fractional Ages**

![[Pasted image 20220314193924.png]]

To compute for frational life variable, given the probability distribution of $K_{x}$, we interpolate between the discrete poitns to create a continuous $S_{x}$ using the following assumptions:

![[Pasted image 20220504014827.png]]


### Uniform Distribution of Death
- Deaths occuring between integer ages are evenly spread out
- Linear interpolation

![[Pasted image 20220504122642.png]]

### Constant Force of Mortality
- Force of mortality within each year of age is constant
- Exponential interpolation

![[Pasted image 20220504122701.png]]





---
**Select and Ultimate Tables**
![[Pasted image 20220315004054.png]]

selection = special treatment (treatment will diminish over time)

![[Pasted image 20220504191505.png]]

A 2-year select life table means you have a better mortality assumption for 2 years - this means mas mababa ang premium na babayaran ni life insured. 

![[Pasted image 20220504191911.png]]



![[Pasted image 20220315005200.png]]



---

# Examples
![[Pasted image 20220314193540.png]]

Answer: d_49 = 70