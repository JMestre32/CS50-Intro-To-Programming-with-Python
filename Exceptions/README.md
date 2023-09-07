# Exceptions

<h2><ins> Topics </ins> </h2>
<ul>
    <li> What are exceptions </li>
    <li> SyntaxError </li>
    <li> ValueError (try/except) </li>
    <li> Catching everything (BAD PRACTICE) </li>
    <li> NameError </li>
</ul>

<h3><ins> What are exceptions? </ins> </h3> 

Exceptions are when there is something wrong with your code. 
If something "exceptional" happens in a program, it means that something
unexpected, like an error, is encountered during the program.

<h3><ins> SyntaxError </ins> </h3>

A SyntaxError is an error in your code that is entirely on you to fix.

However, there are different types of errors (ie. runtime errors) that we as <strong> programmers </strong> must account for. We must code 
<em> defensively </em>.

<h3><ins> ValueError (try/except) </ins> </h3>
A valueError occurs when the user gives input that is unexpected. 
This is exemplified best in the number.py program. try/except is quite literal
we try to do something, and we throw an exception in the event that we get a 
valueError. 

There is an additional feature of the try/except syntax, it supports <strong> else </strong>. It works similar to if/elif/else statements. This is exemplified, again, in number.py.

<h3><ins> Catching everything (BAD PRACTICE)</ins></h3>
In python, there is a way to catch all errors. However, this is considered lazy and bad practice. Instead, we should account for any errors that could happen and program accordingly. 

<ins><em>SIDENOTE: </ins>  David Malan notes that if you read the Python documentation, you will notice that Python isn't great about letting you know proactively what kinds of errors can be raised in your programs. However, you get better at figuring out what errors can happen with practice.
</em>

<h3><ins> NameError </ins> </h3>
NameError usually refers to your code, it typically means that you're doing something with your variable that you shouldn't.

For example, in number.py, look at the third version of the program that produces a name error. In the event that a user inputs something that is NOT a number, something like 'cat', passing 'cat' as an argument to the int conversion function makes the int function raise a ValueError. Notice that the last line is not indented, no matter what it will execute. So, when that line executes it raises a NameError, because it is not defined at the moment. 

Introducing an else to the code makes the last line and the rest of the code mutually exclusive. The else is ONLY used if we try the second line of code AND succeed. 