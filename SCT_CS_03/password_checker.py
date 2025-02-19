import re
import math
import string

def calculate_entropy(password):
    """Calculates password entropy based on character variety and length"""
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26  # Lowercase letters
    if any(c.isupper() for c in password):
        charset_size += 26  # Uppercase letters
    if any(c.isdigit() for c in password):
        charset_size += 10  # Digits
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)  # Special characters
    
    if charset_size == 0:
        return 0  # Avoid log(0) error

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def assess_password_strength(password):
    """Evaluates password strength based on multiple factors"""
    criteria = {
        "length": len(password) >= 12,  # Stronger minimum length
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "no_common_patterns": not re.search(r'(1234|password|qwerty|abcd|admin)', password, re.IGNORECASE),
    }

    score = sum(criteria.values()) + (calculate_entropy(password) / 10)

    if score >= 6:
        strength = "Very Strong 🔥"
    elif score >= 5:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, criteria, calculate_entropy(password)

def suggest_improvements(password):
    """Suggests ways to improve the password"""
    suggestions = []
    
    if len(password) < 12:
        suggestions.append("Increase the length to at least 12 characters.")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        suggestions.append("Add at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Use at least one special character (!@#$%^&*).")
    if re.search(r'(1234|password|qwerty|abcd|admin)', password, re.IGNORECASE):
        suggestions.append("Avoid common patterns like '1234' or 'password'.")

    return suggestions

# Example usage
password = input("Enter your password: ")
strength, criteria, entropy = assess_password_strength(password)
print(f"\n🔍 Password Strength: {strength}")
print(f"🔢 Entropy Score: {entropy} bits")
print(f"✅ Criteria Met: {criteria}")

suggestions = suggest_improvements(password)
if suggestions:
    print("\n💡 Suggestions for a stronger password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("\n🎉 Your password is strong!")
