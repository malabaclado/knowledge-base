Local Path
```
C:\Users\markl\OneDrive - University of the Philippines\Calibre Library\Mark Lutz\Learning Python (1179)
```


# C04. Python Objects

**Python Conceptual Hierarchy**
- Programs
	- Modules
		- Statements = anything that can make up a line (or lines of code)
			- Expressions = anything that evaluates to some value
				- Objects

**Why use built-in Python objects?**
- Built-in objects make programs easy to write.
- Built-in objects are components of extensions.
- Built-in objects are often more efficient than custom data structures.
- Built-in objects are a standard part of the language.

**Python's Core Object Types**[]()
![455](https://i.imgur.com/9oOaoQx.png)

Note that the plus sign (+) means different things for different objects: addition for numbers, and con catenation for strings. This is a general property of Python that we’ll regularly call **polymorphism** in this book—in short, this means that the meaning of an operation depends on the objects being operated on.

Which of the following data types are immutable/mutable: numbers, strings, lists, dictionaries, tuples, sets?
- Numbers, strings and tuples are **immutable**. Lists, dictionaries and sets are **mutable**.

**Although sequence operations are generic, methods are not**—while some objects share some method names, string method operations generally work only on strings, and nothing else

How would you get all the available methods for an object (string, list, integer, etc)?
- Use the `dir` function, eg. `>>>dir(object)`
- Getting help for a specific object/variable: `help(type(S))`


- Lists
	- **Sequence operations**: Like strings, lists support all sequence operations like indexing, slicing and so on.
	- **Type-specific operations**: Lists also have its own methods (eg. append, pop, etc)
	- Lists have **no fixed -type constraints**. Unlike arrays from other programming languages, a list in Python may contain multiple object types.
	- **Bounds checking**: Although lists have no fixed size, Python still doesn’t allow us to reference items that are not present.
	- Lists allow arbitrary **nesting**.
		- For example, we can have a list that contains a dictionary, which contains another list, and so on—as deeply and mixed as needed to describe things in our real world
		- An immediate application of this feature is to represent matrixes
	- **List comprehension**: a way to build a new list by running an expression on each item in a sequence, one at a time, from left to right.
		- ![548](https://i.imgur.com/aCJ3f1v.png)
		- List comprehensions make new lists of results, but they can be used to iterate over **any iterable object**.
		- Comprehension syntax is not just for making lists: enclosing it in parentheses can also be used to create an iterable object known as a **generator**, which produces results on demand per Python’s iteration protocol.
			- ![](https://i.imgur.com/Muhqut4.png)
- Dictionaries
	- Unlike strings and lists, Python dictionaries are not sequences at all but are instead the only core member of a category known as **mappings**. Mappings are also collections of other objects, but they store objects by key instead of by relative position.
	- Dictionaries support multiple **mapping operations**
		- Assigning values to keys 
		  `D[key]=value`
		- Keyword assignment: 
		  `pat1 = dict(name='Pat', job='dev', age=40)`
		- Zipping 
		  `pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))`
	- The `in` test - you can check the existence of a key in a dictionary.
		- ![](https://i.imgur.com/Yj2v2eG.png)
	- Item iteration
		- Turning dictionary key/value into lists
		- ![](https://i.imgur.com/4J9EAaX.png)
		- Using an iterator
		- ![](https://i.imgur.com/sSGYgJy.png)
- Tuples
	- The primary distinction for tuples is that they cannot be changed once created.
	- Like lists and dictionaries, tuples support mixed types and nesting, but they don’t grow and shrink like lists and dictionaries because they are **immutable**.
	- #Question So, why have a kind of object that is like a list, but supports fewer operations?
		- Frankly, tuples are not used as often as lists in practice, but their immutability is the whole point. If you pass a collection of objects around your program as a list, it can be changed anywhere; if you use a tuple, it cannot. That is, tuples provide a sort of integrity constraint that is convenient in programs larger than those here.
- Files
	- File objects are the main way your Python code will access the content of files on your computer. They can be used to read and write text memos, audio clips, Excel documents, saved emails, and whatever else you have stored on your device.
- Unicode and Byte Files
- Sets
	- Python sets are neither mappings nor sequences; rather, they are unordered collections of immutable (technically, “hashable”) objects, which store each object just once.

# C05. Numeric objects

**Python's numeric types**

![510](https://i.imgur.com/HVhpKH2.png)

- integers: decimal digits (base 10)
- floating point: numbers with decimal point
- hexadecimal: base 16 / `hex(I)`
- octal: base 8 / `oct(I)`
- binary: base 2 / `bin(I)`
- complex: `complex(real, imag)`

**Python expression operators**

![488](https://i.imgur.com/IRb1uY6.png)

Regarding precedence:
- Operators lower in the table have higher precedence, and so bind more tightly in mixed expres sions. Put another way, operators higher in the table have lower precedence and bind less tightly than those below them.
- Operators in the same row in the table generally group from left to right when combined (except for exponentiation, which groups right to left, and comparisons, which chain left to right).
- Enclosing subexpressions in parentheses can override Python’s precedence rules.

For example:
- if you write X + Y * Z, Python evaluates the multiplication first (Y * Z) then adds that result to X, because * has higher precedence (is lower in the table) than +.
- both multiplications (A * B and C * D) will happen before their results are added because + is above *.

#Question What happens when you add an integer and a floating-point numeral?
- The less complicated type (integer) gets converted the the more complicated type (floating point), the the operation is applied. 
- Note: You won’t usually need to do this: because Python automatically converts up to the more complex type within an expression, the results are normally what you want.

# C26 Object-Oriented Programming

Terms
- inheritance hierarchy
- inheritance - properties are defined once and can be used by other classes
- composition

Notes
