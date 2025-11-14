from helpers.global_variables import readGlobalVariable, saveGlobalVariable
from constants import ASCII_ART_WINNER, ASCII_ART_LOSER, GREEN, BOLD, RESET
from helpers.clear_console import clear_console

def showWinOrLose():
    # clear console
    clear_console()

    # get global variable score
    current_user_score = readGlobalVariable('current_user_score')
    # checks if user wins or not
    if current_user_score != str(0):
        print(f"{BOLD}{GREEN}{ASCII_ART_WINNER}{RESET}")
    else: 
        print(f"{BOLD}{GREEN}{ASCII_ART_LOSER}{RESET}")
    
    print(f"\nYour Score: {current_user_score}")

