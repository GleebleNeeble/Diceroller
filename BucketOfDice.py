# Copyright 2018 Ursula Searle
# Copyright 2020 Ursula Searle
#!/usr/bin/env python3

####################################################
# Roller for multiple polyhedral types in one pool #
####################################################

import random
from pathlib import Path

# Find a way to define multiple dice pools (make a list)
bucket = []
moredice = "Y"

try:
    while str.upper(moredice)=="Y":
        dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die) ")
        bucket.append(dice)
        moredice=input("Do you want to add more dice to the bucket? Type Y or N: ")

    else:
        explode = input("Do you want your dice to explode? Type Y or N: ")
        if str.upper(explode)=="N":
            for dice in bucket:
                print("\n"+dice)
                pool = int(dice[:dice.find('d')])
                sides = int(dice[dice.find('d') + 1:])
                i = 0
                while i < (pool):
                    roll = random.randint(1, sides)
                    i = i + 1
                    print(roll, end=",")

        elif str.upper(explode)=="Y":
            for dice in bucket:
                print("\n" + dice)
                pool = int(dice[:dice.find('d')])
                sides = int(dice[dice.find('d') + 1:])
                if sides <= 1:
                    raise ValueError
                else:
                    i = 0
                    while i < (pool):
                        roll = random.randint(1, sides)
                        if roll < sides:
                            i = i + 1
                        elif roll == sides:
                            random.randint(1, sides)
                            i = i
                        print(roll, end=",")

except (NameError, TypeError, ValueError):
    print("Sorry, try something else!")
    exec(Path('./Diceroller.py').open('r').read())

print("\n")

rollagain=input("Do you want to roll another bucket of dice? Enter Y or N: ")
if str.upper(rollagain)=="Y":
    import BucketOfDice
else:
    exec(Path('./Diceroller.py').open('r').read())


