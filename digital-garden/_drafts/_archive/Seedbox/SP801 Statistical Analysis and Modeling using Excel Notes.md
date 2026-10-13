---
tags:
alias:
creation-date: Tuesday 3rd October 2023
---

Statistics transforms data into meaningful information, enabling organizations to make better decisions and predictions. Hence, it is a valuable skill to learn in business or academia. This course will teach participants how to perform the most important and commonly used analytics and modeling techniques in Excel. Topics covered include **descriptive**, **diagnostic**, **predictive**, and **prescriptive** analytics.

**Course Instructor**: Frances Claire Tayco

# Descriptive Analytics
## Recall: Data Value Chain
![[Pasted image 20231003100252.png]]

The value of data is realized when it is used to derive insights that guide business decisions.

## Different sources of data
- Transaction data - external related data such as payments
- Contractual/Subscription/Account data - data about a product with customer characteristics (e.g. a loan, subscription service)
- Surveys - aimed at extracting demographic data
- Data poolers
- Unstructured data (e.g. files, pdfs)

## Types of analytics (Gartner)
![[Pasted image 20231003100952.png]]
1. Descriptive - *what has happened?*
2. Diagnostic - *why something is happening?* Dives into the root cause of problems (e.g. drill-down analytics, correlation, probabilities, pattern identification)
3. Predictive - *what is likely to happen?* 
4. Prescriptive - *what I need to do and how can I make it happen?* (e.g. scenario testing, optimization)

## Descriptive analytics
![[Pasted image 20231003101128.png]]

Asks the question: *What is happening?*

## Excel Functions for Descriptive Analytics
- SUM(), SUMIF()
- AVERAGE(), AVERAGEIF()
- MEDIAN()
- MAX(), MIN()
- SMALL(), LARGE()
- COUNT(), COUNTA(), COUNTIF(), COUNTBLANK()
- VAR(), VARP()
- STDEV(), STEVP()

## Practical Use-cases
- Moving Average
- Pareto Chart
	- How to create a dynamic pareto chart?
- Statistical Process Control
	- is a methodology for monitoring a process to identofy special causes of variation and signaling the need for corrective action.
	- Example: Control chart
	- ### Types of variation
		- Common cause variation
		- Special cause variation (uncontrolled)
## Moving Average
*(Add discussion on how to do moving average in Excel)*
## Pareto Chart
Pareto principle
- Helps identify where to focus efforts

## Control Chart (p-chart, c-chart)
![[Pasted image 20231003135537.png]]

![[Pasted image 20231003141915.png]]

## RFM Segmentation
RFM segmentation is a marketing technique used to analyze and categorize a customer base based on their recent purchase behavior.

- RFM stands for Recency Frequency and Monetary.
	1. **Recency:** This refers to how recently a customer has made a purchase. *Customers who have made a purchase more recently are considered more valuable.*
	2. **Frequency:** This represents how often a customer makes a purchase. Customers who make frequent purchases are generally more engaged and valuable to a business.
	3. **Monetary:** This indicates how much money a customer has spent on purchases. Customers who have spent more money are typically more valuable to a business.

