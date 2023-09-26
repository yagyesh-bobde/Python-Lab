class Calculator: 
    def __init__(self, a, b) : 
        self.a = a 
        self.b = b
        self.result = 0

    def add(self) :
        self.result = self.a + self.b
        return self.result

    def subtract(self) :
        self.result = self.a - self.b
        return self.result

    def multiply(self) :
        self.result = self.a * self.b
        return self.result  
    
    def divide(self) :
        if(self.b == 0):
            print("Error: Cannot divide by zero")
        else : 
            self.result = self.a / self.b
        return round(self.result, 2)
    


op1 = int(input("Enter first operand: "))
op2 = int(input("Enter second operand: "))

cal = Calculator(op1, op2)

print("Addition: ", cal.add())
print("Subtraction: ", cal.subtract())
print("Multiplication: ", cal.multiply())
print("Division: ", cal.divide())
