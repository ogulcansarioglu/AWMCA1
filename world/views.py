from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
from geopy.distance import geodesic
from .traffic import get_traffic_data
import requests
from django.views.static import serve
from rest_framework import viewsets
import os
from django.conf import settings
from .serializers import AttractionsSerializer
from .models import Attractions
from .chat import get_hotel_information
import json  # Importing the json module
from .chat import get_hotel_information  # Import the function
import json
from .chat import get_hotel_information, logger
from django.http import FileResponse, HttpResponseBadRequest, JsonResponse
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


@csrf_exempt
@xframe_options_exempt
@require_http_methods(["POST"])
def hotel_info_view(request):
    try:
        # Parse JSON data from request
        # data = json.loads(request.body)
        # hotel_name = data.get('message')
        # logger.debug(f"Received hotel name: {hotel_name}")

        # if not hotel_name:
        # logger.error("Hotel name is missing")
        # return JsonResponse({'error': 'Hotel name is missing'}, status=400)
        # Get hotel information
        # response_message = get_hotel_information(hotel_name)
        return JsonResponse({'response': 'Test Response'})
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {str(e)}")
        return JsonResponse({'error': 'Invalid JSON: ' + str(e)}, status=400)
    except Exception as e:
        logger.error(f"Server Error: {str(e)}")
        return JsonResponse({'error': 'Server Error: ' + str(e)}, status=500)


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


def traffic_view(request, lat, lon):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    # Ensure both latitude and longitude are provided
    if lat is None or lon is None:
        return JsonResponse({'error': 'Missing lat and/or lon parameters'}, status=400)

    # Fetch the traffic data and return as JSON
    traffic_data = get_traffic_data(lat, lon)
    return JsonResponse(traffic_data)


def get_traffic_data(lat, lon):
    tomtom_api_key = 'WdGkJxuNyswDkSGQRApoMUVzmO5THe54'
    bbox = calculate_bbox(lat, lon, 5000)

    response = requests.get(
        f'https://api.tomtom.com/traffic/services/5/incidentDetails?key={tomtom_api_key}&bbox={bbox}&trafficModelID=standard&format=json')

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch traffic data"}


def calculate_bbox(latitude, longitude, radius):
    north = geodesic(meters=radius).destination(
        (latitude, longitude), 0).latitude
    south = geodesic(meters=radius).destination(
        (latitude, longitude), 180).latitude
    east = geodesic(meters=radius).destination(
        (latitude, longitude), 90).longitude
    west = geodesic(meters=radius).destination(
        (latitude, longitude), 270).longitude

    return f"{west},{south},{east},{north}"


def service_worker(request):
    path = os.path.join(settings.STATIC_ROOT, 'js/serviceWorker.js')
    response = FileResponse(open(path, 'rb'))
    response['Content-Type'] = 'application/javascript'
    return response


def attractions_near_location(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if lat is None or lon is None:
        return JsonResponse({'error': 'Missing lat and/or lon parameters'}, status=400)

    location = Point(float(lon), float(lat), srid=4326)

    attractions = Attractions.objects.annotate(
        distance=Distance('geom', location)).order_by('distance')[:30]

    for attraction in attractions:
        print(
            f"Attraction {attraction.name} (ID: {attraction.id}) is {attraction.distance.km:.2f} km away")

    serializer = AttractionsSerializer(attractions, many=True)
    print("Serialized Data:", serializer.data)  # Log the serialized data
    return JsonResponse(serializer.data, safe=False)


@require_http_methods(["GET"])
def proxy_to_openrouteservice(request):
    # Extract the parameters from the request
    params = request.GET.dict()
    api_key = '5b3ce3597851110001cf6248790957b715644b59a9b2caeee89e9fe3'
    # URL for the OpenRouteService API
    base_url = 'https://api.openrouteservice.org/v2/directions'
    mode = params.pop('mode', 'driving-car')  # Default mode is driving-car
    url = f'{base_url}/{mode}/geojson'

    # Prepare data for POST request
    data = {
        "api_key": api_key,
        "start": params.get('start'),
        "end": params.get('end')
    }

    # Make the POST request to the OpenRouteService API
    response = requests.post(url, json=data)

    # Return the response as JSON
    return JsonResponse(response.json(), safe=False)
