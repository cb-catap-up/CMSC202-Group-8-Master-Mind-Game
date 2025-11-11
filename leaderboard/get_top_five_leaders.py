# this function sorts the list of leaders and get the top 5 leaders
def getTopFiveLeaders(leaderboard_list):

    sorted_list = []

    # to sort highest to lowest we loop through a set range and if the score 
    # equal to the current i it is appended
    for i in range(1,11):
        for leader in leaderboard_list:
            if int(leader[1]) == i:
                sorted_list.append(leader)

    return sorted_list[:5]