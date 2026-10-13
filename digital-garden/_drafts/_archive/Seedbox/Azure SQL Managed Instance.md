---
tags:
alias:
creation-date: Friday 7th April 2023
---

**Azure SQL Managed instance effectively runs a ==fully controllable instance of SQL Server in the cloud==.** You can install multiple databases on the same instance. You have complete control over this instance, much as you would for an on-premises server. **SQL Managed Instance automates backups, software patching, database monitoring, and other general tasks, but ==you have full control over security and resource allocation for your databases==.** 

**==Managed instances depend on other Azure services== such as Azure Storage for backups, Azure Event Hubs for telemetry, Azure Active Directory for authentication, Azure Key Vault for Transparent Data Encryption (TDE) and a couple of Azure platform services that provide security and supportability features.** The managed instances make connections to these services.

All communications are encrypted and signed using certificates. To check the trustworthiness of communicating parties, managed instances constantly verify these certificates through certificate revocation lists. If the certificates are revoked, the managed instance closes the connections to protect the data.

# Use cases
**Consider Azure SQL Managed Instance if you want to ==lift-and-shift an on-premises SQL Server instance and all its databases to the cloud, without incurring the management overhead of running SQL Server== on a virtual machine.**

==**Azure SQL Managed Instance provides features not available in Azure SQL Database**== (discussed below). If your system uses features such as linked servers, Service Broker (a message processing system that can be used to distribute work across servers), or Database Mail (which enables your database to send email messages to users), then you should use managed instance. To check compatibility with an existing on-premises system, you can install Data Migration Assistant (DMA). This tool analyzes your databases on SQL Server and reports any issues that could block migration to a managed instance.

# Business benefits
**Azure SQL Managed Instance enables a system administrator to ==spend less time on administrative tasks== because the service either performs them for you or greatly simplifies those tasks.** Automated tasks include operating system and database management system software installation and patching, dynamic instance resizing and configuration, backups, database replication (including system databases), high availability configuration, and configuration of health and performance monitoring data streams.

**Azure SQL Managed Instance has ==near 100% compatibility with SQL Server Enterprise Edition==, running on-premises.**

**Azure SQL Managed Instance supports SQL Server Database engine logins and logins ==integrated with Azure Active Directory (AD)==.** SQL Server Database engine logins include a username and a password. You must enter your credentials each time you connect to the server. Azure AD logins use the credentials associated with your current computer sign-in, and you don't need to provide them each time you connect to the server.

---
See also:
- [[Microsoft Azure Data Fundamentals Note]]