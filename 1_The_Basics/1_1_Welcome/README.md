# Welcome

Ready for your first program? For this exercise you will just be editing an existing program to print out a message. The task is trivial and its main purpose is to introduce you to the **repl.it** development environment. There is a lot to take in at first but it will soon be second nature. 

An important concept in modern software development is *test driven development* (TDD). With TDD you actually write tests for your code before you write the code. This may seem odd but software can be very complicated and TDD is a very powerful tool for helping isolate bugs in your software.

In the early stages of the course the tests will be written for you and your task will be to fix the code until it passes the tests. The *docstrings*, special comments in the code that don't get executed, will help explain the task. Later you will be encouraged to write your own docstrings and tests. In **repl.it** you execute the code by pressing the run button on the top menu bar, or the debug button on the left menu (we will get to debugging soon). This will show you the output of the code in the console window.

You can run the test by going to the shell tab (NOT the console tab) and typing `pytest` at the prompt. 
```
/ $ pytest
```
This will give you a green `passed` message if your code passes all the tests or it will give you a whole lot of ugly coloured information that lets you work out where you went wrong. At first you might find this information a bit difficult to decipher but we will guide you through it and soon you will be a pro at finding your mistakes.

## The python code

If you open the `main.py` script and press `run` you will see that it prints out the message 
```
look at me I am coding
``` 
in the console. If you go to the shell and run `pytest` you will get an error. This is because the test for this code is that it must print out a message but it can't be `look at me I am coding`, in other words to pass the test you need to change the message. This is explained in the *docstring*. Read through the main.py code and see if you can work out how to change the message. Run the code to see your output and then when you think you have it run pytest again.

Keep editing your code until it passes the test.

## The dreaded pseudocode

One unfortunate aspect of the way the SDD curriculum has been designed is that because there is no language specified, the authors of the syllabus have invented one that they can use for examination purposes. Welcome to the hell that is **pseudocode**! Now it is important to know that programmers do use pseudocode which, when used in the real world, is just designing their programs with code-style plain English so they can get their ideas down. In the world of this SDD course pseudocode is much more structured and has a strict syntax that kind of defeats the purpose of pseudocode in the first place. But it does make it easier to examine you so we need to learn to write pseudocode the SDD way. So your second task is to open the main.pseudo file and see if you can edit that to output the same message that your python code outputs (not that it outputs any message because pseudocode can't be executed).

When your code has passed the tests and you have edited the pseudocode submit your work and move on to the next exercise.
