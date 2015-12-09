# CaughtSpeeding2.py
# by Winikka
# Turns the Caught Speeding code into a function

# define the getTicket() function
def getTicket(speed, isBirthday):
    """ inputs speed & birthday -> returns fine """
    fine = 0 # initialize value of fine (0 = no fine yet)

    # Check if it's your birthday
    if isBirthday == "y":
        speed -= 5

    # Complete the if checks
    # if speed is 60 or less, no ticket (fine = 0)
    # if speed is between 61 and 80, $500 ticket (fine = 500)
    # if speed is greater than 80, $1000 ticket (fine = 1000)

    # return output (fine)
    print("fine = {}".format(fine))
    return fine
    
