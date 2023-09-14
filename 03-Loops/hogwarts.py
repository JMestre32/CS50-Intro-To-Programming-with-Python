    # students = ["Hermione", "Harry", "Ron"] #A list of length 3
    # houses =["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

    # for student in students: #This allows us to print the entire list without knowing the list length
    #     print(student)


#How this works is python intializes the student variable and assigns
#the string "Hermione" to student first then iterates over the list. 
#Once we hit "Ron" we have come to the end of the list and thus there
#are no more students to assign to the student variable. 


#An alternative approach, can be interpreted as getting the len of students
#which is 3, so simplified it is for i in range(3).

    # for i in range(len(students)):
    #     print(i, students[i])


#Exemplifying key-value pairs and python dictonaries

#Making dictionaries are different than lists, dictionaries use {}
#whereas lists use []


students = {"Hermione":"Gryffindor", 
            "Harry": "Gryffindor",
            "Ron":"Gryffindor",
            "Draco": "Slytherin"}

#List values are numeric and can be accessed that way. 
#Dictionaries allow you to use actual words. 
#The code below prints the houses of each student.  
    # print(students["Hermione"])
    # print(students["Harry"])
    # print(students["Ron"])
    # print(students["Draco"])


#This just prints the keys, how do we print the values?
    # for student in students:
    #     print(student)


for student in students:
    print(student, students[student], sep = ", ")

    #Again, you can think of this for loop as iterating through 
    #this dictionary as if it were using a number, in this case the 
    #number, typically titled 'i', is titled "student". 
    #student is a key, and it starts at 0. The value associated with the
    #key 0 is "Gryffindor". There are 4 keys within the student dictionary.
    #So, we are saying for as many keys as there are in the students dictionary
    #print the key and it's value. 