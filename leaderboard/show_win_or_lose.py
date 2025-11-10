from helpers.global_variables import readGlobalVariable, saveGlobalVariable
from constants import ASCII_ART_WINNER, ASCII_ART_LOSER
from helpers.clear_console import clear_console
import time

def showWinOrLose():
    # clear console
    clear_console()
    # get global variable user
    current_user = readGlobalVariable('current_user')
    # get global variable score
    current_user_score = readGlobalVariable('current_user_score')

    # checks if user wins or not
    if current_user_score != str(0):
        print(ASCII_ART_WINNER)
    else: 
        print(ASCII_ART_LOSER)
    
    print(f"\nYour Score: {current_user_score}")

