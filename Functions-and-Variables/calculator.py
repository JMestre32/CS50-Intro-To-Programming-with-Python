#Without type conversion, adding user input just concatenates the
#x and y (ie. x = 1, y = 2, z = 12). You must convert the str values
#to int values. 


#The round 
x = float(input("What's x? "))
y = float(input("What's y? "))


z = round(x + y, 0)

#There is a way to include commas in an integer using
#the format string (f)

print(f"{z:,}") 
#The colon : and , output integers like 1,000