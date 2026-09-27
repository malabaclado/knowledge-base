Checking for missing values
`print(data.isna().sum()`


# Strategies for addressing missing data
- Drop missing values 
	- Can be an option if the missing data is < 5% of total values.
- Impute mean, median or mode
	- Impute method depends on data distribution and context
- Impute by subgroup

**Drop missing values**
Can be an option if the missing data is < 5% of total values.

```python
# Dropping missing values < 5%
threshold = len(salaries) * 0.05

# Identify the columns to be applied
cols_to_drop = salaries.columns[salaries.isna().sum() <= threshold]

# Remove missing data from the list of columns
salaries.dropna(subset=cols_to_drop, inplace=True)
```

**Impute mean, median or mode**
Impute method depends on data distribution and context.

**Impute by subgroup**
