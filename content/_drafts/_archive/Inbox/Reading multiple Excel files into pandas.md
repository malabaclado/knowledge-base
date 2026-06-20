---
tags: code-snippets 
alias:
creation-date: Saturday 5th August 2023
---

```py
from pathlib import Path
import pandas as pd

# Directory of this file
this_dir = Path(__file__).resolve().parent


# Read in all Excel files from all subfolders of sales_data
parts = []
for path in (this_dir / "data_folder").rglob("*.xls*"):
    print(f'Reading {path.name}')
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)
```
