import random
from game.validation import validateInput
from game.scoring import calculateScore
from helpers.global_variables import readGlobalVariable
from game.write_score_to_file import writeScoreToFile
from helpers.clear_console import clear_console

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
    valid_colors = ["R", "G", "B", "Y", "W", "O"]  # Available colors
    color_set = randomizer(valid_colors)
    
    print(f"Available colors: {', '.join(valid_colors)}")
    print("Enter your guess as 4 letters without spaces or commas (e.g., RGBY)")
    
    for count in range(0, 10):
        
        while True:  # Keep asking until valid input is provided
            g = input("Enter your guess: ")
            
            # Validate input
            is_valid, error_message, g = validateInput(g, valid_colors)
            
            if is_valid:
                break  # Exit the while loop if input is valid
            else:
                print(f"{error_message}")
                print("Please try again.\n")
        
        is_match = checkMatch(color_set, g)
        #add UI to show black pegs when color is correct and white pegs if incorrect

        if is_match:
            attempt_number = count + 1
            score = calculateScore(attempt_number)
            # write score
            writeScoreToFile(user_name, score)
            print("Your guess is correct!")

        else:
            if count < 9:
                print("Try again.")
            else:
                clear_console()
                print("You've used all 10 attempts.")
                print(f"The secret code was: {color_set}")
                # save 0 points for losing
                writeScoreToFile(user_name, 0)
