def calculator(a, b, operation):
    if operation == "add":
        c = int(a)+int(b)
        print("Your sum: " +str(c))
    elif operation == "subtract" or operation == "minus":
        c = int(b) - int(a)
        print("Your output: " + str(c))
    elif operation == "multiply":
        c = int(a) * int(b)
        print("Your multiplication: " + str(c))
    else:
        c = int(b)//int(a)
        print("Your output: " + str(c))

calculator(12, 10, "add")
calculator(2,6, "divide")
calculator(12, 15, "minus")
calculator(12, 15, "multiply")
