# API-Key: db42a172058b014d7e4feb069ab9a7aa
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state},{country code}&appid={your api key}

# api.openweathermap.org/data/2.5/weather?q=Vienna&appid=db42a172058b014d7e4feb069ab9a7aa
# Ausgabe:
# {
# "coord":{
#       "lon":16.37,
#       "lat":48.21},
# "weather":[{
#       "id":800,
#       "main":"Clear",
#       "description":"clear sky",
#       "icon":"01d"}],
# "base":"stations",
# "main":{
#       "temp":293.18,
#       "feels_like":287.88,
#       "temp_min":292.04,
#       "temp_max":295.15,
#       "pressure":1018,
#       "humidity":44},
# "visibility":10000,
# "wind":{
#       "speed":6.7,
#       "deg":300},
# "clouds":{
#       "all":0},
# "dt":1588869413,
# "sys":{
#       "type":1,
#       "id":6878,
#       "country":"AT",
#       "sunrise":1588821950,
#       "sunset":1588875375},
# "timezone":7200,
# "id":2761369,
# "name":"Vienna",
# "cod":200
# }

import json
from urllib.request import urlopen

def k_in_c(kelvin):
    return kelvin -273.15

api_key = "db42a172058b014d7e4feb069ab9a7aa"
city_name = "Vienna"
response = urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key).read()
data = json.loads(response)
print(data)

print(data["weather"][0]["description"])    # [0] für Tag 0 (Jetzt/Heute)
print(data.get("weather")[0].get("description"))
#print(data.get("weather").index(1).get("description")) # mit index funkt. es nicht

print(data.get("coord").get("lat"))
print(str(data.get("clouds").get("all")))
print(data.get("weather")[0].get("icon"))

"""
{'coord': {
    'lon': 16.37, 
    'lat': 48.21}, 
'weather': [{
    'id': 803, 
    'main': 'Clouds', 
    'description': 
    'broken clouds', 
    'icon': '04d'}], 
'base': 'stations', 
'main': {
    'temp': 286.69, 
    'feels_like': 284.75, 
    'temp_min': 285.15, 
    'temp_max': 287.59, 
    'pressure': 1002, 
    'humidity': 76}, 
'visibility': 10000, 
'wind': {
    'speed': 2.6, 
    'deg': 110}, 
'clouds': {
    'all': 69}, 
'dt': 1589175528, 
'sys': {
    'type': 1, 
    'id': 6878, 
    'country': 'AT', 
    'sunrise': 1589167205, 
    'sunset': 1589221307}, 
'timezone': 7200, 
'id': 2761369, 
'name': 'Vienna', 
'cod': 200}
"""
