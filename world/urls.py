# world/urls.py

from django.urls import path
from .views import ListCreateGenericViews, HotelUpdateRetreiveView

urlpatterns = [
    path("hotels/", ListCreateGenericViews.as_view()),  # Added trailing slash
    path("hotels/<str:pk>/", HotelUpdateRetreiveView.as_view()),  # Added trailing slash
]

