def askToPlayAgain(play_again):

    while True:
        
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False

        if play_again!= 'y' and play_again != 'n':
            print("\nInvalid input. Please enter a valid one.")
