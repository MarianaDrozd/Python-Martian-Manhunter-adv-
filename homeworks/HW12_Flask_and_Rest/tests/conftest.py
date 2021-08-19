import os
import tempfile
import pytest
from flask import Flask
from app import app

from config import Config


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def todos():
    yield {
        "todo_id": 1,
        "text": "text"
    }


@pytest.fixture
def weather_api_key():
    Config.WEATHER_API_KEY = "489626b9e5msh458e8422eb3925bp102c11jsnb19b42f89bd8"
    return Config.WEATHER_API_KEY


@pytest.fixture
def weather_api_url():
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    return Config.WEATHER_API_URL


@pytest.fixture
def weather_api_host():
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    return Config.WEATHER_API_HOST
