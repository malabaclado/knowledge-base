---
title: sqlite
---

Data types in sqlite: https://sqlite.org/datatype3.html
Reference site: https://www.sqlitetutorial.net/

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

# Fetching items through a SELECT statement

```python
c.execute("""
	SELECT *
	FROM table
""")

c.fetchone() # returns one item
c.fetchmany(n) # returns n items as a list
c.fetchall() # returns all results as a list

```

## Fetching all table names
```python
cursor = connection.cursor()
cursor.execute(
    "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%';"
)

tables = cursor.fetchall()

# Extract table names from list of tuples
table_names = [table[0] for table in tables]
print("Tables:", table_names)

connection.close()
```

	# Fetch metadata for all columns in the table
```python
cursor.execute(f"PRAGMA table_info({table_name});")
columns_info = cursor.fetchall()
```

# A better way of inserting values into a database that guards against SQL injection attacks
```python
# first way
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) 

# second way; more readable
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
```

**In-memory database**: Using an in-memory database - better if you want a database that starts from scratch each time the script is run.
```python
conn = sqlite3.connect(':memory:') # Creates an in-memory database
```

# Basic CRUD operations in sqlite

Note: Always add a `commit` statements after your CRUD commands. This pushes the changes to the database.

## Updating records using `rowid`. 
This is useful for updating specific records.
```python
# Below code shows rowid in sqlite
c.execute("""
	SELECT rowid, *
	FROM customers
""")


# Update first row
c.execute("""
	UPDATE customers SET first_name = ' Marty'
	WHERE rowid = 1   # rowid input is int
""")

conn.commit()

```


## Deleting records
```python
# Deleting a record
c.execute("DELETE from customers WHERE rowid = 6")

# Commit changes
conn.commit()

```

