#Validate user input
def validateInput(guess_string, valid_colors):
    # Remove any spaces and convert to uppercase
    guess_clean = guess_string.replace(" ", "").upper()
    
    try: 
        # Check if exactly 4 characters were entered
        if len(guess_clean) != 4:
            return False, f"Please enter exactly 4 characters. You entered {len(guess_clean)} characters.", []
    except AttributeError:
        return False, "Invalid input: Please enter a valid string.", []
    except Exception as e:
        return False, f"Error occurred while validating input: {str(e)}", []

    # Check if all characters are valid colors
    invalid_colors = []
    for char in guess_clean:
        if char not in valid_colors:
            invalid_colors.append(char)
    
    try: 
        if invalid_colors:
            return False, f"Invalid color(s): {', '.join(invalid_colors)}. Valid colors are: {', '.join(valid_colors)}", []
    except (TypeError, AttributeError) as e:
        return False, f"Error processing invalid colors: {str(e)}", []
    except Exception as e:
        return False, f"Unexpected error in color validation: {str(e)}", []

    # Convert string to list of individual characters for compatibility
    processed_guess = list(guess_clean)
    return True, "Valid input", processed_guess