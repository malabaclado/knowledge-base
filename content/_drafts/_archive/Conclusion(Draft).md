---
tags:
alias:
creation-date: Thursday 17th November 2022
last-modified-date: Thursday 17th November 2022 11:55:34
---

# Conclusion(Draft)
- ==Some recommendations from existing literature==
	- For further research, firstly, prior-knowledge database should be built by analyzing historical events on stock markets. Based on the prior-knowledge, the event weighting schema will be developed and each event should be weighted accordingly. Finally, a proposed model which incorporates the weighed events into the numeric time series data should be compared empirically with other models. ([[@yooMachineLearningTechniques2005|yoo2005]])
- ==Current Limitations==
	- No feature selection is employed. Could've used correlation elimination, SBS and/or PCA. 
	- Only five technical indicators (based on existing studies) are used. *There are more TA out there*
	- Hyperparameter tuning is a bit 'traditional'. The study used grid search optimization which is known to be computationally expensive. However, computational efficiency is not the primary objective of this research.