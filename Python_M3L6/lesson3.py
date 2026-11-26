x = []
while True:
    try:
        n = int(input("How many numbers do you want to enter? "))
        if n<=0:
            print("Please enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a whole number.")
for i in range(n):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            x.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


print("Original List: ", x)

a = sum(x)
average = a/len(x)
largest = max(x)
smallest = min(x)

print("Sum = ", a)
print("Average = ", average)
print("Largest number = ", largest)
print("Smallest number =", smallest)
