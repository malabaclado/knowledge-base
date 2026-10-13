There are two core objects in pandas: the **DataFrame** and the **Series**.

**DataFrame** - 2-dimensional data; Analogous to a tabular data with rows and columns; Basically a dictionary with column name as keys and a list as values.

**Index** - The list of row labels used in a DataFrame 

**Series** - A one-dimensional data; analogous to a single column of a DataFrame; basically a list with attribute `name`; You can imagine a DataFrame as a merged series

---
### Accessing columns
Accessing as property: `DataFrame.column_name`
Accessing as values: `DataFrame['column name']`


---
### Indexing
Index-based selection: `DataFrame.iloc[0]`
Label-based selection: `DataFrame.loc[0, 'country']`


> Remember, the i in `iloc` means 'index'.

> Both `loc` and `iloc` are row-first, column-second

> `iloc`  follows python stlib indexing, `loc` does not

---
### Changing the Index
`df.set_index('a')` - changes the dataframe index to `a`


---
### Conditional Selection
and: use ampersand `&`
or : use pipe `|`
`.isin`
`.isnull`
`.notnull`



---
# Summary Functions
- `.describe()` : generates summary of attributes, can be applies to a column
- `.mean()`
- `.unique()` - shows list of unique values
- `value_counts()` - shows the unique values and frequency of occurence


---
# Transformations

`.map()` - requires one input and returns a transformed version of that input variable; outputs a series
`.apply()` - outputs a dataframe


---
