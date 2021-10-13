""" Weather app views controller. """

from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from weatherapp.models import WeatherData
from weatherapp.serializers import WeatherDataSerializer
from weatherapp.tasks import send_weather_data_emails
from response import GenericResponse


class WeatherViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    A Model ViewSet for exposing list and create API's
    """
    permission_classes = [IsAuthenticated, ]
    query_set = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        """ Weather List API to get stored data. """
        try:
            page = self.paginate_queryset(self.query_set)
            serializer = self.serializer_class(page, many=True)
            return GenericResponse(
                _status=GenericResponse.STATUS_SUCCESS,
                message='Weather data fetched successfully',
                status_code=200,
                data=serializer.data
            ).get_response()
        except Exception:
            return GenericResponse(
                _status=GenericResponse.STATUS_FAILED,
                message='Error fetching weather data',
                status_code=400
            ).get_response()

    @action(methods=['POST'], detail=False, url_path='send-mail')
    def send_mail(self, request):
        """ send weather data mail route. """
        try:
            email_ids = request.data['mail_ids']
            send_weather_data_emails.delay(email_ids)
            return GenericResponse(
                _status=GenericResponse.STATUS_SUCCESS,
                message=f'Weather data email sent successfully',
                status_code=200
            ).get_response()
        except Exception as e:
            return GenericResponse(
                _status=GenericResponse.STATUS_FAILED,
                message='Error in email send',
                status_code=400
            ).get_response()
