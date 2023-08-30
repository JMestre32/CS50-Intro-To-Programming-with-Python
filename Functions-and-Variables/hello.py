#Notice the '=' sign. That is the assignment operator.
#Also notice that there is a ' ' space after the ?, this is for formatting reasons.
#We don't want the user's input to be typed right next to the ? like so "?Jacob"

# name = input("What's your name? ")  

#The '+' sign concatenates the string and user input. 
#  print("hello, " + name) 

#You can also use a ',' to print the same thing. Like so:
#  print("hello,", name)

#In this case, we don't need to add an extra space in front of the first string "hello,". 
#The comma does it for us. 


#Let's say we are printing twice and we want the strings to print on the same line
#here is how we would do such a thing by altering the end value.
#This is possible AFTER looking at the python documentation

#  print("hello, ", end="")
#  print(name)


#This shows the sep and end value in action. 
#print("hello, ", name, sep="???", end="hi!")


#This just shows how to print ACTUAL quotes
#  print('hey, "friend"')
#  print("hey, \"backslash\"")

#String documentation allows us to modify the user's input like so
#Removes whitespace
#  name = name.strip()
#Capitalizes first character of str
#  name = name.capitalize()

#You can chain methods like so, this strips any leading or trailing whitespace in the string
#AND capitilizes the first letter of each word in the stringm 
# name = name.strip().title()


#The most modern way to solve the problem of printing both the string
#and the user-given value on the same line. 

#One, very last change is that we can make ALL of these adjustments on TWO lines. 

name = input("What's your name? ").strip().title()

print(f"hello, {name}")

