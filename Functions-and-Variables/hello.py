#Notice the '=' sign. That is the assignment operator.
#Also notice that there is a ' ' space after the ?, this is for formatting reasons.
#We don't want the user's input to be typed right next to the ? like so "?Jacob"

name = input("What's your name? ")  

#The '+' sign concatenates the string and user input. 
print("hello, " + name) 

#You can also use a ',' to print the same thing. Like so:
print("hello,", name)

#In this case, we don't need to add an extra space in front of the first string "hello,". 
#The comma does it for us. 


#Let's say we are printing twice and we want the strings to print on the same line
#here is how we would do such a thing by altering the end value.
#This is possible AFTER looking at the python documentation

print("hello, ", end="")
print(name)