def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("FUNCTION CALCULATOR")

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    op = input("Enter operation (add, subtract, multiply, divide): ")

    if op == "add":
        print(add(x, y))
    elif op == "subtract":
        print(subtract(x, y))
    elif op == "multiply":
        print(multiply(x, y))
    elif op == "divide":
        print(divide(x, y))
    else:
        print("Unknown operation.")

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Thank you for using the calculator!")
