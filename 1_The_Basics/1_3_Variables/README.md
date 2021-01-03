# Variables and Literals

## Background stuff

At the most fundamental level, a computer program just stores and manipulates data or information. In the previous lesson we looked at 4 data types: `int, str, float` and `bool`. The data types can be stored as *literals* or *variables*.

A literal is a constant value. The `int 42` is the number **42**. The `str 'mostly harmless'` is the phrase **mostly harmless**. The characters literally represent themselves.

A variable is a name we give to a value and this value can change throughout the program - it varies!

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

but the value of `42` is still 42.

## Typing
Most languages require that you specify the type of a variable when you *declare* it - that is, the first time you use it. This allows for the correct amount of memory to be allocated to store the variable and results in faster execution. After the variable has been declared, the type is fixed and it is no longer necessary to specify it. Such languages are called statically typed. So in Java for example we would need to write the following:

```java
int meaning_of_life = 42
meaning_of_life = 7
```
if we wrote the following line later in the Java program it would produce an error because we have declared that the variable `meaning_of_life` is an integer not a string.

```java
meaning_of_life = "forty two"
```
Other languages, including Python, are dynamically typed. Space is allocated to store the variable as the program executes which increases flexibility but slows execution. So in python the following would be legal and not produce any errors.

```python
meaning_of_life = 42
meaning_of_life = 7
meaning_of_life = "forty two"
```

Python has an option called type hinting where you can choose to specify the type of a variable. Because this is good practice, makes the code more readable and is in the spirit of the SDD curriculum we will adopt this practice. With type hinting our Python script would be

```python
meaning_of_life: int = 42
planet_earth: str = "harmless"
meaning_of_life = 7
planet_earth = "mostly harmless"
```
Note that we only declare the type each variable first time we use t and we should no longer change a variables type.

## Task

What youse gotta do
