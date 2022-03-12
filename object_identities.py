#object_identities
"""Showing that in de same address can reside 2 seperate objects."""
x = 7    #to the variable x is assigned integer object containing 7 and identity address-id(7)
print(f'x = integer_object={x} and integer_identity=id(x)={id(7)}') #variable x is a memory address containing 2 objects

#cube function displays parameter identity and return parameter value
def cube(number):
    print(f'parameter_identity={id(number)}')
    return number ** 3

print(cube(x))

#using is Operator to show thet arguement and the parameter of the function have the  same identity
def cube2(number):
    print(f'number is x:{number is x}')  

cube2(x)
"""out:
x = integer_object=7 and integer_identity=id(x)=140730714040288
parameter_identity=140730714040288
343
number is x:True

Process finished with exit code 0"""