---
tags:
alias:
creation-date: Thursday 6th April 2023
cards-deck: Microsoft Azure::DP-900 Data Fundamentals
---

# 1. Explore core concepts

## 1.1 Explore core concepts


## 1.2 Explore data roles and services

### 1.2.1 Data roles

The three key job roles that deal with data in most organizations are: {Database administrators}, {Data engineers}, {Data analysts}.
^1680770033793

{Database administrators} **manage databases**, assigning permissions to users, storing backup copies of data and restore data in the event of a failure.
^1680771868221

{Data engineers} **manage infrastructure and processes for data integration** across the organization, applying data cleaning routines, identifying data governance rules, and implementing pipelines to transfer and transform data between systems.
^1680771868224

{Data analysts} **explore and analyze data** to create visualizations and charts that enable organizations to make informed decisions.
^1680771868227

### 1.2.2. Data services

{Azure SQL} is the collective name for a **family of relational database solutions based on the Microsoft SQL Server** database engine.
^1680771868231

It is a fully managed **platform-as-a-service (PaaS) database** hosted in Azure:: **Azure SQL Database**
^1680771868234

It is a **hosted instance of SQL Server** with automated maintenance:: **Azure SQL Managed Instance**
^1680771868236

It is a **virtual machine** with an installation of SQL Server in Azure:: **Azure SQL VM**
^1680771868239

What are included in Azure SQL services?::Azure SQL Database, Azure SQL Managed Instance, Azure SQL VM
^1680771868241

Azure database offers open source relational database which includes: on {MySQL}, {MariaDB} and {PostgreSQL}.
^1680771868244

{Azure Cosmos DB} is an Azure service which is a global-scale **non-relational (_NoSQL_) database system** that supports multiple application programming interfaces (APIs), enabling you to store and manage data as JSON documents, key-value pairs, column-families, and graphs.
^1680771868247

{Azure Storage} is the core Azure service that **enables you to store data**.
^1680771868250

Azure storage allows you to store data in: {blob containers}, {file shares} and {tables}.
^1680771868253

Data engineers use Azure Storage to host {data lakes} - **blob storage** with a hierarchical namespace that enables files to be organized in folders in a distributed file system.
^1680771868255

{Azure Data Factory} is an Azure service that enables you to **define and schedule data pipelines** to transfer and transform data.
^1680771868258

Azure Data Factory is used by data engineers to build {_extract_, _transform_, and _load_ (ETL) solutions }that populate analytical data stores with data from transactional systems across the organization.
^1680771868261

Azure provides a comprehensive, u**nified data analytics solution** that provides a single service interface for multiple analytical capabilities. This is service is called {Azure Synapse Analytics}
^1680771868264

{Azure Databricks} is an **Azure-integrated version of the popular Databricks platform**, which combines the Apache Spark data processing platform with SQL database semantics and an integrated management interface to enable large-scale data analytics.
^1680771868267

{Azure HDInsight} is an Azure service that **provides Azure-hosted clusters** for popular Apache open-source big data processing technologies
^1680771868269

Apache open-source big data processing technologies offered by **Azure HDInsight** includes: {Apache Spark}, {Apache Hadoop}, {Apache HBase}, {Apache Kafka}.
^1680771868272

This Apache technology is a **distributed data processing system that supports multiple programming languages** and APIs, including Java, Scala, Python, and SQL. :: Apache Spark
^1680771868275

This Apache technology is a d**istributed system that uses _MapReduce_ jobs to process large volumes of data** efficiently across multiple cluster nodes. :: Apache Hadoop
^1680771868277

This Apache technology is an **open-source system for large-scale NoSQL data storage and querying**.::Apache HBase
^1680771868280

This Apache technology is a **message broker** for data stream processing.:: Apache Kafka
^1680771868283

This Azure service is a **real-time stream processing engine** that captures a stream of data from an input, applies a query to extract and manipulate data from the input stream, and writes the results to an output for analysis or further processing.:: Azure Stream Analytics
^1680771868286

