import string
import random

# Part A: Individual Validation Functions
# These functions handle specific security checks for the password system.

def check_min_length(password, min_len=8):
    # Check if password meets minimum length requirement (default is 8)
    return len(password) >= min_len

def has_uppercase(password):
    # Check if password contains at least one uppercase letter
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    # Check if password contains at least one lowercase letter
    return any(char in string.ascii_lowercase for char in password)

def has_digit(password):
    # Check if password contains at least one numeric digit
    return any(char in string.digits for char in password)

def has_special(password):
    # Check if password contains at least one special character (punctuation)
    return any(char in string.punctuation for char in password)

# Part B: Master Validation Function
# This function combines all individual checks into a single results dictionary.

def validate_password(password):
    # Store the results of each individual function call
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special': has_special(password)
    }
    
    # overall "is_valid" key is True only if all checks pass
    results['is_valid'] = all(results.values())
    return results

# Part C: User Interface and Testing
# This section handles user input, formatting, and dynamic feedback.

def main():
    print("-" * 50)
    # Ask the user to type in a password
    password = input("Enter password to validate: ")
    
    # Call validate_password() function with the user's input
    results = validate_password(password)
    
    print("-" * 50)
    print("VALIDATION RESULTS")
    print("-" * 50)
    
    labels = {
        'min_length': "Minimum length (8+ chars)",
        'has_uppercase': "Contains uppercase",
        'has_lowercase': "Contains lowercase",
        'has_digit': "Contains digit",
        'has_special': "Contains special char"
    }

    # Display clear feedback for each rule
    for key, label in labels.items():
        met = results[key]
        check_symbol = "✔" if met else "✘"
        print(f"[{check_symbol}] {label}: {met}")
    
    print("-" * 50)
    
    # Tell the user if the password is Strong or Weak overall
    if results['is_valid']:
        print("PASSWORD IS STRONG")
    else:
        print("PASSWORD IS WEAK - Please address failed requirements")
        
        # Use random.choice() to display a random hint if the password is weak
        hints = [
            "Try adding a mix of symbols like @, #, or $.",
            "Remember to use at least one capital letter.",
            "Adding a number can significantly increase strength."
        ]
        print(f"Hint: {random.choice(hints)}")
    print("-" * 50)

if __name__ == "__main__":
    main()