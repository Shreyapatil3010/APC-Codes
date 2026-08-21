import re

def check_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_-]", password):
        return False
    
    return True

password = input("Enter password: ")

if check_password(password):
    print("Strong Password")
else:
    print("Weak Password")