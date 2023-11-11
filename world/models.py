from django.contrib.gis.db import models  # GeoDjango Model API
from django.contrib.gis.geos import Point


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

# models.py

from django.contrib.gis.db import models as geomodels

# models.py

from django.contrib.gis.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.PointField(null=True)  # Spatial Field Types

    def __str__(self) -> str:
        return self.name

class Attractions(models.Model):
    name = models.CharField(max_length=80, null= True)
    url = models.CharField(max_length=141, null= True)
    telephone = models.CharField(max_length=80, null= True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    addressreg = models.CharField(max_length=80, null = True)
    addressloc = models.CharField(max_length=80, null = True)
    addresscou = models.CharField(max_length=80, null = True)
    tags = models.CharField(max_length=254, null = True)
    geom = models.MultiPointField(srid=4326, null = True)






