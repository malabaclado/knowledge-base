---
tags: type/concept
alias: null
creation-date: Friday 29th July 2022
last-modified-date: Friday 29th July 2022 20:02:52
---


# Decision Stage for Regression

**Regression Problem**: What is the value of the target variable $\textbf{t} = y(\textbf{x})$ for new input variable $\textbf{x}$?


How do we choose $\textbf{t} = y(\textbf{x})$? -> Choose $y(\textbf{x})$ such that the expected loss is minimal.

## Expected Loss
*Expected Loss* ![[Pasted image 20211208150740.png]]


where $L(t,y(\textbf{x}))$ is the loss function.

**Some examples of loss function:**
- *Squared loss* :  $L(t,y(\textbf{x}))=\{y(\textbf{x}-t)\}^2$
- *Minkowski loss*

==The optimal solution is the conditional mean $y(\textbf{x})=\mathbb{E}[\textbf{t}| \textbf{x}]$==

## Three Approaches to Making Decision (Regression)
*Approach A* Determine joint density distribution -> normalize to find conditional density -> marginalize to find the conditional mean.


*Approach B* Solve theconditional density directly -> marginalize to find the conditional mean.

*Approach C* Find the regression function $y(\textbf{x})$ directly from the data.