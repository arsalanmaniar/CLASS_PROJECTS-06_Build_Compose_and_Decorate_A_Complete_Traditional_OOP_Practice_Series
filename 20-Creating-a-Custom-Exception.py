# Step 1: Custom Exception
class InvalidAgeError(Exception):
    pass

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        print("Age is valid.")

# Step 3: Handling the exception
try:
    check_age(15)  # Test with an invalid age
except InvalidAgeError as e:
    print(f"Error: {e}")
