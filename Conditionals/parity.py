def main():
    x = int(input("What's x? "))
    if is_even(x): #When writing this line is_even() did not exist, but we knew what type of data we wanted it to return
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 ==0:
    #     return True #Boolean true! It has to be uppercase
    # else:
    #     return False

    #The above code can be condensed into one line:
        # return True if n % 2 == 0 else False

    #We can do even better:
    return n % 2 == 0

main()