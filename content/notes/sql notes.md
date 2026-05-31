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

# References
[SQL Full Course for Beginners (30 Hours) – From Zero to Hero - YouTube](https://www.youtube.com/watch?v=SSKVgrwhzus&t=23640s)