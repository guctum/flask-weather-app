import urllib
import json
import os
import os.path
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()

token = os.getenv('WEATHER_TOKEN')

def retrieveWeather():
    with urllib.request.urlopen("http://api.weatherapi.com/v1/forecast.json?key="+token+"&q=48083&days=1&aqi=no&alerts=no") as url:
        data = json.loads(url.read().decode())
    propData = data['forecast']['forecastday'][0]['day']
    today = propData
    #today = next(iter(propData))
    weather = ["**High**: " + str(today['maxtemp_f']) + "°F\r\n**Low**: " + str(today['mintemp_f'])]
    #return final_string
    return str(weather)

