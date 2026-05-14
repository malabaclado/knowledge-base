---
title: sqlite notes
---

Data types in sqlite: https://sqlite.org/datatype3.html

# Basic connection template
```python
# Create connection object

db = "sqlite-practice\\data\\employee.db" #db file path
conn = sqlite3.connect(db)


# Create a cursor
c = conn.cursor()


# Create an employe table (firstname, lastname, pay)
c.execute("""
          CREATE TABLE employees (
              first_name text,
              last_name text,
              pay integer
          )
          """)
          
          
# Commits changes to the database
conn.commit()

# Closes connection to database
conn.close()
```

# A better way of inserting values into a database that guards against SQL injection attacks
```python
# first way
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) 

# second way; more readable
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
```

# In-memory database
Using an in-memory database - better if you want a database that starts from scratch each time the script is run.
```python
conn = sqlite3.connect(':memory:') # Creates an in-memory database
```



