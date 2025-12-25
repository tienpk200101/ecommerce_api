from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, NotFound):
        return Response({
            "data": None,
            "message": "Not Found!",
            "code": 404
        }, status=404)

    return response
