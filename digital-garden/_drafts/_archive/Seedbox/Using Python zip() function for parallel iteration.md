
---
tags:
alias:
creation-date: Saturday 17th June 2023
---

> [!NOTE]
> The function takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements from each iterable. zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.

# Remarks
## Passing iterables of equal length
- If you use zip() with n arguments, then the function will return an iterator that generates tuples of length n.
- You can call `zip()` with no arguments as well. In this case, you’ll simply get an empty iterator.

```python
>>> zipped = zip()
>>> zipped
<zip object at 0x7f196294a488>
>>> list(zipped)
[]
```

## Passing iterables with unequal length
- When passing arguments of unequal length, the number of elements that `zip()` puts out will be equal to the length of the _shortest_ iterable. The remaining elements in any longer iterables will be totally ignored by `zip()`.

```python
>>> list(zip(range(5), range(100)))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
```

- If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip(). With this function, the missing values will be replaced with whatever you pass to the fillvalue argument (defaults to None). 

```python
>>> from itertools import zip_longest
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> longest = range(5)
>>> zipped = zip_longest(numbers, letters, longest, fillvalue='?')
>>> list(zipped)
[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]
```

## The `strict` argument

- In Python 3.10, a new argument `strict` is introduced with default `strict=False`. Alternatively, if you set `strict=True`, then `zip()` checks if the input iterables you provided as arguments have the same length, raising a  `ValueError` if they don’t. 
	- This new feature of zip() is useful when you need to make sure that the function only accepts iterables of equal length. Setting strict to True makes code that expects equal-length iterables safer, ensuring that faulty changes to the caller code don’t result in silently losing data.

# Snippets
## Traversing lists in parallel using zip
``` python
>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> for l, n in zip(letters, numbers):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')
```


## Traversing dictionary key-value pairs using zip
```python
>>> dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
>>> dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
>>> for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
...     print(k1, '->', v1)
...     print(k2, '->', v2)
```

## Unzipping a sequence in Python
Say you have a list of tuples and want to separate the elements of each tuple into independent sequences. To do this, you can use zip() along with the unpacking operator `*`.

```python
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3, 4)
>>> letters
('a', 'b', 'c', 'd')
```

## Sorting in parallel using zip
Suppose you want to combine two lists and sort them at the same time.

**Don't do this:**
```python
>>> letters = ['b', 'a', 'd', 'c']
>>> numbers = [2, 4, 3, 1]
>>> data1 = list(zip(letters, numbers))
>>> data1
[('b', 2), ('a', 4), ('d', 3), ('c', 1)]
>>> data1.sort()  # Sort by letters
>>> data1
[('a', 4), ('b', 2), ('c', 1), ('d', 3)]
>>> data2 = list(zip(numbers, letters))
>>> data2
[(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
>>> data2.sort()  # Sort by numbers
>>> data2
[(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]
```

**Do this instead:**
```python
>>> letters = ['b', 'a', 'd', 'c']
>>> numbers = [2, 4, 3, 1]
>>> data = sorted(zip(letters, numbers))  # Sort by letters
>>> data
[('a', 4), ('b', 2), ('c', 1), ('d', 3)]
```

## Calculating in pairs using zip
```python
>>> total_sales = [52000.00, 51000.00, 48000.00]
>>> prod_cost = [46800.00, 45900.00, 43200.00]
>>> for sales, costs in zip(total_sales, prod_cost):
...     profit = sales - costs
...     print(f'Total profit: {profit}')
...
Total profit: 5200.0
Total profit: 5100.0
Total profit: 4800.0
```

## Building dictionaries using zip in Pytohn
```python
>>> fields = ['name', 'last_name', 'age', 'job']
>>> values = ['John', 'Doe', '45', 'Python Developer']
>>> >>> a_dict = dict(zip(fields, values))
>>> a_dict
{'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
```

If you need to update add items to the dictionary:

```python
>>> new_job = ['Python Consultant']
>>> field = ['job']
>>> a_dict.update(zip(field, new_job))
>>> a_dict
{'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}
```


---
See also: [[Housing in Mexico]]