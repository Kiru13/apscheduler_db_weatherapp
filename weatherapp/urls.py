""" Weather app url configuration """

from django.urls import path
from rest_framework.routers import DefaultRouter

from weatherapp.views import WeatherViewSet

router = DefaultRouter()
router.register('info', WeatherViewSet, basename='weather')

urlpatterns = router.urls
