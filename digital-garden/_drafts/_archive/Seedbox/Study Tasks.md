---
tags: #MOC, 
alias:
creation-date: Wednesday 11th May 2022
last-modified-date: Wednesday 11th May 2022 16:50:45
---
# Study Tasks
## Tasks 
```dataview
TABLE Todo AS "Tasks" FROM #lecture-note 
WHERE contains(Todo, "")
```

## Questions 
```dataview
TABLE Question AS "Questions" FROM #lecture-note 
WHERE contains(Question, "")
```

## Exercises
```dataview
TABLE Exercise AS "Exercises" FROM #lecture-note 
WHERE contains(Exercise, "")
```
