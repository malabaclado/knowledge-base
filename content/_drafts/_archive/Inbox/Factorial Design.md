---
tags:
  - design-of-experiments
aliases: 
creation-date: Wednesday 13th September 2023
---

Oftentimes, we want to see the effects of multiple variables (say: Factor A,Factor B,Factor C,Factor D ... ) to a response variable. 

In a Factorial Design, all possible combinations of the levels of a factor can be studied against all possible levels of other factors. Therefore, the factorial design of experiments is also called the _crossed factor design of experiments_.

Due to the crossed nature of the levels, the factorial design of experiments can also be called the _completely randomized design (CRD) of experiments_. Therefore, the proper name for the factorial design of experiments would be _completely randomized factorial design of experiments_.

# Example
Suppose we have two factors: Temperature and Humidity, each with 2 levels:
- Factor A (Temperature): 0 F, 75 F
- Factor B (Humidity): 0%, 35%

Below is the graphical representation of this experiment:

![[Pasted image 20230913224522.png]]
Figure 1. Factorial Design of Experiments with two levels for each factor (independent variable, x). The response (dependent variable, y) is shown using the solid black circle with the associated response values.

## Calculating Main Effects

*The main effect is the independent effect of a factor.*

The average effect of the factor A (called the main effect of A) can be calculated from the average responses at the high level of A minus the average responses at the low level of A 

**Average effect of Factor A**
$$A = \frac{9+5}{2} - \frac{2+0}{2} = 7-1 =6$$


**Implication:** the average comfort increases by 6 on a scale of 0 (least comfortable) to 10 (most comfortable) if the temperature increases from 0- to 75-degree Fahrenheit.


![[Pasted image 20230913224836.png]]

**Average effect of Factor B**
$$B=\frac{2+9}{2}- \frac{5+0}{2} = 5.5-2.5=3$$

**Implication:** the average comfort increases by 3 on a scale of 0 (least comfortable) to 10 (most comfortable) if the relative humidity increases from 0 to 35 percent.

![[Pasted image 20230913225105.png]]

## Calculating Interaction Effects
In the real world, factors/variables *DO NOT ALWAYS* affect the response independently. 

In our example:
- at low humidity level (0%): the comfort increases by 5 (=5-0) if the temperature increases from 0 to 75 degrees Fahrenheit.
- at high humidity level (35%): the comfort increases by 7 (=9-2) if the temperature increases from 0 to 75.
So, *at different levels of humidity factor, the changes in comfort are not the same even though the change in temperature is the same (from 0 to 75)*. This is phenomenon is called the **Interaction effect**. 

The average change in comfort (in the interaction effect) is calculated as:
$$AB = \frac{7-5}{2} = \frac{2}{2} =1$$
**Implication:** the change in comfort lvel increases by 1 at the high level as compared to the low level of humidity, if the temperature increases from low to high (0 to 75)

## Interpreting interaction effects
This is what a strong interaction looks like:
![[Pasted image 20230914192539.png]]

This is what no interaction looks like:
![[Pasted image 20230914193034.png]]

## How to estiate the regression coefficients from the main and interaction effects

The regression model with two factors (with two levels for each factor) with the main and interaction effects can be written as: 
$$y= \beta_{0} + \beta_{1}x_{1} + \beta_{2}x_{2} + \beta_{12}x_{1}x_{2} + \epsilon$$


For a two-level factor, using the -1/+1  coding system, the average level increases along two units (from -1 to 0 then from 0 to +1). Therefore, the regression coefficient is one-half the calculated effect.

- Effect of Factor A = 6 >> $\beta_{1}=\frac{6}{2}$
- Effect of Factor B = 3 >> $\beta_{2}=\frac{3}{2}$
- Interaction effect AB = 1 >> $\beta_{12}=\frac{1}{2}$
- Mean: $\beta_{0}=\frac{0+2+9+5}{4}=4$

Hence, the regression equation from our example is:
![[Pasted image 20230914193917.png]]


---
- [[Design of Experiments]]