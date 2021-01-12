# Variables and Literals

## Understanding Variables and Literals
At the most fundamental level, a computer program just stores and manipulates data or information. In the previous lesson we looked at 4 data types: `int, str, float` and `bool`. The data itself can be stored as *literals* or *variables*.

A *literal* is a constant value. The `int 42` is the number **42**. The `str 'mostly harmless'` is the phrase **mostly harmless**. The characters literally represent themselves.

A *variable* is a name we give to a value and this value can change throughout the program - it varies!

So in the code
```python
meaning_of_life = 42
planet_earth = 'harmless'
```

`42` and `'harmless'` are literals, while `meaning_of_life` and `planet_earth` are variables. The values of these variables could be changed later in the program

```python
meaning_of_life = 7
planet_earth = 'mostly harmless'
```

but the value of `42` is still 42, and `mostly harmless` still says mostly harmless.

## Typing Variables
Most languages require that you specify the type of a variable when you *declare* it - that is, the first time you use it. This allows for the correct amount of memory to be allocated to store the variable and results in faster execution of the program. After the variable has been declared, the type is fixed and it is no longer necessary to specify it. Such languages are called statically typed. So in Java, for example, we would need to write the following:

```java
int meaning_of_life = 42
meaning_of_life = 7
```
if we wrote the following line later in the Java program it would produce an error because we have declared that the variable `meaning_of_life` is an integer not a string.

```java
meaning_of_life = "forty two"
```
Other languages, including Python, are dynamically typed. Space is allocated to store the variable as the program executes which increases flexibility but slows execution. So in python the following requires no type declaration and does not produce an error even though we have changed the value of the variable `meaning_of_life` from an integer to a string.

```python
meaning_of_life = 42
meaning_of_life = 7
meaning_of_life = "forty two"
```

Python does have an option called *type hinting* where you can choose to specify the type of a variable when you declare it.

```python
meaning_of_life: int = 42
planet_earth: str = "harmless"
meaning_of_life = 7
planet_earth = "mostly harmless"
```
Note that we only declare the type each variable first time we use them and we should no longer change a variable type.

### Conventions to be used in this course
The examples in the [SDD Course Specifications](https://educationstandards.nsw.edu.au/wps/wcm/connect/44325629-51c6-4330-8bf8-662d5cfbe5fb/software-design-development-course-specs.pdf?MOD=AJPERES&CVID=) appear to follow the convention that variables are only declared with a type when they are in classes (more on classes later). We will adopt this convention for both python and pseudocode scripts.

## Naming Variables
A reoccurring theme of this course will be the importance of good documentation. Probably not for the last time, let's remind ourselves of Martin Fowler's quote
> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”

Human readability is greatly improved by giving your variables meaningful names. Compare the following bits of code.
```python
# bad variable names
a = ["Bluey", "Terry", "Bernie"]
for n in a:
    print(n)

# good variable names
name_array = ["Bluey", "Terry", "Bernie"]
for name in name_array:
    print(name)
```
Both these scripts print each name in an array (more on arrays soon) and both are easily understood by computers, but the second is much easier to understand for humans.

### Keywords
Most programming languages have reserved words that can't be used as variable names called *keywords*. These are predefined, reserved words used in programming that have special meanings to the compiler/interpreter. For example if you were to try the following statement in Python
```python
class = "Year 11 SDD"
```
you would get the following error
```python
SyntaxError: invalid syntax
```

The keywords in Python are: `False, None, True, __peg_parser__, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`

### Camels, snakes and kebabs
Giving variables meaningful names often means choosing multiple-word identifiers. Another practice that improves the readability of your code is to follow the conventions of your language for multiple-word names. In Python the convention is to use `snake_case_names` where the words are separated by an underscore. In Java the convention is to use `camelCaseNames` where the first letter of each word except the first are capitalised. In COBOL the convention is to use `kebab-case-names`. If you don't follow the correct convention it isn't technically wrong, and it wont produce errors when you run your code, but is isn't good practice. What ever you do avoid `flatcasenames` because these are really hard to read.

### Conventions to be used in this course
The [SDD Course Specifications](https://educationstandards.nsw.edu.au/wps/wcm/connect/44325629-51c6-4330-8bf8-662d5cfbe5fb/software-design-development-course-specs.pdf?MOD=AJPERES&CVID=) don't specify a convention for pseudocode but the majority of the examples use camel case so we will adopt this convention for pseudocode. So to be clear, we prefer you to use snake case names in your python code and camel case names in your pseudocode.

## Task

Use the comments in the main.py script as a instructions to edit the code until it runs and passes the tests. Remember, you run the test by going to the shell tab (NOT the console tab) and typing `pytest` at the prompt. Then edit the code in the main.pseudo file. When you are finished, submit.
