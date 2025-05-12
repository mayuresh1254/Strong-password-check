import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # Scoring
    if not length_error:
        strength += 1
    if not digit_error:
        strength += 1
    if not uppercase_error:
        strength += 1
    if not lowercase_error:
        strength += 1
    if not symbol_error:
        strength += 1

    # Strength remarks
    if strength == 5:
        remarks = "Very Strong"
    elif strength >= 4:
        remarks = "Strong"
    elif strength >= 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    # Print Results
    print(f"\nPassword Strength: {remarks}")
    print("Criteria:")
    print(f" - Minimum Length (8): {'✅' if not length_error else '❌'}")
    print(f" - Contains Digit: {'✅' if not digit_error else '❌'}")
    print(f" - Contains Uppercase Letter: {'✅' if not uppercase_error else '❌'}")
    print(f" - Contains Lowercase Letter: {'✅' if not lowercase_error else '❌'}")
    print(f" - Contains Symbol: {'✅' if not symbol_error else '❌'}")

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)
