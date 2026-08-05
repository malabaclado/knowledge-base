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


## Row-level Functions

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
Timestamp: YYYY-MM-DD HH:MM:SS

**Extraction**
- DAY()
	- returns DAY(integer) from a timestamp
	- DAY(2025-08-20) = 20
- MONTH()
	- returns MONTH(integer) from a timestamp
	- DAY(2025-08-20) = 8
- YEAR()
	- returns YEAR(integer) from a timestamp
	- DAY(2025-08-20) = 2025
- DATEPART(part, date)
	- DATEPART(year, 2025-08-20) = 2025
	- Possible parameters for part: 
		- month / day
		- hours / minutes / seconds
		- quarter
		- week
- DATENAME
	- Returns the name of the datepart.
	- 
- DATETRUNC
- EOMONTH

**Format & Casting**
- FORMAT
- CONVERT
- CAST

**Calculations**
- DATEADD
- DATEDIFF

**Validation**
- ISDATE




