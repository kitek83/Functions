#coin_flips
"""Use a for statement, randrange and conditional expression to
simulate 20 coin flips displaying H for heads and T for tails all on
the same line, each seperated by space. Try display number of H-heads
and number of T-tails"""

import random

heads = 0
tails = 0

for roll in range(1,21):                                            #conditional expression assignet to roll, created together a string
    result = (f"{roll}={'H' if random.randrange(2) == 0 else 'T'}") #string assigned to variable result
    print(result, end=' ')

    if result == f"{roll}=H":  #that was confusing but I used f string to create the string the same like in the 1st result
        heads += 1
    else:
        tails += 1

print(f'\nH-heads={heads}')
print(f'T-tails={tails}')
