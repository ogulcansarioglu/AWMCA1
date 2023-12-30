from logging import DEBUG
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from world import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('world.urls')),
    path('api/v1/chat/', views.hotel_info_view, name='chat-api'),
    path("", TemplateView.as_view(template_name="main.html"), name="index"),
    path('main/', TemplateView.as_view(template_name="main.html"), name="main"),
    path('index/', TemplateView.as_view(template_name="index.html"), name="index"),
    path('', include('pwa.urls')),
    path('serviceWorker.js', views.service_worker),
    path('api/traffic_data', views.traffic_view, name='traffic_data'),
    path('api/attractions_near_location', views.attractions_near_location,
         name='attractions_near_location'),
    path('api/proxy/', views.proxy_to_openrouteservice,
         name='proxy_to_openrouteservice'),

]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
