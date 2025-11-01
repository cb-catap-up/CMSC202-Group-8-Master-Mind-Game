# This prints the initial guess first
# Then evaluates and prints the feedback
# To be looped for every guess input
def evaluateAndPrintFeedback(secret_code, guess):
    print(f"[ {' | '.join(secret_code)} ]") #used to check output: delete once okay

    # Prints the initial guess in format
    print(f"[ {' | '.join(guess)} ]")

    # Convert the string arguments into lists of each characters
    secret_list = list(secret_code)
    guess_list = list(guess)

    # Create the initial output list as unmatched
    result = ['X'] * 4
    
    # Initialize empty dictionaries to count unmatched colors
    # Used to determine correct color in the wrong spot (W) without overcounting
    secret_counts = {}
    guess_counts = {}
    
    # Find exact matches (B) and pass it to result
    # Count unmatch colors if not an exact match
    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
        if s == g:
            result[i] = 'B'
        else:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1
    
    # Find correct color in the wrong spot (W) and pass it to result
    for i, g in enumerate(guess_list):
        if result[i] == 'X' and secret_counts.get(g, 0) > 0:
            result[i] = 'W'
            secret_counts[g] -= 1  # prevents overcounting
    
    # Print feedback in the same format as guess
    print(f"[ {' | '.join(result)} ]")

# Test function call
evaluateAndPrintFeedback('RRYG', 'RGRB')