from helpers.yes_or_no_input_validator import validateYesOrNoInput

from constants import (
    STEP_ONE_INSTRUCTION,
    STEP_TWO_INSTRUCTION,
    STEP_THREE_INSTRUCTION,
    STEP_FOUR_INSTRUCTION,
    STEP_FIVE_INSTRUCTION,
)

# this shows a more detailed instruction for the user

def showInstruction():

    # prints first instruction
    print(f"\n1: {STEP_ONE_INSTRUCTION}")

    # prints second instruction
    print(f"\n2: {STEP_TWO_INSTRUCTION}")

    # prints third instruction
    print(f"\n3: {STEP_THREE_INSTRUCTION}")

    # prints fourth instruction
    print(f"\n4: {STEP_FOUR_INSTRUCTION}")

    # prints fifth instruction
    print(f"\n5: {STEP_FIVE_INSTRUCTION}")
    
    # asks if the user wants to continue playing
    would_you_continue_playing = "\nWould you like to continue playing the game Y or N?: "

    return validateYesOrNoInput(would_you_continue_playing)
