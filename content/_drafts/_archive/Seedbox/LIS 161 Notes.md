![[Pasted image 20220411000942.png]]


Variable Name Rules 
- Start with letter or underscore
- Case sensitive
- Only alphanumeric and underscore

Integer division produces a floating point

![[Pasted image 20220411001641.png]]


---
# Lists 
- is a sequence of values 
- elements may or may not be of the same type
- may be nested
- mutable - meaning elements can be updated
- indexing starts with 0
- `in` syntax works
- list operations
	- `+` concatenates/join
	- `*` repetition
- common methods 
	- append - adds new element 
	- extend - appends a list
	- sort
	- pop - returns deleted value 
	- del - does not return deleted value 
	- remove - deletes using item name instead of index
- breaking up into list 
	- `list`
	- `split`
- lists may be equivalent but not identical
- alisasing
	- An object with more than one reference has more than one name, so we say that the object is _aliased_.
	- If the aliased object is mutable, changes made with one alias affect the other
	- Although this behavior can be useful, it is error-prone. In general, it is safer to avoid aliasing when you are working with mutable objects.

---
	Be careful of methods that modify the argument.

---
# Dictionaries
- Is like a list whose indices may not be integer (any type)
- You can think of a dictionary as a mapping between a set of indices (which are called _keys_) and a set of values
- Elements are not ordered
- `len` and `in` works
- `values` method shows the values of the dictionary 
- `get(key,def_val)` returns value of key, otherwise the default value
- 