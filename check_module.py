#check_module
"""A file is a module that groups related functions, data and classes.
Everything what is related with variable students was transferred from the file self_check1.py, so
this file we can treat as a module, because it contains data = students"""
from self_check1 import students as st

print(f'Student: {st}')

"""
out:
students=('Sue', [89, 94, 85])
name: Sue
grades=[89, 94, 85]
Student: ('Sue', [89, 94, 85])
"""