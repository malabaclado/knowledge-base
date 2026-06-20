---
tags:
alias:
creation-date: Tuesday 18th October 2022
last-modified-date: Tuesday 18th October 2022 10:55:19
---

# Streamlining workflows with pipelines
Pipelines allows us to fit a model including an arbitrary number of transformation steps and apply it to make predictions about the new data.

`make_pipeline` takes an arbitrary no. of sklearn transformers, followed by an estimator.

Example: StandardScaler (Transformer 1) ➡ PCA (Transformer 2) ➡ Logistic Regression (Estimator)


![[Pasted image 20220331211726.png]]
