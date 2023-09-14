#The line below imports the entire random module
import random

#As of right now, we have to follow the syntax of
#<module-name>.<function-name>(parameters...) because we used import
# print(random.choice(['heads', 'tails']))

#HOWEVER, if we were to do the following we can just call choice:
#from random import choice

print(random.choice(["head", "tails"]))

#New function from the random module 
#random.randint(a,b) where a and b are the range of numbers that the function
#can randomly select from

number = random.randint(1,10)

print(number)


#Another function from random
#random.shuffle(x) that takes in a list of values and shuffles the list up

cards = ["jack", "queen", "king"]

#The function shuffles the argument in place, it shuffles the list itself
random.shuffle(cards)

for card in cards:
    print(card)

