x = int(input("What's x? "))
y = int(input("What's y? "))

#New syntax! If statement, this is referred to as a boolean expression
#notice we do NOT need parenthesis (x < y)
    # if x < y:
    #     print("x is less than y")
    # if x > y:
    #     print("x is greater than y")
    # if x == y:
    #     print("x is equal to y")

#However, there are too many if statements, we can make this more efficient

#New syntax! elif, this asks a question that takes into account if the
#previous question was true or false. 


if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

#The modification we just made might seem minimal, but when we work
#on a larger scale, optimizing code is vital. This is exemplified in the 
#conditional flow charts in the README.