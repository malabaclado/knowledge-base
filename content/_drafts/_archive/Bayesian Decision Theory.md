---
tags:
alias:
creation-date: Wednesday 24th August 2022
last-modified-date: Wednesday 24th August 2022 11:52:58
---

# Bayesian Decision Theory
Suppose we have a set of data belonging to classes $c_{i}$ where $i=1,2,...,C$.

Our **goal** is to classify new sample $x$ to a class $c_{i}$.  We aim to minimize the probability of error when assigning classes. This is equivalent to assigning  $x$ to a class $c_{i}$  that yields the **maximum posterior probability** $p(c_{i}|x)$. 

But usually, the quantity $p(c_{i}|x)$ is unknown.However, using Bayes' rule: $$p(c_{i}|x) = p(x|c_{i}) p(c_{i})$$ So the main idea of a classifier based on Bayesian decision theory is that: $$x \in c_{i} \text{ if } c_{i}= \arg \max_{c_{j}}  p(x|c_{j}) p(c_{j}) $$
> [!NOTE] Writer's Note
> The above expression says that the a new sample $x$ belongs to the class $c_{i}$ if it has the maximum posterior probability.

---
[[Bayesian Decision Theory for GMM]]
