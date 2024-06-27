def outer(x):  # The outer function returns the inner function itself (not its result).
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)  # Output: 11
print(result)

def factorial(number):
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Sorry, 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry, 'number' must be zero or positive.")

    def compute_factorial(n):
        if n == 0:
            return 1
        else:
            return n * compute_factorial(n - 1)

    return compute_factorial(number)

# Example usage
try:
    result = factorial(5)
    print(f"The factorial of 5 is {result}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
