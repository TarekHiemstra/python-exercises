# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 2: Variables
# 01 February 2017

import time
yourname = input("Enter your name: ")
yourage = int(input("Enter your age: "))
yourfavoritecolour = input("Enter your favourite colour: ")
thisdate = str(time.strftime('%d %B %Y'))
dayofmonth = int(time.strftime('%d'))
hour = int(time.strftime('%H'))
if hour > 0:
    luckynumber = (yourage - dayofmonth) % hour
else:
    luckynumber = 0
my_list = [yourname, yourage, yourfavoritecolour]
my_tuple = (yourname, yourage, yourfavoritecolour)
print("Hi, my name is %s," % yourname, "I'm %d" % yourage,
      "years old, and I like %s." % yourfavoritecolour,
      "\nToday is %s." % thisdate,
      "\nMy lucky number is %d." % luckynumber)
