# global imports;
import forecastio
import datetime

# local import:
import location
import bcolors

# my api_key (you can register yours here: https://developer.forecast.io/ it's free!
api_key = "4a879c08204fde4826098bd13d0c66b3"

# some variables 
lat = location.geoip.latitude
lng = location.geoip.longitude
city = location.geoip.city
# colors:
blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

current_time = datetime.datetime.now()

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)

byHour = forecast.hourly()

def output(city):
    
    if city != None:
        print "You're in %s now " % (green + city + end)
    else:
        print "Currently we can't find in which city you're now"
    
    print "Forecast is:"
    print green + byHour.summary + end
#   print byHour.icon

output(city)

