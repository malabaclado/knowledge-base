---
tags: molecule
alias: null
creation-date: Monday 1st August 2022
last-modified-date: Monday 1st August 2022 14:18:02
---

# Three distinct approaches in solving decision problems
We can identify three distinct approaches in solving decision problems. These are arranged in **decreasing complexity**:
1. First solve the inference problem of determining the class-conditional densities individually. Also separately infer the prior class probabilities then use Bayes’ theorem to find the posterior class probabilities. (Equivalently, we can model the joint distribution directly and then normalize to obtain the posterior probabilities.) Having found the posterior probabilities, we use decision theory to determine class membership for each new input $\text{x}$. These are called [[generative models]].
2. First solve the inference problem of determining the posterior class probabilities, and then subsequently use decision theory to assign each new x to one of the classes. These are called [[discriminative models]].
3. Find a function f (x), called a discriminant function, which maps each input x directly onto a class label. In this case, probabilities play no role.


---
Book: [[📕 Pattern Recognition and Machine Learning (Bishop) 1]]