---
tags:
creation-date: 2023-03-31
---

[[ReadItLater]] [[article]]

# [How to Take User Input in Python - PythonForBeginners.com](https://www.pythonforbeginners.com/basics/how-to-take-user-input-in-python)

While programming , we often need to take user input in our programs. In this article, we will look at different ways to take user input in python. We will discuss ways to take different [python literals](https://www.pythonforbeginners.com/basics/python-literals) such as string, integer and decimal values as input in our program.

We can use the input() method to take user input in python. 

The input() method, when executed, takes an option string argument which is shown as a prompt to the user. After taking input, the input() method returns the value entered by the user as a string. Even if the user enters a number or a punctuation mark, the input() method will always read the input as a string. You can observe this in the following example.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.pythonforbeginners.com/courses/python-3-for-beginners)

```
value = input("Please input a number:")
print("The data type of {} is {}".format(value, type(value)))
```

Output:

```
Please input a number:1243
The data type of 1243 is <class 'str'>
```

While execution of the input() method, the execution of the program is paused until the user presses the enter key after giving an input. Once the user presses the enter key, the input() method completes its execution.

## How to take an integer input in Python

We have just seen that the input() method reads every value as a string. If we want to verify that the user has entered an integer, we can do it using the regular expressions.

We will use the re.match() method to verify if the given input is an integer or not. For this, we will pass the  regular expression for integer i.e “\[-+\]?\\d+$” and the input string to re.match() method as input. If the input string contains characters other than decimal digits with – or + sign at the start, the re.match() method will return **None**. Otherwise, the match() method returns a match object. To check if the user input consists of only an integer, we can use the re.match() method as follows.

```
import re

flag = True
input_value = None
while flag:
    input_value = input("Please input a number:")
    match_val = re.match("[-+]?\\d+$", input_value)
    if match_val is None:
        print("Please enter a valid integer.")
    else:
        flag = False
number = int(input_value)
print("The input number is:", number)
```

Output:

```
Please input a number:Aditya
Please enter a valid integer.
Please input a number:PFB
Please enter a valid integer.
Please input a number:123.4
Please enter a valid integer.
Please input a number:+1234
The input number is: 1234
```

Here, we have used a while loop to prompt the user repeatedly for giving an integer input. We have checked the input value using the re.match() method. If the input is not correct, the while loop is executed again. Otherwise, the while loop is terminated as **flag** becomes **False**. Similarly, we can ask the user for a decimal number input using the re.match() method as discussed below.

## How to take a decimal number as input in Python

Again, we will use the re.match() method to verify if the user has given a valid decimal number as input or not. For this, we will pass the  regular expression for decimal numbers i.e “\[-+\]?\\\\d+(\[/.\]\\\\d+)?$” and the input string to the re.match() method as input. If the input string contains characters other than decimal digits with –  and + at start and an optional decimal point “.” between the digits, the re.match() method will return **None**. Otherwise, the match() method returns a match object. To check if the user input consists of only a decimal number, we can use the re.match() method as follows.

```
import re

flag = True
input_value = None
while flag:
    input_value = input("Please input a number:")
    match_val = re.match("[-+]?\\d+([/.]\\d+)?$", input_value)
    if match_val is None:
        print("Please enter a valid decimal number.")
    else:
        flag = False
number = float(input_value)
print("The input number is:", number)
```

Output:

```
Please input a number:Aditya
Please enter a valid decimal number.
Please input a number:PFB
Please enter a valid decimal number.
Please input a number:-123.456
The input number is: -123.456
```

## Conclusion

In this article, we have seen various ways to take user input in python using the input() method. We also discussed validating the inputs using the re.match() method. To study more about validating strings in python, you can read this article on [regular expressions in python](https://www.pythonforbeginners.com/regex/regular-expressions-in-python). 

## Recommended Python Training

Course: Python 3 For Beginners

Over 15 hours of video content with guided instruction for beginners. Learn how to create real world applications and master the basics.