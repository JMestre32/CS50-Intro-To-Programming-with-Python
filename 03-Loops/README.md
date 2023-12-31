# Loops

<h2> Topic </h2>
<ul>
    <li> While loops </li>
    <li> For loops </li>
    <li> Input validation </li>
    <li> Lists </li>
    <li> dict </li>
</ul>

<h3> While loops </h3>

While loops allow us to check a condition first and if the condition is met, our program executes accordingly. The conditional flowchart below of the first iteration of our program cat.py shows how a while loop works: <br>

<img width="194" alt="while-loops" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/63fa0ba4-3cb6-4caa-b063-6a4653b4246b">


The synax of a while loop is as follows:

while ...:
    do stuff
    increment/decrement


<h3> For loops </h3>
For loops allow us to iterate over a list of items. 
For loops are oftentimes shorter and more concise than while loops.

When using a for loop, we can use the range function to automate the entire process instead of manually typing the range using individual numbers. Like so:

for i in range(3):
    print("meow")

There is a "pythonic" solution that uses an underscore '_'. This is exemplified in the cat.py program. It's a minor improvement. 

<h3> Input validation </h3>
When you want the user to input something a specific way, you can use
this method: 

Enter an infinite loop and break only when your condition is met

while True:
    n = int(input("What's x?"))
    if n > 0:
        break


<h3> Lists </h3>

A list is denoted by square brackets [] and its contents are separated by commas. 

To access list elements we use the list name and [n] where n is a number. This is exemplified in the hogwarts.py program. 

There is a function <strong> len </strong> that allows you to find the length of a list. This allows you to iterate through a list using numbers, if that is how you prefer going through a list. 

Another way to go through a list and print its elements is just by going through the list and assigning each value to a variable and printing that variable until there are no more values in the list. 

Both of these methods are shown in the hogwarts.py program. 


<h3> dict </h3>
dict's allow you to associate something with something else

To programmers this is known as a key-value pair. 

Dictionaries use curly brackets {}

Dictionaries are a bit harder to digest, but at the end of the day remember one thing. Dictionaries are just a collection of values that allow you to associate keys with values. This is exemplified more in the
hogwarts-modified.py program. A visual aid is also given below: <br>

<img width="477" alt="dicts" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/51fd242e-1bc7-4e33-8c90-29ef1e751952">
