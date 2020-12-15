# Data Types

## computers aint smart

Despite appearances, computers aint very smart. They can only do what you tell them and only if they can do it by adding 1s and 0s. But they can add 1s and 0s very, very quickly and this allows them to do complex tasks much faster than you or I (especially you).

But we aren't generally interested in 1s and 0s, we are interested in more complex data types which must be turned into 1s and 0s by the software.

## bits and bytes
Data in computers is stored in memory as 'switches' that can be turned on (1) or off (0). So all data must be converted to a sequence of 0s and 1s and it is these sequences that are manipulated in computer operations. A single switch is called a **bit**, and can store 2<sup>1</sup> values, 0 or 1.

Computers usually manipulate collections of eight bits at a time called a **byte**. Bytes can store 2<sup>8</sup> values, for example the numbers from 0 to 255.

## data types

In this course we will recognise 4 data types:
* integers: usually written as `int`. These are whole numbers or counting numbers 1, 2, 3, -1, -42 etc. Traditionally programming languages have allocated 2 bytes of memory to an `int` meaning they can store whole numbers between -32,767 and +32,767.
* floating point or real numbers: usually written as `float`. These are decimal numbers such as 3.141593. Traditionally programming languages have allocated 4 bytes of memory to an `floating` so storing the number 42 as a float uses tice as much memory as storing it as an int.
* strings: usually written as `str`. These are letters or words (strings of letters) and can include most characters you can type on your keyboard. If a number is represented as a `string` then you can't perform mathematical operations on it unless you convert it back to an `int` or a `float`. Strings are usually allocated one byte per character. An [ASCII table](//http://www.asciitable.com/) is used to convert keyboard characters to numbers. In Python strings are surrounded by single or double quotes eg, 'this string' or "that string".
* boolean: usually written as `bool` can only take two values `true` or `false` which is stored as 1 or 0. The amount of storage allocated to a boolean is 1 bit. In python the first letter of a boolean must be a capital eg. `true` and `False`
 

### Python data types
Like most languages, Python recognises other data types which we will meet throughout the course. One we will come across frequently is `None` which is used to signify the absence of a value. In this exercise we will replace `None` with different data types.
