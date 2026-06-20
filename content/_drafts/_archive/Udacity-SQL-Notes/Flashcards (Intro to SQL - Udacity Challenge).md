---
tags: udacitychallenge, sql
alias:
creation-date: Saturday 18th February 2023
last-modified-date: Saturday 18th February 2023 14:26:08
cards-deck: SQL
---
# Lesson-1-SQL-Basics Flashcards

What does SQL stands for? :: Structured Query Language
^1676702274353

The key point here is that the ERD shows us {relationships} between tables.
^1676702274361

The {primary key} is often the first column in a table.
^1676702676258

A {foreign key} is a column in one table that is the primary key in a different table.
^1676702676264

### Why do businesses like DBs? #card
Remember: ISA
1.	Insurability. Data integrity is ensured
2.	Sharability. Data is easily shared
3.	Accessibility. Data can be accessed quickly
^1676702676269

A {SQL statement} is a command that allows you to perform a certain function.
^1676702676273

(CREATE TABLE) is a SQL statement that creates a new table in a database.

{DROP TABLE} is a SQL statement that removes a table in a database.
^1676702676277

{SELECT} is a SQL statement that allows you to read data and display it. This is called a query.
^1676702676283

The symbol {*} is used in the SELECT statement when you want to query all columns.
^1676702676287

The {LIMIT} clause limits the number of rows returned from a query. For example: You want to show only 10 results.
^1676703117445

The {ORDER BY} clause allows you specify which column you want to use as the basis for your query results ordering and whether you would like your query results to be put in ascending order or descending order.
^1676703117452

What is the default ordering for the ORDER BY clause? Ascending or Descending? :: Ascending
^1676703117459

You add {DESC} statement at the column you are sorting in the ORDER BY clause when you want the sorting order to be listed descendingly.
^1676703117466

The WHERE clause is placed {between FROM and ORDER BY}
^1676703117472

The {WHERE} clause allows you narrow your search to results where one column has a particular value or range of values.
^1676703117478

A {derived column} is a column you create by using mathematical operations on already existing columns.
^1676703117484

List the 5 logical operators in SQL::LIKE, IN, NOT, AND & BETWEEN, OR
^1676703117491

You can add the {NOT} operator before IN or LIKE to get the inverse of the results those queries would otherwise produce. 
^1676703117497

# Lesson-2-SQL-Joins

### Why are different sorts of data stored in different tables? #card 
1.	Some sorts of data are updated more frequently than other sorts and it’s more efficient and safer to store them separately
2.	Storing data in separate tables allows you to access the data much more quickly, because each table contains only a portion of the total available data
^1676708675125

Filtering JOINS can be executed in two ways: using {WHERE} and {ON-AND}
^1676708675133

{NULL} are a datatype that specifies where no data exists in SQL. That's not the same thing as 0. They were often ignored in our aggregation functions such as SUM.
^1676708675140

When identifying NULLs in a WHERE clause, we write {IS NULL (or IS NOT NULL)}.
^1676708675146

### What are two circumstances in which you might encounter NULL? #card 
- NULLs frequently occur when performing a LEFT or RIGHT JOIN. 
- NULLs can also occur from simply missing data in our database.
^1676708675153

The {COUNT} function gives you the total number of records in a table or the number of non-null records in a particular column in a table. 
^1676708675160

True or False: COUNT function works on non-numerical data :: True. It is just counting the non-null records.
^1676708675167

The {SUM} function adds up all of the numerical values in a column, ignoring the null values.
^1676708675174

True or False: MIN and MAX function works on non-numerical data :: True. Depending on the column type, MIN will return the lowest number, earliest date, or non-numerical value as early in the alphabet as possible. 
^1676708675180

The {MIN} function will return the lowest number, earliest date, or non-numerical value as early in the alphabet as possible.
^1676708675187

The {MAX} function returns the highest number, the latest date, or the non-numerical value closest alphabetically to “Z.” 
^1676708675194

The {AVG} function gives the average for a range of numerical values in a column. 
^1676708675200

True or False: When using AVG function, rows with NULL values are ignored :: True. This means you cannot include the null values as part of the average. (There is a solution around this)
^1676708675206

