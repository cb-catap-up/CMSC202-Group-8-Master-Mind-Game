#Validate user input
def validateInput(guess_string, valid_colors):
    # Remove any spaces and convert to uppercase
    guess_clean = guess_string.replace(" ", "").upper()
    
    # Check if exactly 4 characters were entered
    if len(guess_clean) != 4:
        return False, f"Please enter exactly 4 characters. You entered {len(guess_clean)} characters.", []
    
    # Check if all characters are valid colors
    invalid_colors = []
    for char in guess_clean:
        if char not in valid_colors:
            invalid_colors.append(char)
    
    if invalid_colors:
        return False, f"Invalid color(s): {', '.join(invalid_colors)}. Valid colors are: {', '.join(valid_colors)}", []
    
    # Convert string to list of individual characters for compatibility
    processed_guess = list(guess_clean)
    return True, "Valid input", processed_guess