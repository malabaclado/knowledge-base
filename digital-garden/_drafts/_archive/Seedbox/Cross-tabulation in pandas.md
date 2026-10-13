
---
tags:
alias:
creation-date: Saturday 17th June 2023
---

The pandas `crosstab` function is a useful for working with grouped summary statistics for **categorical** data. It starts by picking two categorical columns, then defines one as the index and the other as the column. If the aggregate function and value column is not defined, `crosstab` will simply calculate the frequency of each combination by default.


Example:
```python
import pandas as pd

df = pd.read_csv("data/colombia-real-estate-1.csv")
df.head()
```

![[Pasted image 20230617221308.png]]

```python
pd.crosstab(index=df["department"], columns=df["property_type"])
```

![[Pasted image 20230617221329.png]]



Another example:
```python
import numpy as np

pd.crosstab(
    index=df["department"],
    columns=df["property_type"],
    values=df["area_m2"],
    aggfunc=np.mean,
).round(0)
```

![[Pasted image 20230617221413.png]]