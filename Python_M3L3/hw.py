try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        print("The entered age is even.")
    else:
        print("The entered age is odd.")
except ValueError:
    print("Value Error: Please enter a valid positive whole number for age.")
