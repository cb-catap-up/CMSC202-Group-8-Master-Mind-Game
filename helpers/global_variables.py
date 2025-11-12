from constants import GLOBALS_PATH
import time

"""
    This function saves and reads global variables from a separate text file for use on every part 
    of the application to remove dependency of each application modules with each other
"""

# save variable to global_variables.txt file
def saveGlobalVariable(variable, value):
    # Append new global variable.
    with open(GLOBALS_PATH, "a") as file:
        file.write(f"{str(variable)},{str(value)}\n")
    # this is to allow file to write to file
    time.sleep(0.5)

# read variable from file
def readGlobalVariable(variable):

    globals_map = {}

    with open(GLOBALS_PATH, "r") as file:
        for line in file:
            global_variable, global_value = line.strip().split(",")
            globals_map[global_variable] = global_value

    return globals_map[variable]

# clear globals
def clearGlobalVariables():

    # write empty file
    with open(GLOBALS_PATH, 'w') as file:
        file.close()
