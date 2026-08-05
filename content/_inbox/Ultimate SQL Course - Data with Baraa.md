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
- CONVERT
	- Cnov
- CAST
	- Changing data type

**Calculations**
- DATEADD
- DATEDIFF

**Validation**
- ISDATE


Tips
- Avoid using DATENAME for filtering. Use DATEPART instead. Integers are always faster to search than strings.
- DAY, MONTH, YEAR, DATEPART => INT
  DATENAME => STRING
  DATETRUNC => DATETIME
  EOMONTH => DATE

## Reference

### Decision process for choosing the appropriate DATE function

![](https://i.imgur.com/qJ4V5KP.png)
### Full list of date part specifiers

![](https://i.imgur.com/zaLNXvi.png)


### All possible date format specifiers

![](https://i.imgur.com/ZpAiTxf.png)
