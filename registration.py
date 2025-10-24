import os

def usernameExists(username):
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

        os.makedirs("database", exist_ok=True)
        db_path = os.path.join("database", "players.txt")
        with open(db_path, "a") as file:
            file.write(f"{username},{password}\n")

        print(f"Registration successful! Welcome, {username}!")
        break