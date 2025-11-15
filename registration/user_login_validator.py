import os
from registration.cipher import decryptPassword
from registration.registration import usernameExists
from helpers.clear_console import clear_console
from helpers.global_variables import saveGlobalVariable
from constants import PLAYER_PATH

def askForRegistration():

    while True:

        users = []

        # read users
        file = open(PLAYER_PATH,'r')

        # add users to array
        for i in file:
            users.append(i)
        # if empty force user registration
        if len(users) == 0:
            return True

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
    try:
        with open(PLAYER_PATH, "r") as file:
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

    except FileNotFoundError as e:
        # print error
        print(e)
    
    # save to globals
    saveGlobalVariable('current_user', user_name)
