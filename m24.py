# Printing documentation for the built-in functions
print(help(abs))
print(help(int))
print(help(input))

# Example of adding documentation for a custom function
def square(x):
    """
    Returns the square of a given number.

    Args:
    x (int): A number to be squared.

    Returns:
    int: The square of the given number.
    """
    return x**2

# Printing the documentation for the custom function
print(help(square))
