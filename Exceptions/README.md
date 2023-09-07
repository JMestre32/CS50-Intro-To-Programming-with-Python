# Exceptions

<h2> Topics </h2>
<ul>
    <li> What are exceptions </li>
    <li> SyntaxError </ins>
    <li> ValueError (try/except) </ins>
    <li> Catching everything (BAD PRACTICE) </ins>
</ul>

<h3><ins> What are exceptions? </ins> </h3> 

Exceptions are when there is something wrong with your code. 
If something "exceptional" happens in a program, it means that something
unexpected, like an error, is encountered during the program.

<h3><ins> SyntaxError </ins> <h3>

A SyntaxError is an error in your code that is entirely on you to fix.

However, there are different types of errors (ie. runtime errors) that we as <strong> programmers </strong> must account for. We must code 
<em> defensively </em>.

<h3><ins> ValueError (try/except) </ins> <h3>
A valueError occurs when the user gives input that is unexpected. 
This is exemplified best in the number.py program. try/except is quite literal
we try to do something, and we throw an exception in the event that we get a 
valueError. 

<h3><ins> Catching everything (BAD PRACTICE)</ins></h3>
In python, there is a way to catch all errors. However, this is considered lazy and bad practice. Instead, we should account for any errors that could happen and program accordingly. 