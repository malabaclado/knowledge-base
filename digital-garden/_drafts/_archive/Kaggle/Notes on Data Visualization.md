# Reading data from CSV
```python
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
```


- `index_col` assigns which column would be assigned as index.


# Line Charts
### Creating Line Charts
```python

#Line chart syntax:
sns.lineplot(data=spotify_data)
```


```python
#Adding title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

#Changing plot width and height:
plt.figure(figsize=(14,6))

# Adding labels
plt.xlabel("Date")
plt.ylabel("Date")

#Print the plot
plt.show()
```




---

# Bar Charts and Heatmaps
### Creating bar charts
```python
sns.barplot(x=flight_data.index, y=flight_data['NK'])
```


Bar charts can be created using `sns.barplot()` which takes two necessary arguments: the x-data and y-data values which should be both dataframe columns or list.


### Creating Heatmaps
```python
sns.heatmap(data=flight_data, annot=True)
```


The argument `annot=True` ensures that the values for each cell appear on the chart. (_Leaving this out removes the numbers from each of the cells!_)


---

# Scatter Plots

```python
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
```


To create a simple **scatter plot**, we use the `sns.scatterplot` command and specify the values for:

-   the horizontal x-axis (`x=insurance_data['bmi']`), and
-   the vertical y-axis (`y=insurance_data['charges']`).


### Linear Regression
To double-check the strength of this relationship, you might like to add a **regression line**, or the line that best fits the data. We do this by changing the command to `sns.regplot`.


```python
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
```

### Color-coded scatter plots

We can use scatter plots to display the relationships between (_not two, but..._) three variables! One way of doing this is by color-coding the points.


```python
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
```

### Multiple Regression Lines
```python
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
```


### Categorical Scatterplot
```python
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
```


---

# Distributions
### Histogram
```python

# Histogram 
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)
```

# Kernel Density Estimate (KDE) Plot
```python

# KDE plot 
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
```

### 2D KDE plots
```python
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
```



---

# Choosing Plot Types and Custom Styles

![Data Visualization](https://imgur.com/2VmgDnF.png)


### Changing Styles
`sns.set_style("dark")`


Seaborn has five different themes: (1)`"darkgrid"`, (2)`"whitegrid"`, (3)`"dark"`, (4)`"white"`, and (5)`"ticks"`