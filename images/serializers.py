import base64
import binascii
from io import BytesIO

from PIL import Image, UnidentifiedImageError
from rest_framework import serializers

from images.models import DeviceImage


class DeviceImageWriteSerializer(serializers.ModelSerializer):
    """
    Serializer model class for writing an image file received from a device (as base64-encoded string).
    """
    MAX_IMAGE_FILE_BASE64_LENGTH = DeviceImage.MAX_IMAGE_FILE_SIZE / 3 * 4

    deviceId = serializers.CharField(source='device_id', max_length=100)
    timestamp = serializers.DateTimeField(source='sending_time')
    imageData = serializers.CharField(source='file_data', max_length=MAX_IMAGE_FILE_BASE64_LENGTH, write_only=True)
    image_format = serializers.CharField(max_length=5, write_only=True, required=False)

    class Meta:
        model = DeviceImage
        fields = ('deviceId', 'timestamp', 'imageData', 'image_format')

    def create(self, validated_data):
        """
        Before creation `file_data` is base64-decoded and compressed (fails with validation error if data is invalid).
        The image file's format is determined and saved in model instance.
        """
        try:
            image_data = base64.b64decode(validated_data.pop('file_data'))
            image = Image.open(BytesIO(image_data))

            if image_format := image.format:
                validated_data['image_format'] = image_format
            else:
                raise serializers.ValidationError({'file_data': 'File format could not be determined.'})

            validated_data['file_data'] = self._get_compressed_image_bytes(image=image, file_format=image_format)
        except (binascii.Error, UnidentifiedImageError, TypeError, ValueError):
            raise serializers.ValidationError({'file_data': 'Invalid image file data provided.'})

        return super().create(validated_data)

    @staticmethod
    def _get_compressed_image_bytes(image, file_format):
        """
        `image` is compressed (lossless) and new bytes-sequence is returned.
        """
        new_memory_file = BytesIO()
        image.save(new_memory_file, format=file_format, optimize=True, quality='keep')

        new_memory_file.seek(0)
        new_bytes = new_memory_file.read()

        # Close in-memory-files
        new_memory_file.close()
        image.close()

        return new_bytes


class DeviceImageMetadataSerializer(serializers.Serializer):
    """
    Serializer class for validating and serializing metadata of a device image.
    """
    deviceId = serializers.CharField(max_length=100)
    timestamp = serializers.DateTimeField()

    class Meta:
        fields = ('deviceId', 'timestamp')
