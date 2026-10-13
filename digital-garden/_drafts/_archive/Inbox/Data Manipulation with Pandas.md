	---
tags: molecule , datacamp
alias: null
creation-date: Wednesday 3rd August 2022
last-modified-date: Wednesday 3rd August 2022 16:04:29
---

# Data Manipulation with Pandas

### Grouped Summary Statistics

- Grouping by column and taking applying a descriptive statistic
	- ![[Pasted image 20220803160658.png]]
	- This code groups **dogs** by *color* then takes the *weight_kg* column mean 
- Multiple grouped summaries
	- ![](https://i.imgur.com/o0oFO7i.png)
 
- Grouping by multiple variables
	- ![[Pasted image 20220803160748.png|400]]
- Multiple groups and multiple variables 
	- ![[Pasted image 20220803160845.png|400]]

---
###### Multiple grouped summaries

Earlier in this chapter, you saw that the `.agg()` method is useful to compute multiple statistics on multiple variables. It also works with grouped data. NumPy, which is imported as `np`, has many different summary statistics functions, including: `np.min`, `np.max`, `np.mean`, and `np.median`.

`sales` is available and `pandas` is imported as `pd`.

---

### Pivot Tables 
![[Pasted image 20220803164208.png]]
Pivot table calculates mean by default. 

![[Pasted image 20220803164322.png]]

![[Pasted image 20220803164426.png]]

![[Pasted image 20220803164523.png]]

---
### Slicing and Indexing DataFrames 
**Setting the index**
`new_data  = data.set_index('target_column')`

**Removing an index**
`data.reset_index()`
- `drop=True` drops the index column (would be deleted from the dataframe)

**Sorting index**  
`data.sort_index()` 

⚠️  The values in the index need not be unique.

Subsetting multi-index DataFrames  
![[Pasted image 20220803171201.png|400]]

---
-  **Subsetting with .loc**
	- The killer feature for indexes is `.loc[]`: a subsetting method that accepts index values. When you pass it a single argument, it will take a subset of rows.
	- The code for subsetting using `.loc[]` can be easier to read than standard square bracket subsetting, which can make your code less burdensome to maintain.
- **Setting multi-level indexes**
	- Indexes can also be made out of multiple columns, forming a _multi-level index_ (sometimes called a _hierarchical index_). There is a trade-off to using these.
	- The benefit is that multi-level indexes make it more natural to reason about nested categorical variables. For example, in a clinical trial, you might have control and treatment groups. Then each test subject belongs to one or another group, and we can say that a test subject is nested inside the treatment group. Similarly, in the temperature dataset, the city is located in the country, so we can say a city is nested inside the country.
	- The main downside is that the code for manipulating indexes is different from the code for manipulating columns, so you have to learn two syntaxes and keep track of how your data 


---
## Visualizing DataFrames  in Matplotlib
- Creating Histograms 
	- ![[Pasted image 20220804162731.png]]
- Barplots 
	- ![[Pasted image 20220804162808.png]]
- Line Plots
	- ![[Pasted image 20220804162827.png]]
- Rotating axis plots 
	- ![[Pasted image 20220804162851.png]]
- Scatter plots 
	- ![[Pasted image 20220804162905.png]]
- Layering plots 
	- ![[Pasted image 20220804162928.png]]
	- ![[Pasted image 20220804162944.png]]
---
### Missing Values  
- Detecting missing values
	- ![[Pasted image 20220804174048.png]]
	- ![[Pasted image 20220804174056.png]]
- Counting missing values
	- ![[Pasted image 20220804174124.png]]
- Plotting missing values 
	- 
	- ![[Pasted image 20220804174132.png]]
- Removing missing values
	- ![[Pasted image 20220804174151.png]]
- Replacing missing values 
	- ![[Pasted image 20220804174203.png]]

---
### Creating DataFrames
- Creating DataFrames 
	- There are two ways to create DataFrames from ground up.
		- From list of dictionaries 
		- From dictionary of lists
	- In both cases, we use this syntax: `pd.DataFrame(dict_or_lists)`

---
### Reading and writing CSVs
CSV means *'comma-separated values '*

- Reading CSV to DataFrame 
	- ![[Pasted image 20220804175900.png]]
- Saving a DataFrame to CSV
	- ![[Pasted image 20220804175921.png]]

---
More to learn:
- Joining data with pandas 
- Streamlined Data Ingestion with pandas 