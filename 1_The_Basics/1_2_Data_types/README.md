# Data Types

## computers ain't smart

Despite appearances, computers ain't very smart. They can only do what you tell them to do and only if they can do it by adding 1s and 0s. But they can add 1s and 0s very, very quickly and this allows them to do complex tasks much faster than you humans.

However we aren't generally interested in 1s and 0s, we are interested in more complex data types which must be turned into 1s and 0s by the software.

## bits and bytes
Data in computers is stored in memory as 'switches' that can be turned on (1) or off (0). So all data must be converted to a sequence of 0s and 1s and it is these sequences that are manipulated in computer operations. A single switch is called a **bit**, and can store 2^1 values, 0 or 1.

Computers usually manipulate collections of eight bits at a time called a **byte**. Bytes can store 2^8 values, for example the numbers from 0 to 255.

## data types

In this course we will recognise 4 data types:
* integers: usually written as `int`. These are whole numbers or counting numbers 1, 2, 3, -1, -42 etc. Traditionally programming languages have allocated 2 bytes of memory to an `int` meaning they can store whole numbers between -32,767 and +32,767.
* floating point or real numbers: usually written as `float`. These are decimal numbers such as 3.141593. Traditionally programming languages have allocated 4 bytes of memory to an `floating` so storing the number 42 as a float uses tice as much memory as storing it as an int.
* strings: usually written as `str`. These are letters or words (strings of letters) and can include most characters you can type on your keyboard. If a number is represented as a `string` then you can't perform mathematical operations on it unless you convert it back to an `int` or a `float`. Strings are usually allocated one byte per character. An [ASCII table](//http://www.asciitable.com/) is used to convert keyboard characters to numbers. In Python strings are surrounded by single or double quotes eg, 'this string' or "that string".
* boolean: usually written as `bool` can only take two values `true` or `false` which is stored as 1 or 0. The amount of storage allocated to a boolean is 1 bit. In python the first letter of a boolean must be a capital eg. `True` and `False`
 

### Python data types
Like most languages, Python recognises other data types which we will meet throughout the course. One we will come across frequently is `None` which is used to signify the absence of a value. In this exercise we will replace `None` with different data types.

## More on Comments and Docstrings

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”
― Martin Fowler

One of the main outcomes of this course is the ability to write well documented code, and comments are an important component of this. As you proceed through these introductory lessons we will continually increase your understanding of comments and how to use them. Today we will just point out the difference between simple comments and document strings, usually called docstrings. In upcoming lessons we will learn how and when to use them.

If you look at the `main.py` file you will see two types of non-executing comments. Simple comments which begin with `# ` and docstrings which are `"""surrounded by triple quotation marks"""`. As a rule, docstrings tell us about the code and are often used to automatically build the software's documentation. Simple comments are really memory aids and explain what we are doing and why.

## Task

Use the comments in the main.py script as a instructions to edit the code until it runs and passes the tests. Remember, you run the test by going to the shell tab (NOT the console tab) and typing `pytest` at the prompt. Then edit the code in the main.pseudo file. When you are finished, submit.