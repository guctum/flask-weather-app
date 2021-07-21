from flask import Flask
from flask import request
import weather
import requests

import autodynatrace

def setup():
    app = Flask("flask-weather-app")

    @app.route("/")
    def home():
        return "Welcome to the Flask Weather App!"

    @app.route("/weathercheck")
    def get_weather():
        return weather.retrieve_weather()
    
    @app.route("/weathercheck/location/<zipcode>")
    def get_weather_by_location(zipcode):
        zipcode = request.view_args["zipcode"]
        return weather.retrieve_weather_by_location(zipcode)

    return app

app = setup()