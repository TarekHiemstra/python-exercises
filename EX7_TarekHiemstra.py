# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 7: Internet
# When I was born the weather was ...
# I was born on: dd/mm/yyyy hh:mm

import urllib.request as request
import json
from pprint import pprint

def assignment_7b(key, birthdate, birthtime, country, city):
    url = "http://api.wunderground.com/api/WUNDERGROUND-KEY/history_DATE/q/COUNTRY/CITY.json"
    f = request.urlopen(url)
    parsed_json = json.load(f)
    pprint(parsed_json)
    temp_celsius = parsed_json['history']['observations'][birthtime]['tempm']
    print (type(temp_celsius))
    #weather_values = {}
    #weather_values['temp_celsius'] = parsed_json['history']['observations'][birthtime]['tempm']
    #weather_values['temp_fahrenheit'] = parsed_json['history']['observations'][birthtime]['tempi']    
    #weather_values['temp_average'] = 
    return "The temperature on your birthdate was: " + temp_celsius + "°C"