If you want to get an average that considers NULLs as 0, then you'll have to {divide the SUM by the COUNT for a column.}
^1676708675212

# Lesson-3-Aggregations

GROUP BY is placed in {between the WHERE clause and the ORDER BY clause.}
^1676709750773

The {GROUP BY} statement allows us to create segments within a column that will be aggregated independently of one another. 
^1676709750776

True or False: You can use DISTINCT multiple times in one SELECT statement :: False. You only use DISTINCT once in any particular SELECT statement.
^1676709750779

The HAVING clause is placed {after the GROUP BY clause and before the ORDER BY clause}
^1676709750782

{DATE_TRUNC} is a function that allows you to truncate your date to a particular part of your date-time column. Common truncations are *day*, *month*, and *year*.
^1676709750785

{DATE_PART} can be useful for pulling a specific portion of a date, but notice pulling month or day of the week (dow) means that you are no longer keeping the years in order. Rather you are grouping for certain components regardless of which year they belonged in.
^1676709750787

# Lesson-4-Subqueries-and-Temporary-Tables

What are the four placement types in subqueries? :: With, Inline, Nested, Scalar
^1676709750790

This subquery is used when you’d like to “pseudo-create” a table from an existing table and visually scope the temporary table at the top of the larger query. :: WITH subquery
^1676709750793

This subquery is used when you’d like the temporary table to act as a filter within the larger query, which implies that it often sits within the where clause. :: Nested subquery
^1676709750795

This subquery is used when you’d like to “pseudo-create” a table from an existing table. It’s embedded within the from clause. :: Inline subquery
^1676709750798

This subquery is used when you’d like to generate a scalar value to be used as a benchmark of some sort. :: Scalar
^1676709750801

Which of the 4 subquery placements are most advantageous for readability? :: With and Nested
^1676709750804

Which of the 4 subquery placements are advantageous for performance and are often used on smaller datasets? :: Scalar
^1676709750806

**Simple Subquery** ::: The inner subquery is completely independent of the larger query.
^1676709750809

**Correlated Subquery** ::: The inner subquery is dependent on the larger query. 
^1676709750812

{Views} are virtual tables that are derived from the tables in the db.
^1676709750815

### Can we update the base tables by updating a view? #card 
Since views do not exist physically in the database, **it is may or may not be possible** to execute UPDATE operations on views. It depends on the SELECT query used in the view definition. Generally, if the SELECT statement contains either an AGGREGATE function, GROUPING, or JOIN, then the view may not update the underlying base tables
^1676709750819

Things to consider when writing subqueries :: Readability, Performance
^1676709750821

# Lesson 5 Data Cleaning

{Data cleaning} is the task of cleaning up raw data to make it usable and ready for analysis.
^1676876145663

The {LEFT} function extracts a # of characters from a string starting from the left.
^1676876145668

The {RIGHT} function extracts a # of characters from a string starting from the right.
^1676876145670

The {SUBTR} function extracts a substring from a string (starting at any position).
^1676876145673

Syntax for SUBSTR :: SUBSTR(string, start, length)
^1676876161788

The {POSITION} SQL function returns the position of the first occurrence of a substring in a string
^1676968565268

Syntax for POSITION statement:: *POSITION(substring IN string)*
^1676968565294

The {STRPOS} function is used to determine the location in the string where the substring is being matched
^1676968565306

The {COALESCE} function is used to return the first non-null value that’s commonly used for normalizing data that’s stretched across multiple columns and includes NULLs.
^1676968565315

# SQL Window Functions
# Window functions are primarily used in two ways #card
1.  To understand a running total or a running metric while maintaining individual records
2.  To rank a dataset
^1676997693592

What is the key difference between aggregations and window functions?:: Windows functions retain the number of rows.
^1677041663075

 {Window function} allows users to compare one row to another without doing any joins. It is effective when you want to measure trends over time or rank a specific column, and it retains the total number of records without collapsing or condensing any of the original datasets.
^1677041663091

 {PARTITION BY} allows you to determine what you’d like to “group by” within the window function. Most often, you are partitioning by a month, region, etc. as you are tracking changes over time. This is the the *GROUP BY* equivalent in window functions.
^1677041663098

# Performance Tuning
