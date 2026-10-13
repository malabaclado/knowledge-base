# What is Pydantic?

Pydantic is a data validation and settings management library for Python. It uses standard Python type hints to enforce data schemas at runtime.

If data matches your defined schema, Pydantic parses it into a strongly-typed object. If the data is invalid or malformed, Pydantic immediately throws an error containing clear, structured information detailing exactly what went wrong.

### Key Features

- ****Type Validation:**** Automatically validates data based on type annotations.
- ****Data Parsing:**** Converts input data into Python objects with the correct types.
- ****Error Handling:**** Provides clear and detailed error messages for invalid data.
- ****Field Validators:**** Allows custom validation logic with the @field_validator decorator.
- ****Performance:**** Pydantic is optimized for speed and supports optional Cython extensions for even faster performance.
- ****Integration:**** Provides seamless integration with popular frameworks (FastAPI, Django, Flask) and ORMs like SQLAlchemy.


### Field validation

Data validation using custom functions can be done using `@field_validation` decorator.  

For example: Validating valid age.

```
from pydantic import BaseModel, field_validator

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

    @field_validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18')
        return value

UserProfile(name="Noah Müller", age=17, email="noah.muller@example.com")
```

Remarks:
- In the above code, the `@field_validator` runs the `check_age` function on the `age` input. If `age` is less than 18, it will raise a `ValueError`.
- The argument `cls` in `check_age` indicates that the method is applied to the class itself.

It is possible to re-use a `@field_validator` for multiple fields:

```
@field_validator('age', 'experience', 'years_employed')
def check_positive(cls, value):  # 'value' handles whichever field is currently being checked
    if value < 0:
        raise ValueError('Cannot be negative')
    return value
```

Remarks:
- The above code runs the validator three times, checking the age, experience and years_employed > 0.

### Model validation

For example: Validating input passwords for new account creation.

```
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, model):
        if model.password != model.confirm_password:
            raise ValueError("Passwords do not match")
        return model

User(password="a", confirm_password="b")
```

Remarks:
- `@model_validator` runs after the model is initialized.
- `@field_validator` checks fields in isolation (one-by-one), `@model_validator` looks at the entire object as a whole
- There are 4 validator modes:
	- `after`
		- **When it runs:** At the very end of validation.
		- **Use Case:** Comparing two or more clean fields against each other (e.g., checking if `start_date` is before `end_date`, or if `password == confirm_password`).
	- `before`
		- **When it runs:** Before _any_ field-level type checking or validation happens.
		- **Use Case:** Fixing structural issues with incoming data, renaming input keys dynamically, or handling conditional defaults before Pydantic throws a type error.
	- `wrap`
		- **When it runs:** It completely wraps the validation process. You control exactly when (or if) Pydantic's internal validation runs by calling `handler(value)`.
		- **Use Case:** Advanced error handling. For example, trying to validate input normally, catching a specific validation error, and gracefully falling back to a default state instead of crashing.
	- `plain`
		- **When it runs:** It completely replaces Pydantic's internal validation. Pydantic will _never_ check types or fields; it relies entirely on your custom function to build and return the object.
		- **Use Case:** Rare. Typically used when migrating highly complex legacy systems or creating custom polymorphic models where Pydantic's default behavior is fundamentally incompatible.

Decision matrix for deciding which mode to use:

```
  Are you doing cross-field logic on clean, trusted types?
 └── YES ──> Use mode='after' (Safest & Cleanest)
 └── NO (Data is messy or keys might be missing)
      │
      └── Do you want Pydantic to do its normal type checking afterward?
           └── YES ──> Use mode='before'
           └── NO (You want to control or bypass Pydantic's errors)
                └── Try mode='wrap' (to catch errors) or mode='plain' (to completely override)
```


# References
- [Welcome to Pydantic | Pydantic Docs](https://pydantic.dev/docs/validation/latest/get-started/)
- [Pydantic: A Guide With Practical Examples | DataCamp](https://www.datacamp.com/tutorial/pydantic)
- [Introduction to Python Pydantic Library - GeeksforGeeks](https://www.geeksforgeeks.org/python/introduction-to-python-pydantic-library/)


 