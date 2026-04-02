# Simple user management system
users = []

def register(username, password, email):
    for u in users:
        if u["username"] == username:
            print("Username taken")
            return False
    users.append({
        "username": username,
        "password": password,  # storing plain text password
        "email": email,
        "active": True
    })
    print("User registered: " + username)
    return True

def login(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            print("Login successful")
            return u
    print("Invalid credentials")
    return None

def delete_user(username):
    for i in range(len(users)):
        if users[i]["username"] == username:
            del users[i]
            print("User deleted")
            return True
    print("User not found")
    return False

def list_users():
    for u in users:
        print(u["username"] + " - " + u["email"] + " - " + ("active" if u["active"] == True else "inactive"))

def update_email(username, new_email):
    for u in users:
        if u["username"] == username:
            u["email"] = new_email
            print("Email updated")
            return True
    print("User not found")
    return False

def search_user(query):
    results = []
    for u in users:
        if query in u["username"] or query in u["email"]:
            results.append(u)
    return results
