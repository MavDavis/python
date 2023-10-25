david = "David is coming soon!";
david2 = david.split(" ")
print(david2)
# ['David', 'is', 'coming', 'soon!']
david3 = david[0:4]
print(david3)
# Davi
david4 = david.replace("is", "is not")
print(david4)
# David is not coming soon!
test = david.startswith("Dax")
print(test) 
# False cos david starts with 'david not dax'
# loop through a string
for letter in david:print(letter)
# will print each letter