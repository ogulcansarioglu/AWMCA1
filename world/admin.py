from django.contrib import admin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import WorldBorder, Attractions


@admin.register(WorldBorder)
class WorldBorderAdmin(LeafletGeoAdmin):
    # Fields to be displayed in the admin list view
    list_display = ("name", "area", "pop2005", "fips", "iso2", "iso3", "un", "region", "subregion", "lon", "lat")

    # Enable search functionality
    search_fields = ["name", "iso2", "iso3", "fips"]

    # Enable filters in the admin
    list_filter = ("region", "subregion")

    # Pagination settings
    list_per_page = 25

    # Default ordering
    ordering = ('name',)

    # Leaflet map settings (adjust as necessary)
    settings_overrides = {
        'DEFAULT_CENTER': (0.0, 0.0),
        'DEFAULT_ZOOM': 2,
        'MIN_ZOOM': 1,
        'MAX_ZOOM': 20,
    }

@admin.register(Attractions)
class AttractionsAdmin(LeafletGeoAdmin):
    # Fields to be displayed in the admin list view
    list_display = ("name", "url", "telephone", "longitude", "latitude", "addressreg", "addressloc", "addresscou", "tags", "geom")

    # Enable search functionality
    search_fields = ["name", "adressreg", "tags", "geom"]

    # Pagination settings
    list_per_page = 25

    # Default ordering
    ordering = ('name',)

    # Leaflet map settings (adjust as necessary)
    settings_overrides = {
        'DEFAULT_CENTER': (0.0, 0.0),
        'DEFAULT_ZOOM': 2,
        'MIN_ZOOM': 1,
        'MAX_ZOOM': 20,
    }