---
tags:
alias:
creation-date: Sunday 1st January 2023
last-modified-date: Sunday 1st January 2023 22:03:46
---
This is a notes on the intro course that is part of the Udacity-Bertelsmann Scholarship Program.


# SQL Joins

When creating a database, it is really important to think about how data will be stored. This is known as **normalization.** 

Learn more in this article: [SQL by Design: Why You Need Database Normalization](https://www.itprotoday.com/sql-server/sql-design-why-you-need-database-normalization) 

JOIN - allows adding a new table to the query.
ON - specify the condition for combining the tables. 

```SQL ^f049sa
SELECT orders.*,
       accounts.*
FROM orders 
JOIN accounts
ON orders.account_id = accounts.id;

```

```SQL
SELECT orders.*, accounts.*
FROM accounts
JOIN orders
ON accounts.id = orders.account_id;
```

```SQL
SELECT orders.standard_qty, orders.gloss_qty, 
 orders.poster_qty,  accounts.website, 
 accounts.primary_poc
FROM orders
JOIN accounts
ON orders.account_id = accounts.id
```


## Join More than Two Tables

Let's say we want to join this three tables:
![[Pasted image 20230105165507.png]]

Here's how to do this showing all columns from the tables.
```SQL
SELECT *
FROM web_events
JOIN accounts
ON web_events.account_id = accounts.id
JOIN orders
ON accounts.id = orders.account_id
```

To select specific columns, use the `table.columnname` syntax in the SELECT statement.

```SQL
SELECT web_events.channel, accounts.name, orders.total
```

## Aliasing

We can name columns by using AS.
```SQL
FROM tablename AS t1
JOIN tablename2 AS t2
```

It also works without the keyword AS, as long as there is space between them.

```SQL
FROM tablename t1
JOIN tablename2 t2
```

Adding alias to column names

```SQL 
Select t1.column1 aliasname, t2.column2 aliasname2
FROM tablename AS t1
JOIN tablename2 AS t2
```

## Other Types of Join

![[JOINS.png]]


## Joins and Filtering
A simple rule to remember is that, when the database executes this query, it executes the join and everything in the **ON** clause first. Think of this as building the new result set. That result set is then filtered using the **WHERE** clause.

The fact that this example is a left join is important. Because inner joins only return the rows for which the two tables match, moving this filter to the **ON** clause of an inner join will produce the same result as keeping it in the **WHERE** clause.

```SQL
SELECT orders.*, accounts.*
FROM orders
LEFT JOIN accounts
ON orders.account_id = accounts.id 
WHERE accounts.sales_rep_id = 321500
```

```SQL
SELECT orders.*, accounts.*
FROM orders
LEFT JOIN accounts
ON orders.account_id = accounts.id 
AND accounts.sales_rep_id = 321500
```

## Recap (Joins)

You learned a key element for **JOIN**ing tables in a database has to do with primary and foreign keys. Choosing the set up of data in our database is very important, but not usually the job of a data analyst. This process is known as **Database Normalization**.

You learned how to combine data from multiple tables using **JOIN**s. The three **JOIN** statements you are most likely to use are: JOIN, LEFT JOIN, RIGHT JOIN.

There are a few more advanced **JOIN**s that we did not cover here, and they are used in very specific use cases. [UNION and UNION ALL](https://www.w3schools.com/sql/sql_union.asp), [CROSS JOIN](http://www.w3resource.com/sql/joins/cross-join.php), and the tricky [SELF JOIN](https://www.w3schools.com/sql/sql_join_self.asp). These are more advanced than this course will cover, but it is useful to be aware that they exist, as they are useful in special cases.

You also learned that you can alias tables and columns using **AS** or not using it. This allows you to be more efficient in the number of characters you need to write, while at the same time you can assure that your column headings are informative of the data in your table.
![](https://i.imgur.com/X7eGq4b.png)
# SQL Aggregations 


## NULL

**NULLs** are a datatype that specifies where no data exists in SQL. They are often ignored in our aggregation functions, which you will get a first look at in the next concept using **COUNT**.


When identifying **NULL**s in a **WHERE** clause, we write **IS NULL** or **IS NOT NULL**. We don't use (=), because **NULL** isn't considered a value in SQL. Rather, it is a property of the data.

```SQL
SELECT *
FROM accounts
WHERE primary_poc IS NOT NULL
```


> [!NOTE] Two common ways in which you are likely to encounter **NULL**
> -   **NULL**s frequently occur when performing a **LEFT** or **RIGHT JOIN**. You saw in the last lesson - when some rows in the left table of a left join are not matched with rows in the right table, those rows will contain some **NULL** values in the result set.
> -   **NULL**s can also occur from simply missing data in our database.


## COUNT
The COUNT function **counts all the rows that contain non-null data.**

```SQL
SELECT COUNT(*)
FROM accounts;
```

```SQL
SELECT COUNT(accounts.id)
FROM accounts;
```

```SQL
SELECT COUNT(*) AS order_count
FROM orders
WHERE occurred_at >= '2016-12-01'
AND occurred_at < '2017-01-01
```


> [!NOTE] Note
> The COUNT function does not count rows with NULL values.


## SUM
- You can only use SUM on columns.
- No need to worry about NULLs, SUM treats them as 0.


> [!NOTE] Reminder
> An important thing to remember: **aggregators only aggregate vertically - the values of a column**. If you want to perform a calculation across rows, you would do this with simple arithmetic.


```SQL
SELECT SUM(standard_qty) AS standard,
       SUM(gloss_qty) AS gloss,
       SUM(poster_qty) AS poster
FROM orders
```

## MIN and MAX
Functionally, **MIN** and **MAX** are similar to **COUNT** in that they can be used on non-numerical columns. Depending on the column type, **MIN** will return the lowest number, earliest date, or non-numerical value as early in the alphabet as possible. As you might suspect, **MAX** does the opposite—it returns the highest number, the latest date, or the non-numerical value closest alphabetically to “Z.”

```SQL
SELECT MIN(standard_qty) AS standard_min,
       MIN(gloss_qty) AS gloss_min,
       MIN(poster_qty) AS poster_min,
       MAX(standard_qty) AS standard_max,
       MAX(gloss_qty) AS gloss_max,
       MAX(poster_qty) AS poster_max
FROM   orders
```

## GROUP BY
GROUP BY allows creating segments that will aggregate independent from one another.

The key takeaways here:
-   **GROUP BY** can be used to aggregate data within subsets of the data. For example, grouping for different accounts, different regions, or different sales representatives.
-   Any column in the **SELECT** statement that is not within an aggregator must be in the **GROUP BY** clause.
-   The **GROUP BY** always goes between **WHERE** and **ORDER BY**.
-   **ORDER BY** works like **SORT** in spreadsheet software.

This code results in error:
```SQL
SELECT account_id,
       SUM(standard_qty) AS standard,
       SUM(gloss_qty) AS gloss,
       SUM(poster_qty) AS poster
FROM orders
```

Proper use of GROUP BY 
``` SQL
SELECT account_id,
       SUM(standard_qty) AS standard,
       SUM(gloss_qty) AS gloss,
       SUM(poster_qty) AS poster
FROM orders
GROUP BY account_id
ORDER BY account_id
```


Key takeaways:
-   You can **GROUP BY** multiple columns at once, as we showed here. This is often useful to aggregate across a number of different segments.
-   The order of columns listed in the **ORDER BY** clause does make a difference. You are ordering the columns from left to right.

> [!NOTE] GROUP BY - Expert Tips
> -   The order of column names in your **GROUP BY** clause doesn’t matter—the results will be the same regardless. If we run the same query and reverse the order in the **GROUP BY** clause, you can see we get the same results.
> -   As with **ORDER BY**, you can substitute numbers for column names in the **GROUP BY** clause. It’s generally recommended to do this only when you’re grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.
> -   A reminder here that any column that is not within an aggregation must show up in your GROUP BY statement. If you forget, you will likely get an error. However, in the off chance that your query does work, you might not like the results!
> 

Code from the video:

Query 1:
```
SELECT account_id,
       channel,
       COUNT(id) as events
FROM web_events
GROUP BY account_id, channel
ORDER BY account_id, channel
```

Query 2:
```
SELECT account_id,
       channel,
       COUNT(id) as events
FROM web_events
GROUP BY account_id, channel
ORDER BY account_id, channel DESC
```

## DISTINCT

**DISTINCT** is always used in **SELECT** statements, and it provides the unique rows for all columns written in the **SELECT** statement. Therefore, you only use **DISTINCT** once in any particular **SELECT** statement.

You could write:
```
SELECT DISTINCT column1, column2, column3
FROM table1;
```
which would return the unique (or **DISTINCT**) rows across all three columns.

You would **NOT** write:
```
SELECT DISTINCT column1, DISTINCT column2, DISTINCT column3
FROM table1;
```

You can think of **DISTINCT** the same way you might think of the statement "unique".

> [!NOTE] Expert Tip
> It’s worth noting that using **DISTINCT**, particularly in aggregations, can slow your queries down quite a bit.


Code from the video:

Query 1:
```
SELECT account_id,
       channel,
       COUNT(id) as events
FROM web_events
GROUP BY account_id, channel
ORDER BY account_id, channel DESC
```

Query 2:
```
SELECT account_id,
       channel
FROM web_events
GROUP BY account_id, channel
ORDER BY account_id
```

Query 3:
```
SELECT DISTINCT account_id,
       channel
FROM web_events
ORDER BY account_id
```

## HAVING 


> [!NOTE] Expert Tip
> **HAVING** is the “clean” way to filter a query that has been aggregated, but this is also commonly done using a subquery. Essentially, any time you want to perform a **WHERE** on an element of your query that was created by an aggregate, you need to use **HAVING** instead.




Code from the video:


Query 1:
```
SELECT account_id,
       SUM(total_amt_usd) AS sum_total_amt_usd
FROM orders
GROUP BY 1
ORDER BY 2 DESC
```


Query 2: Results in an error
```
SELECT account_id,
       SUM(total_amt_usd) AS sum_total_amt_usd
FROM orders
WHERE SUM(total_amt_usd) >= 250000
GROUP BY 1
ORDER BY 2 DESC
```

Query 3:
```
SELECT account_id,
       SUM(total_amt_usd) AS sum_total_amt_usd
FROM orders
GROUP BY 1
HAVING SUM(total_amt_usd) >= 250000
```

## DATE Function

**GROUP**ing **BY** a date column is not usually very useful in SQL, as these columns tend to have transaction data down to a second. Keeping date information at such granular levels is both a blessing and a curse, as it gives really precise information (a blessing), but it makes grouping information together directly difficult (a curse).

Lucky for us, there are a number of built-in SQL functions that are aimed at helping us improve our experience in working with dates.

**Here we saw that dates are stored in the year, month, day, hour, minute, second, which helps us in truncating. In the next concept, you will see a number of functions we can use in SQL to take advantage of this functionality.**

In [this link, you can find the formatting of dates around the world, as referenced in the video](https://en.wikipedia.org/wiki/Date_format_by_country).

CODE FROM THE VIDEO

Query 1:
```
SELECT occurred_at,
       SUM(standard_qty) AS standard_qty_sum
FROM orders
GROUP BY occurred_at
ORDER BY occurred_at 
```

The first function you are introduced to in working with dates is **DATE_TRUNC**.

**DATE_TRUNC** allows you to truncate your date to a particular part of your date-time column. Common truncations are `day`, `month`, and `year`. [Here](https://blog.modeanalytics.com/date-trunc-sql-timestamp-function-count-on/) is a great blog post by Mode Analytics on the power of this function.

**DATE_PART** can be useful for pulling a specific portion of a date, but notice pulling `month` or day of the week (`dow`) means that you are no longer keeping the years in order. Rather you are grouping for certain components regardless of which year they belonged in.

For additional functions you can use with dates, check out the documentation [here](https://www.postgresql.org/docs/9.1/static/functions-datetime.html), but the **DATE_TRUNC** and **DATE_PART** functions definitely give you a great start!

You can reference the columns in your select statement in **GROUP BY** and **ORDER BY** clauses with numbers that follow the order they appear in the select statement. For example

SELECT standard_qty, COUNT(*)

FROM orders

GROUP BY 1 _(this 1 refers to standard_qty since it is the first of the columns included in the select statement)_

ORDER BY 1 _(this 1 refers to standard_qty since it is the first of the columns included in the select statement)_

Code from the video:

Query 1:
```
SELECT occurred_at,
       SUM(standard_qty) AS standard_qty_sum
FROM orders
GROUP BY occurred_at
ORDER BY occurred_at
```

Query 2:
```
SELECT DATE_PART('dow',occurred_at) AS day_of_week,
       account_id,
       occurred_at,
       total
FROM orders
```

Query 3:
```
SELECT DATE_PART('dow',occurred_at) AS day_of_week,
       SUM(total) AS total_qty
FROM orders
GROUP BY 1
ORDER BY 2
```

## CASE
CASE statement is the equivalent of 'if-then' statements in SQL.


> [!NOTE] Expert Tip
> - The CASE statement always goes in the SELECT clause.
> - CASE must include the following components: WHEN, THEN, and END. ELSE is an optional component to catch cases that didn’t meet any of the other previous CASE conditions.
> - You can make any conditional statement using any conditional operator (WHERE) between WHEN and THEN. This includes stringing together multiple conditional statements using AND and OR.
> - You can include multiple WHEN statements, as well as an ELSE statement again, to deal with any unaddressed conditions.

Sample Codes 

Query 1:  Outputs 'yes' in `is_facebook` column if channel is Facebook
```SQL
SELECT id,
       account_id,
       occurred_at,
       channel,
       CASE WHEN channel = 'facebook' THEN 'yes' END AS is_facebook
FROM web_events
ORDER BY occurred_at
```

Query 2: Identify whether the channel used is Facebook, or not.
```SQL
SELECT id,
       account_id,
       occurred_at,
       channel,
       CASE WHEN channel = 'facebook' THEN 'yes' ELSE 'no' END AS is_facebook
FROM web_events
ORDER BY occurred_at
```

Query 3:  You can use AND, OR, WHERE in CASE statements
```SQL
SELECT id,
       account_id,
       occurred_at,
       channel,
       CASE WHEN channel = 'facebook' OR channel = 'direct' THEN 'yes' 
       ELSE 'no' END AS is_facebook
FROM web_events
ORDER BY occurred_at
```

Query 4: It is **bad practice** to create WHEN statements that are overlapping.
``` SQL
SELECT account_id,
       occurred_at,
       total,
       CASE WHEN total > 500 THEN 'Over 500'
            WHEN total > 300 THEN '301 - 500'
            WHEN total > 100 THEN '101 - 300'
            ELSE '100 or under' END AS total_group
FROM orders
```

Query 5: Fix for Query 4. Make sure that your WHEN statements are not ovelapping.
```SQL
SELECT account_id,
       occurred_at,
       total,
       CASE WHEN total > 500 THEN 'Over 500'
            WHEN total > 300 AND total <= 500 THEN '301 - 500'
            WHEN total > 100 AND total <=300 THEN '101 - 300'
            ELSE '100 or under' END AS total_group
FROM orders
```

### Case with Aggregation

Query 6:  
```SQL
SELECT CASE WHEN total > 500 THEN 'OVer 500'
            ELSE '500 or under' END AS total_group,
            COUNT(*) AS order_count
FROM orders
GROUP BY 1
```

Output of Query 6:
![[Pasted image 20230128112211.png]]


## Recap (Key Terms)

- DISTINCT
	- Always used in SELECT statements, and it provides the unique rows for all columns written in the SELECT statement.

- GROUP BY
	- Used to aggregate data within subsets of the data. For example, grouping for different accounts, different regions, or different sales representatives.

- HAVING
	- is the “clean” way to filter a query that has been aggregated

- NULLs
	- A datatype that specifies where no data exists in SQL 


---
# Subqueries and Temporary Tables

**A subquery is a query inside a query.**

As a reminder, a query has both **SELECT** and **FROM** clauses to signify what you want to extract from a table and what table you’d like to pull data from. A query that includes subquery, as a result, has multiple **SELECT** and **FROM** clauses.

When to use a subquery? When you need to manipulate an existing table to "pseudo-create" (you do not really create it, in a sense) a table as part of a larger query.

![](https://i.imgur.com/Q4sjfJC.png)


> [!NOTE]
> ### Differences between Subqueries and Joins
> 
> #### Use Cases:
> 
> _Subquery:_ When an existing table needs to be manipulated or aggregated to then be joined to a larger table.
> 
> _Joins:_ A fully flexible and discretionary use case where a user wants to bring two or more tables together and select and filter as needed.
> 
> #### Syntax:
> 
> _Subquery:_ A subquery is a query within a query. The syntax, as a result, has multiple **SELECT** and **FROM** clauses.
> 
> _Joins:_ A join is simple stitching together multiple tables with a common key or column. A join clause cannot stand and be run independently.
> 
> #### Dependencies:
> 
> _Subquery:_ A subquery clause can be run completely independently. When trying to debug code, subqueries are often run independently to pressure test results before running the larger query.
> 
> _Joins:_ A join clause cannot stand and be run independently.

> [!NOTE]
> ### Similarities between Subqueries and Joins
> 
> #### Output:
> 
> Both subqueries and joins are essentially bringing multiple tables together (whether an existing table is first manipulated or not) to generate a single output.
> 
> #### Deep-dive topics:
> 
> _What happens under the hood:_ Query plans are similar for both subqueries and joins. You can read more about how query plans are [here](https://www.essentialsql.com/what-is-a-query-plan/). We will not be going in-depth for these in this lesson.

> [!NOTE]
> ### Fundamentals to Know about Subqueries:
> 
> -   Subqueries must be fully placed inside parentheses.
> -   Subqueries must be fully independent and can be executed on their own
> -   Subqueries have two components to consider:
>     -   Where it’s placed
>     -   Dependencies with the outer/larger query
> 

> [!NOTE]
> **A caveat with subqueries being independent:**
> 
> In almost all cases, subqueries are fully independent. They are "interim”/temp tables that can be fully executed on their own. **However, there is an exception.** When a subquery, _typically in the form of a nested or inline subquery_, is correlated to its outer query, it cannot run independently. This is most certainly an edge case since correlated subqueries are rarely implemented compared to standalone, simple subqueries.


> [!NOTE]
> ### Placement:
> 
> There are four places where subqueries can be inserted within a larger query:
> 
> -   With
> -   Nested
> -   Inline
> -   Scalar

> [!NOTE]
> ### Dependencies:
> 
> A subquery can be **dependent** on the outer query or **independent** of the outer query.

## Subquery placement
The key concept of placement is where exactly the subquery is placed within the context of the larger query. There are four different places where a subquery can be inserted. 

From my experience, the decision of which placement to leverage stems from:
1. the problem at hand; and
2. the readability of the query.

> [!NOTE]
> **Subquery Placement**
> 
> **With:** This subquery is used when you’d like to “pseudo-create” a table from an existing table and **visually scope** the temporary table at the top of the larger query.
> 
> **Nested:** This subquery is used when you’d like the temporary table to act as a filter within the larger query, which implies that it often sits within the **where clause.**
> 
> **Inline:** This subquery is used in the same fashion as the **WITH** use case above. However, instead of the temporary table sitting on top of the larger query, it’s embedded within the **from clause.**
> 
> **Scalar:** This subquery is used when you’d like to generate a scalar value to be used as a benchmark of some sort.

For example, when you’d like to calculate the average salary across an entire organization to compare to individual employee salaries. Because it’s often a single value that is generated and used as a benchmark, the scalar subquery often sits within the **select clause.**

> [!NOTE]
> ### Advantages:
> 
> **Readability:** `With` and `Nested` subqueries are most advantageous for readability.
> 
> **Performance:** `Scalar` subqueries are advantageous for performance and are often used on smaller datasets.

Sample Query:
```SQL
SELECT channel,
       AVG(event_count) AS avg_event_count
FROM
(SELECT DATE_TRUNC('day',occurred_at) AS day,
        channel,
        count(*) as event_count
   FROM web_events
   GROUP BY 1,2
   ) sub
   GROUP BY 1
   ORDER BY 2 DESC
```


## Subquery Formatting

The first concept that helps when thinking about the format of a subquery is the placement of it: with, nested, inline, or scalar.

The second concept to consider is an indentation, which helps heighten readability for your future self or other users that want to leverage your code. The examples in this class are indented quite far—all the way to the parentheses. This isn’t practical if you nest many subqueries, but in general, be thinking about how to write your queries in a readable way. Examples of the same query written in multiple different ways are provided below. You will see that some are much easier to read than others.

> [!NOTE] Expert Tip
> Note that you should not include an alias when you write a subquery in a conditional statement. This is because the subquery is treated as an individual value (or set of values in the **IN** case) rather than as a table. **Nested and Scalar subqueries often do not require aliases the way With and Inline subqueries do.**

SAMPLE CODE

``` SQL
SELECT *
FROM orders
WHERE DATE_TRUNC('month',occurred_at) =
 (SELECT DATE_TRUNC('month',MIN(occurred_at)) AS min_month
  FROM orders)
ORDER BY occurred_at
```
