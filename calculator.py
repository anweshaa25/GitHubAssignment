

def add(a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
print("Simple Calculator")
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))
print("/n--- Calculation Results ---")
print(f"Addition: {add(num1, num2):.2f}")
print(f"Subtraction: {subtract(num1, num2):.2f}")
print(f"Multiplication: {multiply(num1, num2):.2f}")

