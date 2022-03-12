#self_check1.py
"""Pack a student touple with the name 'Sue' and the list [89,94,85],
display the touple, then unpack it into variables name and grades, and display their values"""

students = ('Sue', [89,94,85])

#display touple
print(f'students={students}')

#unpack touple into variables name and grades
name, grades = students

#display values of unpacked variables
print(f'name: {name}')
print(f'grades={grades}')

"""
out:
students=('Sue', [89, 94, 85])
name: Sue
grades=[89, 94, 85]
"""