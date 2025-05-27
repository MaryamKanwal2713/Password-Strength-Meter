import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback

def generate_password(length=12):
    special_chars = "!@#$%^&*"
    if length < 8:
        length = 8
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(special_chars)
    ]
    all_chars = string.ascii_letters + string.digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("Password Strength Meter")
    print("-----------------------")
    while True:
        pwd = input("Enter password (or 'gen' to generate, 'exit' to quit): ").strip()
        if pwd.lower() == "exit":
            print("Goodbye!")
            break
        if pwd.lower() == "gen":
            print("Generated strong password:", generate_password())
            continue
        strength, score, feedback = check_password_strength(pwd)
        print(f"Strength: {strength} (Score: {score}/4)")
        if strength == "Strong":
            print("✅ Your password is strong!")
        else:
            print("Suggestions to improve your password:")
            for f in feedback:
                print("-", f)
        print()

if __name__ == "__main__":
    main()
