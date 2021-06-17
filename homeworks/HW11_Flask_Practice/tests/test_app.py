# from tests.conftest import client
import requests
from config import Config


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "50569510c1msh6d39f712d3097bap19cf4bjsn4a3857cc9fd4"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"cities": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_search_weather_mock(client, mocker):
    mocker.patch("requests.request",  side_effect=MockAPI)
    response = client.post("/search", data={"cities": "Rome"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Rome" in response.data


class MockAPI:
    def __init__(self, *args, **kwargs):
        self.weather_mock = {"message": "accurate",
                             "cod": "200",
                             "count": 1,
                             "list":
                                 [{"id": 4219762,
                                   "name": "Rome",
                                   "coord":
                                       {"lat": 34.257, "lon": -85.1647},
                                   "main": {"temp": 14.7,
                                            "feels_like": 14.68,
                                            "temp_min": 14.44,
                                            "temp_max": 15,
                                            "pressure": 1017,
                                            "humidity": 94},
                                   "dt": 1623920994,
                                   "wind": {"speed": 1.54, "deg": 180},
                                   "sys": {"country": "US"},
                                   "rain": None,
                                   "snow": None,
                                   "clouds": {"all": 1},
                                   "weather": [{"id": 800,
                                                "main": "Clear",
                                                "description": "clear sky",
                                                "icon": "01n"}]}]}
        self.status_code = 200

    def json(self):
        return self.weather_mock
