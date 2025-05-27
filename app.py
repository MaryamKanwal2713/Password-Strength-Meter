import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):                   
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "Strong", feedback
    elif score >= 2:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

st.title("Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if st.button("Evaluate"):
    strength, feedback = check_password_strength(password)

    if strength == "Strong":
        st.success("✅ Strong Password!")
    elif strength == "Moderate":
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
        st.write("Feedback:")
        for item in feedback:
            st.write(f"❌ {item}")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")
        st.write("Feedback:")
        for item in feedback:
            st.write(f"❌ {item}")

if st.button("Generate Password"):
    st.write(f"Generated Password: {generate_password()}")
