# Aim: Write a python program that calculates the factorial of a number.

def factorial(n): 
    if(n == 1) : 
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))

print("Factorial of ", number, " is ", factorial(number))
    