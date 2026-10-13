---
tags:
alias: ['API']
creation-date: Tuesday 10th October 2023
---

# Getting to know API
- API stands for **application programming interface**.
- An API acts as a communication layer, or interface, that allows different systems to talk to each other without having to understand exactly what the others do.
- **Functionality.** No matter the type, all APIs function mostly the same way. 
	- You usually make a **request** for information or data,  
	- the API returns a **response** with what you requested. 
	- For example, every time you open Twitter or scroll down your Instagram feed, you’re basically making a request to the API behind that app and getting a response in return. This is also known as **calling** an API.
- ## Design Models
	- ### SOAP
		- **SOAP (Simple Object Access Protocol)** is typically ==associated with the enterprise world==, has a stricter contract-based usage, and is mostly designed around actions.
	- ### REST
		- 1. **REST (Representational State Transfer)** is typically ==used for public APIs and is ideal for fetching data from the Web==. It’s much lighter and closer to the HTTP specification than SOAP.
	- ### GraphQL
		- Created by Facebook, GraphQL is a very flexible query language for APIs, where the clients decide exactly what they want to fetch from the server instead of letting the server decide what to send.
- ## Some terminologies
	- The first piece of information necessary for consuming an API is the API URL, typically called the **base URL**.
	- An **endpoint** is a part of the URL that specifies what **resource** you want to fetch.
- ## HTTP Methods
	- ### GET
		- This method allows you to retrieve resources from a given API.
	- ### POST
		- Sending information to the server to create a new resource.
	- ### PUT
		- Update a transaction
	- ### PATCH 
		- Partially update a transaction
	- ### DELETE 
		- Delete a transaction


---
Sources:
- [Python & APIs: A Winning Combo for Reading Public Data – Real Python](https://realpython.com/python-api/)
- [Python and REST APIs: Interacting With Web Services – Real Python](https://realpython.com/api-integration-in-python/)