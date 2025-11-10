import time
from description.descriptions import showDescription
from registration.registration import registerUser
from registration.user_login_validator import askForRegistration
from registration.user_login_validator import askAndValidateUsernameAndPassWord
from helpers.clear_console import clear_console
from game.game import playMastermind
from game.validate_play_again_input import askToPlayAgain
from helpers.global_variables import clearGlobalVariables
from leaderboard.leaderboard import leaderboard
from constants import END_SCREEN_ART, END_CREDITS

# main function for the application
def runApplication(re_run = False):

    if not re_run:
                # clear console for user experience
        clear_console()

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

    # show leaderboard
    leaderboard()

    # ask user if they want to play again
    ask_user_to_play_again = str(input(f"\nWould you like to play again Y or N?: "))

    if askToPlayAgain(ask_user_to_play_again):
        runApplication(True)

    else:
        # clear variables, console and print end screens
        clearGlobalVariables()
        clear_console()
        print(END_SCREEN_ART)
        print(END_CREDITS)




# this starts the application
# this ensures the correct script is running
if __name__ == "__main__":

    # this shows the user the instructions and asks if they want to play
    if showDescription():
        runApplication()
