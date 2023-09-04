def main():
    x = int(input("What's x "))
    print("x squared is", square(x))

#Return is exemplified here, we must return a value in hopes for our program
#to function the way we'd like.
def square(n):
    return n * n

    #Another way to do this is return n ** 2
    #or pow function return pow(n, 2)


    
    
main()