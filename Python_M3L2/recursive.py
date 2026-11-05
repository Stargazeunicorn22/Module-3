def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")
a = factorial(10)
print(a)