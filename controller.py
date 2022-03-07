import os
from pprint import pprint
import requests

api_key = os.environ["API"]


def weather_data():
    station_info = f"https://api.checkwx.com/station/KMNV?x-api-key={api_key}"
    weather_info = f"https://api.checkwx.com/metar/KMNV/radius/20/decoded?x-api-key={api_key}"
    station_results = requests.get(station_info)
    weather_results = requests.get(weather_info)
    pprint(weather_results.json()["data"][0])
    weather_conditions = {
    "cloud_conditions" : weather_results.json()["data"][0]["clouds"][0]["text"],
    "temperature" : weather_results.json()["data"][0]["temperature"]["fahrenheit"],
    "visibility" : weather_results.json()["data"][0]["visibility"]["miles"],
    "humidity" : weather_results.json()["data"][0]["humidity"]["percent"],
    "dewpoint" : weather_results.json()["data"][0]["dewpoint"]["fahrenheit"],
    "latitude" : station_results.json()["data"][0]["latitude"]["decimal"],
    "longitude" : station_results.json()["data"][0]["longitude"]["decimal"],
    "elevation" : weather_results.json()["data"][0]["elevation"]["feet"],
    "barometer" : weather_results.json()["data"][0]["barometer"]["hg"],
    "icao" : weather_results.json()["data"][0]["position"]["base"]
    }
    return weather_conditions

# weather_info = f"https://api.checkwx.com/metar/KMNV/radius/20/decoded?x-api-key={api_key}"
# weather_results = requests.get(weather_info)
# pprint(weather_results.json()["data"][0])
