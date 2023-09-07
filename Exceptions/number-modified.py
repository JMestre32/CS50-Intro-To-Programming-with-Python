def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            #We can pass, so we still catch the error, but we just keep 
            #prompting the user the same thing "What's x? "
            pass
        
main()

