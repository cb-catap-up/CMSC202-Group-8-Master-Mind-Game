import time
from description.descriptions import showDescription
from registration.registration import registerUser
from registration.user_login_validator import askForRegistration
from registration.user_login_validator import askAndValidateUsernameAndPassWord
from helpers.clear_console import clear_console
from game.game import playMastermind
from helpers.global_variables import saveGlobalVariable, readGlobalVariable, clearGlobalVariables

# main function for the application
def runApplication():

    is_application_running = True

    while is_application_running:
        """
            -Put all the game logic and other proper features of the application detailed by the speciations here
            -All must be independent features must be an independent function with a proper return value
        """
        # ask if new user and validate
        is_new_user = askForRegistration()
        # if new register the user
        if is_new_user:
            # clear console
            clear_console()
            # register user
            registerUser()

            # this allows time for python to write to file
            time.sleep(1)
            # clear console
            clear_console()
            print('Please enter your credentials again')

        # login user
        askAndValidateUsernameAndPassWord()

        # clears console for better experience for the players
        clear_console()

        # start and play game
        playMastermind()

        break



# this starts the application
# this ensures the correct script is running
if __name__ == "__main__":

    # this shows the user the instructions and asks if they want to play
    if showDescription():
        runApplication()
    # temporary we will put a proper end screen later
    print('\napplication has ended')
