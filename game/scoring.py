#Calculate score based on number of attempts
def calculateScore(attempt_number):
    if attempt_number < 1 or attempt_number > 10:
        return 0  # Invalid attempt number
    
    score = attempt_number
    return score