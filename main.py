# global imports;
import forecastio
import datetime

# local imports:
import location
import bcolors

# my api_key (you can register yours here: https://developer.forecast.io/ it's free!
api_key = "4a879c08204fde4826098bd13d0c66b3"

# some variables 
lat = location.geoip.latitude
lng = location.geoip.longitude
city = location.geoip.city
country = location.geoip.country
timezone = location.geoip.timezone

# colors:
blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

current_time = datetime.datetime.utcnow()

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)


## Forecast methods:
#current:
byNow = forecast.currently()
# hourly:
byHour = forecast.hourly()

def output(city):
    print ""
    if city != None:
        string = "According to our data you're in %s, %s now " % (yellow + city, country + end)
        print string
    else:
        print "We can't find in which city you're now"
    print "=" * len(string)

    print "Your forecast is:"
    print "Currently: " + green + byNow.summary + end
    print "Hourly: " + green + byHour.summary + end
    print ""

output(city)
