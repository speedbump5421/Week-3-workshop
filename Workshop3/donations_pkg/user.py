def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Incorrect password. Please try again.")
            return ""
    else:
        print("Username not found. Please register.")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"Username '{username}' has been registered successfully!")
        return username
