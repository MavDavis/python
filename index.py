score = float(input("Enter the student's score: "))

# Use if, elif, and else to determine the grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Output the result
print(f"The student's grade is {grade}")

# to find a number that is least in an array

numbers = [10, 5, 7, 2, 15, 1, 8]

# Initialize a variable to store the smallest number
smallest = numbers[0]

# Loop through the array to find the smallest number
for num in numbers:
    if num < smallest:
        smallest = num

# Print the smallest number
print("The smallest number in the array is:", smallest)
    # else:
    #     print(f"{num} is odd")


