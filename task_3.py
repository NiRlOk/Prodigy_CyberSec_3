import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_criteria
    ])

    if strength_score == 5:
        strength = 'Very Strong'
    elif strength_score == 4:
        strength = 'Strong'
    elif strength_score == 3:
        strength = 'Moderate'
    elif strength_score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

# Example usage
password = "P@ssw0rd"
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
print("Feedback:")
for fb in feedback:
    print(f"- {fb}")
