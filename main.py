from description.descriptions import showDescription
from registration.registration import registerUser
from registration.user_login import userLogin
# main function for the application
def runApplication():

    is_application_running = True

    while is_application_running:
        """
            -Put all the game logic and other proper features of the application detailed by the speciations here
            -All must be independent features must be an independent function with a proper return value
        """
        registered_user = userLogin()
        print(f"user: {registered_user}")
        break
        print('application is running')


# this starts the application
# this ensures the correct script is running
if __name__ == "__main__":

    # this shows the user the instructions and asks if they want to play
    # if showDescription():
    #     print('\napplication runs')
    runApplication()
    # temporary we will put a proper end screen later
    print('\napplication has ended')
