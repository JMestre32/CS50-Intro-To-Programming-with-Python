def main():
    hello("world")
    goodbye("world")
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


#How might I go about compiling functions such as these ones and
#turning them into a library?

#See say-modified.py

#Be sure NOT to include a lone main() call when making your own library
#The entire sayings.py program will run if you do!
#Instead conditionally call main:

if __name__ == "__main__":
    main()




#__name__ is a special variable in python whose value is set 
#by python to be "main" when you run this file from the command line
#using the command: python sayings.py

#__name__ is not going to be set to "main" instead it will be set to 
#something else, technically the name of the module when you, instead, 
#import the module like in say-modified.py

#When you are IMPORTING a file, like in say-modified.py, and not 
#running saying.py directly in the command line, main() will not get called. 