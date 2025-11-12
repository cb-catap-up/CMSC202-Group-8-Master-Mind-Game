import os

ASCII_ART = ("""
   __  ___         __                _         __  _____               __
  /  |/  /__ ____ / /____ ______ _  (_)__  ___/ / / ___/__ ___ _  ___ / /
 / /|_/ / _ `(_-</ __/ -_) __/  ' \/ / _ \/ _  / / (_ / _ `/  ' \/ -_)_/ 
/_/  /_/\_,_/___/\__/\__/_/ /_/_/_/_/_//_/\_,_/  \___/\_,_/_/_/_/\__(_)  
                                                                         
""")

ASCII_ART_WINNER = ("""
 __     __           __          ___         _ 
 \ \   / /           \ \        / (_)       | |
  \ \_/ /__  _   _    \ \  /\  / / _ _ __   | |
   \   / _ \| | | |    \ \/  \/ / | | '_ \  | |
    | | (_) | |_| |     \  /\  /  | | | | | |_|
    |_|\___/ \__,_|      \/  \/   |_|_| |_| (_)
                                               
""")

ASCII_ART_LOSER = ("""
 __     __            _                      _ 
 \ \   / /           | |                    | |
  \ \_/ /__  _   _   | |     ___  ___  ___  | |
   \   / _ \| | | |  | |    / _ \/ __|/ _ \ | |
    | | (_) | |_| |  | |___| (_) \__ \  __/ |_|
    |_|\___/ \__,_|  |______\___/|___/\___| (_)
                                               
""")


LEADERBOARD_ART = ("""
   __               __        __                    __  
  / /  ___ ___ ____/ /__ ____/ /  ___  ___ ________/ /__
 / /__/ -_) _ `/ _  / -_) __/ _ \/ _ \/ _ `/ __/ _  (_-<
/____/\__/\_,_/\_,_/\__/_/ /_.__/\___/\_,_/_/  \_,_/___/
                                                                  
""")

END_SCREEN_ART = ("""
  _______ _                 _          ______           _____  _             _             _ 
 |__   __| |               | |        |  ____|         |  __ \| |           (_)           | |
    | |  | |__   __ _ _ __ | | _____  | |__ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _| |
    | |  | '_ \ / _` | '_ \| |/ / __| |  __/ _ \| '__| |  ___/| |/ _` | | | | | '_ \ / _` | |
    | |  | | | | (_| | | | |   <\__ \ | | | (_) | |    | |    | | (_| | |_| | | | | | (_| |_|
    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, (_)
                                                                        __/ |         __/ |  
                                                                       |___/         |___/   
""")


END_CREDITS = ("""
Made by: CMSC202 group 8

Group Members:
   
   - Abril, Alric 
   - Baluyot, Maydie
   - Bolado, Christine Joy
   - Catap, Clyde Bryon
   - Dela Cruz, Grosby
   - Pacio, Frank Christopher
   - Papaya, Wilross Angelico

""")


DESCRIPTION = "Mastermind is an addictive puzzle game that you can spend a lot of time playing. Here, your task is to guess the color of the four circles on the decoding board. \nAt the beginning of the game, you will see a board with eight rows of four empty circles each. The color pattern is encrypted, and your task is to guess what color \neach circle is and in what order the colors should be arranged."

DETAILED_INSTRUCTION = "Detailed Instruction"

STEP_ONE_INSTRUCTION = "At the beginning of the game, you will see a decoding board with ten rows of four empty circles each. " \
"Your task is to guess which color pattern is encrypted."

STEP_TWO_INSTRUCTION = "Enter a sequence of 4 letters for your guesses (you will have Red, Blue, Green, Orange, White, and Yellow)." \
"Hit enter to submit your guess."

STEP_THREE_INSTRUCTION = "The table near the decoding board shows how close you are to the correct answer () means correct," \
"X means the color is present but in a different location and * if it does not appear at all"

STEP_FOUR_INSTRUCTION = "Start with different colors to test as many variations as possible and weed out colors that don't appear in the code."

STEP_FIVE_INSTRUCTION = 'You have ten attempts to crack the code by the number of lines on the board.' \
'The game ends when you find the correct sequence and all the key circles turn (), or when you run out of tries.'

GLOBALS_PATH = os.path.join("globals", "global_variables.txt")

SCORE_PATH = os.path.join('database', 'score.txt')
