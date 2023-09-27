# create a set
# employee = {'samuel', 'pius', 'gideon'} 

#add an item to a set
# employee.add('james')

# for emp in employee:
#     print(emp)

students = {1, 2, 'you', 3.0, True}
students2 = {'you', 'solomon'}

print(students)

# add two sets together, students & students2
students.update(students2)

# remove item from a set
students.remove('you')
students.discard(3.0)

for student in students:
    print(student)

