---
tags:
  - video-note
  - youtube
Source:
  - "[How I'd Learn to be a Data Engineer (Ranked w/ 4M Job Postings) - YouTube](https://www.youtube.com/watch?v=_-DzZeixu0w)"
---
Stopped at 18:00: https://youtu.be/_-DzZeixu0w?t=1096

---

Top skills in Data Engineer job posts: https://datanerd.tech/skills?title=Data+Engineer

![](https://i.imgur.com/kivnq6T.png)
	

# Data Engineering Lifecycle

![](https://i.imgur.com/tEEa3Aj.png)

Book Recommendation: Fundamentals of Data Engineering (O'Reilly) - Reis & Housley

Source systems =  Where data is generated
Analytics systems = Where our data goes

![](https://i.imgur.com/71M19EI.png)


## Storage
Data Warehouse (Structured data only) -> Great to use for BI; Limiting for Data Sciance
Data Lake (Structured & Unstrucured data) -> Not good for BI; Great for DS and ML
Data Lakehouse (Combinations of Warehouse and Lake)

Tip: Start with Data Warehouse, then Data Lakehouse

Google Cloud Warehouse Example
![](https://i.imgur.com/BOJgh12.png)

Google Cloud Lakehouse Example
![](https://i.imgur.com/FX5aR0O.png)

Tip: Start learning a cloud provider over data platform.
- Why? Because once you understand how data is built on cloud, you understand how to do it on data platforms as well.

Data Platforms: Snowflake / Databricks = Runs on top of a cloud provider

## Generation & Ingestion

Data ingestion
1. Batching = loads data at specific time
2. Streaming = loads data real-time (used for something like fraud detection)

Popular tools for batch ingestion
![](https://i.imgur.com/PM38Akn.png)

Popular tools for steaming
![](https://i.imgur.com/VmghXby.png)

## Transformation

### Table design pattern

Normalize tables = better storage
Denormalized tables = faster computation for anlaysis

![](https://i.imgur.com/IgiQVoX.png)

The whole purpose of data modelling is figuring just how much and how far you should denormalize tables to make it useful for analysis.

### Two major types of databases

A data engineer needs to be able to pick the correct database for their use-case.

- OLTP = Online Transaction Processing
	- Built for running applications
	- Fast CRUD; Slow on scanning and aggregating data
	- Typically contains normalized tables
- OLAP = Online Analytical Processing
	- Built for analyzing data
	- Fast scanning/aggregating; Slow at handling updates at scale.
	- Typically contains denormalized tables

![](https://i.imgur.com/XFTKhuG.png)

TODO Stopped at 18:00: https://youtu.be/_-DzZeixu0w?t=1096
# Skills tier-list
Most essential:
- SQL
- Python
- Cloud Platform
- Git (version control)
- Bash

dbt (Datacamp, Zoomcamp)


Orchestration tool: Airflow (Can you talk about it??)
Transformation at scale: Spark


Data Platform (Snowflake)
Ingestion: Kafka

BI tool (PowerBI / Tableau)

Java
Scala