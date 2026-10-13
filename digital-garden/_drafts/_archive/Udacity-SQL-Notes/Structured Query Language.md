---
tags:
alias: ["SQL"]
creation-date: Tuesday 18th July 2023
---

Structured Query Language (SQL) is a language that allows us to access information in a database. A typical query might look like this: 

```sql
SELECT account_id, standard_qty, gloss_qty 
FROM orders 
WHERE (standard_qty = 0 OR gloss_qty = 0) AND occurred_at = ‘2016-1-01’;
```


