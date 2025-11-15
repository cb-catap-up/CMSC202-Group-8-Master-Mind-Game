from helpers.global_variables import readGlobalVariable, saveGlobalVariable
from constants import ASCII_ART_WINNER, ASCII_ART_LOSER, GREEN, BOLD, RESET
from helpers.clear_console import clear_console
from helpers.map_colors import mapColors

def showWinOrLose():
    # clear console
    clear_console()

    # get global variable score
    current_user_score = readGlobalVariable('current_user_score')

    # get global answer
    answer = readGlobalVariable('answer')

    # checks if user wins or not
    if current_user_score != str(0):
        print(f"{BOLD}{GREEN}{ASCII_ART_WINNER}{RESET}")
    else:
        print("You've used all 10 attempts.")
        print(f"\nThe secret code was: {showCorrectAnswer(answer.upper())}")
        print(f"{BOLD}{GREEN}{ASCII_ART_LOSER}{RESET}")
    
    print(f"\nYour Score: {current_user_score}")

# returns correct text
def showCorrectAnswer(color_set):
    mapped_colors = mapColors(color_set)
    return ', '.join(mapped_colors)

