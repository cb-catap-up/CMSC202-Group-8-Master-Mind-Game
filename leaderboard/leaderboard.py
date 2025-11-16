from constants import SCORE_PATH
from leaderboard.show_win_or_lose import showWinOrLose
from leaderboard.get_top_five_leaders import getTopFiveLeaders
from helpers.clear_console import clear_console
from helpers.yes_or_no_input_validator import validateYesOrNoInput

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

    show_leaderboard = "\nWould you like to see the leaderboards Y or N?: "

    # ask if the user wants to see the leaderboards
    if validateYesOrNoInput(show_leaderboard):
        # clear console for better user experience
        clear_console()
        # show leaderbords
        title = f" Leaderboards "
        player_name = "Player Name"
        player_score = "score"
        width = 35
        print("┌" + "─" * (width - 2) + "┐")

        # Title line
        print("│" + title.center(width - 2) + "│")

        # table sides
        print("├" + "─" * (width - 2) + "┤")

        # header line
        player_line = f"{player_name:<2}{'':<10}{player_score:>8}"
        print("│" + player_line.ljust(width - 2) + "│")

        leaders = getTopFiveLeaders(leaderboard_list)

        # Leaderboard entries
        for i, lead in enumerate(leaders, start=1):
            name = str(lead[0])
            score = str(lead[1])

            # Medal assignment
            if i == 1:
                medal = " 🥇"
            elif i == 2:
                medal = " 🥈"
            elif i == 3:
                medal = " 🥉"
            else:
                medal = " 🏅"
            #  add medal to name based on user score
            name_with_medal = f"{name}{medal}"
            # format line
            line = f"{i:<2} {name_with_medal:<18}{score:>5}"
            # print line for scores in the middle
            print("│" + line.ljust(width - 3) + "│")
        # footer of the tables
        print("└" + "─" * (width - 2) + "┘")

