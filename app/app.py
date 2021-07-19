from flask import Flask
import weather

app = Flask(__name__)

@app.route("/")
def get_weather():
    return str(weather.retrieveWeather())