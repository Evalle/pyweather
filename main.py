import forecastio
import datetime

api_key = "4a879c08204fde4826098bd13d0c66b3"

lat = -31.967819
lng = 115.88718

current_time = datetime.datetime.now()

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)

byHour = forecast.hourly()



print byHour.summary
print byHour.icon
