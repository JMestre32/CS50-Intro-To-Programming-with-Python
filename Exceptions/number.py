#Original code:
    # x = int(input("What's x? "))
    # print(f"x is {x}")

#Code with error handling, this is still considered lazy
    # try: 
    #     x = int(input("What's x? "))
    #     print(f"x is {x}")
    # except ValueError:
    #     print("x is not an integer")


#What this is saying is, if we see a value error (ie. if the user types 'cat')
#we would print "x is not an integer" instead of getting a valueError in the 
#terminal


#You should really only "try" lines of code that may raise an error like so:
    # try:
    #     x = int(input("What's x? "))
    # except ValueError:
    #     print("x is not an integer")

    # print(f"x is {x}")

#The code above introduces a new error called a NameError, the reason for 
#the nameError appearing boils down to order of operations. 
#Troubleshooting: 
#1. The input function seems fine, it always returns a string
#2. We are passing that string from input to the int function, it is likely
#   that the int function is the code that is creating a NameError

#Because the error is happening on the right of the equal sign, there is
#no value being copied to the left, the error is interrupting that whole
#process

#How do we solve this? Use else

#Python will 'try' to execute line 44
#If line 44 doesn't work, it'll throw an exception and print "x is not an integer"

#Otherwise, it'll execute line 48
try: 
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

