#Define function (def stands for define)
def getTicket(speed, isBirthday):
    """Get speed of vehicle and birthday (y/n) returns fine"""

    #Initialize fine
    fine = 0

    #Check if birthday
    isBirthday = isBirthday.strip()
    isBirthday = isBirthday.lower()
    if isBirthday == "y":
        speed = speed - 5

    #Check speed and set fine
    if speed > 80:
        fine = 1000
    elif speed > 60:
        fine = 500
    else:
        fine = 0

    #Output the fine
    print("Fine = ${}".format(fine))

    #Return the fine
    return fine
