---
title: sql
---
# Data Definition (DDL)

These commands modify the definition of the data (or tables) in a database.

## CREATE TABLE

Below is a sample code for creating tables in SQL. 

Note the format for defining table columns:`[col_name] [data_type] [constaint]`

```SQL
Create TABLE persons (
	id INT NOT NULL,
	name VARCHAR(50) NOT NULL,
	birthday DATE,
	phone VARCHAR(15) NOT NULL,
	CONSTRAINT pk_persons PRIMARY KEY id
)
```

## ALTER TABLE

This command is used to change the definition of a table (eg. adding a new column).

```sql
-- Adding a column
ALTER TABLE persons
ADD email VARCHAR(50) NOT NULL -- adds email column as last column


-- Dropping a column
ALTER TABLE persons
DROP COLUMN phone -- drops `phone` column
```

## DROP TABLE
```sql
DROP TABLE persons
```


# Data Manipulation (DML)

This command directly affects the data in a database.

## INSERT INTO

This command adds data into an empty or an already existing table.

```sql

-- basic syntax
INSERT INTO table_name (col1,col2,col3,...)
VALEUS (val1, val2, val3,...),
		(val1, val2, val3,...) -- you can insert multiple values at a time

-- example
INSERT INTO customers (id, name, country, score)
VALUES (6, 'Anna', 'USA', NULL),
		(7, 'Sam', NULL, 100)
```

Remarks
- Specifying each column in the INSERT INTO statement is optional. If not provided, SQL expects a new value for each and every column.
- For obvious reasons, the number of columns and values must match. Additionally, the order must also be the same.
- Return message shows how many tables are affected

**INSERT using SELECT**

Task:  copy data from `customers` table to `persons` table

persons columns: id, name, birthday, phone
customers columns: id, first_name, country, score

```sql
--task: copy data from customers table to persons
SELECT *
FROM persons


-- first we match the customers table to the columns in persons table
INSERT INTO persons (id, name, birthday, phone)
SELECT 
id,
first_name,
NULL, -- we don't have birthday data from customers table
'Unknown' -- placeholder; we also don't have phone data, but phone is defined as not null
FROM customers
```

Remarks
- SQL does not compare column names when inserting, only the order matters. So columns names can be different (or even empty).

# Subqueries

There are four ways to construct subqueries depending on the placement of the inner query.
- WITH subquery: Uses the `WITH` statement
- Nested subquery: the inner query is placed on the `WHERE` clause
- Inline subquery: the inner query is placed in the `FROM` clause
- Scalar subquery: the inner query is defined in the `SELECT` statement

## WITH Subquery 

The inner query is placed in the `WITH` statement.

Example:
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

### When to use a WITH subquery?
-   When a user wants to **create a version** of an existing table **to be used in a larger query** (e.g., aggregate daily prices to an average price table).
-   It is advantageous for readability purposes.

### WITH Common Table Expression

A Common Table Expression in SQL allows you to define a temporary result, such as a table, to then be referenced in a later part of the query.

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

CTE makes the code maintenance easier and allows for the simple implementation of recursive queries.

## Nested Subquery

Nested subquery is a subquery placed on the `WHERE` clause.

Example: 
```SQL
SELECT *
FROM students
WHERE student_id
IN (SELECT DISTINCT student_id
    FROM gpa_table
    WHERE gpa>3.5
    );
```

### When to use a nested subquery?
1. When a user wants to filter an output using a condition met from another table. 
2. To make code easier to read.

## Inline Subquery

Inline subquery is subquery placed in the `FROM` clause.

Example: 
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

It has a very similar use case for `WITH` subquery, but it is less readable. Use less often. It is better to use the `WITH` subquery.

## Scalar Subquery

A scalar subquery selects only one column and one row, used in `SELECT` clause.

Example: 
```SQL
SELECT 
   (SELECT MAX(salary) FROM employees_db) AS top_salary,
   employee_name
FROM employees_db;
```

**Remarks:**
- If a scalar subquery does not find a match, it returns a `NULL`. 
- If a scalar subquery finds multiple matches, it returns an `ERROR`.

### When to use a scalar subquery?
1. When the dataset is small
2. When you need performance over complexity

**Common Use Case:** Finding records that are above or below an average, or matching a specific calculated metric.
# References
[SQL Full Course for Beginners (30 Hours) – From Zero to Hero - YouTube](https://www.youtube.com/watch?v=SSKVgrwhzus&t=23640s)


I've written an update.