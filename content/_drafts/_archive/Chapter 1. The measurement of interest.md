---
tags:
alias:
creation-date: Monday 23rd October 2023
---

# Accumulation and Amount Functions

Some terms:
- Principal - refers to the initial amount of money (capital) invested
- Accumulated value - refers to the amount received after a period of time
- Interest - the amount earned during the period of investment; the difference between principal and accumulated value.


> [!definition] **Accumulation function**
> Consider an investment of one unit of principal. We define the accumulation function $a(t)$ which gives the accumulated value at time $t \geq 0$ of an original investment of 1.

Remarks: Properties of accumulation function
1. $a(0) = 1$
2. $a(t)$ is an increasing function on cases when interest is growing.
3. If interest accrues continuously, $a(t)$ is a continuous function.


> [!Definition] Amount function
The amount function $A(t)$ denotes accumulated value at time t of an original investment k. Therefore:
$$A(t) = k\cdot a(t)$$


---
# Effective Rate of Interest

> [!definition] Effective rate of interest $i$
> The effective rate of interest i is the amount of money that one unit invested at the beginning of a period will earn during the period, where interest is paid at the end of the period.

**In terms of the accumulation function**, the effective rate of interest can be expressed as:
$$i = a(1) - a(0)$$
or $$a(1) = 1 + i$$
**In terms of the amount function**, the effective rate of interest can be expressed as:
$$i = \frac{(1+i)-1}{1}=\frac{I}{A(0)}$$

---
# Simple Interest
