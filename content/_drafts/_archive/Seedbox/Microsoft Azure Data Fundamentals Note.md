# 1. Explore core concepts 
- Data solutions include software technologies and platforms that can help facilitate the collection, analysis, and storage of valuable information.
- Data is a collection of facts such as numbers, descriptions, and observations used to record information.
- Data structures in which this data is organized often represents _entities_ that are important to an organization (such as customers, products, sales orders, and so on). 
- Each entity typically has one or more _attributes_, or characteristics (for example, a customer might have a name, an address, a phone number, and so on).
- # Types of data 
	- Structured data 
		- Example: Table data in a relational database
		- Structured data is data that adheres to a fixed _schema_, so all of the data has the same fields or properties. 
	- Semi-structured 
		- _Semi-structured_ data is information that has some structure, but which allows for some variation between entity instances.
		- Example: *JavaScript Object Notation* (JSON)
	- Unstructured 
		- Example: documents, images, audio and video data 
- # File storage 
	- There are two broad categories of data store in common use: File stores and Databases
- # Common data formats 
	- Delimited text files 
		- comma-separated values (CSV)
		- tab-separated values (TSV)
	- JavaScript Object Notation (JSON)
		- JSON is a ubiquitous format in which a hierarchical document schema is used to define data entities (objects) that have multiple attributes. Each attribute might be an object (or a collection of objects); making JSON a flexible format that's good for both structured and semi-structured data.
	- Extensible Markup Language (XML)
		- XML is a human-readable data format that was popular in the 1990s and 2000s. It's largely been superseded by the less verbose JSON format, but there are still some systems that use XML to represent data.
		-  XML uses _tags_ enclosed in angle-brackets (**<../>**) to define _elements_ and _attributes_.
		- ![](https://i.imgur.com/zxKsz98.png)
	- Binary Large Object (BLOB)
		- Ultimately, all files are stored as binary data (1's and 0's), but in the human-readable formats discussed above, the bytes of binary data are mapped to printable characters (typically through a character encoding scheme such as ASCII or Unicode).
		- Common types of data stored as binary include images, video, audio, and application-specific documents.
		- When working with data like this, data professionals often refer to the data files as _BLOBs_ (Binary Large Objects).
	- Optimized file formats 
		- While human-readable formats for structured and semi-structured data can be useful, they're typically not optimized for storage space or processing. Over time, some specialized file formats that enable compression, indexing, and efficient storage and processing have been developed.
		- Example: Avro, ORC, Parquet 
			- Avro
				- A row-based format. 
				- Created by Apache.
				- This header is stored as JSON. The data is stored as binary information.
				- Avro is a good format for compressing data and minimizing storage and network bandwidth requirements.
			- Optimized Row Columnar (ORC) format 
				- Organizes data into columns rather than rows. 
				- Developed by HortonWorks
				- An ORC file contains _stripes_ of data. Each stripe holds the data for a column or set of columns. A stripe contains an index into the rows in the stripe, the data for each row, and a footer that holds statistical information (count, sum, max, min, and so on) for each column.
			- Parquet 
				- Is a columnar data format 
				- Created by Cloudera and Twitter 
				-  A Parquet file contains row groups. Data for each column is stored together in the same row group. Each row group contains one or more chunks of data. A Parquet file includes metadata that describes the set of rows found in each chunk.
				- Parquet specializes in storing and processing nested data types efficiently. It supports very efficient compression and encoding schemes.
- A database is used to define a central system in which data can be stored and queried. In a simplistic sense, the file system on which files are stored is a kind of database; but when we use the term in a professional data context, we usually mean a dedicated system for managing data records rather than files.
- # Types of database 
	- Relational database 
		- Used to store and query structured data 
		- The data is stored in tables that represent entities, such as customers, products, or sales orders. Each instance of an entity is assigned a _primary key_ that uniquely identifies it; and these keys are used to reference the entity instance in other tables.
	- Non-relational database 
		- Non-relational databases are data management systems that don’t apply a relational schema to the data. 
		- Non-relational databases are often referred to as NoSQL database. 
		- ## Four common types of non-relational database 
			- Key-value database 
				- each record consists of a unique key and an associated value, which can be in any format.
			- Document database 
				- specific form of key-value database in which the value is a JSON document (which the system is optimized to parse and query)
			- Column family database 
				- store tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.
			- Graph database 
				-  store entities as nodes with links to define relationships between them.
- A transactional data processing system is what most people consider the primary function of business computing.
	-  A transactional system records _transactions_ that encapsulate specific events that the organization wants to track.
	- Transactional systems are often high-volume, sometimes handling many millions of transactions in a single day. The data being processed has to be accessible very quickly. 
	- The work performed by transactional systems is often referred to as Online Transactional Processing (OLTP).
	- OLTP solutions rely on a database system in which data storage is optimized for both read and write operations in order to support transactional workloads in which data records are created, retrieved, updated, and deleted (often referred to as _CRUD_ operations). These operations are applied transactionally, in a way that ensures the integrity of the data stored in the database. To accomplish this, OLTP systems enforce transactions that support so-called ACID semantics.
	- ## ACID Semantics 
		- Atomicity 
			- transactions are treated as a single unit (which either succeeds or fails)
		- Consistency
			- transactions can only take data from one valid state to another 
		- Isolation 
			- concurrent transactions cannot interfere with one another, all transactions are isolated 
		- Durability 
			- when a transaction has been committed, it will remain committed (even when the database system is switched off)
- Analytical data processing 
	- Analytical data typically uses read-only systems. 
	- Analytics are based on a *snapshot* of the data at any givien point in time (or a series of snapshots)
	- Common architecure looks like this:
		1. Data files may be stored in a central data lake for analysis.
		2. An extract, transform, and load (ETL) process copies data from files and OLTP databases into a data warehouse that is optimized for read activity.
		3. Data in the data warehouse may be aggregated and loaded into an online analytical processing (OLAP) model, or cube. Aggregated numeric values (measures) from fact tables are calculated for intersections of dimensions from dimension tables.
		4. The data in the data lake, data warehouse, and analytical model can be queried to produce reports, visualizations, and dashboards.
	- _Data lakes_ are common in large-scale data analytical processing scenarios, where a large volume of file-based data must be collected and analyzed.
	- _Data warehouses_ are an established way to store data in a relational schema that is optimized for read operations – primarily queries to support reporting and data visualization. 
		- The data warehouse schema may require some denormalization of data in an OLTP data source (introducing some duplication to make queries perform faster).
	- An OLAP model is an aggregated type of data storage that is optimized for analytical workloads. 
		- Data aggregations are across dimensions at different levels, enabling you to _drill up/down_ to view aggregations at multiple hierarchical levels; for example to find total sales by region, by city, or for an individual address. 
		- Because OLAP data is pre-aggregated, queries to return the summaries it contains can be run quickly.
	- Different types of user might perform data analytical work at different stages of the overall architecture.
		- Data scientists might work directly with data files in a data lake to explore and model data.
		- Data Analysts might query tables directly in the data warehouse to produce complex reports and visualizations.
		- Business users might consume pre-aggregated data in an analytical model in the form of reports or dashboards.



## 1.2. Explore job roles in the world of data
### Data Roles

**Database administrator**
- responsible for the design, implementation, maintenance, and operational aspects of on-premises and cloud-based database systems
- responsible for the overall availability and consistent performance and optimizations of databases.
- work with stakeholders to implement policies, tools, and processes for backup and recovery plans to recover following a natural disaster or human-made error.
- responsible for managing the security of the data in the database, granting privileges over the data, granting or denying access to users as appropriate.

**Data Engineer**
- collaborates with stakeholders to **==design and implement data-related workloads==**, including data ingestion pipelines, cleansing and transformation activities, and data stores for analytical workloads.
- use a **wide range of data platform technologies, including ==relational and non-relational databases**==, file stores, and data streams.
- **responsible for ensuring that the ==privacy of data is maintained== within the cloud** and spanning from on-premises to the cloud data stores.
- **own the ==management and monitoring of data pipelines== to ensure that data loads perform as expected.**

**Data Analyst**
A data analyst enables businesses to maximize the value of their data assets. **They're ==responsible for exploring data to identify trends and relationships==, designing and building analytical models, and enabling advanced analytics capabilities through reports and visualizations.**

A data analyst **==processes raw data into relevant insights==** based on identified business requirements to deliver relevant insights.

# 2. Explore relational database in Azure

## 2.1. Explore relational data in Azure

> [!NOTE] Objectives
> -   Identify characteristics of relational data
> -   Define normalization
> -   Identify types of SQL statement
> -   Identify common relational database objects

### Core Normalization Principles
1.  Separate each _entity_ into its own table.
2.  Separate each discrete _attribute_ into its own column.
3.  Uniquely identify each entity instance (row) using a _primary key_.
4.  Use _foreign key_ columns to link related entities.

Unnormalized:
![](https://i.imgur.com/gi8rrng.png)

Normalized:
![](https://i.imgur.com/ib3mSXd.png)

### Popular SQL dialects
-   **Transact-SQL (T-SQL)**. This version of SQL is used by Microsoft SQL Server and Azure SQL services.
-   **_pgSQL_**. This is the dialect, with extensions implemented in PostgreSQL.
-   **_PL/SQL_**. This is the dialect used by Oracle. PL/SQL stands for Procedural Language/SQL.

### SQL statement types
SQL statements are grouped into three main logical groups:

-   **Data Definition Language (DDL)**
	- You use DDL statements **==to create, modify, and remove tables and other objects in a database==** (table, stored procedures, views, and so on).
	- Common examples of DDL: CREATE, ALTER, DROP, RENAME
-   **Data Control Language (DCL)**
	- Database administrators generally use DCL statements **==to manage access to objects in a database==** by granting, denying, or revoking permissions to specific users or groups.
	- Three main DCL statements: GRANT,DENY, REVOKE
-   **Data Manipulation Language (DML)**
	- You use DML statements to **==manipulate the rows in tables==**. These statements enable you to retrieve (query) data, insert new rows, or modify existing rows. You can also delete rows if you don't need them anymore.
	- The four main DML statements are: SELECT, INSERT, UPDATE, DELETE


### What is a view?
A view is a virtual table based on the results of a **SELECT** query. You can think of a view as a window on specified rows in one or more underlying tables. 

For example, you could create a view on the **Order** and **Customer** tables that retrieves order and customer data to provide a single object that makes it easy to determine delivery addresses for orders:

```SQL
CREATE VIEW Deliveries
AS
SELECT o.OrderNo, o.OrderDate,
       c.FirstName, c.LastName, c.Address, c.City
FROM Order AS o JOIN Customer AS c
ON o.Customer = c.ID;
```

### What is a stored procedure?
A stored procedure defines **==SQL statements that can be run on command==**. Stored procedures are used to encapsulate programmatic logic in a database for actions that applications need to perform when working with data.

You can define a stored procedure with parameters to create a flexible solution for common actions that might need to be applied to data based on a specific key or criteria. For example, the following stored procedure could be defined to change the name of a product based on the specified product ID.

```SQL
CREATE PROCEDURE RenameProduct
	@ProductID INT,
	@NewName VARCHAR(20)
AS
UPDATE Product
SET Name = @NewName
WHERE ID = @ProductID;
```

When a product must be renamed, you can execute the stored procedure, passing the ID of the product and the new name to be assigned:

```SQL
EXEC RenameProduct 201, 'Spanner';
```


### What is an index?
An index helps you search for data in a table. Think of an index over a table like an index at the back of a book.

When you create an index in a database, you specify a column from the table, and the index contains a copy of this data in a sorted order, with pointers to the corresponding rows in the table. When the user runs a query that specifies this column in the **WHERE** clause, the database management system can use this index to fetch the data more quickly than if it had to scan through the entire table row by row.

For example, you could use the following code to create an index on the **Name** column of the **Product** table:

```SQL
CREATE INDEX idx_ProductName
ON Product(Name);
```

The index creates a tree-based structure that the database system's query optimizer can use to quickly find rows in the **Product** table based on a specified **Name**.

![](https://i.imgur.com/roeL3xI.png)


You can create many indexes on a table. So, if you also wanted to find products based on price, creating another index on the **Price** column in the **Product** table might be useful. **However, indexes aren't free. ==An index consumes storage space==, and each time you insert, update, or delete data in a table, the indexes for that table must be maintained.** This additional work can slow down insert, update, and delete operations. You must strike a balance between having indexes that speed up your queries versus the cost of performing other operations.

## 2.2 Explore relational database services in Azure

### 2.2.1 Azure SQL services
Azure SQL is a collective term for a family of Microsoft SQL Server based database services in Azure. 

Specific Azure SQL services include:
- [[SQL Server on Azure Virtual Machines]] (VM)
- [[ Azure SQL Managed Instance]]
- [[Azure SQL Database]]
- Azure SQL Edge

### 2.2.2 Azure services for open-source databases
In addition to Azure SQL services, Azure data services are available for other popular relational database systems, including MySQL, MariaDB, and PostgreSQL. The primary reason for these services is to enable organizations that use them in on-premises apps to move to Azure quickly, without making significant changes to their applications.

MySQL started life as a simple-to-use open-source database management system. It's the leading open source relational database for _Linux, Apache, MySQL, and PHP_ (LAMP) stack apps. It's available in several editions; Community, Standard, and Enterprise. The Community edition is available free-of-charge, and has historically been popular as a database management system for web applications, running under Linux. Versions are also available for Windows. Standard edition offers higher performance, and uses a different technology for storing data. Enterprise edition provides a comprehensive set of tools and features, including enhanced security, availability, and scalability. The Standard and Enterprise editions are the versions most frequently used by commercial organizations, although these versions of the software aren't free.

MariaDB is a newer database management system, created by the original developers of MySQL. The database engine has since been rewritten and optimized to improve performance. MariaDB offers compatibility with Oracle Database (another popular commercial database management system). One notable feature of MariaDB is its built-in support for temporal data. A table can hold several versions of data, enabling an application to query the data as it appeared at some point in the past.

PostgreSQL is a hybrid relational-object database. You can store data in relational tables, but a PostgreSQL database also enables you to store custom data types, with their own non-relational properties. The database management system is extensible; you can add code modules to the database, which can be run by queries. Another key feature is the ability to store and manipulate geometric data, such as lines, circles, and polygons.

PostgreSQL has its own query language called _pgsql_. This language is a variant of the standard relational query language, SQL, with features that enable you to write stored procedures that run inside the database.

- [[Azure Database for MySQL]]
- [[Azure Database for MariaDB]]
- [[Azure Database for PostgreSQL]]