Examples: 
1. [RFM Analysis Tutorial: Simple Segmentation Analysis - YouTube](https://www.youtube.com/watch?v=i-HNJZeOOMY)
2. [RFM Analysis With Excel - YouTube](https://www.youtube.com/watch?v=0BwBJvGAovI)

# Diagnostic Analytics
Week 2 discusses techniques that deep dive into the data and determine causes or drivers of problems or events of interest. Particularly, the focus is on the use of hypothesis testing and correlation analysis to drill down into causal relationships.  This week also includes tutorials on how to perform diagnostic analytics in Excel using functions and the Analysis ToolPak.

## Descriptive vs Diagnostic Analytics
![[Pasted image 20231003150128.png]]


## Functions of Diagnostic Analytics
- Identifying anomalies
- Drill into the analytics (discovery)
- Determine causal relationships

Examples:
- Correlation analysis
- Drill-down analytics
- Hypothesis testing

Guide questions:
1. Which factors move together? *Check correlation coefficient*
2. Are there differences in distribution? *Check categorical distribution (chi-square)*
3. Are two populations similar? *Perform analysis of variance/ analysis of means*

## Correlation
- [[Correlation analysis]]
	- Customer satisfaction analysis
- [[Phi correlation]]
	- Product affinity analysis

## Hypothesis Testing
- [[Analysis of Variance]]
- Test of means
	- [[AB Testing]]
- [[Chi-square Test]]
	- Attrition model

# Predictive Analytics
## What is Predictive Analytics?
- It answers the question: ==*What is likely to happen?*==
- Diagnostic analytics does not help prevent siilar problems from occuring in the future.
- Predictive analytics ==provides foresight==. It allows us to forecast future trends, behaviors, or events based on historical data and patterns
---
## Predictive analytics process
![[Pasted image 20231010215748.png]]

The predictive analytics process in order:
1. Project Design
2. Data sampling
3. Data exploration
4. Model training
	1. Data modification
	2. Model development
	3. Model validation
5. Champion model
---
## Common classes of predictive analytics
### Classification
- predicting a label
- example: customer churn vs non-churn
### Regression
- predicting a value

## Linear Regression
- Used for cause-effect analysis and forecasting future values.
- Regression equation: $y = \beta x + \alpha + \varepsilon$
	- $\varepsilon$: error term
- Practical use-case: Sales attribution

## Practical Use-case: Sales Attribution
1. Plot data using scatterplot.
2. Find values using Excel functions:
	- Intercept: Use INTERCEPT()
	- Slope: SLOPE()
	- R-Squared: RSQ()
	- Standard Error: STEYX()
3. To forecast, use FORECAST(x, knownxs, knownys)
4. Create forecast boundaries (i.e. upper and lower boundaries at a certain significance level)
	- Empirical rule
		- 68% falls within first sd
		- 95% falls within the first 2 sd
		- 99.7% falls within the first 3 sd

## Multiple Linear Regression
- More than one variable is involved
- Visualize using a scatterplot matrix
## Practical Use-case: Marketing Mix Modelling
- Use multiple linear regression to determine ... 
- Use formula: LINEST() or Data analysis toolpak




## Practical Use-case: International Criminal Tribunal Sentence 
- Goal: Understanding the factors that affect the length of a defendant's senstence from the ICT.
- Concept: Using qualitative data (categorical variables) on multiple linear regression. This involves converting the categorical variables into dummy variables.
	- Example:
		- Sex with values male/female may be coded as 0=female, 1=male.
		- Civil status: Single flag {0=no, 1=yes}, Married flag {0=no, 1=yes}, Separated/Divorced flag {0=no, 1=yes}

## Logistic Regression

## Practial Use-case: Bankruptcy Scoring
- Given a sample of companies, predict the likelihood of financial distress, based on their financial and non-financial data.

## Predictive Strength Measures
- ROC Curve
	- Area under curve (AUC)
	- Gini coefficient or accuracy ratio
	- KS (Kolmogorov-Smirnov) statistic

## Further readings
- [The 6 Steps of Predictive Analytics - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2022/09/the-6-steps-of-predictive-analytics/)
- [A Guide To Predictive Analytics | Tableau](https://www.tableau.com/learn/articles/what-is-predictive-analytics)
- [What is predictive analytics? | IBM](https://www.ibm.com/topics/predictive-analytics)
# Prescriptive Analytics
![[Pasted image 20231011231301.png]]


- Optimization
- Sensitivity analysis
- What-if analysis tools
	- ![[Pasted image 20231011231548.png]]
	- Goal seek (e.g. Breakeven analysis)
	- Data table (e.g. Marketing Mix Model from Week 3)
	- Scenatio manager (e.g. Direct Mail Marketing)
	- Solved (e.g. RFM Optimization, Employee Scheduling)

> [!NOTE]- Test yourself
> Search the words related to the statements below:
> 1. It is the process of finding the best values of the variables for a particular criterion. 
> 2. It is a simplified representation of a situation or problem.
> 3. These variables are unknown quantities whose values the decision-maker is allowed to choose.
> 4. Its function defines the value to be optimized in the model. It can either be minimized or maximized.
> 5. It restricts the feasibility of certain conditions according to predefined conditions.
> 6. It is a method for solving one desired output by changing an assumption that drives it.
> 7. It is a table that allows you to try out different input values for formulas and see how changes in those values affect the formula’s output.
> 8. It is where values of multiple inputs are adjusted to obtain the optimal value for an outcome.
> 9. A ____________ Manager is a tool that sees the different values of the outcome when the variables are changed.

---
Book: "Financial Modelling in Excel for Dummies" by Fairhurst, D.

### Goal Seek

> [!NOTE]
> "Goal Seek" is a built-in feature in Microsoft Excel that allows you to find the input value needed to achieve a specific goal or result in a formula. It's particularly useful when you have a target value in mind and want to determine the input value that will make that target achievable.
>
Goal Seek is helpful for various scenarios, such as determining the sales volume required to reach a specific profit level or finding the interest rate needed to pay off a loan within a certain time frame. It's a valuable tool for performing reverse calculations and solving for unknowns in your Excel spreadsheets.

### Breakeven Analysis

> [!NOTE]
> Breakeven analysis is a financial technique used to determine the point at which a business's total revenue equals its total costs, resulting in neither profit nor loss. It helps businesses understand the level of sales or production they need to cover their expenses.

Goal: Determing the number of units needed to be sold to breakeven.

Steps:
1. The assumptions tab contain information that were arbitrarily chosen.
2. To get the breakeven units, use the goal seek function in Excel.
	1. Data > What if analysis > Goal Seek
	2. Set cell: Profit
	3. To value: *The value you are trying to reach. Only takes values and not reference cell*
		1. Set to value to 0 (this means equal cost and revenue or *breakeven*)
	4. By changing cell: *Your assumptions, things you want to change in order to breakeven*

### Data Table

### Marketing Mix Model
