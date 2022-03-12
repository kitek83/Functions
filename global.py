#global.py
"""Checking usage of the global. Shadow the global by the global statement.
Shadow buil in function sum()"""

x = 4

def access_global():
    print(f'access to global x={x}')

def try_to_modify_global():
    x = 2
    print(f'local inside  try_to_modify_global() -> x={x} ')

def shadow_global():
    global x   #using global statement to define new global inside function block
    x = 'hello'
    print(f'new global x={x}')

access_global()
try_to_modify_global()
print(f'global=x={x}')
shadow_global()
print(f'new global x={x}')

print()
#shadow built in function sum
touple1 = (3,4,566,7,8,44/555)
print(f'sum={sum(touple1):.3f}')

list1 = [20,30,40]
print(f'sum1a={sum(list1)}')     #sum function works with the iterable

sum = 10 + 5
print(f'new_sum={sum}')

#try to use sum method, however sum() is shadowed by sum variable
touple2 = (3,4,5,6)
print(f'sum_touple2={sum(touple2)}') #TypeError: 'int' object is not callable -> sum finction is not working, because is shadowed



