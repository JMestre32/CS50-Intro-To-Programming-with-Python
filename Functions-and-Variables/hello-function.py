#How can we modify hello.py and make it better using functions?

def main():
    name = input ("What's your name? ")
    hello()
    hello(name)

#You can set a parameter value manually and the function will use that
#value in the invent that the user doesn't provide a value. Like this:

def hello(to = "world"):
    print("Hello,", to)

main()