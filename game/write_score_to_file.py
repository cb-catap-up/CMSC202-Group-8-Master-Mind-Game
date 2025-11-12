import time
from constants import SCORE_PATH


def writeScoreToFile(user_name, score):

    # Append new global variable.
    with open(SCORE_PATH, "a") as file:
        file.write(f"{str(user_name)},{str(score)}\n")
    # allows time to write to file
    time.sleep(1)
