def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's x? "))
        if n > 0:
            return n

def meow(n=1):
    for _ in range(n):
        print("meow")

main()