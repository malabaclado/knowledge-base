---
tags:
alias:
creation-date: Saturday 8th July 2023
---

> [!NOTE]
> Source: [R Programming Tutorial - Learn the Basics of Statistical Computing - YouTube](https://www.youtube.com/watch?v=_V8eKsto3Ug&t=79s)

- ## Why R?
	- R is free and open source
	- R is optimized for vector operations
	- It has great community
	- Has over 9000 packages available
- R is the language of data science
- ## Useful packages in R
	- dplyr - manipulating dataframes
	- tidyr - data cleaning
	- stringr - strings
	- lubridate - manipulating dates
	- httr - working with website data
	- ggvis - for visualization
	- ggplot2 - for visualization
	- shine - create interactive applications
	- rio - importing and exporting data
	- rmarkdown - create interactive notebook
	- pacman - one package to load all
- Data types - level of measurement of a variable
	- numeric (integer, single & double)
	- character (string)
	- logical (boolean)
	- complex numbers
	- raw
- Regardless of data type, you can arrange them in different structures
- Kinds of Data structures
	- Vector - 1 or more numbers in a 1-dimensional array
		- Scalars in are still vectors of length one
		- R's basic data object
		- All same data type
	- Matrix
		- 2-dimensional data
		- All must be of the same length and data class
		- The columns are not named
	- Array
		- A matrix with multiple dimensions
	- Dataframe
		- Collection that can have vectors of multiple types
		- Rule: They all need to be of same length
		- Analogous to spreadsheet in R
		- R has special functions only for datarames
	- List
		- R's most flexible data format
		- It is an ordered collection of elements
		- Could have contain any type, and could have length.
- Coercion: changing a data object from one type to another
	- Ex. character to logical
- ## Creating data structures
	- Creating matrix
		- `m <- matrix(c(...))`
	- Creating array
		- `a <- array(c(...))`
	- Creating dataframes
		- `df <- as.data.frame(cbind(vector1, vector2, vector3))`
- ## Commands
	- `typeof(variable)` - shows the type of an object
	- Conversion
		- `as.data.frame()` *converts to dataframes*
		- `as.integer()` *converts to integer*
		- `as.numeric()` *converts to numeric type*
- Factors - an attribute of a vector that specifies the possible values in their order.
	- Gives you an opportunity to assign labels to numerical variables.
	- Useful in experimental research.


# Entering data

## The assignment operator

```R
x1 <- 0:10 ## assigns a sequence of values to x1
```

> [!TIP]
> Shortcut: `Alt + -`


## The colon operator
```R
x1 <- 0:10 ## Assigns 0 1 2 3 4 5 6 7 8 9 10 to x1
```

## The seq function
```R
x4 <- seq(30, 0, by=-3)
## Assigns a sequence of numbers from 30 to 0 with decreasing intervals of 3
```

## Creating a collection of objects
```R
x5 <- c(1,2,3,4,5,6)
## c stands for concatenate
## for mnemonics, c could mean collect
```

# Importing data
- You'd want to learn how to import the following:
	- CSV
	- TXT
	- XLSX
	- JSON

```R
## Installing rio package for easy importing of data

library(datasets)  # Load base packages manually

# Installs pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use pacman to load add-on packages as desired
pacman::p_load(pacman, rio) 
```

```R
# IMPORTING WITH RIO #######################################

# CSV
rio_csv <- import("ImportingData_Datasets/mbb.csv")
head(rio_csv)

# TXT
rio_txt <- import("ImportingData_Datasets/mbb.txt")
head(rio_txt)

# Excel XLSX
rio_xlsx <- import("ImportingData_Datasets/mbb.xlsx")
head(rio_xlsx)
```

# Hierarchical Clustering


