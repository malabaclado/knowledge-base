---
tags: datacamp
alias:
creation-date: Wednesday 10th August 2022
last-modified-date: Wednesday 10th August 2022 16:37:31
---

# Joining Data with Pandas
## Data Merging Basics
- Inner Join - Combining the intersection of two dataframes into a new dataframe.
	- ![[Pasted image 20220810164049.png]]
	- ![[Pasted image 20220810164106.png]]
	- ![[Pasted image 20220810164308.png]]
- Merging multiple dataframes at the same time 
	- ![[Pasted image 20220815175120.png]]
	- ![[Pasted image 20220815175136.png]]
	- ![[Pasted image 20220815175203.png]]

## Merging Tables with Different Join Types 
---
## Advanced Merging and Concatenating 
- Semi-join 
	- Takes the intersection of two sets but only takes the columns of the left set. This is like an inner join on the elements while doing a left join on the columns.
	- ![[Pasted image 20220823172630.png]]
	- 
- Concatenate two dataframes vertically
	- Remember: `pd.concat` always takes a list.
	- ![[Pasted image 20220823181359.png]]
- Concatenate two dataframes vertically while ignoring the index 
	- Add parameter `ignore_index=True`
	- ![[Pasted image 20220823181507.png]]
- Concatenate two dataframes vertically with labels to original tables 
	- Remember: Make sure to  set `ignore_index=False`. Otherwise, this will not work.
	- ![[Pasted image 20220823181621.png]]
- Concatenate two dataframes vertically with different column names
	- Add `sort=True` if you want to sort the columns alphabetically.
	- If you only want to join common columns, set `join=inner`
	- ![[Pasted image 20220823181755.png]]
	- ![[Pasted image 20220823181804.png]]
- Concat VS Append
	- ![[Pasted image 20220823181929.png]]
	- Append is a method, so you use it as a dot form function. 
	- ![[Pasted image 20220823181946.png]]

#### Verifying Integrity
- Where possible issues might come from
	- Merging may cause unintentional relationships. 
	- Concatenating may cause duplicate issues
	- ![[Pasted image 20220823184428.png]]
- Validating merges
	- Use `validate` parameter.
	- ![[Pasted image 20220823184547.png]]
	- If the merge is NOT valid, then python will raise an error.
- Verifying concatenations
	- Use `verify-integrity` parameter which takes a value either `True` or `False`
	- ![[Pasted image 20220823184707.png]]
- Why verify integrity and what to do
	- Often, real world data is NOT clean.
	- What to do: 
		- Fir incorrect data 
		- Drop duplicate rows
---
## Merging Ordered and Time Series Data
#### Using merge_ordered()
- Merging ordered and time series data with `pd.merge_ordered()`
	- ![[Pasted image 20220824171109.png]]
- `.merge()` and `pd.merge_ordered ` comparison
	- the most striking difference between the two is that you have to call pandas on `merge_ordered`
	- ![[Pasted image 20220824171142.png]]
- Fill missing with previous values via Forward Fill
	- ![[Pasted image 20220824171255.png]]
	- ![[Pasted image 20220824171348.png]]

#### Using merge_asof()
- How to use `pd.merge_asof`
	- `merge_asof` is similar to `merge_ordered` but its matches on the nearest key column. It does not need exact matches. This is especially useful when working with time series data.
	- ![[Pasted image 20220824174335.png]]
	- ![[Pasted image 20220824174445.png]]
			
- Using `merge_asof` with direction
	- You can use `merge_asof` with `direction` parameter which takes values such as `forward` and `nearest`. 
	- ![[Pasted image 20220824174537.png]]



#### Selecting data with .query
- Using the `.query` method 
	- ![[Pasted image 20220824181117.png]]
	- ![[Pasted image 20220824181252.png]]
#### Reshaping data with .melt()
- Using `melt` to convert wide format to long format data
	- ![[Pasted image 20220824182425.png]]
	- ![[Pasted image 20220824182435.png]]
- Melt with filtered values 
	- Use the parameter `value_vars` 
	- ![[Pasted image 20220824182513.png]]
- Melt with column names 
	- Use `var_name` and `value_name` for column names 
	- ![[Pasted image 20220824182614.png]]