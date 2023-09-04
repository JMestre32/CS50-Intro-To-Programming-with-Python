students = ["Hermione", "Harry", "Ron"] #A list of length 3

for student in students: #This allows us to print the entire list without knowing the list length
    print(student)


#How this works is python intializes the student variable and assigns
#the string "Hermione" to student first then iterates over the list. 
#Once we hit "Ron" we have come to the end of the list and thus there
#are no more students to assign to the student variable. 


#An alternative approach, can be interpreted as getting the len of students
#which is 3, so simplified it is for i in range(3).

for i in range(len(students)):
    print(i, students[i])