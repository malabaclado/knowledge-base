---
tags:
alias:
creation-date: Tuesday 20th December 2022
---

# Basic SQL Course
![[Pasted image 20221222225145.png]]

```SQL
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty
FROM orders
WHERE (standard_qty = 0 OR gloss_qty = 0 OR poster_qty = 0)
AND occurred_at = '2016-10-01'
```


Using LIMIT 
```SQL
SELECT occurred_at, account_id, channel
FROM web_events
LIMIT 15;
```

Sorting using ORDER BY
``` SQL
SELECT *
FROM orders
ORDER BY occurred_at
LIMIT 1000;
```

Multiple sorting using ORDER BY
```SQL
SELECT  account_id,
        total_amt_usd
FROM orders
ORDER By total_amt_usd DESC, account_id 
```

Filtering using WHERE
```SQL
SELECT *
FROM orders
WHERE account_id = 4251
ORDER BY occurred_at
LIMIT 1000;
```


Adding additional columns based on arithmetic
```SQL
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty + poster_qty AS nonstandard_qty
FROM orders
```


Searching with wildcards using LIKE
```SQL
SELECT *
FROM accounts
WHERE website LIKE '%google%';
```

Using IN
```SQL
SELECT *
FROM orders
WHERE account_id IN (1001,1021);
```

Using NOT
```SQL
SELECT sales_rep_id, 
       name
FROM accounts
WHERE sales_rep_id NOT IN (321500,321570)
ORDER BY sales_rep_id
```

AND and BETWEEN queries
```SQL
SELECT *
FROM orders
WHERE occurred_at >= '2016-04-01' AND occurred_at <= '2016-10-01'
ORDER BY occurred_at
```

```SQL
SELECT *
FROM orders
WHERE occurred_at BETWEEN '2016-04-01' AND '2016-10-01'
ORDER BY occurred_at
```


Using OR 
```SQL
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty
FROM orders
WHERE standard_qty = 0 OR gloss_qty = 0 OR poster_qty = 0
```

Using parenthesis on logical connectors is possible too
```SQL
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty
FROM orders
WHERE (standard_qty = 0 OR gloss_qty = 0 OR poster_qty = 0)
AND occurred_at = '2016-10-01'
```

# Subqueries Exercises

```SQL


```























