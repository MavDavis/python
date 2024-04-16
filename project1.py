import random

# define a function
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
user1 = input("Enter your username: ")
computer = "Computer"
user1_value = 0
computer_value = 0
if user1:
    value = input("How many times do you want to roll? ")
    value = int(value)
    while value > 0:
            dice = roll()
            print(dice)
            value -=1
            
            continue
    user1_value += dice 
else:
  value = roll()
  while value > 0:
        dice = roll()
        value -=1
        continue
