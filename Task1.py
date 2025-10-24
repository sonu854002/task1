"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

"""

"""
num1=5
num2=10
Addition=num1+num2
Subtraction=num1-num2
Multiplication=num1*num2
Division=num1/num2
"""

num1= input("Enter the first number: ")
num2= input("Enter the second number: ")
Addition= int(num1) + int(num2)
Subtraction=int(num1) - int(num2)
Multiplication= int(num1) * int(num2)
Division=int(num1) / int(num2)

print("Addition:", Addition,)
print("Subtraction:", Subtraction,)
print("Multiplication:", Multiplication,)
print("Division:", Division)
