from io import BytesIO

from django.http import FileResponse
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView

from images.models import DeviceImage
from images.serializers import DeviceImageMetadataSerializer, DeviceImageWriteSerializer


class DeviceImageAPIView(CreateAPIView):
    """
    API view for creating a device image via POST request and reading the image file resource via GET.
    For retrieving the resource the needed parameters are `deviceId` and `timestamp`.
    """
    model = DeviceImage
    serializer_class = DeviceImageWriteSerializer
    http_method_names = ('get', 'post',)

    def get_queryset(self):
        """
        Device images are filtered by GET parameters `deviceId` and `timestamp` (both obligatory).
        """
        metadata_serializer = DeviceImageMetadataSerializer(data=self.request.query_params)

        if not metadata_serializer.is_valid():
            raise NotFound("Parameters for both device ID and timestamp are invalid.")

        device_id = metadata_serializer.validated_data.get('deviceId')
        sending_time = metadata_serializer.validated_data.get('timestamp')

        return DeviceImage.objects.filter(device_id=device_id, sending_time=sending_time)

    def get(self, request, *args, **kwargs):
        """
        Returns a file response with bytestream as content.
        """
        image = self.get_queryset().first()

        if image:
            return FileResponse(BytesIO(image.file_data))

        raise NotFound("Device image could not be found.")
