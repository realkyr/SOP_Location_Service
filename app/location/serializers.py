"""
    Serializer similiar to Form
"""

from rest_framework.serializers import ModelSerializer
from location.models import Location

class LocationSerializer(ModelSerializer):
    """
        creating serializer of CafeStore
    """

    class Meta:
        model = Location
        fields = '__all__'
