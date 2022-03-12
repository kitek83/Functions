#arbitrary_arguments.py
"""Function with default parameter values, function with keys arguments, function with arbitrary argument lists
(iterable operators). Passing iterable's individual elements as a function arguements = *iterable"""
import numpy as np
import pandas as pd

#1.Function with default parameter values.
def rectangle(length=2, width=3):
    return length * width

#function's call without arguments, so Python uses deafult parameter values
print(f'rectangle()={rectangle()}')

#calle the function with argument assigned to length, sp Python will ignore default value
print(f'rectangle(10)={rectangle(10)}')

#call the function with 2 arguements assignet to function rectangle paramenters
print(f'rectangle(10,4)={rectangle(10,4)}')

#2.When calling the function, you cane use keyword arguments to pass arguments in any order
def rectangle2(width,length):
    return width * length

#keyword arument in function call has the form parameter name = value
print(f'rectangle2(width=20, length=2)={rectangle2(width=20,length=2)}')
#the same result is for the call with only passed 2 arguments
print(f'rectangle2(20,2)={rectangle2(20,2)}')

#3.Function with arbitrary argument lists. *args indicates that function can receive any number of arguments
print()
def average(*args):
    return sum(args) / len(args)      #*args is a touple. Instead of *args, we cam use name *operator

print(f'average(4,5,5,6,7,8)={average(4,5,5,6,7,8):.2f}')

#Instead of *args, we cam use name *iterable operator
grades = [88,75,96,55,83,90]
print(f'grades={grades}')
print(f'average(*grades)={average(*grades):.2f}')
"""out:
average(4,5,5,6,7,8)=5.83
grades=[88, 75, 96, 55, 83, 90]
average(*grades)=81.17
"""

# *operator = ndarray
print()
ndarray1 = np.array(grades).reshape(2,3)
print(f'ndarray1={ndarray1}')
#passing ndarray1 as an arbitrary argument
print(f'average(*ndarray1)={average(*ndarray1)}')  #showing the average of values in columns for 2 rows
"""out:
average(*ndarray1)=[71.5 79.  93. ]
"""
print('nd.array2 - without reshape attribute')
ndarray2 = np.array(grades)
print(f'ndarray2={ndarray2}')
print(f'average(*ndarray2)={average(*ndarray2):.2f}')  #calculates the average fo 1 row
#out: average(*ndarray2)=81.17

print()

#*operator = pd.Series([])
print(f'grades={grades}')
pd_Series = pd.Series(grades)
print(f'pd_Series=\n{pd_Series}')
print(f'average(*pd_Series)={average(*pd_Series):.2f}')

"""out:
grades=[88, 75, 96, 55, 83, 90]
pd_Series=
0    88
1    75
2    96
3    55
4    83
5    90
dtype: int64
average(*pd_Series)=81.17"""































