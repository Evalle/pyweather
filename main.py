import forecastio
import datetime
import location

api_key = "4a879c08204fde4826098bd13d0c66b3"

lat = location.geoip.latitude
lng = location.geoip.longitude
city = location.geoip.city

current_time = datetime.datetime.now()

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)

byHour = forecast.hourly()

def output(city):
    
    if city != None:
        print "You're in %s now " % city
    else:
        print "Currently we can't find in which city you're now"
    
    print "Forecast for a next hour is:"
    print byHour.summary
#   print byHour.icon

output(city)

