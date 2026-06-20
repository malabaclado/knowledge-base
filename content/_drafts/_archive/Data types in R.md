# Common Data Types

- **Numeric**: Used for real or decimal numbers, including integers and floating-point numbers.
- **Character**: Used for storing text or strings of characters.
- **Logical**: Stores Boolean values (`TRUE` or `FALSE`) for logical operations.
- **Integer**: Specialized numeric type for whole numbers.
- **Complex**: Used for complex numbers.
- **Vector**: A one-dimensional collection of elements of the same data type.
- **Matrix**: A two-dimensional collection of elements in rows and columns.
- **List**: A collection of elements of different data types.
- **[[Data Frame (Data type)]]**: A table-like structure with rows and columns, capable of holding different data types in columns.
- **[[Factor (Data type)]]**: Represents categorical variables with a limited set of values.
- **NULL**: Represents a lack of value or undefined value.

# Complex data 
In R, complex numbers are created using the `complex()` function or by using the `+` symbol between the real and imaginary parts. 

```R
# Creating complex numbers
z1 <- complex(real = 2, imaginary = 3)  # Using complex()
z2 <- 1 + 2i                           # Using +

print(z1)
print(z2)
```

Complex numbers in R support arithmetic operations, just like real numbers. You can perform addition, subtraction, multiplication, division, and more on complex numbers. R automatically handles the mathematical operations involving complex numbers, ensuring that both the real and imaginary parts are treated appropriately.

---
# Vector data type
==In R, a vector is a fundamental data type that represents a one-dimensional collection of elements of the **same data type==**. Vectors are used to store and manipulate sequences of values, such as numbers, characters, or logical values.

## Key characteristics of vectors
1. **Homogeneity:** All elements within a vector must be of the **same data type**, whether they are numeric, character, logical, or other types.
2. **One-Dimensional:** Vectors are one-dimensional arrays, meaning they have a single axis and contain elements in a linear sequence.
3. **Atomic Data Types:** Vectors hold atomic data types, which are the fundamental building blocks in R. **Examples of atomic data types include numeric, character, logical, integer, complex, and raw.**

## Creating vectors
- **Using `c()`:** The `c()` function is used to concatenate elements into a vector. 
```R
numeric_vector <- c(1.2, 3.4, 5.6) 
character_vector <- c("apple", "banana", "cherry")
```

- **Using `seq()`:** The `seq()` function generates sequences of numbers.
```R
sequence <- seq(from = 1, to = 10, by = 2)
```

- **Using `rep()`:** The `rep()` function replicates values to create a vector.
```R
repeated_vector <- rep("hello", times = 3)
```

# List data type
In R, you can create lists using the `list()` function. Lists allow you to store elements of different data types, including vectors, matrices, data frames, other lists, and even custom objects. Here's how you can create lists in R:

**Basic List:**
You can create a basic list by passing the elements you want to include as arguments to the `list()` function. Each element is separated by a comma.

```R
# Creating a basic list
my_list <- list("apple", 3.14, TRUE)
print(my_list)
```

**Named Elements:**
You can also assign names to elements in the list using the names parameter or by using the `names()` function.

```R
# Creating a named list
my_named_list <- list(fruit = "apple", pi = 3.14, is_valid = TRUE)
print(my_named_list)
```

**Nested Lists:**
Lists can also contain other lists as elements, allowing you to create complex data structures.

```R
# Creating a nested list
nested_list <- list(
  info = list(name = "John", age = 25),
  scores = c(90, 85, 78),
  matrix_data = matrix(1:6, nrow = 2)
)
print(nested_list)
```

**Adding Elements:**
You can add elements to a list using the assignment operator (`<-`).

```R
# Adding elements to a list
my_list$city <- "New York"
my_list[["country"]] <- "USA"
print(my_list)
```

**Accessing Elements:**
You can access elements in a list using either the `$` notation or the double square brackets `[[ ]]`.

```R
# Accessing elements from the list
print(my_list$city)
print(my_list[["country"]])
```

Creating and using lists allows you to organize and manage diverse types of data within a single data structure. Lists are particularly useful for cases where the data does not fit neatly into a homogeneous structure like vectors or matrices.

# Lists VS vector in R

Here's a comparison of the list and vector data types in R, presented in bullet point format:

**Lists:**

- **Heterogeneous:** Can hold elements of different data types.
- **Structure:** Can store vectors, matrices, data frames, other lists, and custom objects.
- **Named Elements:** Supports naming elements for easy access.
- **Flexibility:** Accommodates diverse and complex data structures.
- **Use Case:** Useful when dealing with data of varying types or custom structures.

**Vectors:**

- **Homogeneous:** Contains elements of the same data type.
- **One-Dimensional:** Stores a sequence of elements in a single dimension.
- **Efficiency:** Optimized for storage and computation efficiency.
- **Vectorized Operations:** Enables operations on multiple elements simultaneously.
- **Use Case:** Ideal for homogeneous data, numerical calculations, and data analysis tasks.

**When to Use Lists:**

- For storing elements of different data types or varied structures.
- When you need to organize complex data hierarchies.
- When elements require distinct names for identification.
- When working with data frames, matrices, and custom structures.

**When to Use Vectors:**

- For storing a homogeneous sequence of data elements.
- When performing arithmetic or logical operations on elements.
- When dealing with numeric, character, or logical data.
- When efficiency and vectorized operations are critical.

