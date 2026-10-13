---
tags: query-note 
alias:
creation-date: Friday 26th May 2023
---
![](https://i.imgur.com/3UjTrAp.png)


# Check-in & Sleep
```dataview
TABLE Check-in , Sleep
FROM #daily-note
SORT file.name DESC
LIMIT 10
```



# Daily Summary
```dataview
TABLE Daily-summary AS Summary
FROM #daily-note
SORT file.name DESC
LIMIT 10
```

