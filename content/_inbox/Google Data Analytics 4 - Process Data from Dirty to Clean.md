---
title: Process Data from Dirty to Clean
description:
date: 
lastmod: 
draft: false
tags:
aliases:
---
# The Importance of Data Integrity

> A strong analysis depends on the integrity of the data.

- **Data integrity** is the accuracy, completeness, consistency, and trustworthiness of data throughout its lifecycle.
- The **data manipulation process** involves changing the data to make it more organized and easier to read. Data manipulation is meant to make the data analysis process more efficient, but an error during the process can compromise the efficiency.
- **Data replication** is the process of storing data in multiple locations. If you're replicating data at different times in different places, there's a chance your data will be out of sync.
- A good analysis depends on the integrity of the data, and data integrity usually depends on using a common format.

## Things to watch out for
- **Data replication compromising data integrity** 
	- Continuing with the example, imagine you ask your international counterparts to verify dates and stick to one format. One analyst copies a large dataset to check the dates. But because of memory issues, only part of the dataset is actually copied. The analyst would be verifying and standardizing incomplete data. That partial dataset would be certified as compliant but the full dataset would still contain dates that weren't verified. Two versions of a dataset can introduce inconsistent results. A final audit of results would be essential to reveal what happened and correct all dates. 
- **Data transfer compromising data integrity** 
	- Another analyst checks the dates in a spreadsheet and chooses to import the validated and standardized data back to the database. But suppose the date field from the spreadsheet was incorrectly classified as a text field during the data import (transfer) process. Now some of the dates in the database are stored as text strings. At this point, the data needs to be cleaned to restore its integrity. 
- **Data manipulation compromising data integrity** 
	- When checking dates, another analyst notices what appears to be a duplicate record in the database and removes it. But it turns out that the analyst removed a unique record for a company’s subsidiary and not a duplicate record for the company. Your dataset is now missing data and the data must be restored for completeness

## Data constraints and examples

As you progress in your data journey, you'll come across many types of data constraints (or criteria that determine validity). The table below offers definitions and examples of data constraint terms you might come across.

| **Data constraint**                     | Definition                                                                                       | Examples                                                                                                                                                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Data type**                           | Values must be of a certain type: date, number, percentage, Boolean, etc.                        | If the data type is a date, a single number like 30 would fail the constraint and be invalid                                                                                                                                                                 |
| **Data range**                          | Values must fall between predefined maximum and minimum values                                   | If the data range is 10-20, a value of 30 would fail the constraint and be invalid                                                                                                                                                                           |
| **Mandatory**                           | Values can’t be left blank or empty                                                              | If age is mandatory, that value must be filled in                                                                                                                                                                                                            |
| **Unique**                              | Values can’t have a duplicate                                                                    | Two people can’t have the same mobile phone number within the same service area                                                                                                                                                                              |
| **Regular expression (regex) patterns** | Values must match a prescribed pattern                                                           | A phone number must match ###-###-#### (no other characters allowed)                                                                                                                                                                                         |
| **Cross-field validation**              | Certain conditions for multiple fields must be satisfied                                         | Values are percentages and values from multiple fields must add up to 100%                                                                                                                                                                                   |
| **Primary-key**                         | (Databases only) value must be unique per column                                                 | A database table can’t have two rows with the same primary key value. A primary key is an identifier in a database that references a column in which each value is unique. More information about primary and foreign keys is provided later in the program. |
| **Set-membership**                      | (Databases only) values for a column must come from a set of discrete values                     | Value for a column must be set to Yes, No, or Not Applicable                                                                                                                                                                                                 |
| **Foreign-key**                         | (Databases only) values for a column must be unique values coming from a column in another table | In a U.S. taxpayer database, the State column must be a valid state or territory with the set of acceptable values defined in a separate States table                                                                                                        |
| **Accuracy**                            | The degree to which the data conforms to the actual entity being measured or described           | If values for zip codes are validated by street location, the accuracy of the data goes up.                                                                                                                                                                  |
| **Completeness**                        | The degree to which the data contains all desired components or measures                         | If data for personal profiles required hair and eye color, and both are collected, the data is complete.                                                                                                                                                     |
| **Consistency**                         | The degree to which the data is repeatable from different points of entry or collection          | If a customer has the same address in the sales and repair databases, the data is consistent.                                                                                                                                                                |

