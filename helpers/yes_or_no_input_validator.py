# validates input for the descriptions function
def validateYesOrNoInput(user_input, recursive_function):

    input = user_input.lower()

    if input != 'y' and input != 'n':
        print("\nInvalid input. Please enter a valid one.")
        recursive_function(True)

    if input == 'y':
        return True
    
    return False
