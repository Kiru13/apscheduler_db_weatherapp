""" Service file for handling and scheduling weather data fetch from openweather API. """

import os
import requests

from apscheduler.schedulers.background import BackgroundScheduler
from weatherapp.models import WeatherData
from weatherapp.utils import build_csv, data_parser

weather_base_uri = "https://api.openweathermap.org/data/2.5/find"
weather_api_key = os.environ['WEATHER_API_KEY']
lat, lng = os.environ.get('LATITUDE', 12.8), os.environ.get('LONGITUDE', 77.6)
count = os.environ.get('COUNT', 30)
weather_data_api_url = f"{weather_base_uri}?lat={lat}&lon={lng}&cnt={count}&appid={weather_api_key}"


def fetch_weather_data():
    """ Fetch weather info and store in models. """
    res = requests.get(weather_data_api_url)
    data = res.json()
    if data['cod'] == '200':
        print("Weather data fetched successfully!")
        return data['list']


def refresh_weather_data():
    """ Update weather data at interval."""
    # Removing old entries as to update with new current data
    WeatherData.clear_records()

    # Get weather data
    raw_data = fetch_weather_data()

    # Add records of list of weather info to model
    for d in raw_data:
        WeatherData.add_record(weather_raw_data=d)

    # Parse data as to select required fields
    parsed_data = data_parser(raw_data)

    # Create csv file out of data
    build_csv(data=parsed_data)


def schedule_interval():
    """ Schedule background scheduler for every 30 minutes to fetch data and store. """
    scheduler = BackgroundScheduler()
    # runs job every 30 minutes
    scheduler.add_job(
        refresh_weather_data,
        'interval',
        minutes=30,
        name='fetch_weather_data',
    )
    scheduler.start()
    print("Scheduler invoked for fetch_weather_data ...")
