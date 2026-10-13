[How Can You Structure Your Python Script? – Real Python](https://realpython.com/python-script-structure/)

- Use `UPPER_SNAKE_CASE` variable names for constants. This naming signals the intent that they should remain fixed throughout the script’s execution.
- Sample code to guard main execution script
```
def main():
    """Fetch the Iris dataset from UCI."""
    urllib.request.urlretrieve(
        IRIS_DATA_URL,
        LOCAL_ZIP_FILENAME
    )
    print(f"Downloaded {LOCAL_ZIP_FILENAME}")

if __name__ == "__main__":
    main()
```

- 