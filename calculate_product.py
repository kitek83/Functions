#calculate_product.py
"""Create a function named calculate_product that receives an arbitrary argument list of
 and returns the product (ratio) of all arguments. Call the function with the arguments 10,20,30,
 then with the sequence of argument produced by range (1,6,2)"""
sequence = [x for x in range(1,6,2)]
print(sequence)

def calculate_product(*args):  #receives arbitrary argument list
    product = 1

    for num in args:
        product *= num
    return product

print(f'calculate_product(10,20,30)= {calculate_product(10,20,30)}')  #passing touple

print()
#using sequence the sequence of arguments produced by range(1,6,2)
print(f'calculate_product([x for x in range(1,6,2)])={calculate_product([x for x in range(1,6,2)])}') #passing comprehension list not working with the function. We must use *operator
print(f'calculate_product(*[x for x in range(1,6,2)])={calculate_product(*[x for x in range(1,6,2)])}')

print(f'range(1,6,2)={range(1,6,2)}')                                                                                                        #to unpack its elents to touple
print(f'[x for x in range(1,6,2)]={[x for x in range(1,6,2)]}')   #range() works with the comprehension list
print(f'calculate_product(*range(1,6,2))={calculate_product(*range(1,6,2))}')  #*range(1,6,2) -> * unpack range as touple (1,3,5)


print()
print(f'check1={[x**3 for x in range(100)]}')

print()
#passing list comprehension as an *args - arbitrary argument list
print(f'=calculate_product([x**3 for x in range(100)])={calculate_product([x**3 for x in range(100)])}')
print()

print(f'calculate_product(*[x**3 for x in range(1,101)])={calculate_product(*[x**3 for x in range(1,101)])}')
print()
print()


#try tu use round function, which rounds the results


