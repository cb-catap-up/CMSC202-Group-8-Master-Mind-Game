from helpers.global_variables import readGlobalVariable
from constants import COLOR_FEEDBACK_MAP, COLOR_MAP
# This prints the initial guess first
# Then evaluates and prints the feedback
# To be looped for every guess input
def showUi(secret_code, guess, count, current_user):
    # get previous guess
    previous_guesses = getPreviousGuesses(current_user, count)
    
    # if a previous guess is present evaluate and print
    if count > 0:
        for g in previous_guesses:
            evaluateAndPrintFeedback(secret_code, g)
    # evaluate current guess
    evaluateAndPrintFeedback(secret_code, guess)

    # print extra input for other then board
    displayBoard(10 - len(previous_guesses) - 1)

# gets previous guess from global variables
def getPreviousGuesses(current_user, count):
    guess_array = []
    
    for i in range(count):
        guess_array.append(readGlobalVariable(f"{current_user}_guess_{i}"))
    
    return guess_array

# prints the extra empty input when starting game
def displayBoard(count):
    init = [COLOR_FEEDBACK_MAP['*']] * 4
    empty_guess = "  ".join(init)
    empty_feedback = "  ".join(init)
    board = [empty_guess for _ in range(count)]
    feedback = [empty_feedback for _ in range(count)]
    for i in range(count):
        guess_display = board[i] if board[i] != empty_feedback else empty_guess
        print(f"\n{guess_display}   ➤   {feedback[i]}\n")

def evaluateAndPrintFeedback(secret_code, guess):
    secret_list = [c.upper() for c in secret_code]
    guess_list = [c.upper() for c in guess]
    result = [COLOR_FEEDBACK_MAP['*']] * 4  # * = not present
    secret_counts = {}

    # Step 1: Exact matches
    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
        if s == g:
            result[i] = COLOR_FEEDBACK_MAP['b']  # correct position
        else:
            secret_counts[s] = secret_counts.get(s, 0) + 1

    # Step 2: Correct color, wrong position
    for i, g in enumerate(guess_list):
        if result[i] == COLOR_FEEDBACK_MAP['*'] and secret_counts.get(g, 0) > 0:
            result[i] = COLOR_FEEDBACK_MAP['w']
            secret_counts[g] -= 1
    # Step 3: Print formatted feedback (with attempt count)
    initial_result = '  '.join(result)
    guess_result = '  '.join(mapGuessList(guess_list))
    print(f"\n{guess_result}   ➤   {initial_result}\n")

# map color guess list
def mapGuessList(guess_list):

    mapped_guess_list = []

    for guess in guess_list:
        mapped_guess_list.append(COLOR_MAP[guess.lower()])

    return mapped_guess_list

