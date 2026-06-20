---
tags:
alias:
creation-date: Tuesday 22nd August 2023
---

Tidymodels is a collection of packages in the [[R (Programming Language)|R]] programming language that aims to provide a consistent and tidy interface for various aspects of the machine learning workflow, from data preprocessing and feature engineering to model training, evaluation, and deployment. Tidymodels is built upon the principles of the tidyverse, which is a set of R packages designed to make data manipulation and visualization more intuitive and consistent.

# Core packages in Tidymodels
The core packages within the Tidymodels ecosystem include:

1. **rsample**: This package provides tools for resampling and creating data splits, which is crucial for techniques like cross-validation and bootstrapping to evaluate model performance.
2. **recipes**: Recipes help you define a set of data preprocessing steps and transformations that can be applied consistently to both training and test data. This is an important part of ensuring your machine learning pipeline is reproducible.
3. **parsnip**: Parsnip provides a consistent and easy-to-use interface for specifying different machine learning algorithms (regression, classification, etc.) without needing to know the specifics of each algorithm's implementation.
4. **dials**: Dials is used for specifying hyperparameters and tuning parameters for models in a consistent and organized manner. It's particularly useful for conducting hyperparameter tuning experiments.
5. **tune**: This package helps you perform hyperparameter tuning using different methods like grid search, random search, or [[Bayesian Optimization]]. It can be used in conjunction with other Tidymodels packages to systematically search for the best combination of hyperparameters for your models.
6. **workflows**: Workflows allow you to assemble the various components of a [[Machine Learning]] pipeline, including data preprocessing, model specification, and tuning, into a cohesive structure. This promotes modularization and reuse of code.
7. **yardstick**: Yardstick provides functions to compute various evaluation metrics for model performance, such as accuracy, AUC, RMSE, etc.

Tidymodels emphasizes the use of tidy data principles, where data is organized in a consistent format with rows representing observations and columns representing variables. This approach makes it easier to reason about and manipulate data throughout the machine learning process.