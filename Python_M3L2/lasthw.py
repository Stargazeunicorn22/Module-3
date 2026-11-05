def calculate_circumference(radius):
    """
    Calculates the circumference of a circle without any imports.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    # Using a high-precision approximation of Pi
    pi = 3.141592653589793
    
    circumference = 2 * pi * radius
    return circumference

# Example usage:
radius_input = 5
result = calculate_circumference(radius_input)
print(f"The circumference of a circle with radius {radius_input} is: {result:.2f}")
