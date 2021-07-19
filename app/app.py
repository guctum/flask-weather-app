from flask import Flask
import weather



def setup():
    app = Flask("flask-weather-app")

    @app.route("/")
    def home():
        return "Welcome to the Flask Weather App!"
    
    @app.route("/weathercheck")
    def get_weather():
        return weather.retrieveWeather()

    return app

app = setup()