while True: #Purposely entering an infinite loop to validate input from the user
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")