# This prints the initial guess first
# Then evaluates and prints the feedback
# To be looped for every guess input
#def evaluateAndPrintFeedback(secret_code, guess):
#    print(f"[ {' | '.join(secret_code)} ]") #used to check output: delete once okay

    # Prints the initial guess in format
 #   print(f"[ {' | '.join(guess)} ]")

    # Convert the string arguments into lists of each characters
 #   secret_list = list(secret_code)
  #  guess_list = list(guess)

    # Create the initial output list as unmatched
#    result = ['X'] * 4
    
    # Initialize empty dictionaries to count unmatched colors
    # Used to determine correct color in the wrong spot (W) without overcounting
#    secret_counts = {}
#    guess_counts = {}
    
    # Find exact matches (B) and pass it to result
    # Count unmatch colors if not an exact match
#    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
#        if s == g:
#            result[i] = 'B'
#        else:
#            secret_counts[s] = secret_counts.get(s, 0) + 1
#            guess_counts[g] = guess_counts.get(g, 0) + 1
    
    # Find correct color in the wrong spot (W) and pass it to result
#    for i, g in enumerate(guess_list):
#        if result[i] == 'X' and secret_counts.get(g, 0) > 0:
#            result[i] = 'W'
#            secret_counts[g] -= 1  # prevents overcounting
    
    # Print feedback in the same format as guess
#    print(f"[ {' | '.join(result)} ]")

#----------
#def evaluateAndPrintFeedback(secret_code, guess, count):
#    secret_list = [c.upper() for c in secret_code]
#    guess_list = [c.upper() for c in guess]
#    result = ['_'] * 4
#    secret_counts = {} 

    # Step 1: Find exact matches (Black pegs)
#    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
#        if s == g:
#            result[i] = 'B'
#        else:
#            secret_counts[s] = secret_counts.get(s, 0) + 1

    # Step 2: Find correct colors in wrong positions (White pegs)
#    for i, g in enumerate(guess_list):
#        if result[i] == '_' and secret_counts.get(g, 0) > 0:
#            result[i] = 'W'
#            secret_counts[g] -= 1
    
    # Step 3: Display formatted feedback
#    print(f"[ {' | '.join(guess_list)} ] → [ {' | '.join(result)} ]")
    
    # Step 4: Return True if all 4 are Black (correct code guessed)
#    return result.count('B') == 4
#evaluateAndPrintFeedback(['r','g','b','y'],['g','u','e','s'], 1)

def evaluateAndPrintFeedback(secret_code, guess, count):
    secret_list = [c.upper() for c in secret_code]
    guess_list = [c.upper() for c in guess]
    result = ['*'] * 4  # * = not present
    secret_counts = {}

    # Step 1: Exact matches
    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
        if s == g:
            result[i] = '()'  # correct position
        else:
            secret_counts[s] = secret_counts.get(s, 0) + 1

    # Step 2: Correct color, wrong position
    for i, g in enumerate(guess_list):
        if result[i] == '*' and secret_counts.get(g, 0) > 0:
            result[i] = 'X'
            secret_counts[g] -= 1

    # Step 3: Print formatted feedback (with attempt count)
    print(f"\nAttempt {count}: [ {', '.join(guess_list)} ] → [ {', '.join(result)} ]")

    # Step 4: Return True if guessed correctly
    return result.count('()') == 4


def displayBoard(board, feedback):
    print("\nCurrent Board:")
    for i in range(10):
        guess_display = board[i] if board[i] != [' ', ' ', ' ', ' '] else ['( )', '( )', '( )', '( )']
        print(f"{guess_display} -> {feedback[i]}")


def playGame(secret_code):
    board = [[' ', ' ', ' ', ' '] for _ in range(10)]
    feedback = [[' ', ' ', ' ', ' '] for _ in range(10)]

    for attempt in range(10):
        displayBoard(board, feedback)
        guess = input(f"\nAttempt {attempt + 1}: Enter 4 colors (e.g. R G B Y): ").split()

        if len(guess) != 4:
            print("⚠️ Please enter exactly 4 letters.")
            continue

        board[attempt] = [g.upper() for g in guess]
        is_correct = evaluateAndPrintFeedback(secret_code, guess, attempt + 1)
        feedback[attempt] = evaluateAndPrintFeedback(secret_code, guess, attempt + 1)

        if is_correct:
            displayBoard(board, feedback)
            print("\n🎉 Congratulations! You cracked the code!")
            break
    else:
        print("\n❌ Game Over! You ran out of attempts.")
        print(f"The correct code was: {', '.join(secret_code).upper()}")
        
    evaluateAndPrintFeedback(['r','g','b','y'],['g','u','e','s'], 1)
