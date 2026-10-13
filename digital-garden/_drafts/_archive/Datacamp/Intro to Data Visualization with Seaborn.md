---
tags:
alias:
creation-date: Thursday 25th August 2022
last-modified-date: Thursday 25th August 2022 17:08:29
---

# Intro to Data Visualization with Seaborn
#### Introduction to Seaborn
- How to make scatterplot with sns
	- ![[Pasted image 20220825174311.png]]
- How to make countplot with sns
	- ![[Pasted image 20220825174321.png]]
	- 
- How to plot dataframe columns in sns plots
	- When using columns, enclose with quotation marks `""`  and call the dataframe on `data=` 
	- ![[Pasted image 20220825174401.png]]
- How to make scatterplot with hue in sns
	-  ![[Pasted image 20220825174637.png]]
- How to set hue order in scatterplot 
	- ![[Pasted image 20220825174655.png]]
- How to set hue colors with palette in sns scatterplot
	- ![[Pasted image 20220825174809.png]]
- Matplotlib defined colors, abbreviation and HTML color codes
	- ![[Pasted image 20220825174835.png]]

#### Visualizing Two Quantitative Variables 
###### Relational plots and subplots
- How to use `relplot()` in sns
	- `relplot()` allows us to create scatter or line plots **with subplots**
	- ![[Pasted image 20220825175952.png]]
- How to plot with column subplots in sns
	- ![[Pasted image 20220825180055.png]]
- How to plot with row subplots in sns
	- ![[Pasted image 20220825180105.png]]
- How to plot with row and column subplots 
	- ![[Pasted image 20220825180118.png]]
- Wrapping columns in subplots 
	- ![[Pasted image 20220825180213.png]]
- Ordering columns and rows 
	- ![[Pasted image 20220825180230.png]]
	- Similarly, use `row_order` to order rows.
	- 


###### Customizing scatterplots and relplots
- How to make plots with different size and hue
	- ![[Pasted image 20220825181735.png]]
- How to make plots with varying point style 
	- ![[Pasted image 20220825181707.png]]
- How to change point transparency
	- ![[Pasted image 20220825181725.png]]


###### Line Plots
- How to make line plots from relplot 
	- ![[Pasted image 20220825182933.png]]
- Adding a third categorical variable in the line plot 
	- ![[Pasted image 20220825183013.png]]
	- The third variable here is `"location"` which is categorical.
- Adding markers 
	- ![[Pasted image 20220825183056.png]]
- Turning off dahses in line style 
	- ![[Pasted image 20220825183122.png]]
- Multiple observations per x-value 
	- ![[Pasted image 20220825183204.png]]
	- ![[Pasted image 20220825183216.png]]
- Replacing/Turning off the confidence interval 
	- ![[Pasted image 20220825183251.png]]
	- ![[Pasted image 20220825183302.png]]

#### Visualizing a Categorical and Quantitative Variable
Categorical Plots
- How to use categorical plot in sns
	- ![[Pasted image 20220826175543.png]]
- Changing order of categories in categorical plots 
	- ![[Pasted image 20220826175614.png]]
- Creating bar plots using catplot()
	- ![[Pasted image 20220826175635.png]]
		- To turn off confidence interval in bar plots is similar in relplots, use `ci=None`
		- To change the orientation of the barplot, simple interchange the x and y variables. 

Box plots
- What is a box plot and what is it for?
	- ![[Pasted image 20220826180855.png]]
- Creating box plots with catplot 
	- ![[Pasted image 20220826180907.png]]
	- Setting order of categories is same as in count plots: using parameter `order=`
- Omitting outliers in box plots 
	- ![[Pasted image 20220826181009.png]]
- Changing the whiskers using 'whis' 
	- ![[Pasted image 20220826181033.png]]
Point plots 
- What is a point plot
	- ![[Pasted image 20220826182341.png]] 
	- Point plot vs line plot ![[Pasted image 20220826182352.png]]
	- Point plot vs bar plot ![[Pasted image 20220826182405.png]]
	- It is easier to compare slopes in point plots ![[Pasted image 20220826182521.png]]
- Removing joins 
	- ![[Pasted image 20220826182557.png]]
- Changing estimator in point plots 
	- ![[Pasted image 20220826182629.png]]
- Customizing confidence intervals 
	- ![[Pasted image 20220826182652.png]]


