---
tags:
alias:
creation-date: Tuesday 22nd February 2022
last-modified-date: Tuesday 22nd February 2022 01:25:32
---
⬅️ 

# Handling categorical data
## Nominal and ordinal features
Nominal 👉 Purely categorical (without ordering)
Ordinal 👉 Categorical **with ordering**
<!--ID: 1645617152658-->





## Mapping ordinal features
To make sure that the learning algorithm interprets the ordinal features correctly,  we need to convert the categorical string values into integers. We do these by manually mapping categories to their values.
<!--ID: 1645617152665-->


`inv_size_mapping = {v: k for k, v in size_mapping.items()}`
## Encoding class labels

## Performing one-hot encoding on nominal features
