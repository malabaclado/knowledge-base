---
tags:
  - design-of-experiments
aliases: 
creation-date: Wednesday 13th September 2023
---

A one-way ANOVA is used to determine whether or not there is a statistically significant difference between the means of three or more independent groups.

The hypotheses used in a one-way ANOVA are as follows:
- H0: The means are equal for each group.
- HA: At least one of the means is different from the others.

If the p-value from the ANOVA is less than some significance level (like α = .05), we can reject the null hypothesis and conclude that at least one of the group means is different from the others.

But in order to find out exactly which groups are different from each other, we must conduct a post-hoc test.

Post-hoc tests:
- Fisher's Least Significant Difference (LSD) test - *most basic*
- Tukey - *most conservative*
- Dunnet

> [!NOTE] 
> When the levels of a factor are selected randomly from a long list of options for the levels, the factor is called the random factor. The analysis of variance model used for a random factor is called the [[Random Effects Model]]. ^xbbog7