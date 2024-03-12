import random
user_wins = 0
computer_wins = 0
while True:
    user_input = input("Enter Rock, Paper, Scissors or q to Quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in ["Rock", "Paper", "Scissors"]:
        continue