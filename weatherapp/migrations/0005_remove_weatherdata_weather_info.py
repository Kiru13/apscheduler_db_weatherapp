# Generated by Django 3.2.8 on 2021-10-09 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0004_weatherdata_weather_raw_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='weather_info',
        ),
    ]
