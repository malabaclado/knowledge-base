---
tags: topic/python, 
alias:
creation-date: Tuesday 19th April 2022
last-modified-date: Tuesday 19th April 2022 10:10:03
---
⬅️ 

---

# Class Inheritance
Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the parent class in parentheses after the new class name.

The child class inherits the attributes of its parent class, and you can use those attributes as if they were defined in the child class. A child class can also override data members and methods from the parent.

## Syntax

```python
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
```