import os
from registration.cipher import decryptPassword
from registration.registration import usernameExists
from helpers.clear_console import clear_console

def askForRegistration():

    while True:
        new_player = str(input('Are you a new user Y / N?: ')).lower()
        
        if new_player == 'y':
            return True
        if new_player == 'n':
            return False

        if new_player!= 'y' and new_player != 'n':
            print("\nInvalid input. Please enter a valid one.")

def askAndValidateUsernameAndPassWord():
    # ask to input username
    user_name = str(input('\nEnter username: '))
    # ask to input password
    password = str(input('\nEnter password: '))
    # save all read files with username and password as a dictionary
    username_and_password_map = {}
    # Check if password is correct
    db_path = os.path.join("database", "players.txt")
    try:
        with open(db_path, "r") as file:
            for line in file:
                saved_user_name, encrypted_password = line.strip().split(",")
                username_and_password_map[saved_user_name] = encrypted_password
        
        if not (usernameExists(username=user_name)):
            raise Exception('\nWrong user name, please enter a registered user name')
        

        if not (decryptPassword(username_and_password_map[user_name]) == password):
            raise Exception('\nWrong password, please enter the correct password')
            

    except Exception as e:
        # # clear console
        clear_console()
        # print error
        print(e)
        # run userlogin again
        askAndValidateUsernameAndPassWord()

    except FileNotFoundError:

        return None
    
    return user_name
