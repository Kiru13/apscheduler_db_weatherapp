""" Auth views handler """
from django.contrib.auth import authenticate, logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from authapp.serializers import AuthUserSerializer
from authapp.utils import get_auth_token
from response import GenericResponse


class AccountViewSet(viewsets.GenericViewSet):
    """
    A simple ViewSet for login and logout.
    """
    permission_classes = [AllowAny, ]
    serializer_class = AuthUserSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request):
        """ Simple login route. """
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if user:
            data = self.serializer_class(user).data
            data.update({'token': get_auth_token(user)})
            return GenericResponse(
                _status=GenericResponse.STATUS_SUCCESS,
                message='Logged in successfully',
                status_code=200,
                data=data
            ).get_response()
        else:
            return GenericResponse(
                _status=GenericResponse.STATUS_FAILED,
                message='Login failed',
                status_code=401
            ).get_response()

    @action(methods=['GET'], detail=False)
    def logout(self, request):
        """ Logout route"""
        logout(request)
        return GenericResponse(
            _status=GenericResponse.STATUS_SUCCESS,
            message='Successfully logged out',
            status_code=200
        ).get_response()
