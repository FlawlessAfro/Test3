
students = ['Henrik Pettersen', 'Tore Sporet', 'Jan Helgerud', 'Petter Solbakken', 'Dennis Yeboah' ]

print(students[2])

print(students[2][0])

#change the name of the 3rd
#  student to ole

#students = students.remove('Jan Helgerud')
students.insert(2, 'Ole Nordmann')

print(students)

students.insert(len(students), 'Jan Helgerud')

print(students)

students.insert(4, 'Monty Python')

print(len(students))

students.remove('Ole Nordmann')

print(len(students))

print(students.index('Monty Python'))

print(students[0:3])

students_reverse = students[::-1]

print(students)
print(students_reverse)

students_even = students[::2]
print(students_even)

students_odd = students[1::2]
print(students_odd)