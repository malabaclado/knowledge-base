### Standard machine representation of real numbers.
The [[IEEE]] created [[Binary Floating Point Arithmetic Format]]. Real numbers are stored as [[Floating Point number]].


A [[floating point number]]  consists of 3 parts: the sign, a mantissa and an exponent.

![[Pasted image 20210330100542.png]]

The number of bits allocated for each floating point number depends on its level of precision. There are 3 levels of precision for floating point numbers:
1. Single Precision *(32-bit)*
2. Double Precision *(64-bit)*
3. Extended Double Precision *(80-bit)*

**Single Precision Format**
![[Pasted image 20210330100718.png]]

**Double Precision Format**
![[Pasted image 20210330100827.png]]

By default, MATLAB uses double precision format.

---
**Normalization of Double Precision Floating Numbers**
![[Pasted image 20210330101106.png]]
 
So, how do infinite binary numbers like 1.2 stored as floating point number?
- Choice 1: Chopping -> truncate up to the 52nd bit
- Choice 2: Rounding (this is the IEEE standard) -> if the 53rd bit is 1, add 1 to the 52nd bit. 

![[Pasted image 20210330101523.png]]


---
**Definition.** [[Machine Epsilon]]
The number machine epsilon, denoted $\epsilon_{\text{mach}}$ is the distance between 1 and the smallest floating point number greater than 1.

For the IEEE double precision standard, $\epsilon_{\text{mach}}=2^{-52}$.

---
**Floating Point Number Representations**
Denote the floating point representation of a number $x$ as $\text{fl}(x)$
![[Pasted image 20210330121942.png]]

---
**Relative Rounding Error**
In the IEEE model, the relative rounding error of $\text{fl}(x)$ is no more than 1/2 the machine epsilon.
![[Pasted image 20210330121705.png]]

---