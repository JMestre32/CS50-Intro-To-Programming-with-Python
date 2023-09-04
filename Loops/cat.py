#How can we print a string multiple times using loops? 

#While loop approach

    # i = 0
    # while i < 3:
    #     print("meow")
    #     i += 1

#Sidenote, if you accidentally make a loop that goes on infinitely
# Ctrl + C terminates the program. 

#Another sidenote, we cannot increment or decrement like we do in C++ using '++' and '--'. 
#The closest we can get to it is in line 8 += and -=. 

#For loop approach
    # for i in [0, 1, 2]:
    #     print("meow")

#Prediction: this may not be the best way because we have to manually type 0, 1, 2. We
#should figure out a case where we can automate this. 

    # for i in range(3):
    #     print("meow")


#Pythonic solution, replacing the 'i' variable with an '_'.
#This implies that we are iterating a variable, but it's sole purpose is to push the 
#for loop forward.

for _ in range(3):
    print("meow")


#SUPER pythonic solution:
print("meow\n" *3, end="")
#Changing the default value of end to "" resolves the issue of having an extra newline
#at the end of the output. 