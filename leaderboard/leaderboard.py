from constants import SCORE_PATH, LEADERBOARD_ART
from helpers.global_variables import readGlobalVariable, saveGlobalVariable
from leaderboard.show_win_or_lose import showWinOrLose
from leaderboard.get_top_five_leaders import getTopFiveLeaders
from leaderboard.leaderboard_input_validator import askToshowLeaderboard
from helpers.clear_console import clear_console

def leaderboard():

    # show if the player wins or lose
    showWinOrLose()

    leaderboard_list = []

    # show leaderboard
    try:
        with open(SCORE_PATH, "r") as file:
            # save user and score to leaderboard list
            for line in file:
                user, score = line.strip().split(",")
                leaderboard_list.append((user,score))

    except FileNotFoundError:
        print("Error: The file does not exist!")

    show_leaderboard = str(input(f"\nWould you like to see the leaderboards Y or N?: "))

    # ask if the user wants to see the leaderboards
    if askToshowLeaderboard(show_leaderboard):
        # clear console for better user experience
        clear_console()
        # show leaderbords
        print("LEADERBOARDS\n")
        leaders = getTopFiveLeaders(leaderboard_list)

        for lead in leaders:
            print("{:<10} {:<10}".format(lead[0], lead[1]))
