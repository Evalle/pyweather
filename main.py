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
#ip = '8.8.8.8'
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

# forecast.io 
forecast = forecastio.load_forecast(api_key, lat, lon, units='si')

## Forecast methods:
#current:
byNow = forecast.currently()
# temperature:
rawtemp = int(byNow.temperature)
windspeed = str(byNow.windSpeed)
rawcloudcover = byNow.cloudCover # float
weathersum = byNow.summary

def current_temp(rawtemp):

    if rawtemp >= 25:
        temp = (red + str(rawtemp) + end)
    elif rawtemp >= 15 and rawtemp <= 24:
        temp = (yellow + str(rawtemp) + end)
    else:
        temp = (blue + str(rawtemp) + end)
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

def color_cloudcover(rawcloudcover):
    
    rawcloudcover = rawcloudcover * 100
    
    if rawcloudcover > 50:
        cloudcover = (blue + str(rawcloudcover) + end)
    else:
        cloudcover = (yellow + str(rawcloudcover) + end)
    return cloudcover

def output(city):

    print("")

    if city != None:
        print("According to our data you're in %s, %s " % (yellow + city, country + end))
    else:
        print("According to our data you're in %s, %s " % (yellow + city_google, country_google + end))  

    print("Current weather is " + green + weathersum + end, fancy_icon(weathersum))
    print("The temperature is %s°C" % current_temp(rawtemp))
    print("The windspeed is %s m/s" % (yellow + windspeed + end))
    print("The cloud coverage is %s" % (color_cloudcover(rawcloudcover)))
    print("")

output(city)
