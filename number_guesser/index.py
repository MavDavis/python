import random

top_of_number = input("Enter max number: ")
# test
if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number <=0:
        print("Please enter a number next time")
        quit()
else:
    print("Please enter a number next time")
    quit()
number_of_guesses = 0
random_number = random.randint(0,top_of_number)
while True:
   number_of_guesses +=1
   guess = input("Enter a number: ")
   if guess.isdigit():
       guess=int(guess)
   else:
       print("Please enter a number")        
       continue
   if guess == random_number:
       print("you got it")
       break
   elif guess < random_number:
       print("greater than your guess, try again")
   else: 
       print("less than your guess, try again")

print("you had ", number_of_guesses,"number of guesses")

