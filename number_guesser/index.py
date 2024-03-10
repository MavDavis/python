import random

top_of_number = input("Enter a number: ")
if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number <=0:
        print("Please enter a number next time")
        quit()
else:
    print("Please enter a number next time")
    quit()
random_number = random.randint(-5,11)
print(random_number) 