---
tags:
  - video-note
  - youtube
Source:
  - "[FastAPI Crash Course - Modern Python API Development](https://www.youtube.com/watch?v=8TMQcRcBnW8)"
---
Cheat sheet: [FastAPI Cheat Sheet](https://devsheets.io/sheets/fastapi)

Terms
- ASGI = Asynchronous Server Gateway Interface
	- a standard for web servers to communicate with asynchronous-capable Python applications

What is FastAPI?
- FastAPI is a modern, high-performance web framework for building APIs with Python.
- It is build on top of Starlette, which is a lightweight ASGI framework/toolkit.


Features of FastAPI
- Speed: on par with Node.js
- Automatic data validation: Uses Pydantic for type checking
- Automatic Interactive Documentation (Swagger and ReDoc)
- Dependency injection System
- Security Utilities 
- Developer Experience Focused
- Websockets & Streaming

Setting up a Python Virtual Environment
```
# Setting up the environment
>>> python -m venv .venv

# Running the environment
>>> .\.venv\Scripts\activate 

# Closing the environment
>>> deactivate
```

Instaling FastAPI
```
pip install "fastapi[standard]"
```

Wrapper to run the API from terminal
```
fastapi dev main.py
```

 #Question What is uvicorn?
 #Question When is it fine to use async function and when is it fine not to use in FastAPI?
#Question What is enum?
- Enums in Python are used to define a set of named constant values. They make code cleaner, more readable and prevent using invalid values.
- [enum in Python - GeeksforGeeks](https://www.geeksforgeeks.org/python/enum-in-python/)
- [Enum HOWTO — Python 3.14.5rc1 documentation](https://docs.python.org/3/howto/enum.html)

##### Using routers
```
# app/routers/items.py
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def read_items():
    return []

# app/main.py
from fastapi import FastAPI
from app.routers import items, users

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
```


##### Explaining middlewares
```
app.middleware("http")(timing_middleware)
```

Explanation: This line registers `timing_middleware` as an HTTP middleware function on the FastAPI app. `app.middleware("http")` returns a decorator for HTTP request/response middleware, and then calling it with `timing_middleware` attaches that function to the app’s middleware stack.

The result is that every incoming request passes through `timing_middleware` before reaching your route handlers, and the middleware can also inspect or modify the response on the way back.


##### Generating requirements.txt file
```
pip freeze > requirements.txt
```


# Query Parameters
