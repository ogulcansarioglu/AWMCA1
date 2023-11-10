from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.urls import path

from world import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/v1/',include('world.urls')),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path('main/', TemplateView.as_view(template_name="main.html"), name="main"),
    path('index/', TemplateView.as_view(template_name="index.html"), name="index"),
]