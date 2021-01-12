# Operators
We have discussed that computers are essentially tools for storing and manipulating data. Data manipulation is done with special symbols called *operators*.

## Operators, Operands and Outputs
Consider the simple statement below
```python
> 40 + 2
42
```
In this code the `+` *operator* performs the addition *operation* on the *operands* `40` and `2` with an *output* of `42`. So an operator is a symbol that performs an operation (data manipulation) on operands to produce an output.

## Types of Operators

The main types of operators are: *assignment*, *arithmetic*, *comparison*, *logical*. In addition most languages have bitwise and special operators which are beyond the scope of this course.

### Assignment
The assignment operator `=` is used to assign a value to a variable. Example:
```python
meaning_of_life = 42
```
The statement above assigns the value `42` to the variable `meaning_of_life`.

### Comparison
In maths, the symbol `=` is used for comparison, that is to ask the question whether 2 things are equal, however in programming this symbol is used for assignment (see above), so comparison is done with the symbol `==`. For most languages, the comparison operators are:

Symbol | Comparison
:---:|:---
`==`| is equal to
`!=`| is not equal to
`>`| is greater than
`<`| is less than
`>=`| is greater than or equal to
`<=`| is less than or equal to

All the comparison operators yield a boolean `True` or `False` as a result.

### Arithmetic
Arithmetic operators perform mathematical operations. The basic ones are generally the same as those encountered in maths.

Symbol | Arithmetic operation
:---: | :---
`+` | addition
`-` | subtraction
`*` | multiplication
`/` | division

note that the symbol `x` is not used for multiplication. In addition to these basic operators, most languages have additional ones that vary slightly between languages. We will learn the Python operators as there are no operators prescribed for SDD pseudocode.

Symbol | Arithmetic operation
:---: | :---
`**` | exponentiation - `x**3` means `x` to the power of `3` or x cubed.
`%` | modulo - calculates the remainder of a division. `8 % 3` would yield 2. This operator is surprisingly more useful than it sounds!

### Logical
Logical operators are used to combine conditional statements, which is just a jargon way of saying that they are used to take two statements and evaluate whether they are both true, at least one is true or none is true. Like the comparison operators the result is a boolean `True` or `False`.

Symbol | Logical operation
:---: | :---
`AND` | `True` if both statements are true
`OR` | `True` if one on the statements is true
`NOT` | `True` if the statement is false

These logical operators are written in all capitals in pseudocode but all lower case in python.
```python
and or not
```

## Task

Use the comments in the main.py script as a instructions to edit the code until it runs and passes the tests. Remember, you run the test by going to the shell tab (NOT the console tab) and typing `pytest` at the prompt. Then edit the code in the main.pseudo file. When you are finished, submit.
