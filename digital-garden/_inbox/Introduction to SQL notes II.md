---
title: Introdution to SQL
tags:
  - sql
---

# Subqueries
## WITH Placement
### When to use `WITH` subquery?
-   When a user wants to **create a version** of an existing table **to be used in a larger query** (e.g., aggregate daily prices to an average price table).
-   It is advantageous for readability purposes.

Example: WITH Subuery
```SQL
WITH average_price as
( SELECT brand_id, AVG(product_price) as brand_avg_price
  FROM product_records
),
SELECT a.brand_id, a.total_brand_sales, b.brand_avg_price
FROM brand_table a
JOIN average_price b
ON b.brand_id = a.brand_id
ORDER BY a.total_brand_sales desc;
```

## WITH Common Table Expression

- CTE stands for Common Table Expression. A Common Table Expression in SQL allows you to define a temporary result, such as a table, to then be referenced in a later part of the query.

```SQL
WITH table1 AS (
          SELECT *
          FROM web_events),

     table2 AS (
          SELECT *
          FROM accounts)


SELECT *
FROM table1
JOIN table2
ON table1.account_id = table2.id;
```

## Placement: Nested
- Nested subquery is a subquery placed on the `WHERE` clause.
- Q: When to use a Nested subquery?
	- A: (1) When a user wants to filter an output using a condition met from another table. (2) To make code easier to read.

Example: Nested Subquery
```SQL
SELECT *
FROM students
WHERE student_id
IN (SELECT DISTINCT student_id
    FROM gpa_table
    WHERE gpa>3.5
    );
```

## Placement: Inline
- Inline subquery is subquery placed in the `FROM` clause.
- It has a very similar use case for With subquery, but it is less readable. Use less often. It is better to use the With subquery.

Example: Inline Subquery
```SQL
SELECT dept_name,
       max_gpa
FROM department_db x
     (SELECT dept_id
             MAX(gpa) as max_gpa
      FROM students
      GROUP BY dept_id
      )y
WHERE x.dept_id = y.dept_id
ORDER BY dept_name;
```

## Placement: Scalar
- Scalar subquery selects only one column and one row, used in `SELECT` clause.
- Why use a scalar subquery?
	- It is advantageous for performance.
	- Use when dataset is small.
- If a scalar subquery does not find a match, it returns a `NULL`. 
- If a scalar subquery finds multiple matches, it returns an `ERROR`.

Example: Scalar Subquery
```SQL
SELECT 
   (SELECT MAX(salary) FROM employees_db) AS top_salary,
   employee_name
FROM employees_db;
```


## Wrap-up for subqueries
- Subqueries are used to:
	- filter/aggregate data from another table
	- create a temporary table
	- increase readability within your code

# SQL Data Cleaning
- Data cleaning is a foundational skill for a data scientist

## Real-world Applications
- Q: What is data cleaning?
	- A: Manipulating data to make it usable for analysis.
	- A: The task of cleaning up raw data to make it usable and ready for analysis
- Q: When to use data cleaning techniques?
	- A: All the time! After collecting data -- and before making analyses.
		- Your data could all be lumped together in a single column, and you need to parse it to extract useful information.
		- Your data could all default to string data types, and you need to cast each column appropriately to run computations.
		- Your data could have un-standardized units of currency, and you need to normalize the column to ensure you are comparing equally across records.
- **Normalization** - Standardizing or “cleaning up a column” by transforming it in some way to make it ready for analysis. 
- A few normalization techniques are below:
	- Adjusting a column that includes multiple currencies to one common currency
	- Adjusting the varied distribution of a column value by transforming it into a z-score
	- Converting all price into a common metric (e.g., price per ounce)

