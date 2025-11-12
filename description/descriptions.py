from constants import DESCRIPTION, ASCII_ART
from description.descriptions_input_validator import validateDescriptionsInput
from description.instructions import showInstruction
from helpers.clear_console import clear_console

# This function provides the rules and decription on how to play the game
def showDescription(clear_description = False):

    # clear console for better user experiece
    clear_console()

    if not clear_description:
        # prints out art for game
        print(ASCII_ART)

    if not clear_description:
        # prints out description of the game
        print(DESCRIPTION)

    # type cast user input to string
    is_game_starting = str(input("\nWould you like to play the game Y or N?: "))

    # this validates the input for the user if the users wants to play
    validated_game_starting = validateDescriptionsInput(is_game_starting, showDescription)


    if validated_game_starting:
        # shows instructions
        show_instruction = str(input("\nWould you like to see the instructions Y or N?: "))

        # this validates the input for the user if the user wants to see the instruction
        validated_show_instruction = validateDescriptionsInput(show_instruction, showDescription)

        if validated_show_instruction:
            # shows a more detailed instruction
            validated_game_starting = showInstruction()

    # clears console to run the game cleaner
    clear_console()
    
    return validated_game_starting
