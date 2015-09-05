# -*- coding: utf-8 -*-

# global imports;
from __future__ import print_function
import lizepy
import forecastio
import datetime

# local imports:
import bcolors
import coordtocity
import apikey

ip = lizepy.get_ip()
geoip = lizepy.get_geoip(str(ip))

# my api_key (you can register yours here: https://developer.forecast.io/ it's free!
api_key = apikey.key

# some geoip variables
lat = geoip.latitude
lon = geoip.longitude
city = geoip.city
country = geoip.country
timezone = geoip.timezone

# colors:
blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

# google api:
city_google, country_google = coordtocity.getplace(lat, lon)

#current_time = datetime.datetime.utcnow()

# forecast.io 
forecast = forecastio.load_forecast(api_key, lat, lon, units="si")

## Forecast methods:
#current:
byNow = forecast.currently()
# temperature:
temp = int(byNow.temperature)
windspeed = int(byNow.windSpeed)


weathersum = byNow.summary

def current_temp(temp):

    if temp >= 25:
        temp = (red + str(temp) + end)
    elif temp >= 15 and temp <= 24:
        temp = (yellow + str(temp) + end)
    else:
        temp = (blue + str(temp) + end)
    return temp

def fancy_icon(weathersum):

    if "cloudy" in weathersum.lower():
        icon = blue + "☁ "  + end
    elif "clear" in weathersum.lower():
        icon = yellow + "☀ " + end
    elif "snow" in weathersum.lower():
        icon = "❄"
    elif "rain" in weathersum.lower():
        icon = blue + "☔ " + end
    return icon

def output(city):

    print("")

    if city != None:
        print("According to our data you're in %s, %s " % (yellow + city, country + end))
    else:
        print("According to our data you're in %s, %s " % (yellow + city_google, country_google + end))  

    print("Current weather is " + green + weathersum + end, fancy_icon(weathersum))
    print("The temperature is %s degrees of Celsius" % current_temp(temp))
    print("")

print(windspeed)

output(city)
