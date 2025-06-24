import re

password = input("Please enter your password: ")

checks = [
    (re.compile(r"[a-z]"), "lowercase letter"),
    (re.compile(r"[A-Z]"), "uppercase letter"),
    (re.compile(r"[0-9]"), "digit"),
    (re.compile(r"[!@#$%^&*]"), "special character (!@#$%^&*)"),
]

error = [desc for regex, desc in checks if not regex.search(password)]

if error:
    print("Weak password. Missing: " + ", ".join(error))
else:
    print(f"Your password: {password} is a strong password")
