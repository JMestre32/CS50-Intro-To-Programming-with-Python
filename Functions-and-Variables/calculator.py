#Without type conversion, adding user input just concatenates the
#x and y (ie. x = 1, y = 2, z = 12). You must convert the str values
#to int values. 

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)