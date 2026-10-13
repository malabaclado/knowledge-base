
- `log` is in base e by default
- other available logarithms:
	- `log10`, `log2`
- available functions
	- `factorial(n)`
	- `mod(a,b)`

`who` command
- shows active varialbles

`clear` command
- erases variables

- On matrix notation, semicolon ends rows.
- Adding `'` mark transposes a vector
- Matlab starts counting with 1 (In contrast to python that starts with 0)


Getting the roots of an equation
- Solutions for an equation can be solved using the `roots` command.
- passing a variable (should be a vector) `roots(p)`
	- If `p=[1 1 1]`, then `roots(p)` solves for $x^2+x+1$

- writing inline `roots([1 1 1])`