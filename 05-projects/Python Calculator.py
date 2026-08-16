# ==============================================================================
# Project Name: Simple Command-Line Calculator
# Topic Focus : Conditional Statements and Basic Arithmetic
# Author      : Maria Chinmayi
# College     : VIT Chennai (B.Tech, First Year)
# Date        : August 16, 2026
# Description : A simple terminal-based calculator built to practice user input,
#               type casting, and if-elif-else control flow in Python.
# ==============================================================================

# Your actual Python code starts right below this line
print("Welcome to my Python Calculator!")

operator = input("Enter an operator (+ - * /)")
num1 = float(input("Enter the 1st number"))
num2 = float(input("Enter the 2nd number"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1/num2

print(result)

