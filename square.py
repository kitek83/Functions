#square.py
"""Function return square number, squere_root, other simple ops with functions"""
import random

def square(num):
    return num ** 2

def squere_root(num):
    return num ** 0.5

number = float(input('Enter the float number on integer: '))

print(f'square({number}) = {square(number):.2f}')
print(f'square_root{number} = {squere_root(number):.2f}')

list = [23,4,5,66,78,99,33]
print(f'list={list}')
print(f'max_list={max(list)}')
print(f'min_list={min(list)}')

print()
#produce 10 integers in the range 1-6 simulating rolling a 6 sided die

for x in range(10):
    print(f'{random.randrange(1,7)}',end=' ')