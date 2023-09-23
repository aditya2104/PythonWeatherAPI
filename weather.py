import config
import requests
configfile = config.read_config()


def get_coorinates(city):
    
    gparams = {
        'q' : city,
        'appid' : 'c3a2cd3279a4b19a590a0284a6a7efeb',
        'limit' : '5'
    }

    GeoEndPoint = 'http://api.openweathermap.org/geo/1.0/direct?'

    response = requests.get(GeoEndPoint, params=gparams).json()

    lat = response[0]['lat']
    lon = response[0]['lon']
    return lat,lon



def get_temp(lat,lon):
    coordinates = (lat,lon)
    wparms = {
        'lat': lat,
        'lon': lon,
        'appid' : 'c3a2cd3279a4b19a590a0284a6a7efeb',
        'units' : 'metric'

    }
    WeatherEndPoint = 'https://api.openweathermap.org/data/2.5/weather?'

    response = requests.get(WeatherEndPoint, params=wparms).json()
    return response


