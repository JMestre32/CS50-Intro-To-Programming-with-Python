import sys

# print("hello, my name is", sys.argv[1])

#What the above line does is expect the user to pass anything as a 
#parameter to the function through the command line. 

#The command would look something like:
#   python3 name.py berry

#Which would output:  hello, my name is berry

#This begs the question, what is in sys.argv[0]?

#The answer is the NAME OF THE PROGRAM. So in the command above
#sys.argv[0] is name.py

#Say for example you don't provide a name, you would run into an
#IndexError. So, let's handle that.

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

#However! We can be even more defensive like so:

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) >2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

#We don't have to handle exceptions if we can be a little smarter 
#about it and just check for the things we're worried about using
#conditionals.