---
tags: type/lecture-note, course/math-171, 
alias:
creation-date: Wednesday 11th May 2022
last-modified-date: Wednesday 11th May 2022 11:09:37
---
⬅️ 

---

# Math 164 Lecture 6

**Todo** ::📝 Recit 1.4 (Solutions are in Lecture 6)

**Todo** ::📝Quick review: Variance of Z 

**Todo** ::📝Review examples 1,2,3 Non-Level Benefit Insurance (Week 6 Slides)

**Todo** ::📝Homework 3 


**Exercise**:: 🖊️ Prove the two equations under UDD assumption: [[Pasted image 20220511114312.png]]

![[Pasted image 20220511114312.png]]

Note: Hindi kasama sa exam si $A^{(m)}_x$. Inintroduce lang yung actuarial symbol.

---
## Annually Increasing Insurance
![[Pasted image 20220511115155.png]]

![[Pasted image 20220511115253.png|200]]
Remarks:
- For EOYOD, the benefit is always K+1. That is, if a person dies in the interval (K,K+1], the insurance is paid at K+1.
- For MOD, the benefit is always the greatest integer function of T+1. Example, if death happens in the interval (0,1), let's say 0.2, the benefit will be $1 = \lfloor 1.02\rfloor$.

## Continuously Increasing Insurance
![[Pasted image 20220511115955.png]]

---

## Annually Decreasing Insurance 
![[Pasted image 20220516142341.png]]

Note: You just need to see the pattern of benefit. 

Decreasing benefits do not apply to whole life insurances (there's a possibility the benefit will approach zero). 

---

**Todo** ::📝Recit 1.5 | Week 5 Slides | March 26 Lecture 1:38:27 

---
PDF to use when:
- MOD: $_{t}p_{x} \mu_{x+t}$
- EOYOD: $_{k}p_{x}q_{x+k}$

---
Interpret the actuarial symbol: $(I^{(4)}A^{(12)})_{25}$

- This is a whole life insurance issued to $(25)$
- Death benefit increases by $\frac{1}{4}$ every quarter 
- Death benefit is payable at every $\frac{1}{12}$ of year (or every end of month).

---
**Todo** ::📝Homework 4 | Non-Level Benefit Insurances 

---
## Commutation Functions 
![[Pasted image 20220516143358.png]]

*Note: Hindi kasama ang commutation functions sa exam*

**Exercise** ::🖊️ Commutation Functions Examples 1-3 | Week 6 Slides 

---
## Life Annuities 
![[Pasted image 20220516145145.png]]

Recall all our random variables so far:
T: Future lifetime RV 
K: No. of completed years RV 
S: Fractional part RV (S=T-K)
Z: Present Value RV (of single payment)
Y: Present value of series of payments


$\mathbb{E}[Z] = A$
$\mathbb{E}[Y]=a$

discrete: annuity-due (payment at beginning of period, time=0)

Recall: Basic Annuities (Annuity Certain)
![[Pasted image 20220516145540.png]]




## Life Annuities 
### Whole Life Annuity Due
![[Pasted image 20220516145907.png]]

![[Pasted image 20220516150243.png]]


