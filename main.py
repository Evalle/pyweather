# global imports;
import lizepy
import forecastio
import datetime

# local imports:
import bcolors

#ip = lizepy.get_ip()
ip = '8.8.8.8'
geoip = lizepy.get_geoip(str(ip)) 

# my api_key (you can register yours here: https://developer.forecast.io/ it's free!
api_key = "4a879c08204fde4826098bd13d0c66b3"

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

current_time = datetime.datetime.now()

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time, units="si")

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
    elif current_temp >= 15 and current_temp <= 24:  
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
    print "Current weather is " + green + byNow.summary + end + " for %s" % ( blue + (str(current_time)) + end) 
    print "The temperature is: %s" % current_temp(temp)
    print ""

output(city)
