---
tags:
alias:
creation-date: Monday 3rd July 2023
---

# Importing BeautifulSoup environment
To install beautifulsoup: `pip install beautifulsoup4`

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
```

Remarks:
- `urlopen` is native to python, no installation needed, while `BeautifulSoup` needs to be installed to your system.

# Creating a beautiful soup object
```python
bs = BeautifulSoup(html.read(), 'html.parser')
```

Sample
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

This outputs the first heading 1.

Other type of parser:
- `lxml`
- `html5lib`

# Handling exceptions
Two main problems you'd usually encounter:
1. The page is not found on the server (HTTP error)
2. The server is not found (URL error)

Solution via exceptions:

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
```

- Here's how the above code works:
	- If there's an HTTP error, the code will print the error.
	- If the server cannot be found, it returns "The server could not be found!"
	- If no error occur, the code proceeds with the *else*

Another problem you could come across is `AttributeError`. 


----
