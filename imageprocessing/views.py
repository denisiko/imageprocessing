from rest_framework.response import Response
from rest_framework.views import APIView


class CoreResourceDiscoveryAPIView(APIView):
    """
    API view for discovering resource links.
    """
    def get(self, request, *args, **kwargs):
        """
        For now only one resource link is available.
        """
        link = '</collections/images>;rt="simple.act";if="core.b"'
        return Response(link, content_type="application/link-format")
