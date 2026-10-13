---
tags: type/concept 
alias:
creation-date: Friday 2nd December 2022
last-modified-date: Friday 3rd February 2023 14:50:33
---


In [[Machine Learning]], the situation when one class is more frequent is called class imbalance (ex. the class of real emails contains way more instances than the class of spam). This is a very common situation in practice and requires a more nuanced metric to assess the performance of our model.

Consider a spam classification problem in which 99% of emails are real and only 1% are spam. I could build a model that classifies all emails as real; this model would be correct 99% of the time and thus have an accuracy of 99%, which sounds great. However, this naive classifier does a horrible job of predicting spam: it never predicts spam at all, so it completely fails at its original purpose.