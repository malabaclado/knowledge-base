Numpy is a numeric processing library that sits on top of python.

**WAYS TO CREATE ARRAYS**
- `np.zeros()` - creates an array with zeros as entries. 
- `np.ones()` - creates array with ones as entries
- `np.array()` - creates array by passing a python list
- `np.random.randint(10, size=6)` - creates array of 6 elements of random integers from 0 to 10.

---
**DESCRIBING AN ARRAY**

`array.shape` - show row, column number
`array.ndim` - show no. of dimensions
`array.size`

---

> indexing in numpy is row first, column second
> 

> numpy arrays are immutable 

Summary statistics
sum, mean, std, var

---

**BROADCASTING AND VECTOR OPERATIONS**

`[0,1] + 10 = [10,11]`
`[0,1] * 10 = [0,10]`

> numpy allows matrix operations
> 

> numpy also allows boolean arrays
> 

--

**Linear Algebra**
Dot product `@`
Transposing matrices `B` to `B.T`

 Other numpy functions
 - random
 - arange
 - reshape
 - linspace
 - zeros
 - ones
 - empty
 - identity
 - eye


