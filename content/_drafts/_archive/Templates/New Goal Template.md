---
<%*
 let qcFileName = await tp.system.prompt("New Note Title")
 titleName = qcFileName
 await tp.file.rename(titleName)
 -%>
tags: #type/goal
alias:
creation-date: <%tp.file.creation_date("dddd Do MMMM YYYY") %>
last-modified-date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---


# <%qcFileName%>

Objective:
- [ ] 

Key Actions:
- 









