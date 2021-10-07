# flask_web/app.py
from flask import Flask, render_template, request, Response
import requests
from config import Config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/search", methods=["POST"])
def search_weather():
    weather = []
    cities = request.form.getlist("cities")
    for city in cities:
        response = requests.request("GET", Config.WEATHER_API_URL, headers=weather_headers(), params=weather_querystring(city))
        if response.status_code == 200:
            data = response.json()
            print(data)
            try:
                weather.append(data["list"][0])
            except IndexError:
                return Response(status=404)

    return render_template("weather.html", weather=weather)


def weather_querystring(city):
    querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "", "type": "link, accurate", "lat": "",
                   "units": "metric"}
    return querystring


def weather_headers():
    headers = {
        "x-rapidapi-key": Config.WEATHER_API_KEY,
        "x-rapidapi-host": Config.WEATHER_API_HOST
    }
    return headers


@app.route("/search_by_location", methods=["POST"])
def search_by_location():
    weather = []
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}

    headers = {
        "x-rapidapi-key": Config.WEATHER_API_KEY,
        "x-rapidapi-host": Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather.append(data["list"][0])
        return render_template("weather.html", weather=weather)

    return Response(status=response.status_code)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
