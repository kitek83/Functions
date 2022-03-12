#value_in_iterable.py
"""checking expression value in iterable: touple, list, ndarray, pa.Series."""
import numpy as np
import pandas as pd

value = 3

#1st - checking expression value in iterable with touple
if value in (12,13,3,4,5,6):
    print(f'Value={value} in touple.')

else:
    print(f'Value not found in touple.')

#2nd - checking expression value in iterable with touple
if value in [12,13,3,4,5,6]:
    print(f'Value={value} in the list.')
else:
   print(f'Value not found in list.')

#3rd - checking expression value in iterable with ndarray
print()
ndarray = np.array([12,13,3,4,5,6])
print(f'ndarray={ndarray}')

if value in ndarray:
    print(f'Value={value} in the ndarray={ndarray}.')
else:
    print(f'Value not found in ndarray.')

#4th - checking expression value in iterable pandas Series
print()
pd_series = pd.Series([12,13,3,4,5,6])
print(f'pd_series=\n{pd_series}')

if value in pd_series:
    print(f'Value={value} in the pd_series.')
else:
    print(f'Value not found in pd_series.')





























