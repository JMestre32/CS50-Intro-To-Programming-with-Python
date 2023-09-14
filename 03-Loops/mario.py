#One of the nice things about functions is that they allow us to create 
#abstractions. Abstractions are simplifications of a potentially
#more complicated idea. 

def main():
    print_square(3)

def print_square(size):
    #How might we print a square? (rows AND columns)
    #Think about how a typewriter functions
    for _ in range(size):
        print_row(size)


#This print_row function is an example of abstraction.
#We are taking a complicated idea like the inner machinations of 
#printing a row and instead making a function for it that helps
#us simplify the act. 
def print_row(row_width):
    print("#" * row_width)

main()