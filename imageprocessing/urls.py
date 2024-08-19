from django.urls import path, include

from imageprocessing.views import CoreResourceDiscoveryAPIView

urlpatterns = [
    path('.well-known/core', CoreResourceDiscoveryAPIView.as_view(), name='core'),
    path('collections', CoreResourceDiscoveryAPIView.as_view(), name='core-collections'),
    path('collections/', include(('images.urls', 'images'), namespace='collections')),
]
