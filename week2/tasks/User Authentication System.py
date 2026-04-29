def login_system(username, password, is_verified, attempts):
    if attempts >= 3:
        return "Account locked."
    
    if not is_verified:
        return "Please verify your account."
    if not username or not password:
        return "Invalid input."
    if username != "admin" and password != "password123":
        return "Incorrect Credentials!"
    return "Login successful!"
    
print(login_system("admin", "password123", True, 1))  