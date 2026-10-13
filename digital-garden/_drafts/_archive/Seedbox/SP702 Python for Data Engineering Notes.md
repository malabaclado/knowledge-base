---
tags:
alias:
creation-date: Wednesday 13th September 2023
---

Instructors:
- Simon Anthony Lorenzo
- Pierre Allan Villena

# Module 1 Python Basics
Module 1 is just a review of Python.

# Module 2 Data Gathering & Storing

## Importing data from CSV files

Importing a single CSV file
```python
data = pd.read_csv("csv_file_directory.csv")
```

Importing and joining from multiple CSV files
```python
data1=pd.read_csv("data1.csv")
data2=pd.read_csv("data2.csv")
data3=pd.read_csv("data3.csv")


data=pd.concat([data1, data2, data3])
```

Outputting from CSV
```python
pd.to_csv("output_file_directory.csv")
```

---
## Importing data from Excel files

Importing from Excel
```python
data = pd.read_excel("file_directory.xlsx", sheet_name="sheet_name")
```


Outputting to Excel (Excel Writer)
```python
from pandas import ExcelWriter

writer=ExcelWriter("output_file_directory.xlsx")

filter.to_excel(writer, 'Sheet_name', index=False)
writer.save()
```

---
## Importing data from PDF files

---
## Scraping data from websites
**We use three libraries.** Request library is used to request access from the website and collect the website's content. Beautiful Soup is a python library used to extract data from http and html files. The lxml library allows for easy handling of xml and html files.

```python
import requests
import bs4
import lxml

url="https://yourwebsite.com"
req=requests.get(url)  
print(req.text) #This line outputs the entire html

# Create a beautiful soup object
data=bs4.BeautifulSoup(req.text, 'lxml') 

Title = data.select('title')
print(Title) # This line prints the title of the webpage

# Headlines - Print all headings
head=data.select('.mw-headline') #observe that headlines have the tag 'mw-headline'
x=len(head)
for row in range(x):
	print(head[row].getText())
```

---
## Importing data from postgreSQL database


# Module 3. Cleaning and Preparation
Data Cleaning Cheat Sheet
- 