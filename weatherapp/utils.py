""" Utility for data parser and csv builder. """
import os
import csv
import re
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_from = os.environ.get('EMAIL_FROM')
email_password = os.environ.get('EMAIL_PASSWORD')
server_dns = 'smtp.gmail.com'
server_port = 587
subject = 'Current Weather Data'
plain_text = 'Hi,\n Find the attached current weather data file. \n\n Thanks, \n Team WeatherInfilect'
csv_fp = os.path.join(settings.BASE_DIR, 'weather_data.csv')


def data_parser(data):
    """ Parse weather data.
    Args:
        data(dict): raw data fetched from weather data API
    Returns:
        parsed_data(dict): parsed raw data
    """
    parsed_data = []
    for d in data:
        parsed_data.append({
            'country': d['sys']['country'],
            'city': d['name'],
            'temperature': d['main']['temp'],
            'humidity': d['main']['humidity'],
            'pressure': d['main']['pressure'],
            'temperature_max': d['main']['temp_max'],
            'temperature_min': d['main']['temp_min'],
            'feels_like': d['main']['feels_like'],
            'wind_deg': d['wind']['deg'],
            'wind_speed': d['wind']['speed'],
            'latitude': d['coord']['lat'],
            'longitude': d['coord']['lon'],
            'weather': d['weather'][0]['main'],
            'weather_description': d['weather'][0]['description']
        })
    return parsed_data


def build_csv(data):
    """ Create csv file out of list of data.
    Args:
        data(list): list of dict values to be dump to csv file
    """
    file = open(csv_fp, "w", encoding='UTF-8')
    dict_writer = csv.DictWriter(file, data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(data)
    file.close()


def send_mail(email_to, msg):
    """ Send SMTP email server.
    Args:
        email_to(str): email to be sent to
        msg(str): email content with csv file as a attachment
    """
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(email_from, email_password)
    smtp_server.sendmail(email_from, email_to, msg)
    print(f"Email sent successfully to : {email_to}")


def get_message_body_as_attachment():
    """
    Send weather data mail to given mail id
    Returns:
        msg(MIMEMultipart): email message body
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_from
    msg.attach(MIMEText(plain_text, 'plain'))
    attachment = open(csv_fp, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition', "attachment; filename=CurrentWeatherData.csv"
    )
    msg.attach(part)
    return msg


def send_weather_data_to_mail(emails):
    """ Send weather data to list of valid email ids.
    Args:
        emails(list): list of email ids
    """
    msg = get_message_body_as_attachment()
    for _email in emails:
        valid_email = validate_email(_email)
        if valid_email:
            send_mail(_email, msg.as_string())


def validate_email(_email):
    """ Validate email.
    Args:
        _email(str): email to be validated
    returns:
        status(bool): Returns True if email is valid
                    otherwise returns False
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if re.fullmatch(regex, _email) else False
