import sys
#Generally speaking, it's nice to keep code that does all of your
#error handling separate from the code that you actually care about.

#We'd like to NOT hide the code we care about in an else statement

# #Check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) >2:
#     print("Too many arguments")

# #Print name tags
# print("hello, my name is", sys.argv[1])

#The format above, however, introduces a NameError/IndexError. 

#The format below exits prematurely if the program cannot proceed. 
# if len(sys.argv) <2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) >2:
#     sys.exit("Too many argument")

#Now it is safe to assume there is an item in sys.argv[1] and only there
# print("hello, my name is", sys.argv[1])

#We now want multiple values at the prompt,

if len(sys.argv) <2:
    sys.exit("Too few arguments")

#To do so, we loop through sys.argv and print the arguments given
#to the program

#Remember that argv is a list of things the user gives us, so we
#we can treat it as such.
for arg in sys.argv[1:]:
    print("hello, my name is", arg)