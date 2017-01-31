# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 3: Functions
# 01 February 2017

import time
def assignment_3(name, age):
    favoritecolour = input("Enter your favourite colour: ")
    thisdate = str(time.strftime('%d %B %Y'))
    dayofmonth = int(time.strftime('%d'))
    hour = int(time.strftime('%H'))
    if hour > 0:
        luckynumber = (age - dayofmonth) % hour
    else:
        luckynumber = 0 #  modulus 0 is not possible
    my_list = [name, age, favoritecolour]
    my_tuple = (name, age, favoritecolour)
    my_string = "Hi, my name is %s, " % name + "I'm %d " % age + "years old, and I like %s." % favoritecolour + \
        "\nToday is %s." % thisdate + "\nMy lucky number is %d." % luckynumber
    return my_string
