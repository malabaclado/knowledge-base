---
tags:
creation-date: 2023-03-31
---

[[ReadItLater]] [[article]]

# [# Python List Comprehension: single, multiple, nested, & more – LearnDataSci](https://www.learndatasci.com/solutions/python-list-comprehension/)

## Python List Comprehension: single, multiple, nested, & more

The general syntax for list comprehension in Python is:

```
new_list = [x for x in old_list]
```

We've got a list of numbers called `num_list`, as follows:

```
num_list = [4, 11, 2, 19, 7, 6, 25, 12]
```

Using **list comprehension**, we'd like to append any values greater than ten to a new list. We can do this as follows:

```
new_list = [num for num in num_list if num > 10]
new_list
```

This solution essentially follows the same process as using a `for` loop to do the job, but using list comprehension can often be a neater and more efficient technique. The example below shows how we could create our new list using a `for` loop.

```
new_list = []
for num in num_list:
    if num > 10:
        new_list.append(num)
new_list
```

Using list comprehension instead of a `for` loop, we've managed to pack four lines of code into one clean statement.

In this article, we'll first look at the different ways to use list comprehensions to generate new lists. Then we'll see what the benefits of using list comprehensions are. Finally, we'll see how we can tackle **multiple list comprehensions**.

A list comprehension works by translating values from one list into another by placing a `for` statement inside a pair of brackets, formally called a **generator expression**.

A **generator** is an iterable object, which **yields** a range of values. Let's consider the following example, where `for num in num_list` is our generator and `num` is the yield.

```
num_list = [4, 11, 2, 19, 7, 6, 25, 12]

[num for num in num_list]
```

Out:

```
[4, 11, 2, 19, 7, 6, 25, 12]
```

In this case, Python has iterated through each item in `num_list`, temporarily storing the values inside of the `num` variable. We haven't added any conditions to the list comprehension, so all values are stored in the new list.

Let's try adding in an `if` statement so that the comprehension only adds numbers greater than four:

```
[num for num in num_list if num > 4]
```

Out:

```
[11, 19, 7, 6, 25, 12]
```

The image below represents the process followed in the above list comprehension:

