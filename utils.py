import hashlib
import random
import string
import re

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 20
    if re.search(r"[A-Z]", password):
        score += 20
    if re.search(r"[a-z]", password):
        score += 20
    if re.search(r"\d", password):
        score += 20
    if re.search(r"[!@#$%^&*]", password):
        score += 20

    if score == 100:
        return "Very Strong"
    elif score >= 80:
        return "Strong"
    elif score >= 60:
        return "Moderate"
    elif score >= 40:
        return "Weak"
    else:
        return "Very Weak"

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))
