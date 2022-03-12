#map_round_lambda.py
"""Refreshing.Using function map(), round() and lambda"""

#using function map
list1 = [x for x in range(0,58)]

def multiply(n):
    return ((n * n) + (5 * n)) / 2345

result1 = list(map(multiply, list1))  # function map() use function multiply() for each element from list1
print(f'result1={result1}')
print(f'len(result1)={len(result1)}')

result1_rounded = [round(num, 2) for num in result1]  # using function round(number,digit) with comprehension list
print(f'result1_rounded={result1_rounded}')
print()

list2 = [2,3,4,5]
print(f'list(map(multiply,list2))={list(map(multiply,list2))}')
print(2*'-------------------lambda-----------------------')

adde_one = (lambda x: x + 1)(2)
print(f'adde_one={adde_one}')

add_two = lambda x: x + 2
print(f'adde_two={add_two(2)}')
print()

full_name = lambda first, last: f'full_name: {first.upper()} {last.upper()}'
print(f"{full_name('krzysztof', 'kozak')}")
































