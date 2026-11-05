def greet(name, message = 'Hi'):
    return f"{message} {name}"

greeting = greet('John')
print(greeting)

def my_function():
    """Demonstates triple double quotes 
    docstrings and does nothing really."""
    return None
print("Using __doc__:")
print(my_function.__doc__)