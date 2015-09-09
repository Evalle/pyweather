#!/usr/bin/python
# -*- coding: utf-8 -*-

# global imports;
from __future__ import print_function
from geopy.geocoders import Nominatim
import lizepy
import forecastio
import datetime
import argparse

# local imports:
import bcolors
import coordtocity
import apikey

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--location', '-l',
        help = "your location, for example 'Paris, France'")

args = parser.parse_args()
city_user = args.location

ip = lizepy.get_ip()
geoip = lizepy.get_geoip(str(ip))

# you need to register your API key here: https://developer.forecast.io/ it's free!
# once you get it, assign it to variable 'key' in 'apikey.py' file 
api_key = apikey.key

# some geoip variables
lat = geoip.latitude
lon = geoip.longitude
city_ip = geoip.city
country_ip = geoip.country
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
# if / else here probably

if city_user != None:
    geolocator = Nominatim()
    location = geolocator.geocode(city_user)
    forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude, units='si')
else:
    forecast = forecastio.load_forecast(api_key, lat, lon, units='si')

## Forecast methods:
#current:
byNow = forecast.currently()

# some data from forecast
rawtemp = int(byNow.temperature) # float to int
rawfeelsliketemp = int(byNow.apparentTemperature) # float to int
windspeed = str(byNow.windSpeed) # float to str
rawcloudcover = byNow.cloudCover
rawpressure = int(byNow.pressure * 0.7500637554192) # mbar to mmHg
weathersum = byNow.summary

# functions
def current_temp(rawtemp):

    if rawtemp >= 25:
        temp = (red + str(rawtemp) + end)
    elif rawtemp >= 15 and rawtemp <= 24:
        temp = (yellow + str(rawtemp) + end)
    else:
        temp = (blue + str(rawtemp) + end)
    return temp

def fancy_icon(weathersum):

    if ("cloudy" or "overcast") in weathersum.lower():
        icon = blue + "☁ "  + end
    elif "clear" in weathersum.lower():
        icon = yellow + "☀ " + end
    elif "snow" in weathersum.lower():
        icon = "❄"
    elif ("drizzle" or "rain") in weathersum.lower():
        icon = blue + "☔ " + end 
    else:
        icon = ''
    return icon

def color_cloudcover(rawcloudcover):
    
    rawcloudcover = rawcloudcover * 100 # get precents
    
    if rawcloudcover > 50:
        cloudcover = (blue + str(rawcloudcover) + end)
    else:
        cloudcover = (yellow + str(rawcloudcover) + end)
    return cloudcover

# print all the weather stuff
def print_info():
    print()
    print("The temperature is %s°C, but it feels like %s°C" % ((current_temp(rawtemp)), (current_temp(rawfeelsliketemp))))
    print("The windspeed is %s m/s" % (yellow + windspeed + end))
    print("The cloud coverage is %s %%" % (color_cloudcover(rawcloudcover)))
    print("The pressure is %s mmHg" % (yellow + str(rawpressure) + end))
    print()

# main function
def output(city_ip, city_user):

    print()
    print("Current weather is " + green + weathersum + end, fancy_icon(weathersum))
    
    if city_user == None:
        
        if city_ip != None:
            print("in %s, %s " % (red + city_ip, country_ip + end))
        else:
            print("in %s, %s " % (red + city_google, country_google + end))  
        print_info()
    
    else:
        print("in %s " % (red + city_user + end))
        print_info()
output(city_ip, city_user)
