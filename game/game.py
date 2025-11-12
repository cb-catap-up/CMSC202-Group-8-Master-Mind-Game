import random
from game.validation import validateInput
from game.scoring import calculateScore
from helpers.global_variables import readGlobalVariable
from game.write_score_to_file import writeScoreToFile
from helpers.clear_console import clear_console
from helpers.global_variables import saveGlobalVariable
from ui.ui import showUi

#Generate secret code of 4 colors
def randomizer (colors):
    return random.sample(list(colors), 4)

#Check if the guess matches the secret code
def checkMatch(secret_code, guess):
    # Convert both to the same format for comparison
    secret_mod = [color.strip().upper() for color in secret_code]
    guess_mod = [color.upper() for color in guess]
    
    return secret_mod == guess_mod

#Main game function
def playMastermind():

    # gets currently logged in user
    user_name = readGlobalVariable('current_user')

    # Available colors
    valid_colors = ["R", "G", "B", "Y", "W", "O"]

    # show basic instructions
    showBasicInstructions(valid_colors)

    # random color set
    color_set = randomizer(valid_colors)

    print(color_set)

    for count in range(0, 10):
        
        while True:  # Keep asking until valid input is provided
            g = input("Enter your guess: ")
            
            # Validate input
            is_valid, error_message, g = validateInput(g, valid_colors)
            
            if is_valid:
                break  # Exit the while loop if input is valid
            else:
                print(f"{error_message}")
                print("\nPlease try again.\n")
        # clears console and update instructions
        if count > 0:
            clear_console()
            # show basic instructions
            showBasicInstructions(valid_colors)

        is_match = checkMatch(color_set, g)

        #save guess to global variable
        saveGlobalVariable(f"{user_name}_guess_{count}", ''.join(g).lower())

        #show UI to show black pegs when color is correct and white pegs if incorrect
        showUi(color_set, g, count, user_name)

        if is_match:
            attempt_number = count + 1
            score = calculateScore(attempt_number)
            # write score
            writeScoreToFile(user_name, score)
            saveGlobalVariable('current_user_score', score)
            print("Your guess is correct!\n")
            break

        else:
            if count < 9:
                print("\nTry again.\n")
            else:
                clear_console()
                print("You've used all 10 attempts.")
                print(f"\nThe secret code was: {color_set}")
                # save 0 points for losing
                writeScoreToFile(user_name, 0)
                saveGlobalVariable('current_user_score', 0)

def showBasicInstructions(valid_colors):
    print(f"Available colors: {', '.join(valid_colors)}\n")
    print("Enter your guess as 4 letters without spaces or commas (e.g., RGBY)\n")
