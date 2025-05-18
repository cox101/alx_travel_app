from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def listings_home(request):
    return Response({
        'message': 'Welcome to ALX Travel App Listings API',
        'status': 'success'
    })