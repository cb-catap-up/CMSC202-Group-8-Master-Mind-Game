def askToPlayAgain(play_again):
    
    validated_play_again = play_again.lower()

    while True:
        
        if validated_play_again == 'y':
            return True
        if validated_play_again == 'n':
            return False

        if validated_play_again!= 'y' and validated_play_again != 'n':
            print("\nInvalid input. Please enter a valid one.")
