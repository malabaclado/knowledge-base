---
tags:
  - design-of-experiments
aliases: 
creation-date: Wednesday 13th September 2023
---

As the _factorial design of experiments_ is primarily used for screening variables, using only two levels are enough to determine whether a variable is significant to affect a process or not. If k number of variables/factors are studied to determine/screen the important ones, the total number of treatment combinations for a k number of factors can be calculated as in Equation 1. Therefore, this screening technique is known as the _2K design of experiments_.

---
Factorial design of experiments is primarily used for screening varuables. Using only two levels are enough to determine whether a variable is significant to affect the process or not. Of k number of variables/factors are studied to determine/screen the important ones, the total number of treatment is $2^k$, hence its name.

---
# Layout, Data Structure and Level Coding System

Different coding systems can be used such as: +/-, -1/+1, 0/1, or using the actual levels. Normally, the low level is the control and the high level is the treatment factor. For example: in medicine, the low level is the placebo, the high level is the medicine/drug.

![[Pasted image 20230914195512.png]]

A graphical representation of a $2^2$ factorial design looks like this:
![[Pasted image 20230913224522.png]]

# The Contrast, Effect, Sum of Squares, Estimate Formula
## Contrast
The contrast is defined by the total responses.
$$AB=(a-1)(b-1)$$

## The Effect
The estimates for each of the effects are simply the one-half of their respective effect.
![[Pasted image 20230914200222.png]]


## The Sum of Square SS
![[Pasted image 20230914200237.png]]

## The Total Sum of Square
![[Pasted image 20230914200256.png]]

## The Sum of Square of the Experimental Error
![[Pasted image 20230914200321.png]]

## The ANOVA Table for a $2^2$ Factorial Design
![[Pasted image 20230914200347.png]]


