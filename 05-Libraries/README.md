# Libraries
Libraries are generally files of code that you/other people have written that you/they can use in your/their own programs. 

<h2><ins>Topics:</ins></h2>
<ul>
    <li>Modules</li>
    <li>import</li>
    <li>from</li>
    <li>command-Line Arguments</li>
    <li>sys</li>
    <li>Slices (of lists)</li>
    <li>Packages</li>

<h3><ins>Modules</ins></h3>
Python supports the idea of sharing code via <em>modules</em>.
A library that, typically, has one or more functions or other features built into it. The purpose of modules/libraries is for reusability (ie. modules can resolve the issue of using the same code over and over again)

When you install the python interpreter, you get a few modules with it. 

Different modules in Python:
<ul>
    <li>random</li>
    used in generate.py
</ul>

[Random Documention](https://docs.python.org/3/library/random.html)
<ul>
    <li>statistic</li>
    used in average.py
</ul>

[Statistic Documentation](https://docs.python.org/3/library/statistics.html) 
<ul>
    <li>sys</li>
    short for system
    contains a whole lot of functionality that pertains to the system and commands typed by the user
    used in name.py
</ul>

[Sys Documentation](https://docs.python.org/3/library/sys.html)






<h3><ins>import</ins></h3>
How do you go about loading a module into your program so you can use the funtions in that module? We need <em>import</em>

Say for example, random.choice(seq), exists within the random module. (seq stands for a sequence or a list of elements) See how to handle this in the generate.py program.  

We would just have to type the following: import ``module-name``

<h3><ins>from</ins></h3>
from is another keyword in python that you can use when importing functions from a module, but it allows you to be more specific than import alone. (See generate.py)

Instead of importing an entire module we can simply import one function from a module like so: 

from ``module-name`` import ``module-function``


<h3><ins>command-line arguments</ins></h3>

Command-line arguments allow users to provide input not when prompted by the command-line but when you are executing the program at the command-line.

Up until now we have ONLY called programs like so:
python hello.py

command-line arguments change this up a little (exemplified in name.py)

Why should we use command-line arguments? They aren't "user-friendly".

As we delve into programming with python and programming in general. You will become more comfortable with using command-line arguments as opposed to being prompted during a program's runtime. It tends to make you faster and more productive. 

Instead of manually typing input over and over again, you can just pass the program the same command over and over again (which is faster). 

<h3><ins>sys</ins></h3>

As previously stated, sys (short for system) provides a bunch of functionality that has to do with the system and the users input. 

There exists a variable that "magically" exists for you called 'argv'. It stands for argument vector, which is a fancy way of describing ``the list of all of the words that the human typed in at the prompt before they hit enter``. 

All of these arguments are provided to you via python in a variable called sys.argv 

Similar to the C programming language, sys.argv[0] is the program name and anything after that are parameters the program expects the user to provide. 

All of this is exemplified in ``name.py`` and ``name-modified.py``

<h3><ins>slices(of lists)</ins></h3>

Slices are subsets of lists or data sets. 

In python it is relatively easy to get a slice of a list. You can simply do this:

<code>
for arg in sys.argv[1:]
</code>

What this does is loop through a 'slice' of the list and loop through the rest of the list. Effectively, this omits the first element of argv, the program name, and loops through arguments we actually pass to the program. 

You can also slice from the end of a list using negative values like so:

<code>
for arg in sys.argv[1:-1]
</code>

This code removes the last element passed into the program. 


<h3><ins>Packages</ins></h3>

A package is a third-party library that you can install on your own device that gives you access to even more functionality. 

You can access these packages at [PyPi](https://pypi.org)

Fun lil package: [cowsay](phttps://pypi.org/project/cowsay/)
What this package does is allow the user to make a cow say something. 

<em>How do you actually get the package into your system? </em>
 
These days a lot of languages, python among them, have these things called package managers. <ins>pip</ins> is a program that generally comes with python itself nowadays that allows you to install packages onto your own devices by running a command. Then BOOM you now have access to the package.

By running the command in the terminal:

``pip install cowsay``

You will <em>hopefully</em> see the message:
"Successfully installed cowsay

In my case, I had to run the command:

``pip3 install cowsay``

cowsay's capabiilities are exemplified in ``say.py``