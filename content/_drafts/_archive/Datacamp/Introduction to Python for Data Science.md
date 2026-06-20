### Anatomy of a Function in Python
- What makes up a function in python?
	- **ANSWER:** Function name, positional arguments and keyword arguments.



	- A function is made up of (up to) three parts: A **function name**, **positional arguments** and **keyword arguments**. Some function **may not have** keyword arguments. 


	- Functions that does not have any arguments at all are called **method**.

- What are two types of function argument\input?
	- **ANSWER:** Positional and Keyword Arguments

	- **Positional Arguments** are the **necessary inputs** to a function.  *Order is important*.
	- **Keyword Arguments** are **optional inputs** to a function. These often comes after positional arguments. *Order is NOT important*

---

### Loading data in Pandas
- What is pandas?
	- ANSWER: **PANDAS** is a *python module* used to work with **tabled data**. It has very useful data type called *dataframe*.


- What does CSV mean?
	- ANSWER: **CSV** means *comma separated values*

- How to load a csv file (eg. `data.csv`) into a dataframe variable?
	- ANSWER:  ```var = pandas.read_csv('data.csv')```

	-  `.read_csv()` is part of pandas module

- Given a dataframe (eg. `df`), you may want to preview some of its information. How would you print the first 5 lines of this dataframe?
	-  ANSWER: ```df.head()``` 
	-  This line will **print the first 5 lines** of the  dataframe variable named `df`.

- What module is used to output technical information from a dataframe (eg. `df`)? 
	-  ANSWER: ```df.info()``` 
	-  **Prints out technical information** about the dataframe variable named `df`.

- What are two methods for selecting columns in a dataframe?
	- ANSWER: Bracket method or Dot Method

	1. **Bracket method**
		- Example: ```df_name['column_name']```
		- Column name *must always be inside quotations*.


	2. **Dot method**
		-	Example: ```df_name.column_name```
		-	Column name should not be in quotations.
		-	This method **cannot be used if** the column name have *space *or *special characters* in it.


- How to select columns of a dataframe based on a certain criteria?
	- We can select certain values of a column based on a given criteria. We usually filter these desired values by using a logical operator. 
	- ![[Pasted image 20210707155139.png]]

---
### Creating and styling Line Plots
- How do you import `pyplot`?
	- ANSWER: `from matplotlib import pyplot`
	- `pyplot` resides in `matplotlib` module


- How to plot two dataframe values (eg. plot `x_values` against `y_values`)?
	- `plt.plot(x_values, y_values)` *Plot two data sets *
	-  `plt.show()` *Outputs the plot*
	- **To plot multiple lines**, *just stack them together, then show*.
	![[Pasted image 20210707160524.png]]
	
	
- How do you add labels to x and y-axis of a line plot?
	- `plt.xlabel('Values of X)'` *adds label to x-axis*
	- `plt.ylabel('Values of Y')` *adds label to y-axis*

- How do you add a title and legend to a plot?
	- `plt.title('Plot Title')` *adds title to the line plot*
	- `plt.legend()`
	
	- Keyword arguments:
		- `fontsize` needs an integer input
		- `color` accepts pre-defined colors and hexadecimal


- How to add text anywhere in the plot?
	- ANSWER: `plt.text(xcoor,ycoor,'Text Message')` *pins text at the designated coordinate*

---
### Styling the Plot
These are the known keyword arguments for `plt.plot()`
- `color='Color'` *change color of the line plot; input string*
- `linewidth=20` *change width size of line plot; input integer*
- `linestyle='-'` change line style; input string pattern
	- solid line `'-'`
	- dashed `'--'`
	- dotted dashed `'-.'`
	- dotted `':'`
- `marker='-'` change marker; input string pattern
	- cross `'x'`
	- square `'s'`
	- circle `'o'`
	- diamond `'d'`
	- star`'*'`
	- hex `'h'`


--- 
### Other types of plots
- How to create a scatter plot? (eg. plot `x_values` against `y_values`)
	- ANSWER: `plt.scatter(x_values, y_values)`


	- **Changing transparency.** Use the keyword argument `alpha` which accepts floating type inputs between 0 and 1.


- How to make a vertical bar chart?
	- ANSWER: `plt.bar(x_values, y_values)` creates vertical bar chart

- How to make a horizontal bar chart?
	- ANSWER: `plt.barh(x_values, y_values)` creates horizontal bar chart

	- To stack bar plots, simply write multiple lines of `plt.bar()`

- How to add error bar to a horizontal bar chart?
	- ANSWER: `yerr=df.error` keyword argument to `plt.barh()`

- How to make a histogram? 
	- ANSWER: `plt.hist(data, bins=nbins, range=(xmin,xmax))`

	- creates a histogram from `data` , with `nbins` number of unit spaces, which ranges from `xmin` to `xmax`

- How to normalize histograms?
	- ANSWER: To normalize, just add the keyword argument `density=True` to `plt.hist()`
	