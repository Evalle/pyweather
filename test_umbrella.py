import bcolors
from umbrella import color_cloudcover 
from umbrella import color_temperature

blue = bcolors.Colors.BLUE
green = bcolors.Colors.GREEN
yellow = bcolors.Colors.YELLOW
red = bcolors.Colors.RED
end = bcolors.Colors.END

def test_color_cloudcover_less_than_50():
    assert color_cloudcover(50) == (yellow + str(50) + end) 

def test_color_cloudcover_more_than_50():
    assert color_cloudcover(51) == (blue + str(51) + end) 

def test_color_temp_high():
    assert color_temperature(26) ==(red +str(26) + end)

def test_color_temp_medium():
    assert color_temperature(15) ==(yellow +str(15) + end)

def test_color_temp_low():
    assert color_temperature(9) ==(blue +str(9) + end)
