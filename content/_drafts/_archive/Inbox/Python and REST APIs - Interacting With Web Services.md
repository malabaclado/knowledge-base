---
tags:
alias:
creation-date: Sunday 1st October 2023
---


> [!NOTE]- Source
> [Python and REST APIs: Interacting With Web Services – Real Python](https://realpython.com/api-integration-in-python/#rest-architecture)

---
- **REST** stands for representational state transfer 
- REST is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.
- ## REST Architectural Constraints
	- **Stateless:** The server won’t maintain any state between requests from the client.
	- **Client-server:** The client and server must be decoupled from each other, allowing each to develop independently.
	- **Cacheable:** The data retrieved from the server should be cacheable either by the client or by the server.
	- **Uniform interface:** The server will provide a uniform interface for accessing resources without defining their representation.
	- **Layered system:** The client may access the resources on the server indirectly through other layers such as a [proxy](https://en.wikipedia.org/wiki/Proxy_server) or [load balancer](https://en.wikipedia.org/wiki/Load_balancing_(computing)).
	- **Code on demand (optional):** The server may transfer code to the client that it can run, such as [JavaScript](https://realpython.com/python-vs-javascript/) for a single-page application.
- REST is *not* a specification but a set of guidelines on how to architect a network-connected software system.
- A **REST web service** is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.
- ## API Endpoints
	- A REST API exposes a set of public URLs that client applications use to access the resources of a web service. These URLs, in the context of an API, are called **endpoints**.
- ## REST API and Python
	- To write code that interacts with REST APIs, most Python developers turn to requests to send HTTP requests. This library abstracts away the complexities of making HTTP requests. It’s one of the few projects worth treating as if it’s part of the standard library.
	- 