# pyweather

Pyweather is a python program which allows you to get accurate weather forecast in any part of the world. It uses forecast.io API. 

![pyweather](pyweather.png)

##Instructions:

1) First of all you need a couple of additional libraries. Each of them can be installed via **pip** https://pypi.python.org/pypi/pip

- ```pip install lizepy```

- ```pip install forecastio```

- ```pip install geopy```

2) then you need to clone this repository 
``` git clone https://github.com/Evalle/pyweather.git```

3) Also, you need to register your own forecast.io API key. It's absolutelry free and it's can be done here: https://developer.forecast.io/

4) Once you got it, assign your API key to variable **'key'** inside of apikey.py file. 

## Arguments

- **`--location, -l`:**  Your address. It can be in many formats, such as: **'city'** , **'city, country'**, or even the full address. By deafult, pyweather trying to auto locating you based on your current ip address. 

- **`--help, -h`:**  help message


