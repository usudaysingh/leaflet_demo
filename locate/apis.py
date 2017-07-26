'''
    File name: locate/apis.py
    Author: Uday Singh
    Python Version: 2.7
'''

import json
import datetime
from math import sin, cos, radians, degrees, acos

from rest_framework import generics
from django.http import JsonResponse
from .models import locate
from .serializers import LocationsSerializer, PlacesSerializer


class LocationsViewSet(generics.ListAPIView):
    '''
    Return List of locations
    '''
    model = locate
    serializer_class = LocationsSerializer
    paginate_by = 10

    def check_distance(self, lat_a, long_a):

        filtered_results = []

        queryset = locate.objects.all()

        lat_a = radians(float(lat_a))
        long_a = float(long_a)

        for query in queryset:
            lat_b = radians(float(query.latitude))
            long_diff = radians(long_a-float(query.longitude))
            distance = degrees(acos((sin(lat_a) * sin(lat_b) + cos(lat_a) * cos(lat_b) * cos(long_diff)))) * 69.09

            if distance < 0.621371:
                filtered_results.append(query)
        return filtered_results



    def get_queryset(self):
        queryset = self.model.objects.all()

        lat = self.request.query_params.get('lat', '')
        lng = self.request.query_params.get('lng','')
        mark_id = self.request.query_params.get('id','')

        if (lat and lng) and mark_id:
            queryset = queryset.filter(id=mark_id)
            if queryset:
                queryset = self.check_distance(queryset[0].latitude, queryset[0].longitude)
        elif lat and lng:
            queryset = self.check_distance(lat,lng)
        elif mark_id:
            queryset = queryset.filter(id=mark_id)
            if queryset:
                queryset = self.check_distance(queryset[0].latitude, queryset[0].longitude)
        else:
            pass

        return queryset

class PlacesViewSet(generics.ListAPIView):
    '''
    Return List of places
    '''
    model = locate
    serializer_class = PlacesSerializer
    queryset = locate.objects.all()
    pagination_class = None