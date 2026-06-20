---
tags:
alias:
creation-date: Saturday 17th June 2023
---

# Removing rows with NaN values
```python
df1.dropna(inplace=True)
```

Remarks:
- The argument `inplace` means you are dropping from the dataset itself. If you don't set this to `True`, you have to set a name to a new dataframe.


# Removing symbols and saving numeric data
```python
df1['price_usd'] = (
    df1['price_usd']
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
```

- In the code above, we used `str` methods such as `replace` to remove `$` and `,`, then we save it as `float`.

# Splitting a column into multiple columns
```python
df3[['lat', 'lon']]=df3['lat-lon'].str.split(",", expand=True)
```

The code above splits `lat-lon` column which contains latitude and longitude location data, was split and is saved to two separate columns in the dataframe. 
