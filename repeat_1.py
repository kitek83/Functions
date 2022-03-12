#coin_flips
"""Use a for statement, randrange and conditional expression to
simulate 20 coin flips displaying H for heads and T for tails all on
the same line, each seperated by space. Try to display number of H-heads
and number of T-tails"""
import random

heads = 0
tails = 0

for roll in range(1,21):
    result = f"{roll}={'H' if random.randrange(2) == 0 else 'T'}"
    print(result, end=' ')

    if result == f"{roll}=H":
        heads += 1
    else:
        tails +=1


print(f'\ntails = {tails}')
print(f'heads = {heads}')



