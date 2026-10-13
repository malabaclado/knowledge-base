---
tags: type/concept 
alias: [Receiver Operator Characteristic, ROC]
---

A [[ROC Curve|Receiver Operator Characteristic]] (ROC) curve is a graphical plot used to show the diagnostic ability of binary classifiers. It was first used in signal detection theory but is now used in many other areas such as medicine, radiology, natural hazards and [[Machine Learning]].


### Creating a ROC curve
A ROC curve is constructed by plotting the true positive rate (TPR) against the false positive rate (FPR).


 The **true positive rate** is the proportion of observations that were correctly predicted to be positive out of all positive observations

$$\frac{\text{true positive}}{\text{true positive}+\text{false negative}}$$

The **false positive rate** is the proportion of observations that are incorrectly predicted to be positive out of all negative observations.
$$\frac{\text{false positive}}{\text{true positive} + \text{false negative}}$$

### Area Under ROC
Larger area under ROC curve 👉 "better model"


If the AUC is greater than 0.5, the model is better than random guessing.

[[How to do AUC in scikit-learn]]
[[How to find AUC using cross-validation]]