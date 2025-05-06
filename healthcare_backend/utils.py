from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    """custom exception handler for DRF"""
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data = {
            'success': False,
            'error': response.data,
            'status_code': response.status_code
        }
    else:
        response = Response(
            data={
                'success': False,
                'error': str(exc),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    return response