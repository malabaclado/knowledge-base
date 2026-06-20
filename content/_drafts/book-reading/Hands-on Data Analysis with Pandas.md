---
tags:
  - type/book
title: Hands-on Data Analysis with Pandas
---
# II. Working with Pandas DataFrames

`%%timeit` - this is a magic command from IPython (a special command preceded by %) to see how long codes run

**IPython** (https:/​/​ipython.​readthedocs.​io/​en/​stable/​index. html) provides an interactive shell for Python. Jupyter Notebooks are built on top of IPython. While knowledge of IPython is not required for this book, it can be helpful to be familiar with some of the functionality. IPython includes a tutorial in their documentation: https:/​/​ipython.​readthedocs.​io/​en/​stable/ interactive/​.


## `Index` object

We access the Index object through the `index` attribute.
```
df.index
```

![553](https://i.imgur.com/jYK77HZ.png)

## DataFrame

The `DataFrame` class builds upon the `Series` class; we can think of it as representing the spreadsheet as a whole. It can have many columns, each with its own data type.

The column names are actually an Index object as well.

-- note under construction