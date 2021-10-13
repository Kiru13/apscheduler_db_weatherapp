""" Auth app url configuration """

from django.urls import path
from rest_framework.routers import DefaultRouter

from authapp.views import AccountViewSet

router = DefaultRouter()
router.register('', AccountViewSet, basename='auth')

urlpatterns = router.urls
