from constants import SCORE_PATH, RESET, BOLD, GREEN
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
        title = f" {BOLD}{GREEN}Leaderboards{RESET}  🥇 🥈 🥉 🏅       "
        width = 35  # a bit wider to fit medals
        print("┌" + "─" * (width - 2) + "┐")
        print("│" + title.ljust(width - 2) + "│")
        print("├" + "─" * (width - 2) + "┤")

        leaders = getTopFiveLeaders(leaderboard_list)

        # Print leaderboard entries inside the box
        for i, lead in enumerate(leaders, start=1):
            name = str(lead[0])
            score = str(lead[1])

            # Add medals
            medal = " 🏅"

            if i == 1:
                medal = " 🥇"
            elif i == 2:
                medal = " 🥈"
            elif i == 3:
                medal = " 🥉"

            # Combine name + medal and pad properly
            name_with_medal = f"{name}{medal}"
            line = f"{i:<2} {name_with_medal:<18}{score:>8}"
            print("│ " + line.ljust(width - 4) + "│")

        print("└" + "─" * (width - 2) + "┘")
