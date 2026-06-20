---
tags: code-snippets
alias:
creation-date: Saturday 17th June 2023
---

# Problem
Suppose we have a dataframe named 'df' and we want to filter the following:
- 'class' column must be 'type1'
- 'category' column must be 'category2'
- 'price' must be less than 100,000.00

# Solution

```python
mask1 = df['class'] == 'type1'
mask2 = df['category'] == 'category2'
mask3 = df['price'] < 100000

df = df[mask1 & mask2 & mask3]
```


# Remarks
- The masks must be boolean masks, that is, they must be logical statements.

---
See also: [[Housing in Buenos Aires - Predictive Data Science]]