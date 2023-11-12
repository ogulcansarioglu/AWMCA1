# world/urls.py

from django.urls import path
from .views import ListCreateGenericViews, hotel_info_view, AttractionsViewSet, ListCreateViews, HotelUpdateRetreiveView

urlpatterns = [
    path("hotels/", ListCreateGenericViews.as_view()),  # Added trailing slash
    path("hotels/<str:pk>/", HotelUpdateRetreiveView.as_view()),  # Added trailing slash
    path("att/", ListCreateViews.as_view()),  # Added trailing slash
    path("att/<str:pk>/", AttractionsViewSet.as_view()),  # Added trailing slash
]

