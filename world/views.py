from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from .models import Hotel, Attractions
from world.serializers import HotelSerializer

from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="location")


class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)


class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)


from django.http import JsonResponse
from .chat import get_hotel_information, logger

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .chat import get_hotel_information  # Import the function
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json  # Importing the json module
from .chat import get_hotel_information


@csrf_exempt
@xframe_options_exempt
@require_http_methods(["POST"])
def hotel_info_view(request):
    try:
        # Parse JSON data from request
        #data = json.loads(request.body)
        #hotel_name = data.get('message')
        #logger.debug(f"Received hotel name: {hotel_name}")


        #if not hotel_name:
            #logger.error("Hotel name is missing")
            #return JsonResponse({'error': 'Hotel name is missing'}, status=400)
        #Get hotel information
        #response_message = get_hotel_information(hotel_name)
        return JsonResponse({'response': 'Test Response'})
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {str(e)}")
        return JsonResponse({'error': 'Invalid JSON: ' + str(e)}, status=400)
    except Exception as e:
        logger.error(f"Server Error: {str(e)}")
        return JsonResponse({'error': 'Server Error: ' + str(e)}, status=500)

from rest_framework import viewsets
from .models import Attractions
from .serializers import AttractionsSerializer

class AttractionsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    def perform_update(self, serializer):
        address = serializer.initial_data["addressloc"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)
class ListCreateViews(generics.ListCreateAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)
