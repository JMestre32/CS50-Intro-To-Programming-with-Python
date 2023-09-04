#How can we modify hello.py and make it better using functions?

#You can set a parameter value manually and the function will use that
#value in the invent that the user doesn't provide a value. Like this:

def hello(to = "world"):
    print("Hello,", to)

hello()

name = input("What's your name? ")

hello(name)