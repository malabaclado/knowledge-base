---
tags:
alias:
creation-date: Sunday 9th July 2023
---

In this course, you will learn how to use the R programming language to work with your data without tool limitations. You will get plenty of practice using R for statistical analysis, and RStudio—an integrated developer environment (IDE) for R that you will use to create advanced data visualizations with lots of detail. R makes it easier to present your data with beautiful, artistic style. 

- ## Advantages of using R
	- **Popularity**: R is frequently used for data analysis
	- **Tools:** R has a convenient library of ready-to-use tools for data cleaning and analysis
	- **Focus**: R was created with statistics in mind; data analysts can conveniently use a rich library of statistical routines
	- **Adaptability**: R adapts well for use in both machine learning and data analysis projects
	- **Availability**: R is an open source programming language

# Week 1 Programming and Data Analytics

R is a programming language that can be used to perform tasks in every phase of the data analysis process. In this part of the course, you will learn about R and RStudio, an integrated developer environment (IDE) for R. You will explore the benefits of using RStudio to work with R. RStudio enables you to easily leverage the features and functionality of R.

> [!NOTE]- Learning Objectives
> - Compare and contrast the R programming environment and the RStudio programming environment
> - Describe the RStudio programming environment including its components and benefits
> - Describe the R programming language and its programming environment
> - Describe programming languages and appropriate use including examples
> - Download and install R assets to a computer
> - Open R and execute a command
> - Differentiate between the R Console and R programming environments
> - Execute operations in R using mathematical operators such as +, -, *, and /
> - Download and use RStudio Desktop
> - Demonstrate how to complete basic tasks in R

- [[R vs Python Debate]]


# Week 2 Programming using RStudio

In this part of the course, you will explore the fundamental concepts associated with R. You will learn about functions and variables that you can use in your calculations and other programming. You will also learn about R packages, which are collections of R functions, code, and sample data that you can use in RStudio.

> [!NOTE]- Learning Objectives
> - Describe the contents and components of the tidyverse package for R
> - Describe the concept of packages in R programming language
> - Describe the use of operators to complete calculations in the R programming language
> - Describe the fundamental concepts associated with programming in R including functions, variables, data types, pipes, and vectors
> - Install and load the tidyverse package
> - Use the browseVignettes("packagename") function to read through vignettes of a loaded package
> - Locate resources for help using R


- The **Environment pane** in the upper- right part of our work space now shows both of our variables and their values. 
- Simply put, a **vector** is a group of data elements of the same type stored in a sequence in R.
-  A **pipe** is a tool in R for expressing a sequence of multiple operations. A pipe is represented by a % sign, followed by a > sign, and another % sign. It's used to apply the output of one function into another function.
- An **operator** is one of the key components of a calculation. When we first talked about operators, we defined them as a symbol that names the type of operation or calculation to be performed in a formula.
- [[Working with dates and time in R]]
- **Tidyverse** is actually a collection of packages in R with a common design philosophy for data manipulation, exploration, and visualization.
	- The loaded packages are ggplot2, tibble, tidyr, readr, purrr, dplyr, stringr, and forcats. These packages are the core of the tidyverse because you'll use them in almost every analysis. All of them work together to make your data analysis smooth and efficient.

# Week 3 Working with data in R

The R programming language was designed to work with data at all stages of the data analysis process. In this part of the course, you will examine how R can help you structure, organize, and clean your data through functions and other processes. You will learn about data frames and how to work with them in R. You will also revisit the concept of data bias and how you can use R to address it.

> [!NOTE]- Learning Objectives
> - [x] Discuss how R functions may be used to address issues of bias and relationship between data variables
> - [x] Describe R functions that may be used to clean and organize data
> - [ ] Describe functions used to work with data frames including read_csv(), data(), and datapasta()
> - [ ] Discuss the difference between tibbles and tribbles
> - [x] Compare and contrast data cleaning with different tools
> - [x] Create and work with data in R

- # Data exploration in R
	- A **data frame** is a collection of columns. It's a lot like a spreadsheet or a SQL table.
		- Data stored in a dataframe can be many types but each column must have the same data type.
	- In the tidyverse, **tibbles** are like streamlined data frames.
		- Tibbles never change the data type of the inputs.
		- Tibbles also never change the names of your variables, and they never create row names.
	-  Data frames and tibbles are the building blocks for analysis in R so having set standards for how they're built and dealt with is pretty important.
