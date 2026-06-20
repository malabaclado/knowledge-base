---
tags: query-note 
alias:
creation-date: Sunday 28th May 2023
---

```dataview
TABLE Deadline AS "Due Date", Status
FROM #project-sparta 
SORT Deadline ASC, Status DESC
```
