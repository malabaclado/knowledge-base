---
tags:
creation-date: 2023-03-31
---

[[ReadItLater]] [[article]]

# [How To Use the Python Map Function](https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function)

### Introduction

We can use the Python built-in function `map()` to apply a function to each item in an iterable (like a [list](https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3) or [dictionary](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)) and return a new iterator for retrieving the results. `map()` returns a map object (an iterator), which we can use in other parts of our program. We can also pass the map object to the `list()` function, or another sequence type, to create an iterable.

The syntax for the `map()` function is as follows:

```
map(function, iterable, [iterable 2, iterable 3, ...])
```

Instead of using a [`for` loop](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3), the `map()` function provides a way of applying a function to every item in an iterable. Therefore it can often be more performant since it is only applying the function one item at a time rather than making copies of the items into another iterable. This is particularly useful when working on programs processing large data sets. `map()` can also take multiple iterables as arguments to the function by sending one item from each iterable to the function at a time.

In this tutorial, we’ll review three different ways of working with `map()`: with a `lambda` function, with a user-defined function, and finally with a built-in function using multiple iterable arguments.

## Using a Lambda Function

The first argument to `map()` is a function, which we use to apply to each item. Python calls the function once for every item in the iterable we pass into `map()` and it returns the manipulated item within a map object. For the first function argument, we can either pass a user-defined function or we can make use of `lambda` functions, particularly when the expression is less complex.

The syntax of `map()` with a lambda function is as follows:

```
map(lambda item: item[] expression, iterable)
```

With a list like the following, we can implement a `lambda` function with an expression that we want to apply to each item in our list:

```
numbers = [10, 15, 21, 33, 42, 55]
```

To apply an expression against each of our numbers, we can use `map()` and `lambda`:

```
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
```

Here we declare an item in our list as `x`. Then we add our expression. We pass in our list of numbers as the iterable for `map()`.

In order to receive the results of this immediately we print a list of the `map` object:

```
print(mapped_numbers)
```

```
Output[23, 33, 45, 69, 87, 113]
```

We have used `list()` so that the map object is returned to us as a list, rather than a less human-readable object like: `<map object at 0x7fc250003a58>`. The map object is an iterator over our results, so we could loop over it with `for` or we can use `list()` to turn it into a list. We’re doing this here because it’s a good way to review the results.

Ultimately `map()` is most useful when working with large datasets, so we would likely work with the map object further, and generally would not be using a constructor like `list()` on them.

For smaller datasets, list comprehensions may be more suitable, but for the purposes of this tutorial we’re using a small dataset to demonstrate `map()`.

## Implementing a User-defined Function

Similarly to a `lambda` we can use a function we have defined to apply to an iterable. While `lambda` functions are more useful to implement when you’re working with a one-line expression, user-defined functions are more appropriate when the expression grows in complexity. Furthermore, when we need to pass another piece of data to the function that you’re applying to your iterable, user-defined functions can be a better choice for readability.

For example, in the following iterable, each item is a dictionary that contains different details about each of our aquarium creatures:

```
aquarium_creatures = [
	{"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
	{"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
	{"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
	{"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
	{"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
	{"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]
```

We’ve decided that all the aquarium creatures are in fact going to move into the same tank. We need to update our records to reflect that all of our creatures are moving into tank `42`. To have `map()` access each dictionary and each key:value pair in the dictionaries, we construct a nested function:

```
def assign_to_tank(aquarium_creatures, new_tank_number):
	def apply(x):
		x["tank number"] = new_tank_number
		return x
	return map(apply, aquarium_creatures)
```

We define an `assign_to_tank()` function that takes `aquarium_creatures` and `new_tank_number` as parameters. In `assign_to_tank()` we pass `apply()` as the function to `map()` on the final line. The `assign_to_tank` function will return the iterator resulting from `map()`.

`apply()` takes `x` as an argument, which represents an item in our list — a single dictionary.

Next we define that `x` is the `"tank number"` key from `aquarium_creatures` and that it should store the passed in `new_tank_number`. We return each item after applying the new tank number.

We call `assign_to_tank()` with our list of dictionaries and the new tank number we want to replace for each creature:

```
assigned_tanks = assign_to_tank(aquarium_creatures, 42)
```

Once the function completes we have our map object stored in the `assigned_tanks` variable, which we turn into a list and print:

```
print(list(assigned_tanks))
```

We’ll receive the following output from this program:

```
Output[{'name': 'sammy', 'species': 'shark', 'tank number': 42, 'type': 'fish'}, {'name': 'ashley', 'species': 'crab', 'tank number': 42, 'type': 'shellfish'}, {'name': 'jo', 'species': 'guppy', 'tank number': 42, 'type': 'fish'}, {'name': 'jackie', 'species': 'lobster', 'tank number': 42, 'type': 'shellfish'}, {'name': 'charlie', 'species': 'clownfish', 'tank number': 42, 'type': 'fish'}, {'name': 'olly', 'species': 'green turtle', 'tank number': 42, 'type': 'turtle'}]
```

We’ve mapped the new tank number to our list of dictionaries. Using a function that we define, we can incorporate `map()` to apply the function efficiently on each item of the list.

## Using a Built-in Function with Multiple Iterables

In the same way as `lambda` functions or our own defined functions, we can use Python built-in functions with `map()`. To apply a function with multiple iterables, we pass in another iterable name following the first one. For example, using the [`pow()` function](https://www.digitalocean.com/community/tutorials/built-in-python-3-functions-for-working-with-numbers#power) that takes in two numbers to find the power of the base number to the provided exponent.

Here we have our lists of integers that we would like to use with `pow()`:

```
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
```

Next we pass in `pow()` as our function into `map()` and provide the two lists as our iterables:

```
numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
```

`map()` will apply the `pow()` function to the same item in each list to provide the power. Therefore our results will show `2**1`, `4**2`, `6**3`, and so on:

```
Output[2, 16, 216, 4096, 100000]
```

If we were to provide `map()` with an iterable that was longer than the other, `map()` would stop calculating once it reaches the end of the shortest iterable. In the following program we’re extending `base_numbers` with three additional numbers:

```
base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
```

As a result, nothing will change within the calculation of this program and so it will still yield the same result:

```
Output[2, 16, 216, 4096, 100000]
```

We’ve used the `map()` function with a Python built-in function and have seen that it can handle multiple iterables. We’ve also reviewed that `map()` will continue to process multiple iterables until it has reached the end of the iterable with the fewest items.

## Conclusion

In this tutorial, we’ve learned the different ways of using the `map()` function in Python. Now you can use `map()` with your own function, a `lambda` function, and with any other built-in functions. You can also implement `map()` with functions that require multiple iterables.

In this tutorial, we printed the results from `map()` immediately to a list format for demonstration purposes. In our programs we would typically use the returned map object to further manipulate the data.

If you would like to learn more Python, check out our [How To Code in Python 3](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3) series and our [Python topic page](https://www.digitalocean.com/community/tags/python). To learn more about working with data sets in functional programming, check out our [article on the `filter()` function](https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function).