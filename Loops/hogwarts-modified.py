#Trying to make a list of dictionaries. 
#So we will have a list and each element is itself a dictionary.

students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

    #None is a special keyword in python that indicates that that element within this
    #single dictionary element that is itself part of a list of dictionary elements
    #has no value
]

#In each dictionary in this list, there are 
#3 keys and 3 corresponding values. 

#How do we access these values? Like so: 

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")

