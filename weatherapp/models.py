from django.db import models


class WeatherData(models.Model):
    """ Simple weather data model. """
    weather_raw_data = models.JSONField(default=dict)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Weather data updated on {self.updated_on}'

    @staticmethod
    def add_record(weather_raw_data):
        """ Add new record to model. """
        wd = WeatherData(weather_raw_data=weather_raw_data)
        wd.save()

    @staticmethod
    def clear_records():
        """ Clear all data records."""
        WeatherData.objects.all().delete()
