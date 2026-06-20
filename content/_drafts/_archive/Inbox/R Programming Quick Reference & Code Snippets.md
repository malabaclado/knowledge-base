---
tags:
alias:
creation-date: Friday 11th August 2023
---

# ggplot main documentation
[Function reference • ggplot2 (tidyverse.org)](https://ggplot2.tidyverse.org/reference/index.html)

# How to group_by() and count
```r
data %>% group_by(Color) %>%
    summarize(count_unique = n_distinct(Id, Date), count = n())
```

# How to make a pie chart in ggplot
```
ggplot(data, aes(x="", y=amount, fill=category)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) +
  geom_text(aes(label = paste0(amount, "%")), position = position_stack(vjust=0.5)) +
  labs(x = NULL, y = NULL) +
  theme_classic() +
  theme(axis.line = element_blank(),
          axis.text = element_blank(),
          axis.ticks = element_blank()) +
  scale_fill_brewer(palette="Blues")
```

![|400](https://i.imgur.com/NsezVJX.png)

[How to Make Pie Charts in ggplot2 (With Examples) (statology.org)](https://www.statology.org/ggplot-pie-chart/)

# How to set the date range in a plot (ggplot)

*Use xlim()*
```r
ggplot(z, aes(Month, Value)) + 
     geom_bar(
	     fill="orange",size=.3,  
	     stat="identity", position="identity") +
     geom_smooth(
	     data=z,aes(Month,Value,group=1), 
	     method="lm", size=2, color="navyblue") + 
     xlim(as.Date(c('1/1/2011', '1/1/2013'), format="%d/%m/%Y") )
```


*Here's a solution using ggplot 3.1 which requires the least tweaks to the original code:*
```r
ggplot(z, aes(Month, Value)) + 
    geom_bar(fill="orange",size=.3, stat="identity", position="identity") +
    geom_smooth(data=z,aes(Month,Value,group=1), method="lm", size=2, color="navyblue") + 
    scale_x_date(date_breaks = "1 month", 
           limits = as.Date(c('1/1/2011', '1/1/2013'), format="%d/%m/%Y"),
           date_labels="%b-%Y" ) +
    theme(axis.text.x = element_text(angle = 90))
```

[r - set date range in ggplot - Stack Overflow](https://stackoverflow.com/questions/14162829/set-date-range-in-ggplot)

# How to Change the Legend Title in ggplot2
Method 1: Use labs()
```
ggplot(data, aes(x=x_var, y=y_var, fill=fill_var)) + 
  geom_boxplot() + 
  labs(fill='Legend Title')
```

Method 2: Use scale_fill_manual()
```
ggplot(data, aes(x=x_var, y=y_var, fill=fill_var)) + 
  geom_boxplot() +
  scale_fill_manual('Legend Title', values=c('color1', 'color2'))
```

- [How to Change the Legend Title in ggplot2 (With Examples) (statology.org)](https://www.statology.org/change-legend-title-ggplot2/)
- [Modify axis, legend, and plot labels — labs • ggplot2 (tidyverse.org)](https://ggplot2.tidyverse.org/reference/labs.html)

# How to save a plot as png in R
Save as png:
```
PNG
# PNG device
png("my_plot.png")

# Code
plot(rnorm(20))

# Close device
dev.off()
```

- Check more here: [SAVE PLOT in R 📈 [as PDF, SVG, JPG, PNG, BMP, TIFF and PS] (r-coder.com)](https://r-coder.com/save-plot-r/#Save_as_image)

