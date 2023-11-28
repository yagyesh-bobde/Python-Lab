from module import operations

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Addition: ", operations.add(a, b))
print("Subtraction: ", operations.subtract(a, b))
print("Multiplication: ", operations.multiply(a, b))
print("Division: ", operations.divide(a, b))
