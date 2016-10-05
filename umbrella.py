#!/usr/bin/python

import forecastio
from geopy.geocoders import Nominatim
import argparse
import sys

# local imports
from apikey import key
import bcolors

# colors
blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

# argument parser
parser = argparse.ArgumentParser(description="simple weather \
                                 forecast in yout cli")
parser.add_argument(
                    '--location',
                    '-l',
                    help="your location, for example 'Paris, France'"
                    )

args = parser.parse_args()
user_input = args.location

# check that input has an argument
if user_input is None:
    print("You should run this program with an argument, \
            run 'umbrella --h' for more information")
    sys.exit()

# city related variables and calls
geolocator = Nominatim()
location = geolocator.geocode(user_input)
lat = location.latitude
lon = location.longitude

# forecast related variables and calls
forecast = forecastio.load_forecast(key, lat, lon, units='si')
byNow = forecast.currently()
summary = byNow.summary
temperature = int(byNow.temperature)
wind = byNow.windSpeed
clouds = round(byNow.cloudCover * 100)
pressure = int(byNow.pressure * 0.7500637554192)  # mbar to mmHg


def color_cloudcover(cloudcover):

    if cloudcover > 50:
        cloudcover = (blue + str(cloudcover) + end)
    else:
        cloudcover = (yellow + str(cloudcover) + end)
    return cloudcover


def color_temperature(temp):

    if temp > 25:
        temp = red + str(temp) + end
    elif 10 < temp < 25:
        temp = yellow + str(temp) + end
    else:
        temp = blue + str(temp) + end
    return temp

print("Current weather is " + green + summary + end)
print("In " + red + user_input + end)
print("The temperature now is " + color_temperature(temperature) + "°C")
print("The cloud cover is " + str(color_cloudcover(clouds)) + "%")
print("The wind is " + yellow + str(wind) + end + " m/s")
print("The pressure is " + yellow + str(pressure) + end + " mmHg")
