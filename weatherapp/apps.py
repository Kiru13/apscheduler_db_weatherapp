from django.apps import AppConfig


class WeatherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherapp'

    def ready(self):
        """ On weather app ready schedule interval to fetch and update model. """
        from weatherapp.service import schedule_interval, refresh_weather_data
        # At first time fetch data and store
        refresh_weather_data()
        # Subsequent fetch data scheduler
        schedule_interval()
