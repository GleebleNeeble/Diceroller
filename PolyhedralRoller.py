import random

# Define why you're rolling, how many dice, and how many sides on the dice
type = input("What are you rolling for?")
pool = int(input("How many dice are you rolling?"))
sides = int(input("How many sides are on each die?"))


if sides < 1:
    print("Wow, just wow...")
    exit(0)

if pool < 1:
    print("Silly human")
    exit(0)

print(type)
i = 0
while i < (pool):
    roll = random.randint(1, sides)
    i = i + 1
    print(roll, end=",")
print("\n")
