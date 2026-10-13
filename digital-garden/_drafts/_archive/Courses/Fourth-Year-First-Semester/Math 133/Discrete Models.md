Processes are often *dynamic* - changing with respect to time, space or stage of development. 

*Dynamical systems* (as opposed to *static systems*) change with respect to a certain property.

Mathematical models describing these processes can be expressed in terms of difference or differential equations.

![[Pasted image 20210922144403.png | Difference vs Differential Equations]]

---
###### Example
![[Pasted image 20210922150045.png | Example 1]]


![[Pasted image 20210922150057.png | Solution to Example 1]]

---
### Some definitions
#### Difference Equation of Order k

Let $t$ denote time. Assume that the discrete time interval is some fixed length, denoted by $\Delta t$


Denote the state of the system at time $t$, by $x_t$

A difference equation of order k has the form 
$$f(x_{t+k}, x_{t+k-1},...,x_{t+1}, x_t, t) = 0, \quad t=0,1,2,...$$ where $f$ is a real-valued function of the real variables $x_{t+k}$, $x_{t+k-1}$, $x_{t+1}$,  $x_t$ and $t$.

---
###### Autonomous and Nonautonomous
A difference equation is called **autonomous** if $f$ does not depend explicitly on $t$. Otherwise, it is **nonautonomous**.


---
###### Linear and Nonlinear

![[Pasted image 20210922150654.png]]


![[Pasted image 20210922150708.png | Linearity of Difference Equations]]

---
###### Homogenous and Nonhomogenous
![[Pasted image 20210922150716.png | Homogeneity of Difference Equations]]


---
###### Example

![[Pasted image 20210922150823.png]]

Solution:
1. Order 1; Autonomous (bec it doesn't depend on $t$); Linear (since the coefficients are constants), Homogenous (no extra term $b$)
2. Order 1; Autonomous; Nonlinear; Nonhomogenous
3. Order 3; Nonautonomous; Linear; Nonhomogenous
4. Order 2; Nonautonomous; Nonlinear; Nonhomogenous

---
#### System of First-Order Difference Equations

![[Pasted image 20210922151114.png | Extention to a system of difference equations]]

---
###### Autonomy, Linearity and Homogeneity of System of First-Order Difference Equations

![[Pasted image 20210922151246.png]]


###### System of First-Order Difference Equations as a Vector

![[Pasted image 20210922151356.png]]
