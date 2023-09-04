# Loops

<h2> Topic </h2>
<ul>
    <li> While loops </li>
    <li> For loops </li>
    <li> Input validation </li>
    <li> Lists </li>
</ul>

<h3> While loops </h3>

While loops allow us to check a condition first and if the condition is met, our program executes accordingly. The conditional flowchart below of the first iteration of our program cat.py shows how a while loop works: <br>

<img width="194" alt="while-loops" src="https://github.com/JMestre32/CS50-Intro-To-Programming-with-Python/assets/114640505/95d05d4e-889b-4892-84bc-9afa738f19b4"> <br>

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