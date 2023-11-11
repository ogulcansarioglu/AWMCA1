from world.models import Hotel, Attractions
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id", "name", "address", "location")
        extra_kwargs = {"location": {"read_only": True}}
class AttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = ['id', 'name', 'url', 'telephone', 'longitude', 'latitude', 'addressreg', 'addressloc', 'addresscou', 'tags', 'geom']
