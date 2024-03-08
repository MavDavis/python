print("Welcome to my game")
name = input("what is your name? ")
playing=input("Do you want to play? ")
if playing.capitalize() != "yes".capitalize():
#   like return for javascript
    quit()
print("Okay! Lets play :) ")  
score = 0
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")    
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1

else:
    print("Incorrect!") 
# convert score to string to use
print("you got " + str(score) + " questions right")
print("you got " + str((score/2) * 100) + "%")