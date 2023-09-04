# Conditionals

<h2> Topics: </h2>
<ul>
    <li> Conditional Operators</li>
    <li> if/elif Statements </li>
    <li> Else statement </li>
    <li> Or operator </li>
    <li> And operator </li>
    <li> Modulo operator </li>
    <li> Match </li>
</ul>

<h3> Conditional Operators </h3>
<ul>
<li> &gt; Greater than <br> </li>
<li> &lt;= Greater than or equal to <br> </li>
<li> < Less than <br> </li>
<li> <= Less than or equal to <br> </li>
<li> == Equality, comparing the values on the left and right <br> </li>
<li> != Not equal to <br> </li>
</ul>

<h3> if/elif Statements </li> </h3>

Programmers have the power to determine how they want a program to execute given certain circumstances using if/elif statements. 

However, a big thing with these statements is optimization and conditional flowcharts. As exemplified in compare.py, using elif statements answers questions much earlier in a program and thus speeds up execution time. Take a look at the two conditional flowcharts: 

Only if statements: <br>
<img width="161" alt="only-if-statements" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/22fbe98d-2084-47b7-b585-489f3ddba34f">

elif statements: <br>
<img width="341" alt="elif-statements" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/e617a4b1-0a58-42ee-b543-860c9ed85a1e">

<!-- Quick note:
I was able to put screenshots in the github repository by 
1. first adding them to a folder
2. Going to issues in github repo
3. Clicking 'New issue'
4. Dragging my image into the write textbox
5. Copying the code that github generates
6. Pasting it here -->

<h3> Else statements </h3>
An else statement is the final statement, it is what the program resorts to if all if and elif statements are exhausted. Adding else statements make our compare.py program the most efficient. That is exemplified here: <br>

<img width="379" alt="else-statements" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/e219334d-07ee-4a44-a271-2067cde27b91">


<h3> Or operator </h3>
Or operators (||) can help you choose between two options in an if-statement like so:

if x &gt; y or x &lt; y:
    print("x is not equal to y)

This effectively shortens our code, but it is not optimized. Refer to compare.py to see the most efficient code. 

<h3> Modulo operator </h3>

The modulo operator '%' returns the remainder after dividing two numbers:

4 % 3 = 1, 1 % 1 = 0, etc. 

<h3> Match </h3>

Match gives programmers the ability to match a variable to a specific case and execute accordingly. It's sort of like an if statement? In the event that a variable does not match anything, one could use an underscore like so: 

match x:
    case _:
    print("Not accounted for")