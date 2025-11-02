import os
from registration.cipher import decryptPassword
from registration.registration import usernameExists
from helpers.clear_console import clear_console
from helpers.yes_or_no_input_validator import validateYesOrNoInput
from registration.registration import registerUser


def userLogin(show_registration=True):

    if show_registration:
        new_player = str(input('Are you a new user Y / N?: '))

        if validateYesOrNoInput(new_player, userLogin):
            # register user
            registerUser()

        clear_console()

    user_name = str(input('\nEnter username: '))

    password = str(input('\nEnter password: '))

    # check if username and password is correct
    if readAndValidateUsernameAndPassWord(user_name=user_name, pass_word=password, user_login=userLogin):
        clear_console()
        return user_name
    
    return False


def readAndValidateUsernameAndPassWord(user_name, pass_word, user_login):
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
        

        if not (decryptPassword(username_and_password_map[user_name]) == pass_word):
            raise Exception('\nWrong password, please enter the correct password')
            

    except Exception as e:
        # clear console
        clear_console()
        # print error
        print(e)
        # run userlogin again
        user_login(False)

    except FileNotFoundError:

        return False
    
    return True