![](https://i.imgur.com/3VE2zKy.png)

## Data Cleaning Strategy
- Key steps to consider when data cleaning:
	1. What data do you need?
		- Review what data you need to run an analysis and solve the problem at hand.
	2. What data do you have?
		- Take stock of not only the information you have in your dataset today but what data types those fields are. Do these align with your data needs?
	3. How will you clean your data?
		- Have a mental approach or a gameplan for cleaning the data
		- What types of actions and data cleaning techniques will you have to apply? 
		- Do you have the skills you need to go from the current to future state?
	4. How will you analyze your data?
		- How do you run an effective analysis? Build an approach for analysis, as well. And visualize your plan to solve the problem. 
		- Finally, remember to question “so what?” at the end of your results, which will help drive recommendations for your organization.

## Data Cleaning Methods
- The following set of methods cover three types of data cleaning techniques: 
	- extracting information within a column
	- returning the position of information within a column
	- changing the data type of the information.
- Methods to be discussed later on
	-   **Left:** Extracts a number of characters from a string starting from the left
	-   **Right:** Extracts a number of characters from a string starting from the right
	-   **Substr:** Extracts a substring from a string (starting at any position)
	-   **Position:** Returns the position of the first occurrence of a substring in a string
	-   **Strpos:** Returns the position of a substring within a string
	-   **Concat:** Adds two or more expressions together
	-   **Cast:** Converts a value of any type into a specific, different data type
	-   **Coalesce:** Returns the first non-null value in a list
	  
## LEFT, RIGHT, SUBSTR
-   **Left:** Extracts a # of characters from a string starting from the left
-   **Right:** Extracts a # of characters from a string starting from the right

Example: Syntax
```SQL
LEFT(student_information, 8) AS student_id
RIGHT(student_information, 6) AS salary
```

![](https://i.imgur.com/QmJYdXy.png)

-   **Substr:** Extracts a substring from a string (starting at any position)

![](https://i.imgur.com/pdTzfHs.png)

Example: Substr syntax
```SQL
SUBSTR(string, starting position (int), length (int))
SUBSTR(student_information, 11, 1) AS gender
```

![](https://i.imgur.com/9tXtmuM.png)

## Quiz & Solutions: Left and Right
1.  In the **accounts** table, there is a column holding the **website** for each company. The last three digits specify what type of web address they are using. A list of extensions (and pricing) is provided [here](https://iwantmyname.com/domains/domain-name-registration-list-of-extensions). Pull these extensions and provide how many of each website type exist in the **accounts** table.

Solution:
```SQL
SELECT RIGHT(website, 3) AS domain, COUNT(*) num_companies
FROM accounts
GROUP BY 1
ORDER BY 2 DESC;
```

My Solution (Using subqueries)
```SQL
WITH t1 AS 
	(SELECT RIGHT(website, 3) AS extension
	FROM accounts a)
SELECT t1.extension, COUNT(t1.extension)
FROM t1
GROUP BY 1
ORDER BY COUNT(t1.extension) DESC;
```

2.  There is much debate about how much the name [(or even the first letter of a company name)](https://www.quora.com/Does-a-companys-name-matter) matters. Use the **accounts** table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number).

```SQL
SELECT LEFT(UPPER(name), 1) AS first_letter, COUNT(*) num_companies
FROM accounts
GROUP BY 1
ORDER BY 2 DESC;
```

3.  Use the **accounts** table and a **CASE** statement to create two groups: one group of company names that start with a number and the second group of those company names that start with a letter. What proportion of company names start with a letter?

```SQL
SELECT SUM(num) nums, SUM(letter) letters
FROM (SELECT name, CASE WHEN LEFT(UPPER(name), 1) IN ('0','1','2','3','4','5','6','7','8','9') 
                          THEN 1 ELSE 0 END AS num, 
            CASE WHEN LEFT(UPPER(name), 1) IN ('0','1','2','3','4','5','6','7','8','9') 
                          THEN 0 ELSE 1 END AS letter
         FROM accounts) t1;
```

4.  Consider vowels as `a`, `e`, `i`, `o`, and `u`. What proportion of company names start with a vowel, and what percent start with anything else?

```SQL
SELECT SUM(vowels) vowels, SUM(other) other
FROM (SELECT name, CASE WHEN LEFT(UPPER(name), 1) IN ('A','E','I','O','U') 
                           THEN 1 ELSE 0 END AS vowels, 
             CASE WHEN LEFT(UPPER(name), 1) IN ('A','E','I','O','U') 
                          THEN 0 ELSE 1 END AS other
            FROM accounts) t1;
```

## BONUS Concept: `STRING_SPLIT`
![](https://i.imgur.com/eG2l8SN.png)

Solution code:
```SQL
WITH table AS(
SELECT  student_information,
        value,
        ROW _NUMBER() OVER(PARTITION BY student_information ORDER BY (SELECT NULL)) AS row_number
FROM    student_db
        CROSS APPLY STRING_SPLIT(student_information, ',') AS back_values
)
SELECT  student_information,
        [1] AS STUDENT_ID,
        [2] AS GENDER,
        [3] AS CITY,
        [4] AS GPA,
        [5] AS SALARY
FROM    table
PIVOT(
        MAX(VALUE)
        FOR row_number IN([1],[2],[3],[4],[5])
) AS PVT)
```

## Concat
![](https://i.imgur.com/ubxC3Kf.png)

**CONCAT:** Adds two or more expressions together

Example: CONCAT syntax

```SQL
CONCAT(string1, string2, string3)
CONCAT(month, '-', day, '-', year) AS date
```

## Quiz & Solutions: Concat
1.  Suppose the company wants to assess the performance of all the sales representatives. Each sales representative is assigned to work in a particular region. To make it easier to understand for the HR team, display the concatenated `sales_reps.id`, ‘_’ (underscore), and `region.name` as `EMP_ID_REGION` for each sales representative.

```SQL
SELECT CONCAT(SALES_REPS.ID, '_', REGION.NAME) EMP_ID_REGION, SALES_REPS.NAME
FROM SALES_REPS
JOIN REGION
ON SALES_REPS.REGION_ID = REGION_ID;
```


2.  From the `accounts` table, display the name of the client, the `coordinate` as concatenated (latitude, longitude), `email id` of the primary point of contact as `<first letter of the primary_poc><last letter of the primary_poc>@<extracted name and domain from the website>`.
```SQL
SELECT NAME, CONCAT(LAT, ', ', LONG) COORDINATE, CONCAT(LEFT(PRIMARY_POC, 1), RIGHT(PRIMARY_POC, 1), '@', SUBSTR(WEBSITE, 5)) EMAIL
FROM ACCOUNTS;
```

3. From the `web_events` table, display the concatenated value of `account_id, '_' , channel, '_', count of web events of the particular channel`. 

```SQL
SELECT NAME, CONCAT(LAT, ', ', LONG) COORDINATE, CONCAT(LEFT(PRIMARY_POC, 1), RIGHT(PRIMARY_POC, 1), '@', SUBSTR(WEBSITE, 5)) EMAIL
FROM ACCOUNTS;
```

## CAST 
![](https://i.imgur.com/TpXzHlr.png)

**CAST**: Converts a value of any type into a specific, different data type

Example: CAST Syntax
```SQL
CAST(expression AS datatype)
CAST(salary AS int)
```

## Quiz & Solutions: CAST
![](https://i.imgur.com/tQTwUFj.png)

1. Solution:
```SQL
SELECT *
FROM sf_crime_data
LIMIT 10;
```

2. **yyyy-mm-dd**

3. Solution: The format of the `date` column is **mm/dd/yyyy** with times that are not correct also at the end of the date.

4. Solution:
```SQL
SELECT date orig_date, (SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2))::DATE new_date
FROM sf_crime_data;
```

5. Solution:
```SQL
SELECT date orig_date, (SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2))::DATE new_date
FROM sf_crime_data;```


## Advanced Cleaning Functions
- **Position**: Returns the position of the first occurrence of a substring in a string.
- **Strpos:** Returns the position of a substring within a string
- **Coalesce:** Used to return the first non-null value that’s commonly used for normalizing data that’s stretched across multiple columns and includes NULLs.

## POSITION, STRPOS
![](https://i.imgur.com/krK1pbI.png)

Example: POSITION syntax
```SQL
POSITION(substring IN string)

POSITION("$" IN student_information) as
salary_starting_position
```

![](https://i.imgur.com/x75LtYH.png)

Example: STRPOS syntax
```SQL
STRPOS(string, substring)
```

## Quiz and Solution: STRPOS
1.  Use the `accounts` table to create **first** and **last** name columns that hold the first and last names for the `primary_poc`.

```SQL
SELECT LEFT(primary_poc, STRPOS(primary_poc, ' ') -1 ) first_name, 
RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) last_name
FROM accounts;
```

2. Now see if you can do the same thing for every rep `name` in the `sales_reps` table. Again provide **first** and **last** name columns.

```SQL
SELECT LEFT(name, STRPOS(name, ' ') -1 ) first_name, 
       RIGHT(name, LENGTH(name) - STRPOS(name, ' ')) last_name
FROM sales_reps;
```

## Quiz & Solution: CONCAT & STRPOS
1.  Each company in the `accounts` table wants to create an email address for each `primary_poc`. The email address should be the first name of the **primary_poc** `.` last name **primary_poc** `@` company name `.com`.

```SQL
WITH t1 AS (
 SELECT LEFT(primary_poc,     STRPOS(primary_poc, ' ') -1 ) first_name,  RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) last_name, name
 FROM accounts)
SELECT first_name, last_name, CONCAT(first_name, '.', last_name, '@', name, '.com')
FROM t1;
```

2. You may have noticed that in the previous solution some of the company names include spaces, which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account `name`, but otherwise, your solution should be just as in question `1`. Some helpful documentation is [here](https://www.postgresql.org/docs/8.1/static/functions-string.html).

```SQL
WITH t1 AS (
 SELECT LEFT(primary_poc,     STRPOS(primary_poc, ' ') -1 ) first_name,  RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) last_name, name
 FROM accounts)
SELECT first_name, last_name, CONCAT(first_name, '.', last_name, '@', REPLACE(name, ' ', ''), '.com')
FROM  t1;
```

3. We would also like to create an initial password, which they will change after their first log in. The first password will be the first letter of the `primary_poc`'s first name (lowercase), then the last letter of their first name (lowercase), the first letter of their last name (lowercase), the last letter of their last name (lowercase), the number of letters in their first name, the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.

```SQL
WITH t1 AS (
 SELECT LEFT(primary_poc,     STRPOS(primary_poc, ' ') -1 ) first_name,  RIGHT(primary_poc, LENGTH(primary_poc) - STRPOS(primary_poc, ' ')) last_name, name
 FROM accounts)
SELECT first_name, last_name, CONCAT(first_name, '.', last_name, '@', name, '.com'), LEFT(LOWER(first_name), 1) || RIGHT(LOWER(first_name), 1) || LEFT(LOWER(last_name), 1) || RIGHT(LOWER(last_name), 1) || LENGTH(first_name) || LENGTH(last_name) || REPLACE(UPPER(name), ' ', '')
FROM t1;
```


## Coalesce
![](https://i.imgur.com/XtubDxx.png)
![](https://i.imgur.com/hRpw8IB.png)

Example: COALESCE syntax
```SQL
COALESCE(val1, val2, val3...)

COALESCE(hourly_wage*40*52, salary, commission*sales) AS annual_income
```

COALESCE is a command that helps you deal with null values. Now before using COALESCE, take a step back and think through how’d you like to deal with missing values in the first place.

- The three methods below are the most common ways to deal with null values in SQL:
	- **Coalesce**: Allows you to return the first non-null value across a set of columns in a slick, single command. 
		- This is a good approach only if a single column’s value needs to be extracted whilst the rest are null. *See example above.*
	- **Drop records**: Sometimes, if there are null values in records at all, analysts can decide to drop the row entirely. 
		- This is not favorable, as it removes data. Data is precious. Think about the reason those values are null. Does it make sense to use COALESCE, drop records, and conduct an imputation.
	- **Imputation**: Outside of the COALESCE use case, you may want to impute missing values. 
		- If so, think about the problem you are trying to solve, and impute accordingly. Perhaps you’d like to be conversative so you take the MIN of that column or the 25th percentile value. 
		- Classic imputation values are often the median or mean value of the column.

## Quiz & Solution: COALESCE
![](https://i.imgur.com/6PQkkwx.png)

1. Solution:
```SQL
SELECT *
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL; 
```
2. Solution:
```SQL
SELECT COALESCE(a.id, a.id) filled_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id, o.*
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL;
```
3. Solution:
```SQL
SELECT COALESCE(a.id, a.id) filled_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id, COALESCE(o.account_id, a.id) account_id, o.occurred_at, o.standard_qty, o.gloss_qty, o.poster_qty, o.total, o.standard_amt_usd, o.gloss_amt_usd, o.poster_amt_usd, o.total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL;
```
4. Solution:
```SQL
SELECT COALESCE(a.id, a.id) filled_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id, COALESCE(o.account_id, a.id) account_id, o.occurred_at, COALESCE(o.standard_qty, 0) standard_qty, COALESCE(o.gloss_qty,0) gloss_qty, COALESCE(o.poster_qty,0) poster_qty, COALESCE(o.total,0) total, COALESCE(o.standard_amt_usd,0) standard_amt_usd, COALESCE(o.gloss_amt_usd,0) gloss_amt_usd, COALESCE(o.poster_amt_usd,0) poster_amt_usd, COALESCE(o.total_amt_usd,0) total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL;
```
5. Solution:
```SQL
SELECT COUNT(*)
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id;
```
6. Solution:
```SQL
SELECT COALESCE(a.id, a.id) filled_id, a.name, a.website, a.lat, a.long, a.primary_poc, a.sales_rep_id, COALESCE(o.account_id, a.id) account_id, o.occurred_at, COALESCE(o.standard_qty, 0) standard_qty, COALESCE(o.gloss_qty,0) gloss_qty, COALESCE(o.poster_qty,0) poster_qty, COALESCE(o.total,0) total, COALESCE(o.standard_amt_usd,0) standard_amt_usd, COALESCE(o.gloss_amt_usd,0) gloss_amt_usd, COALESCE(o.poster_amt_usd,0) poster_amt_usd, COALESCE(o.total_amt_usd,0) total_amt_usd
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id;
```

## Further readings
- [SQL ISNULL(), NVL(), IFNULL() and COALESCE() Functions (w3schools.com)](https://www.w3schools.com/sql/sql_isnull.asp)
- [Using SQL String Functions to Clean Data | Advanced SQL - Mode](https://mode.com/sql-tutorial/sql-string-functions-for-cleaning/)

# SQL Window Functions
- Window functions are primarily used in two ways:
	1. To understand a running total or a running metric while maintaining individual records
	2. To rank a dataset

- Three different types of window functions
	- Core functions
	- Ranking functions
	- Advanced functions

## Real-world Applications of window functions
- When to use window functions?
	- When you want to measure trends or changes over rows of data.
	- When you want to rank a column for outreach or prioritization.
- Sample use cases
	- Calculate a running average of ticket prices partitioned by month and ordered by time.
	- Calculate the running count of orders and maintain as a separate row within the table.
	- Include a rank column in the output to be used by a Business Development rep to reach out potential customers.

## What is a window function?
- What is a window function?
	-  A window function is a calculation across a set of rows in a table that are somehow related to the current row. 
	- Similar to aggregation functions but window functions retain the total number of rows.

![](https://i.imgur.com/0YcTLk8.png)

Example: code from the video
```SQL
SELECT order_id,
       order_date,
       SUM(order_total) OVER
          (PARTITION BY month(order_date) ORDER BY order_date)
          AS running_monthly_sales
FROM amazon_db
WHERE order_date>'2017-01-01';
```

Here's a good [documentation for window functions](https://www.postgresql.org/docs/9.1/tutorial-window.html).

## Terms to be covered
- Three types of window functions
- Core functions
	- Partition by: A subclause of the OVER clause. Similar to GROUP BY.
	- Over: Typically precedes the partition by that signals what to “GROUP BY”.
	- Aggregates: Aggregate functions that are used in window functions, too (e.g., sum, count, avg).
- Ranking functions
	- Row_number(): Ranking function where each row gets a different number.
	- Rank(): Ranking function where a row could get the same rank if they have the same value.
	- Dense_rank(): Ranking function similar to rank() but ranks are not skipped with ties.
- Advanced functions
	- Aliases: Shorthand that can be used if there are several window functions in one query.
	- Percentiles: Defines what percentile a value falls into over the entire table.
	- Lag/Lead: Calculating differences between rows’ values.

## Core window functions
![](https://i.imgur.com/hfAORhl.png)

![](https://i.imgur.com/jbPLp9a.png)

Example: PARTITION BY Syntax
```SQL
AGGREGATE_FUNCTION (column_1) OVER
 (PARTITION BY column_2 ORDER BY column_3)
  AS new_column_name;
```

There are a few key terms to review as a part of understanding core window functions:

-   **PARTITION BY:** A subclause of the OVER clause. I like to think of PARTITION BY as the GROUP BY equivalent in window functions. PARTITION BY allows you to determine what you’d like to “group by” within the window function. Most often, you are partitioning by a month, region, etc. as you are tracking changes over time.
-   **OVER:** This syntax signals a window function and precedes the details of the window function itself.

### The sequence of code for window functions
Typically, when you are writing a window function that tracks changes or a metric over time, you are likely to structure your syntax with the following components:

1.  An aggregation function (e.g., sum, count, or average) + the column you’d like to track
2.  OVER
3.  PARTITION BY + the column you’d like to “group by”
4.  ORDER BY (optional and is often a date column)
5.  AS + the new column name

Some reading: [SQL SERVER - What is the OVER Clause? - Notes from the Field #101 - SQL Authority with Pinal Dave](https://blog.sqlauthority.com/2015/11/04/sql-server-what-is-the-over-clause-notes-from-the-field-101/)


## Quiz: Core functions 1
1. Create a running total of `standard_amt_usd` (in the `orders` table) over order time with no date truncation. Your final table should have two columns: one with the amount being added for each new row, and a second with the running total.

```SQL
SELECT standard_amt_usd,
       SUM(standard_amt_usd) OVER (ORDER BY occurred_at) AS running_total
FROM orders
```

2. Now, modify your query from the previous quiz to include partitions. Still create a running total of `standard_amt_usd` (in the `orders` table) over order time, but this time, date truncate `occurred_at` by year and partition by that same year-truncated `occurred_at` variable.


Your final table should have three columns:

-   One with the amount being added for each row
-   One for the truncated date,
-   A final column with the running total within each year

```SQL
SELECT standard_amt_usd,
       DATE_TRUNC('year', occurred_at) as year,
       SUM(standard_amt_usd) OVER (PARTITION BY DATE_TRUNC('year', occurred_at) ORDER BY occurred_at) AS running_total
FROM orders
```

## GROUP BY  vs Window Functions
### Similarities

Both groups by/aggregation queries and window functions serve the same use case. Synthesizing information over time and often grouped by a column (e.g., a region, month, customer group, etc.)

### Differences

The difference between group by/aggregation queries and window functions is simple. The output of window functions retains all individual records whereas the group by/aggregation queries condense or collapse information.

### Key Notes

-   You can’t use window functions and standard aggregations in the same query. More specifically, **you can’t include window functions in a GROUP BY clause**.
-   Feel free to use as many window functions as you’d like in a single query. E.g., if you’d like to have an average, sum, and count aggregate function that captures three metrics’ running totals, go for it.

Example: Multiple aggregate windowed function
```SQL
SELECT order_id,
       order_total,
       order_price,
       SUM(order_total) OVER
           (PARTITION BY month(order_date) ORDER BY order_date) AS running_monthly_sales,
       COUNT(order_id) OVER
           (PARTITION BY month(order_date) ORDER BY order_date) AS running_monthly orders,
       AVG(order_price) OVER
           (PARTITION BY month(order_date) ORDER BY order_date) AS average_monthly_price
FROM  amazon_sales_db
WHERE order_date < '2017-01-01';
```

## Aggregates in Window functions with and without ORDER BY

The `ORDER BY` clause is one of two clauses integral to window functions. The `ORDER` and `PARTITION` define what is referred to as the “window”—the ordered subset of data over which calculations are made. Removing `ORDER BY` just leaves an unordered partition; in our query's case, each column's value is simply an aggregation (e.g., sum, count, average, minimum, or maximum) of all the `standard_qty` values in its respective `account_id`.

As Stack Overflow user mathguy [explains](https://stackoverflow.com/questions/41364665/analytic-count-over-partition-with-and-without-order-by-clause):

> The easiest way to think about this - leaving the `ORDER BY` out is equivalent to "ordering" in a way that all rows in the partition are "equal" to each other. Indeed, you can get the same effect by explicitly adding the `ORDER BY` clause like this: `ORDER BY 0` (or "order by" any constant expression), or even, more emphatically, `ORDER BY NULL`.

## Ranking window functions
- There are three types of ranking functions
	- Row_number(): Ranking is distinct amongst records even with ties in what the table is ranked against.
	- Rank(): Ranking is the same amongst tied values and ranks skip for subsequent values.
	- Dense_rank(): Ranking is the same amongst tied values and ranks do not skip for subsequent values.

Example: ROW_NUMBER syntax
```SQL
SELECT ROW_NUMBER() OVER(ORDER BY date_time) AS rank,
       date_time
FROM   db;
```

Example: RANK syntax
```SQL
SELECT RANK() OVER(ORDER BY date_time) AS rank,
       date_time
FROM   db;
```

Example: DENSE_RANK syntax
```SQL
SELECT DENSE_RANK() OVER(ORDER BY date_time) AS rank,
       date_time
FROM   db;
```

## Quiz: ROW_NUMBER and RANK
Select the `id`, `account_id`, and `total` variable from the `orders` table, then create a column called `total_rank` that ranks this total amount of paper ordered (from highest to lowest) _for each account_ using a partition. Your final table should have these four columns.

```SQL
SELECT id,
       account_id,
       total,
       RANK() OVER (PARTITION BY account_id ORDER BY total DESC) AS total_rank
FROM orders
```

## Advanced Functions
**If you are planning to write multiple window functions that leverage the same PARTITION BY, OVER, and ORDER BY in a single query,** leveraging aliases will help tighten your syntax.

### Details of Aliases

-   A **monthly_window** alias function is defined at the end of the query in the **WINDOW** clause.
-   It is then called on **each time** an aggregate function is used within the SELECT clause.


This repetetive code: ![](https://i.imgur.com/jafkw5C.png)
Would become this code
![](https://i.imgur.com/MmCxYhD.png)

## Quiz: aliasing
1. Now, create and use an alias to shorten the following query (which is **_different_** from the one in the Aggregates in Windows Functions video) that has multiple window functions. Name the alias `account_year_window`, which is more descriptive than `main_window` in the example above.

```SQL
SELECT id,
       account_id,
       DATE_TRUNC('year',occurred_at) AS year,
       DENSE_RANK() OVER account_year_window AS dense_rank,
       total_amt_usd,
       SUM(total_amt_usd) OVER account_year_window AS sum_total_amt_usd,
       COUNT(total_amt_usd) OVER account_year_window AS count_total_amt_usd,
       AVG(total_amt_usd) OVER account_year_window AS avg_total_amt_usd,
       MIN(total_amt_usd) OVER account_year_window AS min_total_amt_usd,
       MAX(total_amt_usd) OVER account_year_window AS max_total_amt_usd
FROM orders 
WINDOW account_year_window AS (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at))
```

## Comparing a Row to Previous Row - LAG
- LAG function - It returns the value from a previous row to the current row in the table.

## Comparing a Row to Previous Row - LEAD
- LEAD function - Return the value from the row following the current row in the table.

## LAG and LEAD
### Use Case
When you need to compare the values in adjacent rows or rows that are offset by a certain number, LAG and LEAD come in very handy.

## Quiz: Comparing a Row to the Previous Row

### Percentiles Use Case

When there are a large number of records that need to be ranked, individual ranks (e.g., 1, 2, 3, 4…) are ineffective in helping teams determine the best of the distribution from the rest. Percentiles help better describe large datasets. For example, a team might want to reach out to the Top 5% of customers.

You can use window functions to identify what percentile (or quartile, or any other subdivision) a given row falls into. The syntax is `NTILE(# of buckets)`. In this case, `ORDER BY` determines which column to use to determine the quartiles (or whatever number of ‘tiles you specify).

### Percentiles Syntax

The following components are important to consider when building a query with percentiles:

1.  NTILE + the number of buckets you’d like to create within a column (e.g., 100 buckets would create traditional percentiles, 4 buckets would create quartiles, etc.)
2.  OVER
3.  ORDER BY (optional, typically a date column)
4.  AS + the new column name

### Expert Tip

In cases with relatively few rows in a window, the `NTILE` function doesn’t calculate exactly as you might expect. For example, If you only had two records and you were measuring percentiles, you’d expect one record to define the 1st percentile, and the other record to define the 100th percentile. Using the `NTILE` function, what you’d actually see is one record in the 1st percentile, and one in the 2nd percentile.

In other words, when you use an NTILE function but the number of rows in the partition is less than the NTILE(number of groups), then NTILE will divide the rows into as many groups as there are members (rows) in the set but then stop short of the requested number of groups. If you’re working with very small windows, keep this in mind and consider using quartiles or similarly small bands.

![](https://i.imgur.com/6a0NbzU.png)

Example: Sample code
```SQL
NTILE(# of buckets) OVER (ORDER BY ranking_column) AS new_column_name

SELECT  customer_id,
        composite_score,
        NTILE(100) OVER(ORDER BY composite_score) AS percentile
FROM    customer_lead_score;
```

## Quiz: Percentiles with Partitions


You can use partitions with percentiles to determine the percentile of a specific subset of all rows. Imagine you're an analyst at Parch & Posey and you want to determine the largest orders (in terms of quantity) a specific customer has made to encourage them to order more similarly sized large orders. You only want to consider the `NTILE` for that customer's `account_id`.

In the SQL Explorer below, write three queries (separately) that reflect each of the following:

1.  Use the `NTILE` functionality to divide the accounts into 4 levels in terms of the amount of `standard_qty` for their orders. Your resulting table should have the `account_id`, the `occurred_at` time for each order, the total amount of `standard_qty` paper purchased, and one of four levels in a `standard_quartile` column.

```SQL
SELECT
       account_id,
       occurred_at,
       standard_qty,
       NTILE(4) OVER (PARTITION BY account_id ORDER BY standard_qty) AS standard_quartile
  FROM orders 
 ORDER BY account_id DESC
```

2. Use the `NTILE` functionality to divide the accounts into two levels in terms of the amount of `gloss_qty` for their orders. Your resulting table should have the `account_id`, the `occurred_at` time for each order, the total amount of `gloss_qty` paper purchased, and one of two levels in a `gloss_half` column.

```SQL
SELECT
       account_id,
       occurred_at,
       gloss_qty,
       NTILE(2) OVER (PARTITION BY account_id ORDER BY gloss_qty) AS gloss_half
  FROM orders 
 ORDER BY account_id DESC
```

3. Use the `NTILE` functionality to divide the orders for each account into 100 levels in terms of the amount of `total_amt_usd` for their orders. Your resulting table should have the `account_id`, the `occurred_at` time for each order, the total amount of `total_amt_usd` paper purchased, and one of 100 levels in a `total_percentile` column.

```SQL
SELECT
       account_id,
       occurred_at,
       total_amt_usd,
       NTILE(100) OVER (PARTITION BY account_id ORDER BY total_amt_usd) AS total_percentile
  FROM orders 
 ORDER BY account_id DESC
```

**Note:** To make it easier to interpret the results, order by the account_id in each of the queries.


# SQL Advanced Joins & Performance Tuning

## FULL OUTER JOIN
![](https://i.imgur.com/D4poiTh.png)

```SQL
SELECT column_name(s)
FROM Table_A
FULL OUTER JOIN Table_B ON Table_A.column_name = Table_B.column_name;
```

![](https://i.imgur.com/6o5XxKE.png)


A common application of this is when joining two tables on a timestamp.

If you wanted to return unmatched rows only, which is useful for some cases of data assessment, you can isolate them by adding the following line to the end of the query:

```
WHERE Table_A.column_name IS NULL OR Table_B.column_name IS NULL
```

## Quiz: Full Outer Join
You’re not likely to use `FULL JOIN` (which can also be written as `FULL OUTER JOIN`) too often, but the syntax is worth practicing anyway. `LEFT JOIN` and `RIGHT JOIN` each return unmatched rows from one of the tables—`FULL JOIN` returns unmatched rows from both tables. `FULL JOIN` is commonly used in conjunction with aggregations to understand the amount of overlap between two tables.

Say you're an analyst at Parch & Posey and you want to see:

-   each account who has a sales rep and each sales rep that has an account (all of the columns in these returned rows will be full)
-   but also each account that does not have a sales rep and each sales rep that does not have an account (some of the columns in these returned rows will be empty)

This type of question is rare, but `FULL OUTER JOIN` is perfect for it. In the following SQL Explorer, write a query with `FULL OUTER JOIN` to fit the above described Parch & Posey scenario (selecting all of the columns in both of the relevant tables, `accounts` and `sales_reps`) then answer the subsequent multiple-choice quiz.

## Joining without an equals sign

If you recall from earlier lessons on joins, the join clause is evaluated before the where clause -- filtering in the join clause will eliminate rows before they are joined, while filtering in the WHERE clause will leave those rows in and produce some nulls.

Example: Inequality Join
```SQL
SELECT orders.id,
       orders.occurred_at  AS order_date,
       events.*
FROM   orders
LEFT JOIN web_events events
       ON events.account_id = orders.account_id
      AND events.occurred_at = orders.occurred_at
WHERE  DATE_TRUNC('month', orders.occurred_at)=
       (SELECT DATE_TRUNC('month', MIN(orders.occurred_at)) FROM orders)
ORDER BY orders.occurred_at, orders.occurred_at
```

## Quiz: Inequality Joins

The query in Derek's video was pretty long. Let's now use a shorter query to showcase the power of joining with comparison operators.

Inequality operators (a.k.a. comparison operators) don't only need to be date times or numbers, they also work on strings! You'll see how this works by completing the following quiz, which will also reinforce the concept of joining with comparison operators.

In the following SQL Explorer, write a query that left joins the `accounts` table and the `sales_reps` tables on each sale rep's ID number _and_ joins it using the `<` comparison operator on `accounts.primary_poc` and `sales_reps.name`, like so:

```
accounts.primary_poc < sales_reps.name
```

The query results should be a table with three columns: the account name (e.g. Johnson Controls), the primary contact name (e.g. Cammy Sosnowski), and the sales representative's name (e.g. Samuel Racine). Then answer the subsequent multiple-choice question.

Solution:
```SQL
SELECT accounts.name as account_name,
       accounts.primary_poc as poc_name,
       sales_reps.name as sales_rep_name
  FROM accounts
  LEFT JOIN sales_reps
    ON accounts.sales_rep_id = sales_reps.id
   AND accounts.primary_poc < sales_reps.name
```


## Self join
This comes up pretty commonly in job interviews. Self JOIN logic can be pretty tricky -- you can see here that our join has three conditional statements. It is important to pause and think through each step when joining a table to itself.

Example: Self Join
```SQL
SELECT o1.id AS o1_id,
       o1.account_id AS o1_account_id,
       o1.occurred_at AS o1_occurred_at,
       o2.id AS o2_id,
       o2.account_id AS o2_account_id,
       o2.occurred_at AS o2_occurred_at
FROM   orders o1
LEFT JOIN orders o2
ON     o1.account_id = o2.account_id
AND    o2.occurred_at > o1.occurred_at
AND    o2.occurred_at <= o1.occurred_at + INTERVAL '28 days'
ORDER BY o1.account_id, o1.occurred_at
```

## Quiz: Self join
One of the most common use cases for self JOINs is in cases where two events occurred, one after another. As you may have noticed in the previous video, using inequalities in conjunction with self JOINs is common.

Modify the query from the previous video, which is pre-populated in the SQL Explorer below, to perform the same interval analysis except for the `web_events` table. Also:

-   change the interval to 1 day to find those web events that occurred after, but not more than 1 day after, another web event
-   add a column for the `channel` variable in both instances of the table in your query

Solution: 
```SQL
SELECT we1.id AS we_id,
       we1.account_id AS we1_account_id,
       we1.occurred_at AS we1_occurred_at,
       we1.channel AS we1_channel,
       we2.id AS we2_id,
       we2.account_id AS we2_account_id,
       we2.occurred_at AS we2_occurred_at,
       we2.channel AS we2_channel
  FROM web_events we1 
 LEFT JOIN web_events we2
   ON we1.account_id = we2.account_id
  AND we1.occurred_at > we2.occurred_at
  AND we1.occurred_at <= we2.occurred_at + INTERVAL '1 day'
ORDER BY we1.account_id, we2.occurred_at
```

You can find more on the types of INTERVALS (and other date-related functionality) in the Postgres documentation [here](https://www.postgresql.org/docs/8.2/static/functions-datetime.html).

## UNION
### UNION Use Case

-   The UNION operator is used to combine the result sets of 2 or more SELECT statements. It removes duplicate rows between the various SELECT statements.
-   Each SELECT statement within the UNION must have the same number of fields in the result sets with similar data types.
-   Typically, the use case for leveraging the UNION command in SQL is when a user wants to pull together distinct values of specified columns that are spread across multiple tables. For example, a chef wants to pull together the ingredients and respective aisle across three separate meals that are maintained within different tables.

### Details of UNION

-   There must be the same number of expressions in both SELECT statements.
-   The corresponding expressions must have the same data type in the SELECT statements.
-   For example:
    -   Expression1 must be the same data type in both the first and second SELECT statement.

### Expert Tip

-   UNION removes duplicate rows.
-   UNION ALL does not remove duplicate rows.

### Resources

The resource [here](https://www.techonthenet.com/sql/union.php) on SQL UNIONs is helpful in understanding syntax and examples.

SQL's two strict rules for appending data:

1.  Both tables must have the same number of columns.
2.  Those columns must have the same data types in the same order as the first table.

A common misconception is that column names have to be the same. Column names, in fact, **don't** need to be the same to append two tables but you will find that they typically are.

Example: UNION syntax
```SQL
CREATE VIEW web_events_2
AS (SELECT * FROM web_events)

SELECT *
FROM web_events
UNION
SELECT *
FROM web_events_2
```

Example: Using UNION as a subuery
```SQL
CREATE VIEW web_events_2
AS (SELECT * FROM web_events)

SELECT channel,
       COUNT(*) AS sessions
FROM (
      SELECT *
      FROM web_events
      UNION ALL
      SELECT *
      FROM web_events_2
     ) web_events
GROUP BY 1
ORDER BY 2 DESC
```

Example: A more readable friendly version of the code above
```SQL
CREATE VIEW web_events_2
AS (SELECT * FROM web_events)

WITH web_events AS (
      SELECT *
      FROM web_events
      UNION ALL
      SELECT *
      FROM web_events_2
     )
SELECT channel,
       COUNT(*) AS sessions
FROM  web_events
GROUP BY 1
ORDER BY 2 DESC
```

## Quiz: UNION

### Appending data 
Write a query that uses `UNION ALL` on two instances (and selecting all columns) of the `accounts` table. Then inspect the results and answer the subsequent quiz.

Solution:
```SQL
SELECT *
    FROM accounts

UNION ALL

SELECT *
  FROM accounts
```

### Pretreating Tables before doing a UNION
Add a `WHERE` clause to each of the tables that you unioned in the query above, filtering the first table where `name` equals Walmart and filtering the second table where `name` equals Disney. Inspect the results then answer the subsequent quiz.

Solution:
```SQL
SELECT *
    FROM accounts
    WHERE name = 'Walmart'

UNION ALL

SELECT *
  FROM accounts
  WHERE name = 'Disney'
```

### Performing Operations on a Combined Dataset

Perform the union in your first query (under the **Appending Data via UNION** header) in a common table expression and name it `double_accounts`. Then do a `COUNT` the number of times a `name` appears in the `double_accounts` table. If you do this correctly, your query results should have a count of 2 for each `name`.

Solution:
```SQL
WITH double_accounts AS (
    SELECT *
      FROM accounts

    UNION ALL

    SELECT *
      FROM accounts
)

SELECT name,
       COUNT(*) AS name_count
 FROM double_accounts 
GROUP BY 1
ORDER BY 2 DESC
```

## Performance Tuning
- One way to make a query run faster is to reduce the number of calculations that need to be performed.
- Some of the high-level things that will affect the number of calculations a given query will make include:\
	- Table size
	- Joins
	- Aggregations
- Query runtime is also dependent on some things that you can’t really control related to the database itself:
	- Other users running queries concurrently on the database
	- Database software and optimization (e.g., Postgres is optimized differently than Redshift)
- Filter data to include only the observations you need.
	- When working on time series data, limit to a smaller time window.
- Remember that you can always perform exploratory analysis on a subset of the data.
	- Note that LIMIT works after aggregations. If you aggregate to a single row, LIMIT 10 has no effect.
- The second thing you can do is to make joins less complicated, that is, reduce the number of rows that need to be evaluated. 
	- It is better to reduce table sizes before joining them.
-  Aggregating before joining will improve query speed; however, be sure that what you are doing is logically consistent. Accuracy is more important than run speed.
- Adding the command EXPLAIN at the beginning of any query allows you to get a sense of how long it will take your query to run.
	- This will output a Query Plan which outlines the execution order of the query. The query plan will attach a cost to the query and the higher the cost, the longer the runtime. EXPLAIN is most useful to identify and modify those steps that are expensive. Do this then run EXPLAIN again to see if the speed/cost has improved.

## Joining Subqueries
## Expert Tip
If you’d like to understand this a little better, you can do some extra research on [cartesian products](http://en.wikipedia.org/wiki/Cartesian_product). It’s also worth noting that the FULL JOIN and COUNT above actually runs pretty fast—it’s the COUNT(DISTINCT) that takes forever.

# Additional Practice Resources

If you would like to get more practice writing SQL queries, there are several great websites to practice writing SQL queries. Here are a couple we recommend: [HackerRank](https://www.hackerrank.com/domains/sql) and [ModeAnalytics](https://community.modeanalytics.com/sql/tutorial/sql-business-analytics-training/). We strongly recommend these. The skill test by [AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2017/01/46-questions-on-sql-to-test-a-data-science-professional-skilltest-solution/) is a fun test to take too.

You will need to create a profile for HackerRank and create an account for Mode Analytics, but these are excellent routes to gain more practice and learn more advanced skills along the way. If you come across exercises that require knowledge on concepts you haven't learned yet, feel free to google them. Spending time practicing, making mistakes and learning from it - that is the best way to become a master at anything!

See you in the next lesson!