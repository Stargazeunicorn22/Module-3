def cube(n):
    return n**3

def check_and_cube(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return f"{n} IS NOT DIVISIBLE BY 3"
    
print(check_and_cube(9))
print(check_and_cube(5))