import re

def validate_password(password):
    # Check length
    if len(password) < 6 or len(password) > 12:
        return False
    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return False
    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    # Check for at least one digit
    if not re.search("[0-9]", password):
        return False
    # Check for at least one special character
    if not re.search("[$#@]", password):
        return False
    # If all checks pass, return True
    return True

# Get comma-separated passwords from user input
passwords = input("Enter passwords separated by commas: ").split(",")

# Validate each password and store the valid ones in a list
valid_passwords = [password for password in passwords if validate_password(password)]

# Print the valid passwords separated by commas
print(",".join(valid_passwords))
