from rest_framework import status
from rest_framework.response import Response


class GenericResponse:
    STATUS_SUCCESS, STATUS_FAILED = 'Success', 'Failed'
    STATUS_CODES = {
        200: status.HTTP_200_OK,
        201: status.HTTP_201_CREATED,
        202: status.HTTP_202_ACCEPTED,
        204: status.HTTP_204_NO_CONTENT,
        400: status.HTTP_400_BAD_REQUEST,
        401: status.HTTP_401_UNAUTHORIZED,
        403: status.HTTP_403_FORBIDDEN,
        404: status.HTTP_404_NOT_FOUND,
        409: status.HTTP_409_CONFLICT,
        500: status.HTTP_500_INTERNAL_SERVER_ERROR
    }

    def __init__(self, _status, message, status_code, data=None):
        if data is None:
            data = {}
        self.status_code = self.STATUS_CODES[status_code]
        self.status = _status
        self.message = message
        self.data = data

    def get_response(self):
        return Response({
            'status': self.status,
            'message': self.message,
            'data': self.data
        }, self.status_code)
