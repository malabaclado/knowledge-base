---
tags: query-note 
alias: [Book Library]
creation-date: Tuesday 9th May 2023
---

```dataview
TABLE 
	"![|60](" + cover + ")" AS Cover,
	status AS Status
FROM "Books"
SORT status DESC, file.name 
```
