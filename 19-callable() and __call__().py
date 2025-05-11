class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier
multiply_by_3 = Multiplier(3)

# Check if the object is callable
print(callable(multiply_by_3))  # True

# Call the object like a function
result = multiply_by_3(4)
print(result)  # Output: 12