- ==It's also important to check that the data you use aligns with the business objective.== This adds another layer to the maintenance of data integrity because the data you're using might have limitations that you'll need to deal with.
- *With incomplete data, it's hard to see the whole picture to get a real sense of what is going on.*
- Learning how to deal with data issues while staying focused on your objective will help set you up for success in your career as a data analyst.
- ## Well-aligned objectives and data
	- When there is clean data and good alignment, you can get accurate insights and make conclusions the data supports.
	- If there is good alignment but the data needs to be cleaned, clean the data before you perform your analysis.
	- If the data only partially aligns with an objective, think about how you could modify the objective, or use data constraints to make sure that the subset of data better aligns with the business objective.

# How to deal with insufficient data
## What you can do when you have insufficient data:
- Identify trends with the available data
- Wait for more data (if time permits)
- Talk with stakeholders and adjust your objective
- Look for a new dataset
## Types of insufficient data
- Data from only one source
- Data that keeps updating
- Outdated data
- Geographically-limited data

## What to do when you find an issue with your data

When you are getting ready for data analysis, you might realize you don’t have the data you need or you don’t have enough of it. In some cases, you can use what is known as *proxy data* in place of the real data. Think of it like substituting oil for butter in a recipe when you don’t have butter. In other cases, there is no reasonable substitute and your only option is to collect more data.

Consider the following data issues and suggestions on how to work around them.
### Data issue 1: No data

| Possible Solutions                                                                                                                                               | Examples of solutions in real life                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gather the data on a small scale to perform a preliminary analysis and then request additional time to complete the analysis after you have collected more data. | If you are surveying employees about what they think about a new performance and bonus plan, use a sample for a preliminary analysis. Then, ask for another 3 weeks to collect the data from all employees. |
| If there isn’t time to collect data, perform the analysis using proxy data from other datasets.  _This is the most common workaround._                           | If you are analyzing peak travel times for commuters but don’t have the data for a particular city, use the data from another city with a similar size and demographic.                                     |

### Data issue 2: Too little data

|Possible Solutions|Examples of solutions in real life|
|---|---|
|Do the analysis using proxy data along with actual data.|If you are analyzing trends for owners of golden retrievers, make your dataset larger by including the data from owners of labradors.|
|Adjust your analysis to align with the data you already have.|If you are missing data for 18- to 24-year-olds, do the analysis but note the following limitation in your report: _this conclusion applies to adults 25 years and older_ _only_.|

### Data issue 3: Wrong data, including data with errors*

|Possible Solutions|Examples of solutions in real life|
|---|---|
|If you have the wrong data because requirements were misunderstood, communicate the requirements again.|If you need the data for female voters and received the data for male voters, restate your needs.|
|Identify errors in the data and, if possible, correct them at the source by looking for a pattern in the errors.|If your data is in a spreadsheet and there is a conditional statement or boolean causing calculations to be wrong, change the conditional statement instead of just fixing the calculated values.|
|If you can’t correct data errors yourself, you can ignore the wrong data and go ahead with the analysis if your sample size is still large enough and ignoring the data won’t cause systematic bias.|If your dataset was translated from a different language and some of the translations don’t make sense, ignore the data with bad translation and go ahead with the analysis of the other data.|

_* Important note: sometimes data with errors can be a warning sign that the data isn’t reliable. Use your best judgment._

### Use the following decision tree as a reminder of how to deal with data errors or not enough data:

