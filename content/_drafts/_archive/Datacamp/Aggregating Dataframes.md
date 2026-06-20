#### Summary Statistics
###### Mean and median
Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. For example, mean, median, minimum, maximum, and standard deviation are summary statistics. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.


- `mean()`
- `median()`
- `mode()`
- `min()`
- `max()`
- `var()`
- `std()`
- `sum`
- `quartile`

*Note: It only make sense to use the above functions to a dataframe column.*

###### Summarizing dates

Summary statistics can also be calculated on date columns that have values with the data type `datetime64`. Some summary statistics — like mean — don't make a ton of sense on dates, but others are super helpful, for example, minimum and maximum, which allow you to see what time range your data covers.


###### Efficient summaries

While pandas and NumPy have tons of functions, sometimes, you may need a different function to summarize your data.


The `.agg()` method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making your aggregations super-efficient. For example,

```
df['column'].agg(function)
```

###### Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics over time. In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow you to identify what the total sales were so far as well as what the highest weekly sales were so far.


- `cumsum()`
- `cummin()`
- `cummax()`
- `cumprod()`

*Note that cumulative functions return columns instead of individual values.*

#### Counting
###### Dropping duplicates

Removing duplicates is an essential skill to get accurate counts because often, you don't want to count the same thing multiple times.


- `.drop_duplicates(subset='col'])` removes duplicates; takes a column as an input
- `.drop_duplicates(subset=['col_1','col_2'])` removes duplicates with respect to two columns; works as logical conjunction AND.

###### Counting categorical variables

Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise.


- `.value_counts()` counts the number of frequency of an element in a column; *Note that it must be used on a dataframe column*.
	-	`sort=True` this keyword argument allows sorting in ascending order
	-	`normalize=True` this keyword argument allows expressing the frequency as proportions of the total counts.