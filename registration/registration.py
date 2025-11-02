import os
from cipher import encryptPassword

def usernameExists(username):
    # Check if a given username already exists in the player database.
    db_path = os.path.join("database", "players.txt")
    try:
        with open(db_path, "r") as file:
            for line in file:
                saved_username, _ = line.strip().split(",")
                if saved_username == username:
                    return True
    except FileNotFoundError:
        return False
    return False

def registerUser():
    # Register a new player and return the username upon successful registration.
    print("REGISTER NEW PLAYER")

    while True:
        username = input("Enter username: ").strip()
        if username == "":
            print("Username cannot be empty. Please try again.")
            continue

        if usernameExists(username):
            print(f"Username '{username}' already exists. Please choose another.")
            continue

        password = input("Enter password: ").strip()
        if password == "":
            print("Password cannot be empty. Please try again.")
            continue

        # Encrypt password before saving.
        encrypted_password = encryptPassword(password)

        # Ensure the database folder exists.
        os.makedirs("database", exist_ok=True)
        db_path = os.path.join("database", "players.txt")
        
        # Append new user credentials.
        with open(db_path, "a") as file:
            file.write(f"{username},{encrypted_password}\n")

        print(f"Registration successful! Welcome, {username}!")
        return username
