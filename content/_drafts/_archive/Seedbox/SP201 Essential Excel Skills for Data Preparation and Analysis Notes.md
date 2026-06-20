---
tags:
alias:
creation-date: Saturday 27th May 2023
---

- Selecting ranges
- Copy/Pasting Special
- Absolute address (eg. `$D$4`)
	- Key: `F4`  while referencing
- Transposing copied data
	- Shortcut: Copy data, go to cell and click `ALT+E+S`
	- Method 2: Use Paste Special
- Inserting/Shifting Columns `Ctrl+ Shift+ '+'`
- Hide/Unhide
	- Hide row `ctrl+9`
	- Unhide row `ALT+O+T+U`
	- Hide column `Ctrl+0`
	- Unhide column `ALT+O+C+U`
- Changing to R1C1 Notation
	- File > Options > Formulas>Working with formulas>R1C1 Reference
- Formula auditing
	- Trace precedents (Backward tracing)
	- Trace dependents (Forward tracing)
	- Error Checking
- Range Name - 
	- Naming Conventions
		- **1. First characters must begin with any of the following:** 
			- Letter
			- Underscore (_)
			- Backslash (/)
		- **2. Remaining characters can be:** 
			- Letter
			- Number
			- Period
			- Underscore
		- **3. Not Allowed**
			- A space and most punctuation characters
			- Similar to cell addresses 
			- Excel shortcut
			- Single letters "R" and "C"
	- Method 1: Select the range then change name in formula bar
	- Method 2: Formulas > Name Manager
- # Basic Excel Functions
	- COUNT - count nonempty cells
	- COUNTA - count empty cells
	- COUNTBLANK - count empty cells in a specified range
	- IF - conditional
		- Syntax: `IF(conditional, value if true, value if false)
	- **HLOOKUP –** looks for value in the top row of a table and returns the value in the same column from a specified row
		- Syntax: `HLOOKUP(lookup_value, table_array, row_index, range_lookup)`
	- **VLOOKUP –** looks for value in the leftmost column of a table and returns a value in the same row from a specified column
		- Syntax: `VLOOKUP(lookup_value, table_array, col_index, range_lookup)`
	- ROUND - round off numbers
		- Syntax `ROUND(num, num_of_digits)
	- RAND - Randomize bet 0 and 1
	- MOD - Modulus
	- INT - converts a decimal into lower integet
	- COMBIN - combination (n,p)



# Week 2
- Data validation
- Conditional Formatting

# Week 3
- Y2K Problem
- NOW, TODAY
- YEAR, MONTH, DAY, WEEKDAY
- DATEDIF, DATA, DATEVALUE
- TRIM, VALUE
- DOLLAR, LEFT, LEN, RIGHT
- LOWER, PROPER, UPPER
- REPLACE, REPT, SEARCH, SUBSTITUTE
- COUNTIFS, SUMIFS, AVERAGEIFS
- SUMPRODUCT

---

# Week 4
- MEDIAN, PERCENTILE, QUARTILE
- STDEV, VAR
- CORREL, COVAR
- RANK, LARGE, SMALL
- INDEX, MATCH, OFFSET

---
See also: [[SP201 Essential Excel Skills for Data Preparation and Analysis]]