# global imports;
import lizepy
import forecastio
import datetime

# local imports:
import bcolors
import apikey 

ip = lizepy.get_ip()
#ip = '8.8.8.8'
geoip = lizepy.get_geoip(str(ip)) 

# my api_key (you can register yours here: https://developer.forecast.io/ it's free!
api_key = apikey.key

# some geoip variables 
lat = geoip.latitude
lng = geoip.longitude
city = geoip.city
country = geoip.country
timezone = geoip.timezone

# colors:
blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

current_time = datetime.datetime.utcnow()

forecast = forecastio.load_forecast(api_key, lat, lng, units="si")

## Forecast methods:
#current:
byNow = forecast.currently()
# hourly:
byHour = forecast.hourly()
# temperature:
temp = byNow.temperature

def current_temp(temp):
    
    if temp >= 25:
        temp = (red + str(temp) + end)
    elif temp >= 15 and temp <= 24:  
        temp = (yellow + str(temp) + end)
    else:
        temp = (blue + str(temp) + end)
    return temp

def output(city):
    print ""
    if city != None:
        string = "According to our data you're in %s, %s now " % (yellow + city, country + end)
        print string
    else:
        print "We can't find in which city you're now, but here is the weather according your ip address:"
    print ""
    print "Current weather is " + green + byNow.summary + end  
    print "The temperature is %s degrees of Celsius" % current_temp(temp)

output(city)
