Reference: D:\3 RESOURCES\DataCamp Slides\Intro to Data Visualization with Matplotlib

# Importing the package
```
import matplotlib.pyplot as plt
```

# Creating a simple plot
```
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()
```

You can add multiple data in one plot
```
ax.plot(x1,y1)
ax.plot(x2,y2)
ax.plot(x3,y3)
```

Basic plot parameters
Adding markers: `marker="o"`
Setting linestyle: `linestyle="--")`
Removing line: `linestyle="None"`
Choosing color: `color="r"`

Customizing axis labels
`ax.set_xlabel("Time (months)")`
`ax.set_xlabel("Time (months)")`
`ax.set_title("Weather in Seattle")`
`ax.legend()`

# Creating multiple subplots
```python
fig, ax = plt.subplots(2, 1) 

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b') 
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], linestyle='--', color='b') 
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], linestyle='--', color='b') 

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r') ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], linestyle='--', color='r') ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], linestyle='--', color='r') 

ax[0].set_ylabel("Precipitation (inches)") 

ax[1].set_ylabel("Precipitation (inches)") 
ax[1].set_xlabel("Time (months)") 

plt.show()
```

![440](https://i.imgur.com/MV5Xr1G.png)

Sharing y-axis range
```
fig, ax = plt.subplots(2, 1, sharey=True)
```

