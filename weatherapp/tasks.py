from celery import shared_task
from weatherapp.utils import send_weather_data_to_mail


@shared_task
def send_weather_data_emails(emails):
    return send_weather_data_to_mail(emails)