Data engineers can incorporate **Azure Stream Analytics** into {data analytics architectures} that capture streaming data for ingestion into an analytical data store or for real-time visualization.
^1680771868288

This Azure service is **a standalone service that offers the same high-performance querying of log and telemetry data** as the Azure Synapse Data Explorer runtime in Azure Synapse Analytics.::Azure Data Explorer
^1680771868291

Data analysts can use Azure Data Explorer {to query and analyze} data that includes a timestamp attribute, such as is typically found in log files and _Internet-of-things_ (IoT) telemetry data.
^1680771868294

This Azure service provides a solution for **enterprise-wide data governance** and discoverability.::Microsoft Purview
^1680771868296

You can use Microsoft Purview to {**create a map** of your data and **track data lineage** across multiple data sources} and systems, enabling you to find trustworthy data for analysis and reporting.
^1680771868299

Data engineers can use Microsoft Purview {to enforce data governance across the enterprise} and ensure the integrity of data used to support analytical workloads.
^1680771868302

{Microsoft Power BI} is a **platform for analytical data modeling and reporting** that data analysts can use to create and share interactive data visualizations.
^1680771868304

# 2. Explore relational database in Azure

In the early years of computing systems, every application stored data in its own unique structure. When developers wanted to build applications to use that data, they had to know a lot about the particular data structure to find the data they needed. These data structures were inefficient, hard to maintain, and hard to optimize for good application performance. The {relational database model} was designed to solve the problem of multiple arbitrary data structures.
^1680836695765

In a relational database, you model collections of entities from the real world as {tables}. An entity can be anything for which you want to record information; typically important objects and events.
^1680836695773

{Normalization} is a term used by database professionals for a schema design process that **minimizes data duplication and enforces data integrity**.
^1680836695777

### What are the core principles of data normalization? #card 
1.  Separate each _entity_ into its own table.
2.  Separate each discrete _attribute_ into its own column.
3.  Uniquely identify each entity instance (row) using a _primary key_.
4.  Use _foreign key_ columns to link related entities.
^1680836695781

SQL was originally standardized by the American National Standards Institute (ANSI) in {1986}, and by the International Organization for Standardization (ISO) in 1987. Since then, the standard has been extended several times as relational database vendors have added new features to their systems.
^1680840148124

SQL was originally standardized by the American National Standards Institute (ANSI) in 1986, and by the International Organization for Standardization (ISO) in {1987}. Since then, the standard has been extended several times as relational database vendors have added new features to their systems.
^1680840148128

This version of SQL is used by Microsoft SQL Server and Azure SQL services.::_Transact-SQL (T-SQL)_.
^1680840148131

### SQL statements are grouped into three main logical groups #card 
-   Data Definition Language (DDL)
-   Data Control Language (DCL)
-   Data Manipulation Language (DML)
^1680840148133

You use Data Definition Language (DDL) statements {to create, modify, and remove tables and other objects in a database (table, stored procedures, views, and so on).}
^1680840148136

Database administrators generally use Data Control Language (DCL) statements to manage access to {objects in a database by granting, denying, or revoking permissions to specific users or groups.}
^1680840148139

The three main Data Control Language (DCL) SQL statements:: GRANT, DENY, REVOKE
^1680840148142

You use Data Manipulation Language (DML) statements to {retrieve (query) data, insert new rows, or modify existing rows. You can also delete rows if you don't need them anymore.}
^1680840148145

The four main Data Manipulation Language (DML) statements are:: SELECT, INSERT, UPDATE, DELETE
^1680840148148


What is a view?::A view **is a virtual table** based on the results of a **SELECT** query. You can think of a view as a window on specified rows in one or more underlying tables. 
^1680840594524

What is a stored procedure?::A stored procedure defines **SQL statements that can be run on command**. Stored procedures are used to encapsulate programmatic logic in a database for actions that applications need to perform when working with data.
^1680840594527


# Explore non-relational data in Azure



# Explore data analytics in Azure
