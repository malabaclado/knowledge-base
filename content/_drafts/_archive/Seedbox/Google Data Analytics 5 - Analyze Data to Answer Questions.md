---
tags:
alias:
creation-date: Thursday 29th June 2023
---

Welcome to the fifth course in the series for the Google Data Analytics Certificate! The goal of data analysis is to make sense out of the data you collect and receive. Up until now, your focus has been on the preparations a data analyst goes through before entering the analysis phase. Specifically, in the last course, you learned about checking data for completeness and cleaning it for accuracy and reliability.

In this course, you will have hands-on practice organizing, sorting, filtering, formatting, converting, and combining data in spreadsheets. These are tasks you would complete in a real data analysis project. You will also learn how to sort and filter your data using SQL queries. You will be using functions and writing queries frequently as you continue your learning.

# Week 1 Organizing Data to Begin Analysis

Organizing data makes the data easier to use in an analysis. In this part of the course, you will learn the importance of organizing your data with **sorting and filtering**. You will explore organizing data in both spreadsheets and with SQL queries and temporary tables.


## Data Analysis Basics
- What is analysis?
	- **Analysis** is the process used to make sense of the data collected.
- The **goal of analysis** is to identify trends and relationships within the data so that you can accurately answer the question you're asking.
- Four phases of analysis
	- 1. Organize data - via sorting and filtering
	- 2. Format & Adjust data
	- 3. Get input from others
		- When analyzing data, gaining input from others is important because it gives you a viewpoint you might not understand or have access to. On top of gaining input from other people, it's also important to seek out others' perspectives early. That way, if they predict any obstacles or challenges, you'll know beforehand. 
		- The people you'll look to for input don't have to be experts to be helpful. Sometimes all you need is for someone who's familiar with a topic or data you're considering. 
	- 4. Transform data by observing relationships between data points and making calculations.

## Organize data for analysis
- It's super important that you keep your data organized throughout your analysis. How your data is classified and structured will impact your findings, whether you're working in a spreadsheet or a database.
- Sorting and filtering are two ways you can keep things organized when you format and adjust data to work with it. 
	- **Sorting** is when you *arrange data into a meaningful order* to make it easier to understand, analyze, and visualize.
	- **Filtering** is used when you are only interested in seeing data that meets a specific criteria, and hiding the rest.
		- The **benefit of filtering** the data is that after you fix errors or identify outliers, you can remove the filter and return the data to its original organization.

## Sorting data in spreadsheets
- When you sort data based on a specific metric, you can uncover new patterns and relationships within datasets you might not have otherwise noticed.
- **Sorting in spreadsheets** can be done in two ways (at least for Google Sheets)
	- 1. **Through the menu**
		- *Sort Sheet* - keeps the rows intact as you sort a range
		- *Sort Range* - sorts only the selected range, (caution: might jumble your data)
	- 2. **Via Function** (`SORT` function)
		- Syntax
			- In excel: `SORT(range, row_number)`
			- In google sheets: `=SORT(range, row_number, TRUE/FALSE for ASCENDING/DESCENDING)
- Sorting queries in SQL
	- ```SELECT *
	  FROM 'movie_data.movies'
	  WHERE Genre-"Comedy"
	  ORDER BY Release_Date DESC```
	- 
- 

# Week 2 Formatting and Adjusting Data

As you move closer to analyzing your data, you will want to have the data formatted and ready to go. In this part of the course, you will learn all about **converting and formatting data**, including how to use SQL queries to combine data. You will also discover the value of feedback and support from your colleagues and how it can lead to new insights that you can apply to your work.

- Typecasting data with SQL
- 


# Week 3 Aggregating Data for Analysis

During an analysis, you might need to combine data to gain insights and complete business objectives. In this part of the course, you will explore the functions, procedures, and syntax to combine, or aggregate data. You will learn how to combine data within multiple cells in spreadsheets, and within multiple database tables using SQL queries.

- Typecasting in Spreadsheets
	- String to date
		- [**How to convert text to date in Excel**](https://www.ablebits.com/office-addins-blog/2015/03/26/excel-convert-text-date/#:~:text=Excel%20DATEVALUE%20function%20%2D%20change%20text,Excel%20recognizes%20as%20a%20date.&text=So%2C%20the%20formula%20to%20convert,stored%20as%20a%20text%20string. "This link takes you to a blog on how to convert text to a date in Microsoft Excel."): Transforming a series of numbers into dates is a common scenario you will encounter. This resource will help you learn how to use Excel functions to convert text and numbers to dates, and how to turn text strings into dates without a formula. 
		- [**Google Sheets: Change date format:**](https://www.ablebits.com/office-addins-blog/2019/08/13/google-sheets-change-date-format/ "This link takes you to a blog on how to change to a date format in Google Sheets.") If you are working with Google Sheets, this resource will demonstrate how to convert your text strings to dates and how to apply the different date formats available in Google Sheets.
	- String to Numbers
		- [**How to convert text to number in Excel:**](https://www.ablebits.com/office-addins-blog/2018/07/18/excel-convert-text-to-number/ "This link takes you to a blog on how to convert text to a number in Excel.") Even though you will have values in your spreadsheet that resemble numbers, they may not actually be numbers. This conversion is important because it will allow your numbers to add up and be used in formulas without errors in Excel. 
		- [**How to convert text to numbers in Google Sheets:**](https://productivityspot.com/convert-text-to-numbers-google-sheets/ "This link takes you to instructions to convert text to a number in Google Sheets.") This resource is useful if you are working in Google Sheets; it will demonstrate how to convert text strings to numbers in Google Sheets. It also includes multiple formulas you can apply to your own sheets, so you can find the method that works best for you.
	- Combining Columns
		- [**Convert text from two or more cells:**](https://support.microsoft.com/en-us/office/combine-text-from-two-or-more-cells-into-one-cell-81ba0946-ce78-42ed-b3c3-21340eb164a6 "This link takes you to a Microsoft Support page to merge text in multiple cells in Excel.") Sometimes you may need to merge text from two or more cells. This Microsoft Support page guides you through two distinct ways you can accomplish this task without losing or altering your data. It also includes a step-by-step video tutorial to help guide you through the process.
		- [**How to split or combine cells in Google Sheets:**](https://www.techrepublic.com/article/how-to-split-or-combine-text-cells-with-google-sheets/ "This link takes you to an article with instructions to split or combine text in cells in Google Sheets.") This guide will demonstrate how to to split or combine cells using Google Sheets specifically. If you are using Google Sheets, this is a useful resource to reference if you need to combine cells. It includes an example using real data.
- Data Validation

# Week 4 Performing data calculations

Calculations are one of the more common tasks that data analysts perform during an analysis. In this part of the course, you will explore formulas, functions, and pivot tables in spreadsheets and SQL queries. All of these are used in data calculations. You will also learn about the benefits of using SQL to manage temporary database tables.

[[Types of data validation]]
[[Best practices when working with temporary tables]]