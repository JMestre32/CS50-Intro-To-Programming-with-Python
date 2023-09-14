# Libraries
Libraries are generally files of code that you/other people have written that you/they can use in your/their own programs. 

<h2><ins>Topics:</ins></h2>
<ul>
    <li>Modules</li>
    <li>import</li>

<h3><ins>Modules</ins></h3>
Python supports the idea of sharing code via <em>modules</em>.
A library that, typically, has one or more functions or other features built into it. The purpose of modules/libraries is for reusability (ie. modules can resolve the issue of using the same code over and over again)

When you install the python interpreter, you get a few modules with it. 

Different modules in Python:
<ul>
    <li>random</li>
    [Random Documention](https://docs.python.org/3/library/random.html)
    <li>statistic</li>
    [Statistic Documentation](https://docs.python.org/3/library/statistics.html) 
    
</ul>

<h3><ins>import</ins></h3>
How do you go about loading a module into your program so you can use the funtions in that module? We need <em>import</em>

Say for example, random.choice(seq), exists within the random module. (seq stands for a sequence or a list of elements) See how to handle this in the generate.py program.  

We would just have to type the following: import ``module-name``

<h3><ins>from</ins></h3>
from is another keyword in python that you can use when importing functions from a module, but it allows you to be more specific than import alone. (See generate.py)

Instead of importing an entire module we can simply import one function from a module like so: 

from ``module-name`` import ``module-function``
