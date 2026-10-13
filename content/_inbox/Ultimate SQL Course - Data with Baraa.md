---
tags:
  - type/course-note
---
# Joins and Set

![](https://i.imgur.com/2k0OvhU.png)


#### Why use joins?
1. To recombine data from multiple tables into one table.
2. To enrich data by extracting additional columns from other tables.
3. To check for existence by filtering based on matching data between two tables.

![](https://i.imgur.com/5QJLZKE.png)

#### Basic Join Types
##### No join
Returns two tables

```
SELECT *
FROM A;

SELECT *
FROM B;
```
##### Inner join
Returns only matching data from both tables.

```
SELECT *
FROM A
INNER JOIN B 
ON A.key = B.key
```

##### Left join
Returns all rows from left (A) and only matching rows from right (B)
```
SELECT *
FROM A
LEFT JOIN B
ON A.key=B.key
```

##### Right join
Returns all rows from right (B) and only matching rows from left (A)
```
SELECT *
FROM A
RIGHT JOIN B
ON A.key=B.key
```

![](https://i.imgur.com/rE883WW.png)

##### Full join
Returns ALL rows from both tables.
```
SELECT *
FROM A
FULL JOIN B
ON A.key = B.key
```


#### Advanced Join Types

![](https://i.imgur.com/ms6Jtuo.png)

##### Left anti join
##### Right anti join
##### Full anti join
##### Cross join


# Row-level Functions

### String Functions

**Manipulation**
- CONCAT: Combines multiple strings
- UPPER: Converts characters to uppercase
- LOWER: Converts characters to lowercase
- TRIM: Removes leading and trailing spaces
- REPLACE: Replaces specific character with a new character

**Calculation**
- LEN: Counts the number of characters

**String Extraction**
- LEFT: Extracts specific number of characters from start of string.
- RIGHT: Extracts specific number of characters from end of string.
- SUBSTRING: Extracts a part of a string at a specified position.

### Numeric Functions
- ROUND(num, digits)
- ABS(): Gets absolute value

### Datetime Functions
#### Date Types
- DATETIME: `YYYY-MM-DD HH:MM:SS`
	- Also called "TIMESTAMP" in some other SQL databases.
- DATE: `YYYY-MM-DD`

#### Date formats
- International standard (ISO 8601): `YYYY-MM-dd`
	- *This is the standard used by SQL Server*
- US Standard: `MM-dd-YYYY`
- European Standard: `dd-MM-YYYY`


**Extraction**
- `DAY(date)`
	- returns DAY(integer) from a timestamp
	- DAY(2025-08-20) = 20
- `MONTH(date)`
	- returns MONTH(integer) from a timestamp
	- DAY(2025-08-20) = 8
- `YEAR(date)`
	- returns YEAR(integer) from a timestamp
	- DAY(2025-08-20) = 2025
- `DATEPART(part, date)`
	- DATEPART(year, 2025-08-20) = 2025
	- ALWAYS returns an integer.
	- Possible parameters for part: 
		- month / day
		- hours / minutes / seconds
		- quarter
		- week
- `DATENAME(part, date)`
	- Returns the name of the date part.
	- ALWAYS returns a string.
	- DATENAME(month, 2025-08-20) = 'August'
	- Possible parameters for part: 
		- weekday
		- month
		- day (you get number as a string)
- `DATETRUNC(part, date)`
	- Truncates the date to a specific part / Resets at the level of *part*
	- Always return a DATETIME (Can be CAST to DATE type)
	- DATETRUNC(month, 2025-08-20) = 2025-08-01
	- DATETRUNC(minutes, 2025-08-20 18:45:35) = 2025-08-20 18:45:00
	- Remark:
		- Datepart resets to 01
		- Timepart resets to 00
- `EOMONTH(date)`
	- Changes date to end-of-month
	- EOMONTH(2025-08-10) = 2025-08-31
	- Always return a DATE

**Format & Casting**
- `FORMAT(value, format [,culture])`
	- Changing the format value
	- `culture` = can style based on a specific country/region
	- Examples
		- FORMAT(2025-08-10, 'dd/MM/yyyy') = 10/08/2025
- `CONVERT(data_type, value [,style])`
	- Converts a data or time value to a different data type AND formats the value
	- Examples
		- CONVERT(INT, '123') = 123
- CAST(value AS data_type)
	- Converts a value to a specified data type.
	- CAST has no formatting options unlike CONVERT
	- Examples
		- CAST('123' AS INT) = 123
		- CAST('2025-08-10' AS DATE) = 2025-08-10

**Calculations**
- `DATEADD(part, interval, date)`
	- Adds or subtracts specific time intervals to a date
	- Example
		- DATEADD(month, 2, 2025-08-10) = 2025-10-10
		- DATEADD(month, -4, 2025-08-10) = 2025-04-10
- `DATEDIFF(part, start_date, end_date)`
	- Calculates the differences between two dates
	- Example
		- DATEDIFF(month, 2025-08-10, 2025-10-10) = 2 

**Validation**
- ISDATE(value)
	- Checks if the value is a date. Returns 1 if TRUE, otherwise 0.
	- Can pass an integer.
	- 

Tips
- Avoid using DATENAME for filtering. Use DATEPART instead. Integers are always faster to search than strings.
- DAY, MONTH, YEAR, DATEPART => INT
  DATENAME => STRING
  DATETRUNC => DATETIME
  EOMONTH => DATE

## NULL Functions

![](https://i.imgur.com/DBqhxXi.png)


Replace values
- `ISNULL(value, replacement_value)`
	- Checks if the value is null. IF YES, returns the replacement value. Otherwise, it returns the value.
- `COALESCE(value1, value2, value3...)`
	- Accepts a list of values as input. Returns the first non-null value from a list.
	- You can think of this as multiple ISNULL checks.
	- Remark: ISNULL is faster than COALESCE.
- `NULLIF(value1, value2)`
	- Compares two values and returns NULL if they are equal, otherwise the first value.
	- ![](https://i.imgur.com/ZVo6uEd.png)

Checks
- IS NULL
	- Returns TRUE if value is NULL, otherwise FALSE
- IS NOT NULL
	- Returns TRUE if value is NOT NULL, otherwise FALSE

Use-cases
- Handling nulls before doing data aggregations.
- Handling nulls before doing math operators.
- Handling nulls before doing joins.
- Handling nulls before sorting data.

NULLIF Use-case
- Preventing division by zero
	- ![295](https://i.imgur.com/9sXHrKj.png)


IS NULL Use-case
- Filtering data
	- ![332](https://i.imgur.com/bRvrcFv.png)
- Anti joins
	- ![489](https://i.imgur.com/xIvNmm2.png)


### CASE Statements

## Reference

### Decision process for choosing the appropriate DATE function

![](https://i.imgur.com/qJ4V5KP.png)
### Full list of date part specifiers

![](https://i.imgur.com/zaLNXvi.png)


### All possible date format specifiers

![](https://i.imgur.com/ZpAiTxf.png)

### All possible date & time styles for CONVERT()
![](https://i.imgur.com/Pm2MKqZ.png)

### CAST VS CONVERT VS FORMAT

![](https://i.imgur.com/Q6FYPgq.png)
### ISNULL VS COALESCE
![](https://i.imgur.com/vE7Lk8A.png)

### NULL VS Empty VS Blank
![](https://i.imgur.com/4RxXi0K.png)

# Advanced SQL Techniques

Database Engine = takes care of managing queries and storage

2 primary types of storage:
Disk storage = stores long term memory
Cache storage = short-term memory

Disk stores 3 types of data:
1. User data storage: The main contents of the database (For example: Customers table)
2. System catalog: Database internal storage for its own information; holds metadata (For example: Metadata for the Customers table)
3. Temporary data: Temporary space used by the DB for short-term tasks like processing queries or sorting data. (typically found in "System Databases>tempdb>Temporary Tables" in SQL Server)

Information schema: (In SQL Server) a system-defined schema that consists of built-in views that provides information about a database. 

How normal SQL queries are processed:
1. Analyst runs the SQL query
2. Database engine processes the query
3. Database engine looks for the table in cache, provides results if available.
4. Database engine looks for the table in user data storage.
5. Provides results back to analyst.

## Subqueries

Subquery: A query inside a SQL query.

Remarks:
- The intermediate result of a subquery is only locally known to the main query. It cannot be accessed from a separate query.

Type based on dependency
1. Correlated: Subquery is NOT independent of main query.
2. Non-correlated: Subquery **is independent** of main query.

Type based on result types
1. Scalar: returns a single value
2. Row: returns a row of values
3. Table: returns another table

Type based on location
1. SELECT
2. FROM
3. JOIN
4. WHERE
	1. Via Comparison Operators
	2. Via Logical Operators

### FROM Subquery

![](https://i.imgur.com/qrg1J6L.png)


### SELECT Subquery

This is used to aggregate data side by side with the main query's data, allowing for direct comparison. Note that only Scalar subqueries are allowed on SELECT subqueries.

### JOIN Subquery

Use for preparing the data (by filtering or aggregating) before joining it with other tables.

### WHERE Subqueries
Note: Only scalar subqueries are allowed.

## Common Table Expressions (CTE)

A CTE is a temporary named result set (a virtual table) that can be used multiple times within your query to simplify and organize complex query.

CTE vs Subquery
- Subquery results are used only once in the query. CTE results can be used multiple times.
- Subqueries are written bottom up (main query first then subquery) while CTEs are written top down.
- 