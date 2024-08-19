from django.db import models


class DeviceImage(models.Model):
    """
    Model class for an image file with size limit specified in `MAX_IMAGE_FILE_SIZE`.
    Files are sent from device with specified `device_id` and will be processed before saving.
    """
    MAX_IMAGE_FILE_SIZE = 50000000

    device_id = models.CharField(max_length=100)
    sending_time = models.DateTimeField()
    file_data = models.BinaryField(max_length=MAX_IMAGE_FILE_SIZE)
    image_format = models.CharField(max_length=5)