- # Data cleaning in R
	- Useful packages
		- here - *makes referencing files easier*
		- skimr - *makes summarizing data really easy and let's you skim through it more quickly*
		- janitor - *has functions for cleaning data*
	- [[File naming conventions in R]]
	- [[Some notes on operators in R]]
	- [[Wide to long with tidyr]]
	- [[Checking biased data with R]]

# Week 4 More visualizations, aesthetics and annotations

R is a great tool for creating detailed visualizations. In this part of the course, you will learn how to use R to generate and troubleshoot visualizations. You will also explore the features of R and RStudio that can help you improve the aesthetics of your visualizations. You will learn how to annotate visualizations and save the changes.

> [!NOTE]- Learning Objectives
> - [x] Identify the aesthetics features available in R with reference to size, shape, color, and plots
> - [x] Explain some common problems associated with visualizations in R
> - [x] Use of ggplot() to generate basic visualizations
> - [x] Describe the options for generating visualizations in R
> - [x] Demonstrate an understanding of RStudio functionality for saving visualizations
> - [x] Create a plot in ggplot2
> - [x] Explain the purpose and basic logic of the ggplot2 package

- # Creating data visualizations in R
- ggplot2 was originally created by the statistician and developer Hadley Wickham in 2005. Wickham's inspiration for creating ggplot2 came from the 1999 book The Grammar of Graphics, a scholarly study of data visualization by computer scientist Leland Wilkinson. 
- The first two letters of ggplot2 actually stand for **grammar of graphics**. 
- Benefits of ggplot2
	- create different types of plots
	- customize the look and feel of plots
	- create high quality visuals
	- lets you combine analysis and visualization with pipe operator
- In ggplot2 an **aesthetic** is a visual property of an object in your plot.
- A **geom** refers to the geometric object used to represent your data. Facets let you display smaller groups or subsets of your data. With facets, you can create separate plots for all the variables in your dataset.
- **Facets** let you display smaller groups or subsets of your data. With facets, you can create separate plots for all the variables in your dataset.
- Steps in visualizing data in R
	- Our code follows the common sequence for creating plots in ggplot2. Earlier, we talked about the grammar of graphics, a set of steps for making all kinds of different plots. You can also think of this sequence as the basic grammar for making plots in ggplot2. To create a plot, follow these three steps: 
		- 1. start with the ggplot function and choose a dataset to work with, 
		- 2. add a geom_function to display your data, 
		- 3. map the variables you want to plot in the argument of the aes function.
- Reflection (Tableau vs ggplot2)
	- What are the strengths and limitations of Tableau when it comes to data visualization? What are your favorite features of Tableau?
	- If you’re new to ggplot2, what features do you think will be the most useful for visualizing data? 
	- How do the visualization tools in Tableau differ from the tools in ggplot2?
- # Exploring aesthetics in R
- Aesthetics attributes
	- color
	- size
	- shape
	- alpha
- Geom functions
	- geom_point
	- geom_line
	- geom_bar
- The geom underscore jitter function creates a scatter plot and then adds a small amount of random noise to each point in the plot. Jittering helps us deal with over-plotting, which happens when the data points in a plot overlap with each other. Jittering makes the points easier to find. I'll show you what I mean. Let's replace geom underscore point with geom underscore jitter.
- [[Smoothing in ggplot]]
- **Facet** functions let you display smaller groups or subsets of your data. A facet is a side or section of an object, like the sides of a gemstone. Facets show different sides of your data by placing each subset on its own plot. Faceting can help you discover new patterns in your data and focus on relationships between different variables.
- 2 types of facet function
	- facet_wrap()
	- facet_grid()
- # Annotation and saving visualizations
	- [[Adding annotations in R]]
	- Two ways of saving visualizations:
		- Export (in Plots tab)
		- ggsave (saves last generated image)
	- [[Saving plots using ggsave]]

# Week 5 Documentation and reports

R has a number of different options to explore when you are ready to save and present your analysis. In this part of the course, you will explore R Markdown, a file format for making dynamic documents with R. You will learn how to format and export R Markdown and incorporate R code chunks in your documents.

> [!NOTE]- Learning Objectives
> - Demonstrate an understanding of how to export R Markdown notebooks
> - Incorporate R code chunks into R Markdown notebooks
> - Use basic formatting in R Markdown to create structure and emphasize content
> - Describe the R Markdown notebooks and their use to document R programming code
> - Create and outline a structure for an R Markdown notebook
> - Access and use a customized R Markdown template included in an R package
> - Demonstrate an understanding of the uses of R Markdown templates

- **R Markdown** is a useful tool that allows you to save and execute code, and generate shareable reports for stakeholders. 
- [[Learning resources for R Markdown]]