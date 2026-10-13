Main Question: How do computers store and perform operations on integers and real numbers?


-   Computer arithmetic only gives approximate values. The error arising from these calculations are called the **round-off error.**
-   These errors are due to non-terminating binary numbers
-   Computers use a fixed number of bits to represent integers.
-   Overflow error - when the calculation exceed the largest number the computer can store. Most of the time, the program would stop.
-   For negative numbers, the computer assign one bit to identify the **signed values**.


### Machine Representation of Numbers
Computers uses a fixed number of [[bits]] ("binary digits") to represent integers.


Common bit-lengths: 8-bit, 16-bit, 32-bit and 64-bit

8-bit computers can store up to the integer 255. Once the computation exceeds this integer, the CPU drops the overflow digit.

![[Pasted image 20210330095618.png]]

[[Overflow error]] happen when computations exceed the largest number that a computer can register.

[[Word size]] - the number of bits your processor can handle

A 64-bit computer can handle $2^{64}-1$ integers. That's more than 18 quintillion.

### Negative Integers
To cater negative integers, the CPU assigns one bit to indicate the sign.


![[Pasted image 20210330100139.png]]

The smallest integer you can store in an 8-bit computer is -127.

### Standard machine representation of real numbers.
The [[IEEE]] created [[Binary Floating Point Arithmetic Format]]. Real numbers are stored as [[Floating Point number]].


A [[Floating Point number]] consists of 3 parts: the sign, a mantissa and an exponent.

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
### Weird effects of Floating Point Arithmetic
1. Adding/subtracting very small numbers may not have an effect.
2. The result of multiplying $x(1/x)$ is not always 1.
3. Associativity does not always hold.
4. Subtracting a number from another nearly equal number may result in loss of significance or cancellation error.




---
### Accuracy vs. Precision
Accuracy -> refers to how closely a computed value agrees with the true value.
	Inaccuracy/Bias - systematic deviation from the truth


Precision -> referes to how closely each individual measured values agree with each other.
	Imprecision/Uncertainty - refers to how scattered the data is.
	


### Algorithm 
-> a procedure that describes a finite sequence of steps performed in a specified order.
- Stable
- Conditionally Stable



Definition. Linear and Exponential Error

Definition. [[Rate of Convergence]]


---
Tags: #course/math-171 #topic/math/numerical-analysis #type/lecture-note