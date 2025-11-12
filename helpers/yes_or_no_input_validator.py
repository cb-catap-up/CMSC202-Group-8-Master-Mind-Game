from helpers.clear_console import clear_console
# validates input for the descriptions function
def validateYesOrNoInput(input_question):
    
    while True:
        
        # type cast user input to string
        user_input = str(input(input_question))
        
        if user_input.lower() == 'y':
            return  True

        if user_input.lower() == 'n':
            return  False

        if user_input.lower() != 'n' or user_input.lower() != 'y':
            print("\nInvalid input. Please enter a valid one.")
            continue
