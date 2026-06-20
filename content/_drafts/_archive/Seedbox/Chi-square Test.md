---
tags:
alias:
creation-date: Tuesday 3rd October 2023
---

The chi-square test of independence is a statistical test used to determine whether there is a significant association or relationship between two categorical variables. 

It is particularly useful for analyzing contingency tables, which are tables that display the frequency distribution of two or more categorical variables simultaneously. The chi-square test helps you determine whether the observed relationship between the variables is statistically significant or if it could have occurred by chance.

# Formulation of Hypothesis
- Null Hypothesis (H0): There is no association or relationship between the two categorical variables; they are independent.
- Alternative Hypothesis (Ha): There is a significant association or relationship between the two categorical variables; they are dependent.

# Contingency Table
|                | Category A | Category B | Category C | Total |
|----------------|------------|------------|------------|-------|
| Variable X     |   Count1   |   Count2   |   Count3   | TotalX|
| Variable Y=Yes |   Count4   |   Count5   |   Count6   | TotalY|


# Steps in performing a chi-square test
  


Here are the key steps involved in conducting a chi-square test of independence:

1. **Formulate Hypotheses**:
    - Null Hypothesis (H0): There is no association or relationship between the two categorical variables; they are independent.
    - Alternative Hypothesis (Ha): There is a significant association or relationship between the two categorical variables; they are dependent.
2. **Collect Data and Create a Contingency Table**:
    - Collect data on the two categorical variables of interest.
    - Create a contingency table (also known as a cross-tabulation or two-way table) that shows the observed frequencies or counts for each combination of the two variables.
    Example Contingency Table:
    
|                | Category A | Category B | Category C | Total |
|----------------|------------|------------|------------|-------|
| Variable X     |   Count1   |   Count2   |   Count3   | TotalX|
| Variable Y=Yes |   Count4   |   Count5   |   Count6   | TotalY|
    
3. **Calculate Expected Frequencies**
    - Compute the expected frequencies for each cell in the contingency table under the assumption of independence. This is done using the formula:
        Expected Frequency=TotalX×TotalYTotal ObservationsExpected Frequency=Total ObservationsTotalX×TotalY​
    - Calculate expected frequencies for all cells.
        
4. **Compute the Chi-Square Statistic**:
    - Calculate the chi-square statistic using the formula:
        
        �2=∑(�−�)2�χ2=∑E(O−E)2​
        
        where:
        
        - �O is the observed frequency in a cell.
        - �E is the expected frequency in the same cell.
        - Sum over all cells in the contingency table.
5. **Determine Degrees of Freedom**:
    - Calculate the degrees of freedom (��df) for the chi-square test. It depends on the number of categories in each variable and is calculated as (Number of Categories in Variable X−1)×(Number of Categories in Variable Y−1)(Number of Categories in Variable X−1)×(Number of Categories in Variable Y−1).
6. **Find Critical Value or P-Value**:
    - Consult the chi-square distribution table or use a statistical software package to find the critical value or p-value associated with the chi-square statistic.
7. **Make a Decision**:
    - If the p-value is less than the chosen significance level (e.g., 0.05), reject the null hypothesis. This indicates that there is a significant association or relationship between the two categorical variables.
    - If the p-value is greater than the significance level, fail to reject the null hypothesis. This suggests that there is no significant association between the two variables.

----
See also:
- [[SP801 Statistical Analysis and Modeling using Excel Notes]]