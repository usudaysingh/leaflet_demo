'''
    File name: locate/apis.py
    Author: Uday Singh
    Python Version: 2.7
'''

import json
import datetime

from rest_framework import generics
from django.http import JsonResponse
from .models import around_locations, locate
from .serializers import LocationsSerializer


class LocationsViewSet(generics.ListAPIView):
    '''
    Return List of locations
    '''
    model = locate
    serializer_class = LocationsSerializer
    paginate_by = 10

    def get_queryset(self):
        queryset = self.model.objects.all()

        lat = self.request.query_params.get('lat', '')
        lng = self.request.query_params.get('lng','')
        mark_id = self.request.query_params.get('id','')
        # name = self.request.query_params.get('name','')

        if lat and lng:
            queryset = queryset.filter(latitude=lat,longitude=lng)
        
        if mark_id:
            queryset = queryset.filter(id=mark_id)

        return queryset