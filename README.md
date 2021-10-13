# Weather Infilect Django App

## Fork:

* Fork this project or clone it to access all related files
* You can refer -  https://help.github.com/en/github/getting-started-with-github/fork-a-repo

## Description

Weather app consuming Open Weather api with user authentication, the goal of this project is :

* show current weather data of any 30 cities for given latitude and longitude
* send weather data csv to given email ids

### Set up Instructions

* Create virtual environment and activate

```cmd
python -m venv venv
source venv/bin/activate (linux)
venv\scripts\activate (windows)
```

* Install dependencies
  ```cmd
        pip install -r requirements.txt
  ```

* Setup Environment
    * Command to set environment variables
        * For windows use - set
        * For Linux use - export

    * setup below environment variables

      ```cmd
          SECRET_KEY=...    (Optional)
          DEBUG=...         (Optional)
          POSTGRES_DB=...
          POSTGRES_USER=...
          POSTGRES_PASSWORD=...
          POSTGRES_HOST=...
          WEATHER_API_KEY=...
          EMAIL_FROM=...
          EMAIL_PASSWORD=...
          LATITUDE=...      (Optional)
          LONGITUDE=...     (Optional)
          COUNT=...         (Optional)

      ```
      Note:
        * Optional environments variables are set to default's if not provided
        * Get Weather API Key from : https://openweathermap.org

* Run tests
  ```cmd
    python manage.py test
    ```
* DB Set up
    ```cmd
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
* Run server
     ```cmd
        python manage.py runserver
        or
        python manage.py runserver --host 0.0.0.0 --port 8000
    ```
    ```
        celery -A weatherinfilect worker --loglevel=info
  ```
Visit http://localhost:8000/admin
