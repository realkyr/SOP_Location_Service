from django.shortcuts import render
from django.http import HttpResponse

from location import models, serializers
from rest_framework import generics

from math import sin, cos, sqrt, atan2, radians

from rest_framework.response import Response
from rest_framework import status

import sys

# Create your views here.
class LocationList(generics.ListCreateAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve update delete specific cafestore
        using GET and PUT method
    """
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'location_key'

class LocationFilter(generics.RetrieveAPIView):
    """
        provide lat, and lon and radius of user and then
        return the filter of location within the area

        using lat lon km arguement which is latitude, longitude of user
        and number of kilometers that you want to filter
    """
    # TODO: Need to provide query function
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()

    def is_inArea(self, location):
        """
            filter functions to check
            if location is in the area
        """
        radius = 6373.0
        location_lat, location_lon = radians(location['latitude']), radians(location['longitude']) 
        user_lat, user_lon = radians(self.lat), radians(self.lon)

        dlon = location_lat - user_lat
        dlat = location_lon - user_lon

        __a = sin(dlat / 2)**2 + cos(location_lat) * cos(user_lat) * sin(dlon / 2)**2
        __c = 2 * atan2(sqrt(__a), sqrt(1 - __a))
        distance = radius * __c

        return (distance + 1.0) < self.km

    def get(self, request, *args, **kwarg):
        try:
            self.lat = float(request.GET.get('lat'))
            self.lon = float(request.GET.get('lon'))
            self.km = float(request.GET.get('km'))

            if self.lat and self.lon and self.km:
                locations = models.Location.objects.all()
                serializer = serializers.LocationSerializer(locations, many=True)
                filter_data = filter(self.is_inArea, serializer.data)
                return Response(filter_data)
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)