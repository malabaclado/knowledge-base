
Technical Specifications: [Flash Sale Inventory Reservation Service Technical Specifications - NotebookLM](https://notebooklm.google.com/notebook/0c2d3ae7-2e81-4b0d-8fd9-dee1ba946f84)

# Project Outline

## MVP API Health Check

Initialize a virtual environment
```
python -m venv .venv
```

Install FastAPI and Pydantic
```
pip install "fastapi[standard]"
```

Initial health check
```
@app.get("/")
def health():
    return {"status": "Ok"}
```

Running the server
```
fastapi dev main.py
```






## Setting up inventory table and /inventory endpoint path


TODO: Add database and /inventory endpoint
SQLite database should have 3 tables: users, inventory and transactions



# Notes

Dependency injection in FastAPI
```
# /database.py
def get_db():
    conn = get_db_connection()
    try:
        yield conn # yield means you allow conn to be used in any outside function.
    finally:
        conn.close()

# /app.py
# Using it as a context manager
with get_db() as db:
    db.execute("SELECT ...")
# The moment this block ends, conn.close() happens automatically!
```

Explanation: `yield` allows the function to pause and the other code to use the existing connection `conn`. Regardless of whether the code is successful or throws an error, the function `get_db()` will close the connection.

