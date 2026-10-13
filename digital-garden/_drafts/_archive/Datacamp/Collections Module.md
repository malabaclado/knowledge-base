### Collections module
- Is part of the standard python library
- Contains advanced data types such as: `counter`, `defaultDict`, `OrderedDict` and `namedtuple`.



---
### Counter
- is a special dictionary used for counting data and measuring frequency




###### Importing Counter module
- `from collections import Counter`
	- The counter module allows us to create a dictionary where the values are the frequency of each key.



###### Making a counter object from a list
- `new_object = Counter(list)`
	- You can make a counter object by passing a `list` into `Counter()`. These objects are dictionaries with list item as keys and their frequency as values. Counter objects are identified as `collections.Counter` type.


###### How to find the most common items in the counter
- `print(counter.most_common(5))`
	- You can output the most common items on a counter by using the method `.most_common(n)` where `n` is an integer. 


---
### Default Dict
- dictionaries of unknown structure
- pass a default type that dictionary values will have even if it doesn't currently exist


###### Importing defaultdict
- `from collections import defaultdict`
	- imports defaultdict from the collections module.


###### Creating a defaultdict
- `new_dict = defaultdict([type])`
	- creates a dictionary object whose values are of `[type]`, this means the values are predetermined by the user - it could be a string, an integer, a list, etc.


---
### Ordered Dict
- keeps order in a dictionary



###### Importing OrderedDict
- `from collections import OrderedDict`
	- imports ordered dict


###### Creating an OrderedDict
- `ordered = OrderedDict()`
	- Creates an ordered dictionary
	- Works exactly like a dictionary, but ordered


---
### Namedtuple
- a tuple wher each position has a name


###### Importing namedtuple
- `from collections import namedtuple`
	- imports namedtuple


###### Creating a tuple with field names
- `Eatery = namedtuple('Eatery', ['name', 'location])'`
	- You may pass list data type in tuples and give them field names.
	- It is important to use a capital letter to first item in the tuple.
	- Remember that field names are written as `string` types.





