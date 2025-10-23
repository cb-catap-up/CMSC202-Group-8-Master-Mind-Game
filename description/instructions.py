from description.descriptions_input_validator import validateDescriptionsInput

from constants import (
    STEP_ONE_INSTRUCTION,
    STEP_TWO_INSTRUCTION,
    STEP_THREE_INSTRUCTION,
    STEP_FOUR_INSTRUCTION,
    STEP_FIVE_INSTRUCTION
)

# this shows a more detailed instruction for the user
# and asks if the user wants to continue playing
def showInstruction(hide_instruction = False):

    if not hide_instruction:
        print(f"\n1: {STEP_ONE_INSTRUCTION}")

        print(f"\n2: {STEP_TWO_INSTRUCTION}")

        print(f"\n3: {STEP_THREE_INSTRUCTION}")

        print(f"\n4: {STEP_FOUR_INSTRUCTION}")

        print(f"\n5: {STEP_FIVE_INSTRUCTION}")
    

    would_you_continue_playing = str(input("\nWould you like to continue the game Y or N?: "))

    return validateDescriptionsInput(would_you_continue_playing, showInstruction)
