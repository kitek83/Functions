#crisp_game.py
"""Your roll 2 dice, each with face containing one, two, three, four, five, six spots, respectively.
When the dice come to rest, the sum of the spots on the 2 upward faces is calculated.
If the sum is 7 or 11 on the 1st roll, you win. If the sum is 2,3,12 on the 1st roll (called 'craps'),
you lose. If the sum is 4,5,6,8,9 or 10 on the 1st roll, the sum becomes you point. To win you continue
untill you roll the same sum of values as your previous point. You lose by rolling 7 before making your point"""

import random

def roll_dies():                    #rolling 2 dices
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)

    return (die1, die2)  #packed 2 results to the touple

def display_dies(results):
    die1, die2 = results     #unpacking the touple, assigned argument-results=touple vaules to variables die1, die2

    print(f'die1={die1}')
    print(f'die2={die2}')
    print(f'Player rolled {die1} + {die2} = {sum(results)}') #for function sum() must be iterable list (touple,list,ndarray) as an argument
                                                             #if you put sum(die1,die2) it will cause TypeError
roll_results = roll_dies()  #return touple (die1,die2)
display_dies(roll_results)  #argument is touple (die1,die2)

#1st condition of the game sum of dices = 7 or 11 - won
sum_dieces = sum(roll_results)   #variable roll_results has returned touple (die1,die2) from roll_dies(). Used sum() built in function for the touple (die1,die2)

if sum_dieces in (7, 11):   #for me new expression if value in (num1,num2)-this is touple, value in iterable (touple, list, pd.Series)
    game_status = 'Won'

#1st condition for the 1st roll: sum is 2,3,12 on the 1st roll (called 'craps'),you lose
elif sum_dieces in (2,3,12):
    game_status = 'Lost'

else:
    game_status = 'Continue'
    won_points = sum_dieces
    print(f'Point is = {won_points}')

while game_status == 'Continue':    #variable game_status is a sentinel for while loop
    #make a next roll
    roll_results = roll_dies()
    sum_die1_die2 = sum(roll_results)
    print(f'Next roll sum = {sum_die1_die2}')

    #suit of the while statement
    if sum_die1_die2 == won_points:
        game_status = 'Won'
        print(f'Next roll sum = {sum_die1_die2} = Point is = {won_points} so you Won')
    elif sum_die1_die2 == 7:
        game_status = 'Lost'
        print(f'Next roll sum = {sum_die1_die2} != Point is = {won_points}  so You Lost')

if game_status == 'Won':
    print('You won the game!')
elif game_status == 'Lost':
    print('You lost the game.')
"""
out:
die1=5
die2=3
Player rolled 5 + 3 = 8
Point is = 8
Next roll sum = 10
Next roll sum = 5
Next roll sum = 6
Next roll sum = 9
Next roll sum = 4
Next roll sum = 4
Next roll sum = 4
Next roll sum = 5
Next roll sum = 8
Next roll sum = 8 = Point is = 8 so you Won
You won the game!
"""



















































