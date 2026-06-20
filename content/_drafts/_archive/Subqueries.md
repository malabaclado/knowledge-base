---
tags:
alias:
creation-date: Sunday 12th February 2023
last-modified-date: Sunday 12th February 2023 21:23:10
---

# Tradeoffs to consider when using subqueries
1. Readability
2. Performance
3. Query Plan


# Example 1.
![](https://i.imgur.com/BoLL2RT.png)

The code on the left side is easier to read and understand than the code on the right. 



# Example 2. 
![](https://i.imgur.com/fXvmUgu.png)

The code on the left gives poorer performance because the subquery is dependent on the outer query so the program needs to re-run these queries every time so that it updates.


#Reading Here's a good reference on [optimizing SQL statements](https://dev.mysql.com/doc/refman/8.0/en/optimization.html).

# Subquery Strategy
![](https://i.imgur.com/bw2Dqfz.png)

Some questions yiou might want to ask yourself before ever writing a line of code:

1. Do I really need  to use a subquery? What are the advantages of using it? Is it something that I will use repetitively or just one time?
2. If it is needed, where should I place it?
3. Run the subquery independently first to see if the output is the one you expect.
4. Run the entire query


# Placement: With

# Use Case for `With` subquery:

-   When a user wants to **create a version** of an existing table **to be used in a larger query** (e.g., aggregate daily prices to an average price table).
-   It is advantageous for readability purposes.

![](https://i.imgur.com/gSjjLz6.png)

SAMPLE CODE 
```SQL 
WITH average_price AS
(
	SELECT brand_id, AVG(product_price) as brand_avg_price
	FROM product_records
),
SELECT a.brand_id, a.total_brand_sales, b.brand_avg_price
FROM brand_table a
JOIN average_price b
ON b.brand_id = a.brand_id
ORDER BY a.total_brand_sales DESC;
```

SAMPLE WITH SUBQUERY WITH MULTIPLE TABLES
``` SQL
WITH table1 AS (
          SELECT *
          FROM web_events),

     table2 AS (
          SELECT *
          FROM accounts)


SELECT *
FROM table1
JOIN table2
ON table1.account_id = table2.id;
```