![](https://i.imgur.com/dtW8ZQ1.png)

1. Can you fix or request a corrected dataset? NO 
2. Do you have enough data to omit the wrong data? NO 
3. Can you proxy the data? NO 
4. Can you collect more data? NO 
5. Modify the business objective (if possible)

# Calculating the sample size
Before you dig deeper into sample size, familiarize yourself with these terms and definitions:

| **Terminology**              | **Definitions**                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Population**               | The entire group that you are interested in for your study. For example, if you are surveying people in your company, the population would be all the employees in your company.                                                                                                                                                                                                     |
| **Sample**                   | A subset of your population. Just like a food sample, it is called a sample because it is only a taste. So if your company is too large to survey every individual, you can survey a representative sample of your population.                                                                                                                                                       |
| **Margin of error**          | Since a sample is used to represent a population, the sample’s results are expected to differ from what the result would have been if you had surveyed the entire population. This difference is called the margin of error. The smaller the margin of error, the closer the results of the sample are to what the result would have been if you had surveyed the entire population. |
| **Confidence level**         | How confident you are in the survey results. For example, a 95% confidence level means that if you were to run the same survey 100 times, you would get similar results 95 of those 100 times. Confidence level is targeted before you start your study because it will affect how big your margin of error is at the end of your study.                                             |
| **Confidence interval**      | The range of possible values that the population’s result would be at the confidence level of the study. This range is the sample result +/- the margin of error.                                                                                                                                                                                                                    |
| **Statistical significance** | The determination of whether your result could be due to random chance or not. The greater the significance, the less due to chance.                                                                                                                                                                                                                                                 |

## Things to remember when determining the size of your sample

When figuring out a sample size, here are things to keep in mind:

- Don’t use a sample size less than 30. It has been statistically proven that 30 is the smallest sample size where an average result of a sample starts to represent the average result of a population.
- The confidence level most commonly used is 95%, but 90% can work in some cases.

Increase the sample size to meet specific needs of your project:
- For a **higher** confidence level, use a larger sample size
- To **decrease** the margin of error, use a larger sample size
- For **greater** statistical significance, use a larger sample size

**Note:** Sample size calculators use statistical formulas to determine a sample size. More about these are coming up in the course! Stay tuned.

### **Why a minimum sample of 30?**

This recommendation is based on the **Central Limit Theorem (CLT)** in the field of probability and statistics. As sample size increases, the results more closely resemble the normal (bell-shaped) distribution from a large number of samples. A sample of 30 is the smallest sample size for which the CLT is still valid. Researchers who rely on **regression analysis** – statistical methods to determine the relationships between controlled and dependent variables – also prefer a minimum sample of 30.

Still curious? Without getting too much into the math, check out these articles:
- [Central Limit Theorem (CLT)](https://www.investopedia.com/terms/c/central_limit_theorem.asp "Central Limit Theorem (CLT)"): This article by Investopedia explains the Central Limit Theorem and briefly describes how it can apply to an analysis of a stock index.
- [Sample Size Formula](https://www.statisticssolutions.com/dissertation-resources/sample-size-calculation-and-sample-size-justification/sample-size-formula/ "Sample Size Formula"): This article by Statistics Solutions provides a little more detail about why some researchers use 30 as a minimum sample size.

## Sample sizes vary by business problem

Sample size will vary based on the type of business problem you are trying to solve. 

For example, if you live in a city with a population of 200,000 and get 180,000 people to respond to a survey, that is a large sample size. But without actually doing that, what would an acceptable, smaller sample size look like? 

Would 200 be alright if the people surveyed represented every district in the city?
**Answer**: It depends on the stakes. 
- A sample size of 200 might be large enough if your business problem is to find out how residents felt about the new library
- A sample size of 200 might not be large enough if your business problem is to determine how residents would vote to fund the library

You could probably accept a larger margin of error surveying how residents feel about the new library versus surveying residents about how they would vote to fund it. For that reason, you would most likely use a larger sample size for the voter survey.

## Larger sample sizes have a higher cost

You also have to weigh the cost against the benefits of more accurate results with a larger sample size. Someone who is trying to understand consumer preferences for a new line of products wouldn’t need as large a sample size as someone who is trying to understand the effects of a new drug. For drug safety, the benefits outweigh the cost of using a larger sample size. But for consumer preferences, a smaller sample size at a lower cost could provide good enough results. 
## Knowing the basics is helpful

Knowing the basics will help you make the right choices when it comes to sample size. You can always raise concerns if you come across a sample size that is too small. A sample size calculator is also a great tool for this. Sample size calculators let you enter a desired confidence level and margin of error for a given population size. They then calculate the sample size needed to statistically achieve those results. 

Refer to the [Determine the Best Sample Size](https://www.coursera.org/learn/process-data/lecture/mSj5A/determine-the-best-sample-size "This link takes you to the Determine the Best Sample Size video in this course.") video for a demonstration of a sample size calculator, or refer to the [Sample Size Calculator](https://www.coursera.org/learn/process-data/supplement/ZqcDw/sample-size-calculator "This link takes you to the Sample Size Calculator reading in this course.") reading for additional information.

# Statistical power
- Statistical power is the probability of getting meaningful results from a test.
- Hypothesis testing is a way to see if a survey or experiment has meaningful results.
- [[What to do when there is no data]]
- [[Sample size calculator]]
- [[About margin of error]]
# Week 2 - Data Cleaning
- Dirty data is data that's incomplete, incorrect, or irrelevant to the problem you're trying to solve.
- [[Types of dirty data]]
	1. Duplicate data
	2. Outdated data
	3. Incomplete data
	4. Incorrect data
	5. Inconsistent (formatting) data
- ## Data cleaning tools and techniques
	- Before removing unwanted data, it's always a good practice to make a copy of the data set. That way, if you remove something that you end up needing in the future, you can easily access it and put it back in the data set.
- ## Data cleaning steps
	- Remove duplicate data
	- Remove unwanted/unrelated data
	- Remove spaces and blanks (in spreadsheets)
	- Fixing spellings, punctuation,and typos
- [[Common data cleaning mistakes]]
- ## Cleaning data in spreadsheets
	- Conditional formatting
		- Makes unwanted data stand out
			- Highlight blank cells
	- Remove duplicates (Data > Remove duplicates)
	- Consistent date formatting (Number > Date type)
	- Split text to columns (Data > Split text to columns)
		- Can be used to convert text string(eg. "707") to number (707).
- [[Workflow automation]]
- Sorting and Filtering
- Pivot Tables
- VLOOKUP
- 
# Week 3 - Cleaning data with SQL
- *Basic course*. Passed via assessments.
# Week 4 - Verifying and reporting your cleaning results
- **Verification** is a process to confirm that a data cleaning effort was well- executed and the resulting data is accurate and reliable. 
	- It involves rechecking your clean dataset, doing some manual clean ups if needed, and taking a moment to sit back and really think about the original purpose of the project. 
	- That way, you can be confident that the data you collected is credible and appropriate for your purposes. 
- A **changelog** is a file containing a chronologically ordered list of modifications made to a project. It's usually organized by version and includes the date followed by a list of added, improved, and removed features.
- ## Steps in verification
	- 1. Go back to your original dataset and compare your cleaned data. Go back to common problems.
	- 2. Take a big picture view of your project 
		- *Consider the business problem you're trying to solve.*
		- *Consider the goal of the project. Does the data you've collected and cleaned help your company towards this goal?*
		- *Consider the data is meeting the project objectives.*
	- *Tip: Ask teammates for fresh perspectives of the data.* 
- Verifying your data ensures that the insights you gain from analysis can be trusted. It's an essential part of data-cleaning that helps companies avoid big mistakes. 
- [[Checklist for data verification]]


# Week 5 - Optional: Adding data to your resume
- Keep in mind, you'll need to find a balance between what you want, what they want to give you, and what's fair. 
- ## Creating a resume
	- You can think of building a resume as taking a picture, a snapshot, of your skills.
	- The key here is to be brief. 
		- Try to keep everything in one page and each description to just a few bullet points. Two to four bullet points is enough but remember to keep your bullet points concise.
	- Stick to one page
		- Sticking to one page will help you stay focused on the details that best reflect who you are or who you want to be professionally. 
		- One page might also be all that hiring managers and recruiters have time to look at. They're busy people, so you want to get their attention with your resume as quickly as possible. 
	- Include your contact information
		- Name, Address, Contact Number, Email address
	- A format that focuses more on skills and qualifications and less on work history is great for people are starting out.
	- Summary: Entry-level data analytics professional; recently completed Google Data Analaytics Certificate.
	- Formula:
		- Accomplished [X] as measured by [Y] by doing [Z].
	- Technical Skills
	- Language proficiency
- ## Making your resume unique
	- For data analytics, one of the most important things your resume should do is show that you are a clear communicator.
	-  Speaking of the skill section, make sure you include any skills and qualifications you've acquired through this course and on your own.
		- You might even add in the top functions, packages or formulas that you're comfortable with in each. It also makes sense to include skills you've acquired in spreadsheets like pivot tables.
- [[Soft-skills to add to your resume]]

