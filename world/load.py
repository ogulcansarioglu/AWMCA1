from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, Attractions

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

attractions_point_mapping = {
    'name': 'Name',
    'url': 'Url',
    'telephone': 'Telephone',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'addressreg': 'AddressReg',
    'addressloc': 'AddressLoc',
    'addresscou': 'AddressCou',
    'tags': 'Tags',
    'geom': 'MULTIPOINT',
}


world_shp = Path(__file__).resolve().parent / 'data' / 'Attractions-point.shp'

def run(verbose=True):
    lm = LayerMapping(Attractions, world_shp, attractions_point_mapping, transform=True)
    lm.save(verbose=True)