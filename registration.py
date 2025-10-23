def username_exists(username):
    try:
        with open("players.txt", "r") as file:
            for line in file:
                saved_username, _ = line.strip().split(",")
                if saved_username.lower() == username.lower():
                    return True
    except FileNotFoundError:
        return False
    return False

def register_user():
    print("REGISTER NEW PLAYER")

    while True:
        username = input("Enter username: ").strip()
        if username == "":
            print("Username cannot be empty. Please try again.")
            continue

        if username_exists(username):
            print(f"Username '{username}' is already taken. Please choose another one.")
            continue

        password = input("Enter password: ").strip()
        if password == "":
            print("Password cannot be empty. Please try again.")
            continue

        with open("players.txt", "a") as file:
            file.write(f"{username},{password}\n")

        print(f"Registration successful! Welcome, {username}!")
        break

if __name__ == "__main__":
    register_user()