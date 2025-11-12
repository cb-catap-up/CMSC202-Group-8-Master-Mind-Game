# This prints the initial guess first
# Then evaluates and prints the feedback
# To be looped for every guess input

def displayBoard(count):
    board = ["[ ( ) | ( ) | ( ) | ( ) ]" for _ in range(count)]
    feedback = ["[ ' ' | ' ' | ' ' | ' ' ]" for _ in range(count)]
    for i in range(count):
        guess_display = board[i] if board[i] != "[ ' ' | ' ' | ' ' | ' ' ]" else "[ ( ) | ( ) | ( ) | ( ) ]"
        print(f"\n{guess_display} -> {feedback[i]}\n")

def evaluateAndPrintFeedback(secret_code, guess):

    secret_list = [c.upper() for c in secret_code]
    guess_list = [c.upper() for c in guess]
    result = ['*'] * 4  # * = not present
    secret_counts = {}

    # Step 1: Exact matches
    for i, (s, g) in enumerate(zip(secret_list, guess_list)):
        if s == g:
            result[i] = 'B'  # correct position
        else:
            secret_counts[s] = secret_counts.get(s, 0) + 1

    # Step 2: Correct color, wrong position
    for i, g in enumerate(guess_list):
        if result[i] == '*' and secret_counts.get(g, 0) > 0:
            result[i] = 'W'
            secret_counts[g] -= 1

    # Step 3: Print formatted feedback (with attempt count)
    print(f"\n[  {'  |  '.join(guess_list)}  ] -> [  {'  |  '.join(result)}  ]\n")
