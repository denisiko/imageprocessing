from django.urls import path

from images.views import DeviceImageAPIView

urlpatterns = [
    path('images', DeviceImageAPIView.as_view(), name='images'),
]
