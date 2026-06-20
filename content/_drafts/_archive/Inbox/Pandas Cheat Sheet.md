---
tags:
alias:
creation-date: Thursday 21st September 2023
---

# Data Structures

# Missing Data

## Checking for missing data
To detect missing data:
- `pd.isnull()`
- `pd.notnull()`
- `series1.isnull()`

---
## Filtering out data
- `data.dropna()` Used to drop rows with missing data from any column
- `data.dropna(axis=1)` Used to drop any column with null values
- `df.dropna(how='all')` Drops rows that are all missing
- `df.dropna(thresh=3)` Drops rows containing less than 3 observations

> [!NOTE]
> `dropna()` does not modify source data, it returns a NEW DATAFRAME with non-null data.

---
## Filling in missing data
- `df2=df1.fillna(0)` Used to fill all missing values with 0
- `df1.fillna(inplace=True)` Modify in place
- `df.fillna({'col1':0, 'col2':-1})` Use different fill value for different columns
- `df.fillna(method='ffill', limit=2)` Limited forward fill.