![](https://storage.googleapis.com/lds-media/images/list_comp1.width-1200.jpg)

[](https://storage.googleapis.com/lds-media/images/list_comp1.width-1200.jpg)

We could even add in another condition to omit numbers smaller than eight. Here, we can use `and` inside of a list comprehension:

```
num_list = [4, 11, 2, 19, 7, 6, 25, 12]

[num for num in num_list if num > 4 and num < 8]
```

But we could also write this without `and` as:

```
[num for num in num_list if 4 < num < 8]
```

When using conditionals, Python checks whether our `if` statement returns `True` or `False` for each yield. When the `if` statement returns `True`, the yield is appended to the new list.

List comprehensions aren't just limited to filtering out unwanted list values, but we can also use them to apply functionality to the appended values. For example, let's say we'd like to create a list that contains squared values from the original list:

```
[num**2 for num in num_list]
```

Out:

```
[16, 121, 4, 361, 49, 36, 625, 144]
```

We can also combine any added functionality with comparison operators. We've got a lot of use out of `num_list`, so let's switch it up and start using a different list for our examples:

```
alternative_list = [21, 26, 31, 34, 41, 48, 59, 63]

[num**2 for num in alternative_list if 30 < num < 50]
```

Out:

```
[961, 1156, 1681, 2304]
```

In the above example, our list comprehension has squared any values in `alternative_list` that fall between thirty and fifty. To help demonstrate what's happening above, see the diagram below:

![](https://storage.googleapis.com/lds-media/images/list_comp2.width-1200.jpg)

[](https://storage.googleapis.com/lds-media/images/list_comp2.width-1200.jpg)

List comprehension also works with `or`, `in` and `not`.

Like in the example above using `and`, we can also use `or`:

```
num_list = [21, 26, 31, 34, 41, 48, 59, 63]

[num for num in num_list if num > 50 or num < 30]
```

Using `in`, we can check other lists as well:

```
[num for num in num_list if num in [30, 34, 36, 47, 52, 57, 59]]
```

Likewise, `not in` is also possible:

```
[num for num in num_list if num not in [31, 34, 51]]
```

Out:

```
[21, 26, 41, 48, 59, 63]
```

Lastly, we can use `if` statements **before** generator expressions within a list comprehension. By doing this, we can tell Python how to treat different values:

```
[num if num > 40 else 0 for num in alternative_list]
```

Out:

```
[0, 0, 0, 0, 41, 48, 59, 63]
```

The example above stores values in our new list if they are greater than forty; this is covered by `num if num > 40`. Python stores zero in their place for values that aren't greater than forty, as instructed by `else 0`. See the image below for a visual representation of what's happening:

![](https://storage.googleapis.com/lds-media/images/list_comp3.width-1200.jpg)

[](https://storage.googleapis.com/lds-media/images/list_comp3.width-1200.jpg)

Naturally, you may want to use a list comprehension with two lists at the same time. The following examples demonstrate different use cases for multiple list comprehension.

The following synax is the most common version of multiple list comprehension, which we'll use to flatten a list of lists:

```
list_of_lists = [['4', '8'], ['4', '2', '28'], ['1', '12'], ['3', '6', '2']]

[int(i) for sublist in list_of_lists for i in sublist]
```

Out:

```
[4, 8, 4, 2, 28, 1, 12, 3, 6, 2]
```

The order of the loops in this style of list comprehension is somewhat counter-intuitive and difficult to remember, so be prepared to look it up again in the future! Regardless, the syntax for flattening lists is helpful for other problems that would require checking two lists for values.

We can use multiple list comprehension when nested lists are involved. Let's say we've got a list of lists populated with string-type values. If we'd like to convert these values from string-type to integer-type, we could do this using multiple list comprehensions as follows:

```
[[int(j) for j in i] for i in list_of_lists]
```

Out:

```
[[4, 8], [4, 2, 28], [1, 12], [3, 6, 2]]
```

The problem with using multiple list comprehensions is that they can be hard to read, making life more difficult for other developers and yourself in the future. To demonstrate this, here's how the first solution looks when combining a list comprehension with a `for` loop:

```
new_list = []
for sub_list in list_of_lists:
    new_list.append([int(val) for val in sub_list])
new_list
```

Out:

```
[[4, 8], [4, 2, 28], [1, 12], [3, 6, 2]]
```

Our hybrid solution isn't as sleek to look at, but it's also easier to pick apart and figure out what's happening behind the scenes. There's no limit on how deep multiple list comprehensions can go. If `list_of_lists` had more lists nested within its nested lists, we could do our integer conversion as follows:

```
list_of_lists = [[['4'], ['8']], [['4'], ['2', '28']], [['1'], ['12']], [['3'], ['6', '2']]]
[[[int(k) for k in j] for j in i] for i in list_of_lists]
```

Out:

```
[[[4], [8]], [[4], [2, 28]], [[1], [12]], [[3], [6, 2]]]
```

As the example shows, our multiple list comprehensions have now become very difficult to read. It's generally agreed that **multiple list comprehensions shouldn't go any deeper than two levels**; otherwise, it could heavily sacrifice readability. To prove the point, here's how we could use for loops instead to solve the problem above:

```
new_list = []

for nested_list in list_of_lists: # iterate through each nested list in the parent list
    converted_sub_list = []
    
    for sub_list in nested_list: # for each nested list, iterate through the sub lists
        converted_sub_list.append([int(num) for num in sub_list])
        
    new_list.append(converted_sub_list) # store converted sub list then move on
    
    
new_list
```

Out:

```
[[[4], [8]], [[4], [2, 28]], [[1], [12]], [[3], [6, 2]]]
```

When working with lists in Python, you'll likely often find yourself in situations where you'll need to translate values from one list to another based on specific criteria.

Generally, if you're working with small datasets, then using `for` loops instead of list comprehensions isn't the end of the world. However, as the sizes of your datasets start to increase, you'll notice that working through lists one item at a time can take a long time.

Let's generate a list of ten thousand random numbers, ranging in value from one to a million, and store this as `num_list`. We can then use a `for` loop and a list comprehension to generate a new list containing the `num_list` values greater than half a million. Finally, using `%timeit`, we can compare the speed of the two approaches:

```
import random
import pandas as pd

num_list = random.sample(range(0, 1000000), 10000)

def for_loop():
    new_list = []
    for num in num_list:
        if num > 500000:
            new_list.append(num)

def list_comp():
    new_list = [num for num in num_list if num > 500000]

    
# Calculate timings
for_loop_time = %timeit -o -q for_loop()
list_comp_time = %timeit -o -q list_comp()

# Create data table
data = [['for loop', for_loop_time.average], ['list comprehension', list_comp_time.average]]
df = pd.DataFrame(data, columns=['type', 'microseconds'])
df.microseconds = round(df.microseconds * 1e6, 2) 
df.sort_values('microseconds', inplace=True)

df
```

The list comprehension solution runs twice as fast, so not only does it use less code, but it's also much quicker. With that in mind, it's also worth noting that `for` loops can be much more readable in certain situations, such as when using multiple list comprehensions.

Ultimately, if you're in a position where multiple list comprehensions are required, it's up to you if you'd prefer to prioritize performance over readability.

List comprehensions are an excellent tool for generating new lists based on your requirements. They're much faster than using a `for` loop and have the added benefit of making your code look neat and professional.

For situations where you're working with nested lists, multiple list comprehensions are also available to you. The concept of using comprehensions may seem a little complex at first, but once you've wrapped your head around them, you'll never look back!