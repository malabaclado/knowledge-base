---
tags:
  - type/course-note
---
# Joins and Set

![](https://i.imgur.com/2k0OvhU.png)


#### Why use joins?
1. To recombine data from multiple tables into one table.
2. To enrich data by extracting additional columns from other tables.
3. To check for existence by filtering based on matching data between two tables.

![](https://i.imgur.com/5QJLZKE.png)

#### Basic Join Types
##### No join
Returns two tables

```
SELECT *
FROM A;

SELECT *
FROM B;
```
##### Inner join
Returns only matching data from both tables.

```
SELECT *
FROM A
INNER JOIN B 
ON A.key = B.key
```

##### Left join
Returns all rows from left (A) and only matching rows from right (B)
```
SELECT *
FROM A
LEFT JOIN B
ON A.key=B.key
```

##### Right join
Returns all rows from right (B) and only matching rows from left (A)
```
SELECT *
FROM A
RIGHT JOIN B
ON A.key=B.key
```

![](https://i.imgur.com/rE883WW.png)

##### Full join
Returns ALL rows from both tables.
```
SELECT *
FROM A
FULL JOIN B
ON A.key = B.key
```


#### Advanced Join Types

![](https://i.imgur.com/ms6Jtuo.png)

##### Left anti join
##### Right anti join
##### Full anti join
##### Cross join