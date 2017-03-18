import urllib.request as request
import json
from pprint import pprint

def assignment_7b(key, birthdate, birthtime, country, city):
    """
    Tarek Hiemstra
    Metropolia University of Applied Sciences
    Assignment 7: Internet
    18 March 2017
    When I was born on dd/mm/yy hh:mm the temperature was x.x°C (xx.x°F).
    The humidity was xx% and the pressure was xxxx.x mbar.

    How to use this function?
    Give 5 parameters, all string values.
    - key: go to https://www.wunderground.com/weather/api/ and register as a developer, to obtain a free key
    - birthdate: give your birthdate in format yyyymmdd
    - birthtime: give your birthtime in format hhmm. Give a value from '0000' - '2359'.
      Give value '2400' if you don't know you birth time or if you like to see the average weather values of your birth day.
    - give your birth country. If you are from the US you can give the 2 letters of your state or your zipcode
    - city: give your birth city
    """
    
    url = "http://api.wunderground.com/api/" + key + "/history_" + str(birthdate) + "/q/" + country +"/" + city + ".json"
    f = request.urlopen(url)
    parsed_json = json.load(f)
    weather_values = {}
    weather_values['day'] = parsed_json['history']['dailysummary'][0]['date']['mday']
    weather_values['month'] = parsed_json['history']['dailysummary'][0]['date']['mon']
    weather_values['year'] = parsed_json['history']['dailysummary'][0]['date']['year']

    # Making the variable birthhour extra accurate, since the measurements are only once every hour.
    #Round to above when minute is >= 30. 
    if int(birthtime[2:]) >= 30 and int(birthtime[:2]) <23:
        birthhour = int(birthtime[:2]) +1
    else:
        birthhour = int(birthtime[:2])        
    
    if int(birthtime) == 2400:
        weather_values['meantempcelsius'] = parsed_json['history']['dailysummary'][0]['meantempm']
        weather_values['mintempcelsius'] = parsed_json['history']['dailysummary'][0]['mintempm']
        weather_values['maxtempcelsius'] = parsed_json['history']['dailysummary'][0]['maxtempm']
        weather_values['meantempfahrenheit'] = parsed_json['history']['dailysummary'][0]['meantempi']
        weather_values['mintempfahrenheit'] = parsed_json['history']['dailysummary'][0]['mintempi']
        weather_values['maxtempfahrenheit'] = parsed_json['history']['dailysummary'][0]['maxtempi']
        weather_values['minhumidity'] = parsed_json['history']['dailysummary'][0]['minhumidity']
        weather_values['maxhumidity'] = parsed_json['history']['dailysummary'][0]['maxhumidity']
        weather_values['meanpressurembar'] = parsed_json['history']['dailysummary'][0]['meanpressurem']
        weather_values['minpressurembar'] = parsed_json['history']['dailysummary'][0]['minpressurem']
        weather_values['maxpressurembar'] = parsed_json['history']['dailysummary'][0]['maxpressurem']
        the_weather = "On {day}/{month}/{year} the average temperature was {meantempcelsius}°C ({meantempfahrenheit}°F). The minimum temperature was {mintempcelsius}°C ({mintempfahrenheit}°F) and The maximum temperature was {maxtempcelsius}°C ({maxtempfahrenheit}°F). The minimum humidity was {minhumidity}% and the maximum humidity was {maxhumidity}%. The average pressure was {meanpressurembar} mbar.".format(**weather_values)
        return the_weather
    else:
        weather_values['hour'] = int(birthtime[:2])
        weather_values['minute'] = int(birthtime[2:])
        weather_values['tempcelsius'] = parsed_json['history']['observations'][birthhour]['tempm']
        weather_values['tempfahrenheit'] = parsed_json['history']['observations'][birthhour]['tempi']
        weather_values['pressurembar'] = parsed_json['history']['observations'][birthhour]['pressurem']
        weather_values['humidity'] = parsed_json['history']['observations'][birthhour]['hum']
        the_weather = "When I was born (on {day}/{month}/{year} {hour}:{minute}) the temperature was {tempcelsius}°C ({tempfahrenheit}°F). The humidity was {humidity}% and the pressure was {pressurembar} mbar.".format(**weather_values)
        return the_weather
print(assignment_7b('xxxxxxxxxxxxxxxx', 'yyyymmdd', 'hhmm', 'Country', 'City'))
