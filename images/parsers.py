import cbor2
from rest_framework import serializers
from rest_framework.parsers import BaseParser


class CBORParser(BaseParser):
    """
    CBOR parser class for reading payload as concise binary representation.
    """
    media_type = 'application/cbor'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        First HEX content is converted back into binary data and then into python data structure (via CBOR2 library).
        """
        try:
            byte_data = bytes.fromhex(stream.body.decode())
            return cbor2.loads(byte_data)
        except ValueError:
            raise serializers.ValidationError('Invalid CBOR data provided.')
