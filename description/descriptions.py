from constants import DESCRIPTION, ASCII_ART
from helpers.yes_or_no_input_validator import validateYesOrNoInput
from description.instructions import showInstruction
from helpers.clear_console import clear_console

# This function provides the rules and decription on how to play the game
def showDescription():

    # prints out art for game
    print(ASCII_ART)
    
    # prints out description of the game
    print(DESCRIPTION)

    # text for user if they want to play
    is_game_starting = "\nWould you like to play the game Y or N?: "

    # this validates the input for the user if the users wants to play
    validated_game_starting = validateYesOrNoInput(is_game_starting)


    if validated_game_starting:
        # text for user if they want to see instruction
        show_instruction = "\nWould you like to see the instructions Y or N?: "

        # this validates the input for the user if the user wants to see the instruction
        validated_show_instruction = validateYesOrNoInput(show_instruction)

        if validated_show_instruction:
            # shows a more detailed instruction
            validated_game_starting = showInstruction()

    # clears console to run the game cleaner
    clear_console()

    return validated_game_starting
