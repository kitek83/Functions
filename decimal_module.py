#decimal_module.py
"""Import decimal module as dec.Then create the Decima objest with value 2.5 and square its value."""
import decimal as dec

decimal_object = dec.Decimal('2.5')**2
decimal_object2 = dec.Decimal(2.5)**2

print(f'decimal_object={decimal_object}')
print(f'decimal_object2={decimal_object2}')