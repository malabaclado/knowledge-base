---
tags:
alias:
creation-date: Wednesday 30th August 2023
---

# Introduction to Normalization
- Normalization is a process used in relational databases to eliminate redundancy and improve data integrity.
- It involves organizing data into well-structured tables to avoid data anomalies.

# Goals of Normalization
- Prevent contradictory data and ensure data integrity.
- Eliminate redundancy and improve data storage efficiency.
- Simplify data maintenance and querying.

# Levels of Normalization
1. **First Normal Form (1NF):** First rule of database normalization follows these four principles:
   - Eliminate row order dependency.
   - Avoid mixing data types within columns.
   - Assign a primary key to each table to ensure uniqueness.
   - Remove repeating groups.
2. **Second Normal Form (2NF):** ==*All non-key attribute should depend only on the primary key - nonprimary key dependencies are not allowed*==
   - Non-key attributes should depend on the entire primary key.
   - Avoid partial dependencies.
   - Introduce separate tables if needed to maintain dependencies.
3. **Third Normal Form (3NF) and :** *==Every **non-key attribute** should depend on the key and nothing but the key.==*
   - Avoid transitive dependencies.
   - A more general version is known as Boyce-Codd Normal Form
   - 3.5. **Boyce-Codd Normal Form (BCNF)**
      - Every attribute should depend on the key and nothing but the key.
      - The difference between 3NF and BCNF is very small. The chances of encountering a third normalized table that isn't boyce-codd normal is almost zero.
4. **Fourth Normal Form (4NF):** ==*Multivalued dependencies in a table must be multivalued dependencies on the key.*==
   - Handle multi-valued dependencies.
      - Multiple dependencies happen when a primary key is associated with multiple values of a non-key attribute. (eg. Model ->> Colors)
   - Only allow multi-valued dependencies that involve the primary key.

2. **Fifth Normal Form (5NF):** ==*The table (in 4NF) cannot be describable as a logical result of joining some tables together.*==
   - Ensure tables cannot be logically derived by joining other tables.
   - Prevent unnecessary dependencies by maintaining independent tables.


# Benefits and Importance
- Achieving normalization results in better data integrity, reduced redundancy, and improved database efficiency.
- Normalized tables are easier to query, maintain, and update.

> [!NOTE] Summary
> 
> - Normalization is a crucial process in database design to maintain data integrity and efficiency.
> - The different normal forms provide guidelines to organize data effectively and eliminate potential anomalies.
> 

---

Reference Material: [Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF - YouTube](https://www.youtube.com/watch?v=GFQaEYEc8_8)