---
tags:
alias:
creation-date: Sunday 30th October 2022
last-modified-date: Sunday 30th October 2022 14:16:07
---


# FreeCodeCamp SQL Tutorial Full Database Course


These are my notes from the FreeCodeCamp SQL Tutorial - Full Database for Beginners.

## Update the password
First, get the terminal to recognize MySQL commands. To check, go to terminal and run `mysql` command. 

PROBLEM: `command not found`

To solve this problem,  we need to tell our computer where mySQL is.

SOLUTION: Run this command
```SQL
echo 'export PATH=/usr/local/mysql/bin:$PATH'>>~/.bash_profile
```

--- 
PROBLEM: `Access denied for user...`

SOLUTION: 
- Connect and login to the mySQL server.
- Type and run: mysql -u root -p. This command will ask you to enter a password.
- Login using your password

--- 

PROBLEM: Change the temporary password

SOLUTION:
- Run `ALTER USER 'root'@'localhost' IDENTIFIED BY '<your password of choice>'` 
	- This command changes your password.
- Login using your new password.


## How to create a database

To create a database, run this command: 

```SQL
create database <the name of the database>
```



> [!NOTE] Note
> In the tutorial, the speaker used PopSQL, but everything can be done on the terminal.


Hostname: The address where the database server is located. (default:`localhost`)
Port: (default: `3306`)



---
## How to create tables

Whenever you're working with database management systems, your first step is always to create tables.

**Basic Data Types**
1. INT - Integers
2. DECIMAL(M,N) - Floats; M- total no. of digits, N- no. of digits after the decimal
3. VARCHAR(1) - Strings of length 1
4. BLOB - Binary Large Object, Stores large data (Used for images and files.)
5. DATE - YYYY-MM-DD
6. TIMESTAMP: `YYYY-MM-DD HH:MM:SS`

To create a table:

```SQL
CREATE TABLE student (
	student_id INT PRIMARY KEY, 
	name VARCHAR(20),
	major VARCHAR(20)
);
```

*alternatively,*

```SQL
CREATE TABLE student (
	student_id INT PRIMARY KEY, 
	name VARCHAR(20),
	major VARCHAR(20),
	PRIMARY KEY(student_id)
);
```

> [!NOTE] Note
> We use capital letters to distinguish out the sql commands.

Check if we created the table correctly: Run `DESCRIBE student;.

---
## How to delete and modify the table





