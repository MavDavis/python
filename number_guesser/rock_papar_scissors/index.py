import random
user_wins = 0
computer_wins = 0
options = ["Rock", "Paper", "Scissors"]
while True:
    user_input = input("Enter Rock, Paper, Scissors or q to Quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    # 0=rock, 1=paper, 2=scissors;
print("Goodbye")