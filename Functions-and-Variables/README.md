# Functions and Variables

<h2>Topics:</h2>
<ul>
    <li>Functions </li>
    <li> Bugs </li>
    <li> Variables </li>
    <li> Comments </li>
    <li> Strings </li>
    <li> Integers </li>
    <li> Floats </li>
    <li> Functions </li>
    <li> Interactive Mode </li>
</ul>
<h3>Functions</h3> are like an action or verb that let you do something in the program. Most programming languages come with built-in functions that allow programmers to "do things". <br/>

We see in the hello.py file that print is a function that allows us to print words to the terminal. 

You can <strong> nest </strong> functions like so:

x = int(input("What's x? "))


<h3> Bugs </h3>
Errors in your code are called <strong>bugs</strong>. Throughout this course, we will come across several bugs. Do not worry! By the end of this course, we will be equipped with the necessary tools to debug properly. 


<h3>Variables</h3> allow users to assign values to things. This is seen in hello.py through the "name" variable. 

<h3>Comments</h3> allow users to inform readers what their code does or perhaps write pseudocode to help in figuring out how to get code to work. Compilers ignore comments. 


[Python Documentation](https://docs.python.org)

One of the best things to do when learning a programming language is to get familiar with its documentation. The link provided below is the python documentation for the print function. <br/>

[Print Documentation](https://docs.python.org/3/library/functions.html?highlight=print#print)

Try not to feel overwhelmed when you don't understand what you're looking at

<h3> print(*objects, sep=' ', end='\n', file=None, flush=False) </h3>

Let's break this down.

The name of the function: print

Anything inside the parenthesis: potential arguments/parameters

<em>SIDENOTE: the difference between parameters and arguments. <br/>
When talking about what you CAN pass into a function you are talking about PARAMETERS. <br/>
When you actually DO pass things into a function, those things are called ARGUMENTS. <br/> </em>


More specifically: *objects implies we can take any number of arguments in the print function

sep=' ': The default value of separator is a blank space. This is exemplified when using the ',' in hello.py

end='\n\: '\n' means newline, this means this function will create a newline when it ends


<h3> Strings (Built-in functionality) </h3>

[String Documentation](https://docs.python.org/3/library/string.html)

The string documentation helps with printing and formatting user input correctly. 
This is exemplified in the code below:

name = name.strip()

What strip does is remove whitespace from the str input 

<h3> Integers </h3>
An integer is any whole number (ie. -1, 0, 3, -2). When it comes to int's, there are no decimals. 

Integers support the following operators: +, -, *, /, %

<h3> Floats </h3>
Floating point values have decimals.

When we want to round a float, we use the round function

According to the python documentation the round syntax is as follows:

<h3> round(number[, ndigits]) </h3>

round takes a number, and optionally (indicated by the
',' symbol) the number of digits we want the round function to round to. If it isn't specifed, round just rounds to the nearest integer.

Floats are limited to a specific amount of decimal points

<h3> Functions </h3>


<h3> Interactive Mode </h3>

You can run python in the terminal by typing 'python' and >>> will appear.
There you can run code instead of making a new .py file