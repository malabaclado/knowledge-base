---
tags: molecule 
alias:
creation-date: Monday 1st August 2022
last-modified-date: Monday 1st August 2022 14:10:22
---

# Reasons you may want to compute posterior probabilities
1. **Minimize risk.** If we know the posterior probabilities, we can trivially revise the minimum risk decision criterion by modifying (the objective function) appropriately. If we have only a discriminant function, then any change to the loss matrix would require that we return to the training data and solve the classification problem afresh.
2. **Reject option.**  Posterior probabilities allow us to determine a rejection criterion that will minimize the misclassification rate. 
3. **Compensating for class priors.**  
4. **Combining models.** For example, in our hypothetical medical diagnosis problem, we may have information available from, say, blood tests as well as X-ray images. Rather than combine all of this heterogeneous information into one huge input space, it may be more effective to build one system to interpret the Xray images and a different one to interpret the blood data. As long as each of the two models gives posterior probabilities for the classes, we can combine the outputs systematically using the rules of probability.
---
Book: [[📕 Pattern Recognition and Machine Learning (Bishop)]]