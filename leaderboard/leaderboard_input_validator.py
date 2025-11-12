def askToshowLeaderboard(show_leaderboard):

    show_leaderboard_lower = show_leaderboard.lower()

    while True:
        
        if show_leaderboard_lower == 'y':
            return True
        if show_leaderboard_lower == 'n':
            return False

        if show_leaderboard_lower!= 'y' and show_leaderboard_lower != 'n':
            print("\nInvalid input. Please enter a valid one.")
