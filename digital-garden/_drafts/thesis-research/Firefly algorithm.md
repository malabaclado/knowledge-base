---
tags:
alias: firefly algorithm
creation-date: Tuesday 17th January 2023
last-modified-date: Tuesday 17th January 2023 15:08:19
---

The [[Firefly algorithm|firefly algorithm]] was inspired by the manner in which fireflies flash their lights to attract mates.

	Each individual in the popultation is a firefly and can flash light to attract other fireflies. At each iteration, all fireflies are moved toward all more attractive fireflies. 

The intensity (of light) decreases as the distance $r$ between two fireflies increases and is defined to be 1 when $r=0$. 

Three principles in the [[Firefly algorithm]]:
1. All fireflies are unisex - one firefly will be attracted to another regardless of sex.
2. Attractiveness is proportional to brightness - (1) for any two flashing fireflies, the less brighter one will move towards the brighter one; (2) attractiveness and brightness both decreases as their distance increases.
3. The brightness of a firefly is determined by the landscape of the objective function.

In the firefly algorithm, there are 2 important issues: (1) the variation of light intensity and (2) the formulation of attractiveness.

There are multiple approaches to represent the intensity in mathematical terms:
- Inverse Square Law
	- One approach is to model the intensity as a point source radiating into space, in which case the intensity decreases according to the inverse square law $$I(r)=\frac{1}{r^2}$$
- Exponential Decay
	- $$I(r)= e^{-\gamma r}$$
- Gaussian Brightness Drop-off
	- $$I(r)= e^{-\gamma r^2}$$


## Attractiveness 
$$\beta = \beta_{0} e^{-\gamma r^{2}}$$
## Distance between two fireflies 
$$r_{ij} = ||\text{x}_{i} - \text{x}_{j}||$$
## Movement of fireflies 
$$\text{x}_{i} = \text{x}_{i} + \beta_{0} e^{-\gamma r^{2}}(\text{x}_{j} - \text{x}_{i}) + \alpha (\text{rand} + \frac{1}{2})$$


## Pseudocode for Firefly Algorithm 
from @yangEagleStrategyUsing2010
![[Pasted image 20230118141706.png]]

---
Pseudocode 
1. Define the objective function $f(\text{x})$
2. Generate initial N population of fireflies $\text{x}_{i}$, ($i =1,2,..., N$)
3. Calculate the light intensity $I_i$  of each firefly $\text{x}_{i}$ , according to the objective function $f(\text{x}_{i})$
4. Define the light absorption coefficient $\gamma$
5. Create a loop >> Move the fireflies 
6. Rank the fireflies and find the current best. 
7. Postprocess results and visualization.
---
### Learn more: 
- [Firefly algorithm - Wikipedia](https://en.wikipedia.org/wiki/Firefly_algorithm)