### Container sequences
- What are container sequences?
	- ANSWER: Container sequences are data types that holds other types of data. Examples of these are lists, tuples and sets.
	
- What does it mean for data to be immutable?
	- ANSWER: Immutable means there is n**o direct way to change its elements**. Example of immutable data types are *tuples*. On the other hand, mutable data types can be changed. Examples of mutable data types are *lists* and *sets*.


- This data type holds data in order they are added, can also be indexed but are immutable. These data types allow pairing, and are unpackable.
	- ANSWER: Tuple

- This data type holds data in the other that it is added, mutable, iterable and can be indexed.
	- ANSWER: List

- This data type holds data in keys and values. It is very useful for data with hierarchy. 
	- ANSWER: Dictionary

- This special data type holds unique, unordered elements and is mutable. 
	- ANSWER: Set
	- This data type is Python's implementation of matehmatical sets and thus have operations similar to that in math.





### List Actions
###### Adding elements in a list
- `list.append('item')` 
	- Adds the value `item` to the list named `list`
- `list.extend(another_list)`
	- Adds all the entries of `another_list` to the end of `list`


###### Indexing
- `list.index('item')` 
	- Returns the index of the entry `item`
- `list[1]`
	- Gives out the second term in the list. Indexes start counting at 0.

###### Removing elements in a list
- `list.pop(position)` 
	- Remove the entry in the `position` index of `list`. Note that `position` here is an index and must be an integer.


###### Sorting lists
- `sorted(list)` 
	- Returns another list which is alphanumerically-ordered elements of `list`
- `sorted(list, reverse=True)`
	- sorts the elements of the list but in reverse order


---
### Tuple Actions

- What does "zipping" tuples mean?
	- ANSWER: Zipping means combining corresponding elements of two lists to make a list of tuples.
- `zip_list = list(zip(list_1,list_2))`
	- Returns a list of tuples whose entries are corresponding elements from `list_1` and `list_2`.


- What is "unpacking" tuples mean?
	- ANSWER: Unpacking in tuples is a concept that directly assigns tuple elements to two variables in a one-liner code. Unpacking is also used in iterating a list of tuples.

---
### Set Actions

###### Creating set from a list
- `variable = set(list)` 
	- Creates a set from `list` and giving it the name: `variable`


###### Adding elements to a set
- `set.add('element')` 
	- adds a single element to a set
- `set.update(list)` 
	- adds the elements of `list` to a set


###### Removing elements from a set
- `set.discard('element')` 
	- Removes `element` from `set`; does not report an error is the element is not in the set.
- `set.pop('element')` 
	- Removes and *returns* `element` from `set`. Returns *KeyError* when element is not found in the set.


###### Common Set Operations
- `set_1.union(set_2)` 
	- takes the union of `set_1` and `set_2`
- `set_1.intersection(set_2)` 
	- takes the intersection of `set_1` and `set_2`	
- `set_1.difference(set_2)` 
	- takes the difference of `set_1` and `set_2`; with `set_1` being the base set




---

### Dictionary actions

###### Creating dictionaries
- `variable = {}`
	- Creates an empty dictionary named *variable*
- `dict[key] = value`
	- Adds key-value pair to dictionary named `dict`.



###### Accessing nested data
- `dict[key_1][key_2][key_3]`
	- **To access nested data**, you may stack keys just like this.
	- can be used on `.get()` method


###### Adding elements in a dictionary

- `dict[key] = value` 
	- allows you to add a single key-value to the dictionary. Note that you cannot do this for container sequences.
- `dict[key].update(list)`  
	- allows you to add container sequences (such as list, tuple or sets) to the dictionary. 


###### Removing elements from a dictionary
- `del dict[key]` 
	- deletes the value associated with along its `key` from `dict`
- `dict.pop(key)` 
	- deletes a key and returns it; this is useful if you want to delete an information but you want to keep it assigned to a variable for processing or safekeeping.
	


---

### Dictionary methods
###### The `get()` method
- `dict.get(key)` 
	- Returns the value assigned to `key`. If the key does not exists, it returns a `None`.
-  `dict.get(key, 'Key Not Found')` 
	-  You may add a second argument to output when the key is not in the dictionary. If the key is not found, this code returns `Key Not Found`.


###### The `.keys()` method

- `dict.keys()` 
	- Returns all the keys in the first layer. As dictionaries might be nested, this allows you to see which values you can work on the outer layer.


---
### Pythonically using dictionaries
We can iterate entries of a dictionary using `.items()` method.


```
for key, value in dict.items():
	print(key, value)
```

The above code shows how we can iterate the elements of a dictionary

We can also check if something is a key of some dictionary.

```
if '2013' in years:
	print(years[2013])
```

This is important to  check if something is in a dictionary.

If you want to check if something is in the values of a dictionary, simply add `.values()` to the dictionary variable.


---
### Reading a CSV File


```
csvfile = open('filename.csv', 'r')
for row in csv.reader(csvfile):
	print(row)	
csvfile.close()
```


This will output each row in `filename.csv`. It is a good practice to close files after importing data from it.
