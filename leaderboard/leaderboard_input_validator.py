def askToshowLeaderboard(show_leaderboard):

    while True:
        
        if show_leaderboard == 'y':
            return True
        if show_leaderboard == 'n':
            return False

        if show_leaderboard!= 'y' and show_leaderboard != 'n':
            print("\nInvalid input. Please enter a valid one.")