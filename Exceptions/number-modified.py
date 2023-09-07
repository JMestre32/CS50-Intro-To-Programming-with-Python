def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True: 
        try:
            return int(input(prompt))
        except ValueError:
            #We can pass, so we still catch the error, but we just keep 
            #prompting the user the same thing "What's x? "
            pass


#The change in prompting the user in main as opposed to in the get_int 
#function just makes our code more dynamic and reusable. It is still 
#functionally the same. 
main()

