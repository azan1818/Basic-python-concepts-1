# Task 1: perform basic mathmatical opration
# taking two numbers as input from the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#performing opration
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

#To avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division ="undefined(cannot divide by zero)"

#Displaying the results
print("\nresults:")
print("addition:", addition)
print("subtraction:", subtraction)
print("multiplication:", multiplication)
print("division:", division)
