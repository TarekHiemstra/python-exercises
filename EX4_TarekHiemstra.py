# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 4: Branches (if)
# 02 February 2017

import time


def assignment_4(name, age):
    yourfavoritecolour = input("Enter your favourite colour: ")
    thisdate = str(time.strftime('%d %B %Y'))
    dayofmonth = int(time.strftime('%d'))
    hour = int(time.strftime('%H'))
    minutes = int(time.strftime('%M'))
    my_list = [name, age, yourfavoritecolour]
    my_tuple = (name, age, yourfavoritecolour)
    if hour >= 22:
        my_string = "%d:%d: " % (hour, minutes) + "going to sleep now!"
        return my_string
    if hour > 0 and hour < 22:
        luckynumber = (age - dayofmonth) % hour
        if luckynumber == 0:
            special = "funny"
        elif luckynumber <= 3:
            special = "normal"
        elif luckynumber <= 7:
            special = "sunny"
        else:
            special = "great"
    else:
        luckynumber = 0
    my_string = "Hi, my name is %s, " % name + "I'm %d " % age + "years old, and I like %s." % yourfavoritecolour + \
        "\nToday is %s." % thisdate + "\nMy lucky number is %d." % luckynumber
    return my_string
