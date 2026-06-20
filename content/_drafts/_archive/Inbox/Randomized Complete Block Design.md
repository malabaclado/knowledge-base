---
tags:
  - design-of-experiments
aliases:
  - RCBD
creation-date: Wednesday 13th September 2023
---

A **Randomized Complete Block Design (RCBD)** is defined by an experiment whose treatment combinations are assigned randomly to the experimental units within a block.

Randomized Complete Block Design (RCBD) is arguably the most common design of experiments in many disciplines, including agriculture, engineering, medical, etc. In addition to the experimental error reducing ability, the design widens the generalization of the study findings.

The “**complete block**” part of the name indicates that each treatment combination is applied in all blocks. If a block misses one or more treatment combinations, the experiment would be called **Randomized Incomplete Block Design.**

**Nuisance Factors and Block Design**
Generally, blocks cannot be randomized as the blocks represent factors with restrictions in randomizations such as location, place, time, gender, ethnicity, breeds, etc. It is not simply possible to randomly assign a particular gender to a person. It is not possible to pick a country and call X country. However, the presence of these factors (also known as **nuisance factors**) will introduce systematic variation in the study. For example, the crops produced in the northern vs the southern part will get exposed to different climate conditions. Therefore, they should be controlled whenever possible. Controlling these **nuisance factors** by **blocking** will reduce the experimental error, thereby increasing the precision of the experiment and many other benefits.

**Completely Randomized Design VS RCBD**
In the **[[Completely Randomized Design]] (CRD)**, the experiments can only control the random unknown and uncontrolled factors (also known as lucking nuisance factors). However, the **RCBD** is used to control/handle some systematic and known sources (**nuisance factors**) of variations if they exist.

> [!NOTE] When to use Completely Randomized Design (CRD) and Randomized Completely Block Design (RCBD)?
> In fact, it would be wrong to use the completely randomized design when a known **nuisance factor** is adding variations in the response. Blocking the known nuisance factor not only reduces the experimental error, but also widen the statistical findings over the range of the nuisance factor. Blocking the nuisance factors also improves the signal to noise ratio by reducing the noise (error in this case). Completely randomized design (CRD) can only account for unknown and uncontrolled variations (which are also known as “lurking” nuisance factors). Complete randomization will minimize the effects from the lurking factors as they cannot be blocked simply because we don’t know them. However, systematic source of variations can be controlled by blocking using the randomized block design.

# RCBD Analysis Model
Effects Model
$$y_{ij} = \mu + \tau_{i} + \beta_{j} + \varepsilon_{ij}$$
where $\mu$ is the overall mean, $\tau_{i}$ is the effect to the ith treatment and $\beta_{j}$ is the effect of the jth block.


Nuisance Factor: Cycling Club
Treatment Factor: Sports drink/Water (Drink)
Response Variable: Average Riding Speed